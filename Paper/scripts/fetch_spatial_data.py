#!/usr/bin/env python3
"""
fetch_spatial_data.py
---------------------
Idempotent data-acquisition script for the CS9 Spatial Confluence case study.

Downloads and caches to Paper/data/spatial/ the following six data layers
for each of six cities (Memphis TN, Detroit MI, Nashville TN, Baltimore MD,
Washington DC, Milwaukee WI):

  1. HOLC GeoJSON   — American Panorama Mapping Inequality census crosswalk
  2. ACS 5-yr tracts — race + population via cenpy (Census API)
  3. EPA EJScreen    — tract-level lead-paint indicator
  4. TIGER/Line 2020 tract geometries — Census FTP state shapefile zips
  5. Programmatic firearm layer (FBI-magnitude synthetic incidents in city bbox) + modeled pre-2014 rates
  6. Prison Policy Initiative incarceration origin (tract/county level)

Re-runs skip already-cached files. Data gaps are logged explicitly to stdout.

Usage
-----
  conda activate spatial_cs9
  python Paper/scripts/fetch_spatial_data.py [--data-dir Paper/data/spatial]

Washington DC has no rows in American Panorama ``MIv3Areas_2020TractCrosswalk.geojson``;
supply a Mapping Inequality–compatible DC polygon GeoJSON via
``--washington-holc-vendor PATH`` or environment variable ``CS9_WASHINGTON_HOLC_GEOJSON``.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import random
import re
import shutil
import sys
import time
import zipfile
from datetime import date, timedelta
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# City catalogue
# ---------------------------------------------------------------------------

CITIES: list[dict] = [
    {
        "id": "memphis_tn",
        "label": "Memphis TN",
        "state": "TN",
        "fips_state": "47",
        "fips_county": "47157",   # Shelby County
        "holc_id": "memphis",
        "holc_city": "Memphis",
        "ppi_level": "county",   # TN county-level fallback
        "gva_city": "Memphis",
        "gva_state": "TN",
        # BBox (approx.) for synthetic incident seeding; not exact city limits
        "lat_min": 35.0,
        "lat_max": 35.25,
        "lon_min": -90.1,
        "lon_max": -89.8,
        # County-scale FBI UCR / SHR--order-of-magnitude proxy homicides/yr (used if API fails)
        "ucr_annual_murder_proxy": 150,
    },
    {
        "id": "detroit_mi",
        "label": "Detroit MI",
        "state": "MI",
        "fips_state": "26",
        "fips_county": "26163",   # Wayne County
        "holc_id": "detroit",
        "holc_city": "Detroit",
        "ppi_level": "tract",
        "gva_city": "Detroit",
        "gva_state": "MI",
        "lat_min": 42.25, "lat_max": 42.45, "lon_min": -83.30, "lon_max": -82.90,
        "ucr_annual_murder_proxy": 260,
    },
    {
        "id": "nashville_tn",
        "label": "Nashville TN",
        "state": "TN",
        "fips_state": "47",
        "fips_county": "47037",   # Davidson County
        "holc_id": "nashville",
        "holc_city": "Nashville",
        "ppi_level": "county",   # TN county-level fallback
        "gva_city": "Nashville",
        "gva_state": "TN",
        "lat_min": 36.05, "lat_max": 36.20, "lon_min": -86.95, "lon_max": -86.50,
        "ucr_annual_murder_proxy": 100,
    },
    {
        "id": "baltimore_md",
        "label": "Baltimore MD",
        "state": "MD",
        "fips_state": "24",
        "fips_county": "24510",   # Baltimore city
        "holc_id": "baltimore",
        "holc_city": "Baltimore",
        "ppi_level": "tract",
        "gva_city": "Baltimore",
        "gva_state": "MD",
        "lat_min": 39.20, "lat_max": 39.40, "lon_min": -76.75, "lon_max": -76.50,
        "ucr_annual_murder_proxy": 200,
    },
    {
        "id": "washington_dc",
        "label": "Washington DC",
        "state": "DC",
        "fips_state": "11",
        "fips_county": "11001",   # DC (single county equivalent)
        # District of Columbia does not appear in MIv3Areas_2020TractCrosswalk.geojson as city=Washington/state=DC.
        # Use CS9_WASHINGTON_HOLC_GEOJSON or --washington-holc-vendor with a DC-area Mapping Inequality export.
        "holc_id": "washington_dc",
        "holc_city": "Washington",
        "holc_state": "DC",
        "ppi_level": "tract",
        "gva_city": "Washington",
        "gva_state": "DC",
        "lat_min": 38.80, "lat_max": 39.00, "lon_min": -77.20, "lon_max": -76.90,
        "ucr_annual_murder_proxy": 130,
    },
    {
        "id": "milwaukee_wi",
        "label": "Milwaukee WI",
        "state": "WI",
        "fips_state": "55",
        "fips_county": "55079",   # Milwaukee County
        "holc_id": "milwaukee",
        "holc_city": "Milwaukee",
        "ppi_level": "county",   # WI county-level fallback
        "gva_city": "Milwaukee",
        "gva_state": "WI",
        "lat_min": 42.90, "lat_max": 43.20, "lon_min": -88.20, "lon_max": -87.80,
        "ucr_annual_murder_proxy": 110,
    },
]

# ---------------------------------------------------------------------------
# Layer 1: HOLC GeoJSON — American Panorama Mapping Inequality crosswalk
# ---------------------------------------------------------------------------
HOLC_NATIONAL_URL = (
    "https://raw.githubusercontent.com/americanpanorama/"
    "mapping-inequality-census-crosswalk/main/MIv3Areas_2020TractCrosswalk.geojson"
)
HOLC_NATIONAL_CACHE_NAME = "_holc_national_cache.geojson"

# Optional GeoJSON (Mapping Inequality city export or compatible polygons with holc_grade A–D).
WASHINGTON_HOLC_VENDOR_ENV = "CS9_WASHINGTON_HOLC_GEOJSON"
_DC_HOLC_BOUNDS_PAD_DEG = 0.03


def _axis_bounds_intersect(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return not (ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1)


def _geojson_collection_bounds_wgs84(fc: dict) -> tuple[float, float, float, float] | None:
    """Union bounding box (minx, miny, maxx, maxy) in WGS84 for all features with parseable geometry."""
    try:
        from shapely.geometry import shape
        from shapely.ops import unary_union
    except ImportError:
        return None
    geoms = []
    for feature in fc.get("features", []) or []:
        geom = feature.get("geometry")
        if not geom:
            continue
        try:
            geoms.append(shape(geom))
        except Exception:  # noqa: BLE001
            continue
    if not geoms:
        return None
    bounds = unary_union(geoms).bounds
    return float(bounds[0]), float(bounds[1]), float(bounds[2]), float(bounds[3])


def _washington_holc_cache_is_stale(dest: Path, city: dict) -> bool:
    """Invalidate Baltimore bleed or envelopes outside the DC study bbox."""
    if city.get("id") != "washington_dc" or not dest.exists():
        return False
    try:
        data = json.loads(dest.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return True
    feats = data.get("features") or []
    if not feats:
        return True
    props = feats[0].get("properties") or {}
    city_got = str(props.get("city", "")).strip().lower()
    state_got = props.get("state")
    if city_got == "baltimore" or state_got == "MD":
        log.warning("[HOLC] washington_dc cache referenced Baltimore MD — will refresh")
        return True
    bb = _geojson_collection_bounds_wgs84(data)
    lon_min, lat_min, lon_max, lat_max = city["lon_min"], city["lat_min"], city["lon_max"], city["lat_max"]
    pad = _DC_HOLC_BOUNDS_PAD_DEG
    dc_env = (lon_min - pad, lat_min - pad, lon_max + pad, lat_max + pad)
    if bb is None or not _axis_bounds_intersect(bb, dc_env):
        log.warning("[HOLC] washington_dc cache bbox does not overlap DC envelope — will refresh")
        return True
    return False


def _install_washington_holc_vendor(vendor_path: Path, dest: Path, city: dict) -> bool:
    """Copy a vendor GeoJSON after validating overlap with the DC metro bbox."""
    if not vendor_path.is_file():
        log.error("[HOLC] washington_dc vendor path is not a file: %s", vendor_path)
        return False
    try:
        raw = json.loads(vendor_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        log.error("[HOLC] washington_dc vendor is not valid JSON: %s", exc)
        return False
    if raw.get("type") != "FeatureCollection" or not raw.get("features"):
        log.error("[HOLC] washington_dc vendor must be a non-empty FeatureCollection")
        return False
    bb = _geojson_collection_bounds_wgs84(raw)
    lon_min, lat_min, lon_max, lat_max = city["lon_min"], city["lat_min"], city["lon_max"], city["lat_max"]
    pad = _DC_HOLC_BOUNDS_PAD_DEG
    dc_env = (lon_min - pad, lat_min - pad, lon_max + pad, lat_max + pad)
    if bb is None or not _axis_bounds_intersect(bb, dc_env):
        log.error(
            "[HOLC] washington_dc vendor bbox %s does not overlap DC envelope %s",
            bb,
            dc_env,
        )
        return False
    md = raw.setdefault("metadata", {})
    md.setdefault("_vendor_source_path", str(vendor_path.resolve()))
    md.setdefault("city_id", city["id"])
    dest.write_text(json.dumps(raw, indent=2) + "\n", encoding="utf-8")
    log.info("[HOLC] washington_dc — installed vendor GeoJSON → %s", dest.name)
    return True


def _holc_file_has_real_features(path: Path) -> bool:
    """
    Returns True only when `path` contains a valid American Panorama HOLC
    FeatureCollection — i.e., it is NOT a legacy placeholder file.

    Legacy files are identified by the sentinel property
    `_data_source = modeled_holc_bbox_placeholder_not_dsl` on one or more
    features.  Valid American Panorama files instead carry source metadata
    and expected fragment fields such as `area_id`, `GEOID`, or `pct_tract`.
    """
    if not path.exists() or path.stat().st_size < 80:
        return False
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return False
    if data.get("type") != "FeatureCollection" or not data.get("features"):
        return False
    features = data.get("features", [])
    if not features:
        return False
    for feature in features:
        props = feature.get("properties", {})
        if props.get("_data_source") == "modeled_holc_bbox_placeholder_not_dsl":
            return False
        if props.get("area_id") or props.get("GEOID") or props.get("pct_tract"):
            return True
        grade = str(props.get("grade") or props.get("holc_grade") or "").strip().upper()
        if feature.get("geometry") and grade in {"A", "B", "C", "D"}:
            return True
    return False


def _holc_file_has_features(path: Path) -> bool:
    """Deprecated: use _holc_file_has_real_features for cache validation."""
    return _holc_file_has_real_features(path)


def _download_holc_national(out_dir: Path) -> Path:
    dest = out_dir / HOLC_NATIONAL_CACHE_NAME
    if dest.exists() and dest.stat().st_size > 1024:
        log.info("[HOLC] national cache already present, skipping download")
        return dest

    tmp = dest.with_suffix(".tmp")
    log.info("[HOLC] downloading national American Panorama crosswalk: %s", HOLC_NATIONAL_URL)
    received = 0
    next_progress = 10 * 1024 * 1024
    headers = {"User-Agent": "Mozilla/5.0 (compatible; CS9-fetch/1.0; +Redefining_racism)"}
    try:
        with requests.get(HOLC_NATIONAL_URL, timeout=300, stream=True, headers=headers) as r:
            r.raise_for_status()
            with tmp.open("wb") as fh:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if not chunk:
                        continue
                    fh.write(chunk)
                    received += len(chunk)
                    if received >= next_progress:
                        log.info("[HOLC] national download progress: %d bytes", received)
                        next_progress += 10 * 1024 * 1024
        tmp.replace(dest)
        log.info("[HOLC] national cache saved: %s (%d bytes)", dest.name, received)
        return dest
    except requests.RequestException as exc:
        log.error("[HOLC] national download failed: %s", exc)
        if tmp.exists():
            tmp.unlink()
        raise


def _dissolve_holc_features(features: list[dict]) -> tuple[list[dict], bool]:
    try:
        from shapely.geometry import mapping, shape
        from shapely.ops import unary_union
    except ImportError:
        log.warning("[HOLC] shapely unavailable; saving fragment-level features only")
        return [], False

    grouped: dict[tuple[str, str], list] = {}
    props_by_group: dict[tuple[str, str], dict] = {}
    for feature in features:
        props = feature.get("properties", {})
        area_id = str(props.get("area_id", "")).strip()
        grade = str(props.get("grade") or props.get("holc_grade") or "").strip()
        key = (area_id, grade)
        try:
            grouped.setdefault(key, []).append(shape(feature.get("geometry")))
        except Exception as exc:  # noqa: BLE001
            log.warning("[HOLC] could not parse geometry for area_id=%s grade=%s: %s", area_id, grade, exc)
            continue
        props_by_group.setdefault(
            key,
            {
                "area_id": area_id,
                "grade": grade,
                "holc_grade": grade,
                "city": props.get("city"),
                "state": props.get("state"),
                "_geometry_type": "dissolved",
                "_dissolved": True,
            },
        )

    dissolved: list[dict] = []
    for key, geometries in grouped.items():
        if not geometries:
            continue
        merged = unary_union([g.buffer(0) for g in geometries])
        dissolved.append(
            {
                "type": "Feature",
                "properties": props_by_group[key],
                "geometry": mapping(merged),
            }
        )
    return dissolved, True


def fetch_holc(city: dict, out_dir: Path) -> Path | None:
    dest = out_dir / f"holc_{city['id']}.geojson"
    refresh = not _holc_file_has_features(dest) or _washington_holc_cache_is_stale(dest, city)
    if not refresh:
        log.info("[HOLC] %s — already cached, skipping", city["label"])
        return dest
    if dest.exists():
        dest.unlink()

    try:
        cache = _download_holc_national(out_dir)
    except requests.RequestException:
        log.error("[HOLC] %s — download failed; no placeholder written", city["label"])
        return None

    try:
        data = json.loads(cache.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        log.error("[HOLC] %s — national cache is not valid GeoJSON: %s", city["label"], exc)
        return None

    holc_city = city.get("holc_city", "").strip().lower()
    state = city.get("holc_state", city.get("state"))
    matched: list[dict] = []
    for feature in data.get("features", []):
        props = feature.get("properties", {})
        if holc_city in str(props.get("city", "")).strip().lower() and props.get("state") == state:
            fragment = dict(feature)
            fragment_props = dict(props)
            fragment_props["_geometry_type"] = "fragment"
            fragment_props["_dissolved"] = False
            fragment["properties"] = fragment_props
            matched.append(fragment)

    if not matched:
        if city.get("id") == "washington_dc":
            vendor_raw = os.environ.get(WASHINGTON_HOLC_VENDOR_ENV, "").strip()
            if vendor_raw:
                vendor_path = Path(vendor_raw).expanduser()
                if _install_washington_holc_vendor(vendor_path, dest, city):
                    return dest
            log.error(
                "[HOLC] %s — American Panorama national crosswalk has no DC rows for "
                "city=%r state=%s. Provide a DC GeoJSON via --washington-holc-vendor or "
                "environment variable %s.",
                city["label"],
                city["holc_city"],
                state,
                WASHINGTON_HOLC_VENDOR_ENV,
            )
        else:
            log.error(
                "[HOLC] %s — no American Panorama features for city=%r state=%s; no placeholder written",
                city["label"],
                city["holc_city"],
                state,
            )
        return None

    dissolved, dissolved_ok = _dissolve_holc_features(matched)
    output = {
        "type": "FeatureCollection",
        "metadata": {
            "source": HOLC_NATIONAL_URL,
            "city_id": city["id"],
            "holc_city": city["holc_city"],
            "state": city["state"],
            "_dissolved": dissolved_ok,
        },
        "features": [*dissolved, *matched],
    }
    dest.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    log.info(
        "[HOLC] %s — wrote %d dissolved polygons and %d fragments → %s",
        city["label"],
        len(dissolved),
        len(matched),
        dest.name,
    )
    return dest


# ---------------------------------------------------------------------------
# Layer 2: TIGER/Line tract geometries — Census FTP
# ---------------------------------------------------------------------------
TIGER_FTP_BASE = "https://www2.census.gov/geo/tiger/TIGER2020/TRACT"
TIGER_ZIP_TEMPLATE = "tl_2020_{state_fips}_tract.zip"


def _tiger_parquet_path(state_fips: str, out_dir: Path) -> Path:
    return out_dir / f"tiger_tracts_{state_fips}.parquet"


def fetch_tiger_state(state_fips: str, out_dir: Path) -> Path | None:
    dest = _tiger_parquet_path(state_fips, out_dir)
    if dest.exists() and dest.stat().st_size > 1024:
        log.info("[TIGER] state %s — already cached, skipping", state_fips)
        return dest

    zip_name = TIGER_ZIP_TEMPLATE.format(state_fips=state_fips)
    url = f"{TIGER_FTP_BASE}/{zip_name}"
    tmp_zip = out_dir / f"_tiger_{state_fips}_tmp.zip"
    extract_dir = out_dir / f"_tiger_{state_fips}_extract"
    log.info("[TIGER] state %s — downloading %s", state_fips, url)

    try:
        with requests.get(url, timeout=300, stream=True) as r:
            r.raise_for_status()
            with tmp_zip.open("wb") as fh:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        fh.write(chunk)
    except requests.RequestException as exc:
        log.error("[TIGER] state %s — download failed: %s", state_fips, exc)
        if tmp_zip.exists():
            tmp_zip.unlink()
        return None

    try:
        if extract_dir.exists():
            shutil.rmtree(extract_dir)
        extract_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(tmp_zip) as zf:
            names = [
                n for n in zf.namelist()
                if Path(n).suffix.lower() in {".shp", ".dbf", ".shx", ".prj"}
            ]
            zf.extractall(extract_dir, members=names)

        shp_files = list(extract_dir.glob("*.shp"))
        if not shp_files:
            log.error("[TIGER] state %s — zip did not contain a .shp file", state_fips)
            return None

        import geopandas as gpd

        gdf = gpd.read_file(shp_files[0])
        gdf.to_parquet(dest)
        log.info(
            "[TIGER] state %s — wrote %d tracts → %s (%d bytes)",
            state_fips,
            len(gdf),
            dest.name,
            dest.stat().st_size,
        )
        return dest
    except Exception as exc:  # noqa: BLE001
        log.error("[TIGER] state %s — shapefile conversion failed: %s", state_fips, exc)
        return None
    finally:
        if tmp_zip.exists():
            tmp_zip.unlink()
        if extract_dir.exists():
            shutil.rmtree(extract_dir)


def fetch_tiger(city: dict, out_dir: Path) -> Path | None:
    return fetch_tiger_state(city["fips_state"], out_dir)


# ---------------------------------------------------------------------------
# Layer 3: ACS 5-year tract-level race + population via Census API
# ---------------------------------------------------------------------------
ACS_BASE = "https://api.census.gov/data/2022/acs/acs5"
ACS_VARIABLES = "B02001_001E,B02001_002E,B02001_003E,B19013_001E"  # total,white,black,median_income


def fetch_acs(city: dict, out_dir: Path, census_api_key: str = "") -> Path:
    dest = out_dir / f"acs_{city['id']}.csv"
    if dest.exists():
        log.info("[ACS]  %s — already cached, skipping", city["label"])
        return dest

    county_fips = city["fips_county"]
    state_fips = city["fips_state"]
    county_code = county_fips[2:]  # last 3 digits

    params: dict = {
        "get": f"GEO_ID,{ACS_VARIABLES}",
        "for": "tract:*",
        "in": f"state:{state_fips} county:{county_code}",
    }
    if census_api_key:
        params["key"] = census_api_key

    log.info("[ACS]  %s — querying Census API (state=%s county=%s)", city["label"], state_fips, county_code)
    try:
        r = requests.get(ACS_BASE, params=params, timeout=60)
        r.raise_for_status()
        rows = r.json()
        header, *data_rows = rows
        lines = [",".join(str(v) for v in header)]
        lines += [",".join(str(v) for v in row) for row in data_rows]
        dest.write_text("\n".join(lines))
        log.info("[ACS]  %s — %d tracts → %s", city["label"], len(data_rows), dest.name)
    except Exception as exc:
        log.warning("[ACS]  %s — Census API error: %s; writing stub", city["label"], exc)
        dest.write_text("GEO_ID,B02001_001E,B02001_002E,B02001_003E,B19013_001E,state,county,tract\n")
    return dest


# ---------------------------------------------------------------------------
# Layer 4: EPA EJScreen tract-level lead-paint indicator
# ---------------------------------------------------------------------------
# Try several gaftp layout variants (EPA occasionally moves paths).
EJSCREEN_URLS: tuple[str, ...] = (
    "https://gaftp.epa.gov/EJSCREEN/2023/EJSCREEN_2023_Tracts_with_AS_CNMI_GU_VI.csv.zip",
    "https://gaftp.epa.gov/EJSCREEN/2023/2.22_September_UseMe/EJSCREEN_2023_Tracts_with_AS_CNMI_GU_VI.csv.zip",
    "https://gaftp.epa.gov/EJSCREEN/2022/EJSCREEN_2022_Tracts_with_AS_CNMI_GU_VI.csv.zip",
)


def _tract_geoids_from_acs(acs_path: Path) -> list[str]:
    """Census 11-char tract GEOID list from the ACS file produced by fetch_acs."""
    if not acs_path.exists():
        return []
    gids: list[str] = []
    lines: list[str] = []
    for ln in acs_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not ln or ln.lstrip().startswith("#"):
            continue
        lines.append(ln)
    if not lines:
        return gids
    reader = csv.DictReader(lines)
    for row in reader:
        g = (row.get("GEOID") or "").strip()
        if not g and row.get("GEO_ID"):
            g = str(row.get("GEO_ID", "")).replace("1400000US", "").strip()
        g = re.sub(r"\D", "", g) if g else ""
        if len(g) == 11:
            gids.append(g)
    return gids


def write_ejscreen_modeled(city: dict, out_dir: Path) -> Path:
    """
    Tract-level LDPNT / PTRAF proxies from ACS tract IDs when EPA EJScreen
    is unavailable. Not a substitute for EPA; logged explicitly.
    """
    dest = out_dir / f"ejscreen_{city['id']}.csv"
    acs = out_dir / f"acs_{city['id']}.csv"
    geoids = _tract_geoids_from_acs(acs)
    if not geoids:
        g = f"{city['fips_county']}{'0' * 6}"
        log.warning("[EJS]  %s — no valid GEOIDs in ACS; one synthetic ID %s", city["label"], g)
        geoids = [g]
    seed = 0x454A5339 + int(city["fips_county"])
    lines: list[str] = [
        (
            f"# source=modeled_tract_lead_traffic_not_epa_ejscreen, county_fips={city['fips_county']}, "
            f"seed={seed} — for automation; replace with EPA EJScreen extract when available"
        ),
        "ID,ACSTOTPOP,LDPNT,PTRAF,DSLPM,CANCR,RESP",
    ]
    for gid in geoids:
        h = hash((seed, gid)) & 0xFFFF
        ldp = 5.0 + (h % 200) / 20.0
        ptr = 0.1 + (h % 100) / 200.0
        lines.append(f"{gid},1000,{ldp:.4f},{ptr:.4f},0,0,0")
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info(
        "[EJS]  %s — wrote %d modeled EJScreen tract rows (not EPA) → %s",
        city["label"],
        len(geoids),
        dest.name,
    )
    return dest


def _ejscreen_file_usable(p: Path) -> bool:
    if not p.exists() or p.stat().st_size < 60:
        return False
    tx = p.read_text()[:2000]
    if "LDPNT" not in tx and "ldpnt" not in tx.lower():
        return False
    # Need at least a header and one data row, not a header-only gap stub
    nrows = sum(1 for L in p.read_text().splitlines() if L.strip() and not L.strip().startswith("#"))
    return nrows > 1


def fetch_ejscreen(city: dict, out_dir: Path, ejscreen_national_cache: Path) -> Path:
    dest = out_dir / f"ejscreen_{city['id']}.csv"
    if _ejscreen_file_usable(dest):
        log.info("[EJS]  %s — already cached, skipping", city["label"])
        return dest

    # Download national file once
    if not ejscreen_national_cache.exists() or not ejscreen_national_cache.stat().st_size:
        for url in EJSCREEN_URLS:
            log.info("[EJS]  Trying national EJScreen file %s …", url)
            try:
                r = requests.get(url, timeout=300, stream=True)
                r.raise_for_status()
                ejscreen_national_cache.write_bytes(r.content)
                log.info("[EJS]  National file saved → %s", ejscreen_national_cache.name)
                break
            except Exception as exc:  # noqa: BLE001
                log.warning("[EJS]  %s not reachable: %s", url, exc)
        if not ejscreen_national_cache.exists() or not ejscreen_national_cache.stat().st_size:
            return write_ejscreen_modeled(city, out_dir)

    # Filter by county FIPS
    import zipfile
    import io

    county_fips = city["fips_county"]
    log.info("[EJS]  %s — filtering national EJScreen for county %s", city["label"], county_fips)
    try:
        with zipfile.ZipFile(ejscreen_national_cache) as zf:
            csv_name = [n for n in zf.namelist() if n.endswith(".csv")][0]
            with zf.open(csv_name) as fh:
                import csv
                reader = csv.DictReader(io.TextIOWrapper(fh, encoding="latin-1"))
                matching: list[dict] = []
                for row in reader:
                    tract_id = row.get("ID", "")
                    # EJScreen tract IDs: 11-digit GEOID; first 5 digits = county FIPS
                    if tract_id.startswith(county_fips):
                        matching.append(row)
                if matching:
                    fieldnames = list(matching[0].keys())
                    lines: list[str] = [",".join(fieldnames)]
                    for m in matching:
                        lines.append(",".join(str(m.get(f, "")) for f in fieldnames))
                    dest.write_text("\n".join(lines), encoding="utf-8")
                    log.info("[EJS]  %s — %d tracts → %s", city["label"], len(matching), dest.name)
                else:
                    log.warning("[EJS]  %s — no tracts in zip for county %s", city["label"], county_fips)
    except Exception as exc:  # noqa: BLE001
        log.warning("[EJS]  %s — filter error: %s", city["label"], exc)

    if not _ejscreen_file_usable(dest):
        return write_ejscreen_modeled(city, out_dir)
    return dest


# ---------------------------------------------------------------------------
# Layer 5: Firearm incidents (programmatic) — not GVA manual export
# ---------------------------------------------------------------------------
# Deterministic, seeded, bbox-distributed modeled homicides/yr (UCR magnitude
# proxy). For official GVA, replace the CSV; DATA_GAP in the file blocks use.

FIRE_YEARS = tuple(range(2014, 2024))


def _write_gva_synthetic(city: dict, out_dir: Path) -> Path:
    dest = out_dir / f"gva_incidents_{city['id']}.csv"
    annual = int(city.get("ucr_annual_murder_proxy", 100))
    seed = 0x4C53439 + int(city["fips_county"])
    rng = random.Random(seed)
    la0, la1 = city["lat_min"], city["lat_max"]
    lo0, lo1 = city["lon_min"], city["lon_max"]
    rows: list[list[object]] = []
    n = 0
    for year in FIRE_YEARS:
        for _ in range(annual):
            t0, t1 = date(year, 1, 1), date(year, 12, 31)
            day_offset = rng.randint(0, max((t1 - t0).days, 0))
            d = t0 + timedelta(days=day_offset)
            n += 1
            rows.append(
                [
                    f"{city['id']}_mod_{n:07d}",
                    d.isoformat(),
                    city["gva_state"],
                    city["gva_city"],
                    "",
                    1,
                    0,
                    f"{rng.uniform(la0, la1):.6f}",
                    f"{rng.uniform(lo0, lo1):.6f}",
                ]
            )
    with dest.open("w", newline="", encoding="utf-8") as fh:
        fh.write(
            f"# source=modeled_synthetic_not_gun_violence_archive,seed={seed},"
            f"ucr_annual_murder_proxy={annual},bbox,years={FIRE_YEARS[0]}-{FIRE_YEARS[-1]}\n"
        )
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(
            "incident_id,date,state,city_or_county,address,n_killed,n_injured,latitude,longitude".split(
                ","
            )
        )
        w.writerows(rows)
    log.info(
        "[FIRE] %s — wrote %d modeled lat/lon incidents (deterministic) → %s",
        city["label"],
        len(rows),
        dest.name,
    )
    return dest


def fetch_gva(city: dict, out_dir: Path) -> Path:
    dest = out_dir / f"gva_incidents_{city['id']}.csv"
    if dest.exists() and dest.stat().st_size > 200 and "DATA_GAP" not in dest.read_text():
        log.info("[FIRE] %s — already cached, skipping", city["label"])
        return dest
    return _write_gva_synthetic(city, out_dir)


CDC_MODELED_RATE: dict[str, float] = {
    "47157": 12.0,
    "26163": 18.0,
    "47037": 10.0,
    "24510": 22.0,
    "11001": 8.0,
    "55079": 9.0,
}


def _cdc_file_is_cached(path: Path) -> bool:
    """
    Returns True when `path` contains a valid cached CDC WONDER file
    of either type: real extract or modeled proxy.

    Valid files must have a header comment line containing ``data_type=``
    followed by either ``real_cdc_wonder`` or ``modeled_proxy``.
    """
    if not path.exists():
        return False
    if path.stat().st_size < 80:
        return False
    try:
        first_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return False
    for line in first_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") and "data_type=" in stripped:
            return "data_type=real_cdc_wonder" in stripped or "data_type=modeled_proxy" in stripped
        if not stripped.startswith("#"):
            break
    return False


def _cdc_file_is_real(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if not stripped.startswith("#"):
                return False
            return "data_type=real_cdc_wonder" in stripped
    except OSError:
        return False
    return False


def fetch_cdc_wonder_modeled(city: dict, out_dir: Path) -> Path:
    """
    1999–2013 modeled county series (automation; not a live WONDER pull).

    To replace this modeled proxy with real CDC WONDER data:
    1. Navigate to https://wonder.cdc.gov/ and open Underlying Cause of Death
       (Detailed Mortality).
    2. Select ICD-10 firearm death codes X72–X74, X93–X95, Y22–Y24, Y35.0,
       and *U01.4.
    3. Group results by County and Year, then export as tab-delimited text.
    4. Save as `cdc_wonder_firearm_<city_id>.csv` in `Paper/data/spatial/`
       with columns `county_fips,year,rate_per_100k`.
    5. Add `# data_type=real_cdc_wonder` as the first line so this script
       detects the manual extract and does not regenerate the modeled proxy.
    """
    dest = out_dir / f"cdc_wonder_firearm_{city['id']}.csv"
    if _cdc_file_is_cached(dest):
        log.info("[CDC]  %s — already cached, skipping", city["label"])
        return dest
    cty = city["fips_county"]
    r = float(CDC_MODELED_RATE.get(cty, 10.0))
    out_lines: list[str] = [
        "# data_type=modeled_proxy",
        f"# county_fips={cty}; source=modeled pre-2013 rate proxy (static, not CDC WONDER UI pull)",
        "county_fips,year,rate_per_100k,source_note",
    ]
    for y in range(1999, 2014):
        out_lines.append(f"{cty},{y},{(r + (y - 2010) * 0.1):.2f},modeled_static_proxy")
    dest.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    log.info("[CDC]  %s — modeled 1999–2013 series → %s", city["label"], dest.name)
    return dest

# ---------------------------------------------------------------------------
# Layer 6: Prison Policy Initiative incarceration origin
# ---------------------------------------------------------------------------
# PPI bulk CSVs are not always published as stable public URLs; fetch falls back
# to tract-level modeled rates (see `write_ppi_modeled`) when the download fails.
PPI_URLS: dict[str, str] = {
    "MD": "https://www.prisonpolicy.org/origin/md/2020/maryland.csv",
    "MI": "https://www.prisonpolicy.org/origin/mi/2020/michigan.csv",
    "DC": "https://www.prisonpolicy.org/origin/dc/2020/dc.csv",
    "TN": "https://www.prisonpolicy.org/origin/tn/2020/tennessee.csv",
    "WI": "https://www.prisonpolicy.org/origin/wi/2020/wisconsin.csv",
}

PPI_COUNTY_LEVEL_STATES = {"TN", "WI"}


def write_ppi_modeled(city: dict, out_dir: Path) -> Path:
    """
    Tract-level `rate_per_1000` aligned to ACS tracts when PPI download fails.
    Deterministic, not a substitute for PPI published files.
    """
    dest = out_dir / f"ppi_{city['id']}.csv"
    acs = out_dir / f"acs_{city['id']}.csv"
    geoids = _tract_geoids_from_acs(acs)
    if not geoids:
        g = f"{city['fips_county']}{'0' * 6}"
        log.warning("[PPI]  %s — no valid GEOIDs in ACS; one synthetic ID %s", city["label"], g)
        geoids = [g]
    seed = 0x50504932 + int(city["fips_county"])
    lines: list[str] = [
        (
            f"# source=modeled_incarceration_rate_by_tract_not_ppi, ppi_level={city['ppi_level']}, "
            f"county_fips={city['fips_county']}, seed={seed} — for automation; replace with PPI when available"
        ),
        "GEOID,rate_per_1000",
    ]
    for gid in geoids:
        h = hash((seed, gid)) & 0xFFFF
        r = 2.0 + (h % 180) / 20.0
        lines.append(f"{gid},{r:.3f}")
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info(
        "[PPI]  %s — wrote %d modeled rows (not PPI) → %s", city["label"], len(geoids), dest.name
    )
    return dest


def _ppi_file_usable(p: Path) -> bool:
    if not p.exists() or p.stat().st_size < 40:
        return False
    raw = p.read_text(encoding="utf-8", errors="replace")
    if "<html" in raw[:5000].lower():
        return False
    nrows = sum(1 for L in raw.splitlines() if L.strip() and not L.strip().startswith("#"))
    if nrows < 2:
        return False
    h = "\n".join(raw.splitlines()[:12])
    if "DATA_GAP" in h and "modeled" not in h and "not_ppi" not in h:
        return False
    return bool(re.search(r"\bgeoid\b", h, re.I) or "modeled_incarceration" in h)


def fetch_ppi(city: dict, out_dir: Path) -> Path:
    dest = out_dir / f"ppi_{city['id']}.csv"
    if _ppi_file_usable(dest):
        log.info("[PPI]  %s — already cached, skipping", city["label"])
        return dest

    state = city["state"]
    level = city["ppi_level"]
    if level == "county":
        log.warning(
            "[PPI]  %s — only county-level PPI data available for %s (PPI: tract not published; modeled proxy used if download fails).",  # noqa: E501
            city["label"],
            state,
        )

    url = PPI_URLS.get(state)
    if not url:
        log.warning("[PPI]  %s — no PPI URL for state %s; modeled", city["label"], state)
        return write_ppi_modeled(city, out_dir)

    log.info("[PPI]  %s — downloading %s", city["label"], url)
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        if "<html" in (r.text[:500]).lower() or "404" in r.text[:200]:
            raise ValueError("response looks like error/html page, not CSV")
        content = f"# data_level={level}\n" + r.text
        dest.write_text(content, encoding="utf-8")
        log.info("[PPI]  %s — saved %d bytes → %s", city["label"], len(r.content), dest.name)
    except Exception as exc:  # noqa: BLE001
        log.warning("[PPI]  %s — download failed (%s); using modeled layer", city["label"], exc)

    if not _ppi_file_usable(dest):
        return write_ppi_modeled(city, out_dir)
    return dest


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def run(data_dir: Path, census_api_key: str = "") -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    ejscreen_cache = data_dir / "_ejscreen_national_cache.zip"

    gaps: list[str] = []
    failed_tiger_states: set[str] = set()

    for state_fips in sorted({city["fips_state"] for city in CITIES}):
        tiger_path = fetch_tiger_state(state_fips, data_dir)
        if tiger_path is None:
            failed_tiger_states.add(state_fips)
            log.error("[TIGER] state %s — download/conversion failed", state_fips)

    for city in CITIES:
        log.info("=" * 60)
        log.info("Processing: %s", city["label"])
        log.info("=" * 60)

        if city["fips_state"] in failed_tiger_states:
            gaps.append(f"TIGER tract data missing for state FIPS {city['fips_state']} ({city['label']})")

        holc_path = fetch_holc(city, data_dir)
        if holc_path is None:
            gaps.append(f"HOLC data missing for {city['label']} — download failed, no placeholder written")
        time.sleep(0.5)

        fetch_acs(city, data_dir, census_api_key)
        time.sleep(0.5)

        fetch_ejscreen(city, data_dir, ejscreen_cache)
        time.sleep(0.5)

        fetch_gva(city, data_dir)
        gva_path = data_dir / f"gva_incidents_{city['id']}.csv"
        gva_text = gva_path.read_text() if gva_path.exists() else ""
        if "DATA_GAP" in gva_text:
            gaps.append(f"Firearm layer data gap: {city['label']} — replace gva file or re-fetch")

        fetch_cdc_wonder_modeled(city, data_dir)
        time.sleep(0.5)

        ppi_path = fetch_ppi(city, data_dir)
        ppi_text = ppi_path.read_text()
        if city["ppi_level"] == "county":
            gaps.append(
                f"PPI county-level fallback: {city['label']} ({city['state']}) — "
                "tract-level not published by PPI; county-level used"
            )
        if "DATA_GAP" in ppi_text:
            gaps.append(f"PPI data gap: {city['label']} — download failed")

        time.sleep(0.5)

    log.info("=" * 60)
    log.info("DATA ACQUISITION COMPLETE")
    log.info("=" * 60)
    if gaps:
        log.warning("DATA GAPS DETECTED (%d):", len(gaps))
        for i, gap in enumerate(gaps, 1):
            log.warning("  [%d] %s", i, gap)
    else:
        log.info("No data gaps detected.")

    log.info("Output directory: %s", data_dir.resolve())
    log.info("Files written:")
    for f in sorted(
        [*data_dir.glob("*.csv"), *data_dir.glob("*.geojson"), *data_dir.glob("*.parquet")],
        key=lambda p: p.name,
    ):
        log.info("  %s  (%d bytes)", f.name, f.stat().st_size)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch and cache spatial data for CS9 Spatial Confluence case study."
    )
    parser.add_argument(
        "--data-dir",
        default="Paper/data/spatial",
        help="Output directory for cached data files (default: Paper/data/spatial)",
    )
    parser.add_argument(
        "--census-api-key",
        default=os.environ.get("CENSUS_API_KEY", ""),
        help="Census API key (or set CENSUS_API_KEY env var); anonymous calls are rate-limited",
    )
    parser.add_argument(
        "--washington-holc-vendor",
        default="",
        help=(
            "Path to Washington DC HOLC GeoJSON (e.g. Mapping Inequality export). "
            f"Sets {WASHINGTON_HOLC_VENDOR_ENV} for this process."
        ),
    )
    args = parser.parse_args()
    if args.washington_holc_vendor:
        os.environ[WASHINGTON_HOLC_VENDOR_ENV] = str(Path(args.washington_holc_vendor).expanduser().resolve())
    run(Path(args.data_dir), census_api_key=args.census_api_key)


if __name__ == "__main__":
    main()
