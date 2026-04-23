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
  4. Gun Violence Archive incidents (2014–present); CDC WONDER fallback
  5. Prison Policy Initiative incarceration origin (tract/county level)

Re-runs skip already-cached files. Data gaps are logged explicitly to stdout.

Usage
-----
  conda activate spatial_cs9
  python Paper/scripts/fetch_spatial_data.py [--data-dir Paper/data/spatial]
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
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
    },
]

# ---------------------------------------------------------------------------
# Layer 1: HOLC GeoJSON — Mapping Inequality DSL
# ---------------------------------------------------------------------------
HOLC_BASE = "https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson"


def fetch_holc(city: dict, out_dir: Path) -> Path:
    dest = out_dir / f"holc_{city['id']}.geojson"
    if dest.exists():
        log.info("[HOLC] %s — already cached, skipping", city["label"])
        return dest

    url = f"{HOLC_BASE}/holc-{city['holc_id']}.geojson"
    log.info("[HOLC] %s — downloading %s", city["label"], url)
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        dest.write_bytes(r.content)
        log.info("[HOLC] %s — saved %d bytes → %s", city["label"], len(r.content), dest.name)
    except requests.HTTPError as exc:
        log.warning(
            "[HOLC] %s — HTTP %s; trying alternate endpoint", city["label"], exc.response.status_code
        )
        # Alternate: national file filtered by city
        alt_url = "https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/holc-mapping.geojson"
        log.info("[HOLC] %s — downloading national file %s", city["label"], alt_url)
        r2 = requests.get(alt_url, timeout=120)
        r2.raise_for_status()
        data = r2.json()
        features = [
            f for f in data.get("features", [])
            if city["holc_id"].lower() in str(f.get("properties", {}).get("city", "")).lower()
        ]
        if not features:
            log.warning(
                "[HOLC] %s — no features found in national file; placeholder written", city["label"]
            )
            dest.write_text(json.dumps({"type": "FeatureCollection", "features": []}))
        else:
            filtered = {"type": "FeatureCollection", "features": features}
            dest.write_text(json.dumps(filtered))
            log.info("[HOLC] %s — filtered %d features → %s", city["label"], len(features), dest.name)
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
EJSCREEN_URL = (
    "https://gaftp.epa.gov/EJSCREEN/2023/EJSCREEN_2023_Tracts_with_AS_CNMI_GU_VI.csv.zip"
)


def fetch_ejscreen(city: dict, out_dir: Path, ejscreen_national_cache: Path) -> Path:
    dest = out_dir / f"ejscreen_{city['id']}.csv"
    if dest.exists():
        log.info("[EJS]  %s — already cached, skipping", city["label"])
        return dest

    # Download national file once
    if not ejscreen_national_cache.exists():
        log.info("[EJS]  Downloading national EJScreen file (~300 MB) …")
        try:
            r = requests.get(EJSCREEN_URL, timeout=300, stream=True)
            r.raise_for_status()
            ejscreen_national_cache.write_bytes(r.content)
            log.info("[EJS]  National file saved → %s", ejscreen_national_cache.name)
        except Exception as exc:
            log.warning("[EJS]  National download failed: %s; writing stubs", exc)
            dest.write_text("ID,ACSTOTPOP,LDPNT,DSLPM,CANCR,RESP,PTRAF,state_id,county_id\n")
            return dest

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
                    lines = [",".join(fieldnames)]
                    for m in matching:
                        lines.append(",".join(str(m.get(f, "")) for f in fieldnames))
                    dest.write_text("\n".join(lines))
                    log.info("[EJS]  %s — %d tracts → %s", city["label"], len(matching), dest.name)
                else:
                    log.warning("[EJS]  %s — no tracts found for county %s", city["label"], county_fips)
                    dest.write_text("ID,ACSTOTPOP,LDPNT,DSLPM,CANCR,RESP,PTRAF\n")
    except Exception as exc:
        log.warning("[EJS]  %s — filter error: %s", city["label"], exc)
        dest.write_text("ID,ACSTOTPOP,LDPNT,DSLPM,CANCR,RESP,PTRAF\n")
    return dest


# ---------------------------------------------------------------------------
# Layer 4: Gun Violence Archive incidents (2014–present)
# ---------------------------------------------------------------------------
GVA_NOTE = (
    "NOTE: GVA bulk CSV download requires a manual export from https://www.gunviolencearchive.org/. "
    "Incident-level data for 2014–2024 must be downloaded per year via the GVA query interface "
    "and placed at {dest}. For the pre-2014 window, CDC WONDER county-level firearm mortality "
    "(1999–2013) is used as a fallback (see fetch_cdc_wonder below)."
)

CDC_WONDER_URL = (
    "https://wonder.cdc.gov/controller/datarequest/D76"
)


def fetch_gva(city: dict, out_dir: Path) -> Path:
    dest = out_dir / f"gva_incidents_{city['id']}.csv"
    if dest.exists():
        log.info("[GVA]  %s — already cached, skipping", city["label"])
        return dest

    log.warning(
        "[GVA]  %s — GVA requires manual export; data gap logged.\n  %s",
        city["label"],
        GVA_NOTE.format(dest=dest),
    )
    # Write a stub so the notebook can detect data-gap status
    stub = (
        "incident_id,date,state,city_or_county,address,n_killed,n_injured,latitude,longitude\n"
        "# DATA_GAP: GVA requires manual bulk export from https://www.gunviolencearchive.org/\n"
        "# Place yearly CSVs here and re-run fetch_spatial_data.py\n"
        f"# City: {city['label']} | Years: 2014-2024\n"
    )
    dest.write_text(stub)
    return dest


def fetch_cdc_wonder_stub(city: dict, out_dir: Path) -> Path:
    """CDC WONDER fallback for pre-2014 firearm mortality (county-level)."""
    dest = out_dir / f"cdc_wonder_firearm_{city['id']}.csv"
    if dest.exists():
        log.info("[CDC]  %s — already cached, skipping", city["label"])
        return dest

    log.warning(
        "[CDC]  %s — CDC WONDER requires API key or manual download; writing stub.", city["label"]
    )
    stub = (
        "county_fips,year,firearm_deaths,population,rate_per_100k\n"
        "# DATA_GAP: CDC WONDER county-level firearm mortality 1999-2013\n"
        "# Download from https://wonder.cdc.gov (cause: X72-X74, X93-X95, Y22-Y24, Y35)\n"
        f"# County FIPS: {city['fips_county']}\n"
    )
    dest.write_text(stub)
    return dest


# ---------------------------------------------------------------------------
# Layer 5: Prison Policy Initiative incarceration origin
# ---------------------------------------------------------------------------
PPI_URLS: dict[str, str] = {
    "MD": "https://www.prisonpolicy.org/origin/md/2020/maryland.csv",
    "MI": "https://www.prisonpolicy.org/origin/mi/2020/michigan.csv",
    "DC": "https://www.prisonpolicy.org/origin/dc/2020/dc.csv",
    "TN": "https://www.prisonpolicy.org/origin/tn/2020/tennessee.csv",  # county-level
    "WI": "https://www.prisonpolicy.org/origin/wi/2020/wisconsin.csv",  # county-level
}

PPI_COUNTY_LEVEL_STATES = {"TN", "WI"}


def fetch_ppi(city: dict, out_dir: Path) -> Path:
    dest = out_dir / f"ppi_{city['id']}.csv"
    if dest.exists():
        log.info("[PPI]  %s — already cached, skipping", city["label"])
        return dest

    state = city["state"]
    level = city["ppi_level"]
    if level == "county":
        log.warning(
            "[PPI]  %s — only county-level PPI data available for %s (data-gap: tract-level not published).",
            city["label"],
            state,
        )

    url = PPI_URLS.get(state)
    if not url:
        log.warning("[PPI]  %s — no PPI URL configured for state %s; writing stub", city["label"], state)
        dest.write_text("geoid,incarceration_count,population,rate_per_1000,data_level\n")
        return dest

    log.info("[PPI]  %s — downloading %s", city["label"], url)
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        # Annotate level in first comment line
        content = f"# data_level={level}\n" + r.text
        dest.write_text(content)
        log.info("[PPI]  %s — saved %d bytes → %s", city["label"], len(r.content), dest.name)
    except Exception as exc:
        log.warning("[PPI]  %s — download failed (%s); writing stub", city["label"], exc)
        dest.write_text(
            f"# data_level={level}\n# DATA_GAP: download failed from {url}\n"
            "geoid,incarceration_count,population,rate_per_1000,data_level\n"
        )
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

        gva_path = fetch_gva(city, data_dir)
        gva_text = gva_path.read_text()
        if "DATA_GAP" in gva_text:
            gaps.append(f"GVA pre-2014 gap: {city['label']} — manual export required")

        fetch_cdc_wonder_stub(city, data_dir)
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
    for f in sorted(data_dir.glob("*.csv")) | sorted(data_dir.glob("*.geojson")):
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
