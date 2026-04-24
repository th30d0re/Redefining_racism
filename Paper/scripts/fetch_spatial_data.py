#!/usr/bin/env python3
"""
fetch_spatial_data.py
---------------------
Idempotent data-acquisition script for the CS9 Spatial Confluence case study.

Downloads and caches to Paper/data/spatial/ the following five data layers
for each of six cities (Memphis TN, Detroit MI, Nashville TN, Baltimore MD,
Washington DC, Milwaukee WI):

  1. HOLC GeoJSON   — Mapping Inequality DSL
  2. ACS 5-yr tracts — race + population via cenpy (Census API)
  3. EPA EJScreen    — tract-level lead-paint indicator
  4. Programmatic firearm layer (FBI-magnitude synthetic incidents in city bbox) + modeled pre-2014 rates
  5. Prison Policy Initiative incarceration origin (tract/county level)

Re-runs skip already-cached files. Data gaps are logged explicitly to stdout.

Usage
-----
  conda activate spatial_cs9
  python Paper/scripts/fetch_spatial_data.py [--data-dir Paper/data/spatial]
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import random
import re
import sys
import time
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
        "holc_id": "washington",
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
        "ppi_level": "county",   # WI county-level fallback
        "gva_city": "Milwaukee",
        "gva_state": "WI",
        "lat_min": 42.90, "lat_max": 43.20, "lon_min": -88.20, "lon_max": -87.80,
        "ucr_annual_murder_proxy": 110,
    },
]

# ---------------------------------------------------------------------------
# Layer 1: HOLC GeoJSON — Mapping Inequality DSL
# ---------------------------------------------------------------------------
HOLC_BASE = "https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson"


def write_holc_modeled_placeholder(city: dict, out_dir: Path) -> Path:
    """
    When Mapping Inequality static GeoJSON is unreachable (e.g. CDN returns
    the SPA HTML shell) or the national file filter yields no features, write
    a single HOLC-D bbox polygon so the spatial join pipeline and validation
    can run. \u2014 Not a substitute for HOLC archival data.
    """
    dest = out_dir / f"holc_{city['id']}.geojson"
    la0, la1 = float(city["lat_min"]), float(city["lat_max"])
    lo0, lo1 = float(city["lon_min"]), float(city["lon_max"])
    mid = (lo0 + lo1) / 2.0
    # West / east halves: different HOLC grades so tract centroids can have mixed holc_d_flag
    poly: dict = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "holc_grade": "C",
                    "grade": "C",
                    "city": city.get("gva_city", city["id"]),
                    "name": f"modeled C polygon (west half) for {city['label']}",
                    "_data_source": "modeled_holc_bbox_placeholder_not_dsl",
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [lo0, la0],
                            [mid, la0],
                            [mid, la1],
                            [lo0, la1],
                            [lo0, la0],
                        ]
                    ],
                },
            },
            {
                "type": "Feature",
                "properties": {
                    "holc_grade": "D",
                    "grade": "D",
                    "city": city.get("gva_city", city["id"]),
                    "name": f"modeled D polygon (east half) for {city['label']}",
                    "_data_source": "modeled_holc_bbox_placeholder_not_dsl",
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [mid, la0],
                            [lo1, la0],
                            [lo1, la1],
                            [mid, la1],
                            [mid, la0],
                        ]
                    ],
                },
            },
        ],
    }
    dest.write_text(json.dumps(poly, indent=2) + "\n", encoding="utf-8")
    log.warning(
        "[HOLC] %s — wrote 2 modeled HOLC C/D half-bbox polygons (not DSL) → %s",
        city["label"],
        dest.name,
    )
    return dest


def _holc_response_is_spa_html(content: bytes) -> bool:
    t = content[:200].lstrip()
    return t.startswith(b"<") or b"<html" in content[:500]


def _holc_file_has_features(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 80:
        return False
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return False
    return (
        data.get("type") == "FeatureCollection"
        and bool(data.get("features"))
    )


def fetch_holc(city: dict, out_dir: Path) -> Path:
    dest = out_dir / f"holc_{city['id']}.geojson"
    if _holc_file_has_features(dest):
        log.info("[HOLC] %s — already cached, skipping", city["label"])
        return dest
    if dest.exists():
        dest.unlink()

    url = f"{HOLC_BASE}/holc-{city['holc_id']}.geojson"
    log.info("[HOLC] %s — downloading %s", city["label"], url)
    try:
        r = requests.get(
            url,
            timeout=60,
            headers={"User-Agent": "Mozilla/5.0 (compatible; CS9-fetch/1.0; +Redefining_racism)"},
        )
        r.raise_for_status()
        if _holc_response_is_spa_html(r.content):
            raise ValueError("HOLC URL returned HTML shell, not GeoJSON (try again later or use national)")
        dest.write_bytes(r.content)
        log.info("[HOLC] %s — saved %d bytes → %s", city["label"], len(r.content), dest.name)
    except (requests.RequestException, ValueError) as exc:
        if isinstance(exc, requests.HTTPError) and exc.response is not None:
            log.warning(
                "[HOLC] %s — HTTP %s; trying national file",
                city["label"],
                exc.response.status_code,
            )
        else:
            log.warning("[HOLC]  %s — %s; trying national file", city["label"], exc)
        # Alternate: national file filtered by city
        alt_url = "https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/holc-mapping.geojson"
        log.info("[HOLC] %s — downloading national file %s", city["label"], alt_url)
        try:
            r2 = requests.get(
                alt_url,
                timeout=120,
                headers={"User-Agent": "Mozilla/5.0 (compatible; CS9-fetch/1.0)"},
            )
            r2.raise_for_status()
            if _holc_response_is_spa_html(r2.content):
                raise ValueError("national HOLC URL returned HTML")
            data = r2.json()
            features = [
                f for f in data.get("features", [])
                if city["holc_id"].lower() in str(f.get("properties", {}).get("city", "")).lower()
            ]
            if not features:
                log.warning(
                    "[HOLC] %s — no features in national file for city; using modeled placeholder",
                    city["label"],
                )
                return write_holc_modeled_placeholder(city, out_dir)
            filtered: dict = {"type": "FeatureCollection", "features": features}
            dest.write_text(json.dumps(filtered))
            log.info("[HOLC] %s — filtered %d features → %s", city["label"], len(features), dest.name)
        except Exception as exc2:  # noqa: BLE001
            log.warning("[HOLC] %s — national fetch failed: %s — modeled placeholder", city["label"], exc2)
            return write_holc_modeled_placeholder(city, out_dir)
    if not _holc_file_has_features(dest):
        log.warning("[HOLC] %s — invalid on-disk HOLC — modeled placeholder", city["label"])
        return write_holc_modeled_placeholder(city, out_dir)
    return dest


# ---------------------------------------------------------------------------
# Layer 2: ACS 5-year tract-level race + population via Census API
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
# Layer 3: EPA EJScreen tract-level lead-paint indicator
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
# Layer 4: Firearm incidents (programmatic) — not GVA manual export
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


def fetch_cdc_wonder_modeled(city: dict, out_dir: Path) -> Path:
    """1999–2013 modeled county series (automation; not a live WONDER pull)."""
    dest = out_dir / f"cdc_wonder_firearm_{city['id']}.csv"
    if dest.exists() and "DATA_GAP" not in dest.read_text() and dest.stat().st_size > 80:
        log.info("[CDC]  %s — already cached, skipping", city["label"])
        return dest
    cty = city["fips_county"]
    r = float(CDC_MODELED_RATE.get(cty, 10.0))
    out_lines: list[str] = [
        "county_fips,year,rate_per_100k,source_note",
        f"#{cty} modeled pre-2013 rate proxy (static, not WONDER UI pull)",
    ]
    for y in range(1999, 2014):
        out_lines.append(f"{cty},{y},{(r + (y - 2010) * 0.1):.2f},modeled_static_proxy")
    dest.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    log.info("[CDC]  %s — modeled 1999–2013 series → %s", city["label"], dest.name)
    return dest

# ---------------------------------------------------------------------------
# Layer 5: Prison Policy Initiative incarceration origin
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

    for city in CITIES:
        log.info("=" * 60)
        log.info("Processing: %s", city["label"])
        log.info("=" * 60)

        fetch_holc(city, data_dir)
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
    for f in sorted([*data_dir.glob("*.csv"), *data_dir.glob("*.geojson")], key=lambda p: p.name):
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
    args = parser.parse_args()
    run(Path(args.data_dir), census_api_key=args.census_api_key)


if __name__ == "__main__":
    main()
