"""Retrieve per-axis political identity article counts from the NYT Article Search API.

This script queries the New York Times Article Search API (free, requires API key)
for quarterly article counts on four identity axes (race, gender, religion, sexuality)
and a class-language band, covering 1979–2024.  Results are written to

    Paper/data/raw/nyt_per_axis_raw.csv

which is then preprocessed by preprocess_spectral_data.py (via `make data-refresh`)
into Paper/data/nyt_per_axis.csv with per-axis shares of total coverage.

Why NYT vs. GDELT
-----------------
The NYT Article Search API requires only a free API key (register at
developer.nytimes.com).  GDELT BigQuery requires a GCP project.  NYT coverage
extends back to 1851, giving 45 years of quarterly data (1979–2024) = 180 data
points per axis.  Quarterly resolution (Nyquist: 0.5 yr) is sufficient to detect
dominant periods ≥ 1 yr, covering the race (3.6 yr), gender (6.2 yr), and religion
(8.5 yr) bands found in the SCOTUS Lomb-Scargle analysis.

Setup
-----
1. Register at https://developer.nytimes.com/ (free)
2. Create an app and copy the API key
3. Run:
       python3 Paper/scripts/nyt_per_axis_query.py --api-key YOUR_KEY

   Or set env var NYT_API_KEY and run without --api-key.

Rate limits
-----------
NYT API: 10 requests/minute, ~4,000/day.  This script queries 5 axes ×
45 years × 4 quarters = 900 requests.  With a 6-second inter-request sleep it
completes in ~90 minutes.  Use --start-year / --end-year to resume after
interruption; existing rows in the output CSV are skipped.

Output columns
--------------
year_quarter  : YYYY-QN  (e.g. 1979-Q1)
race_count    : article hits for race/civil-rights query
gender_count  : article hits for gender/women query
religion_count: article hits for religion/evangelical query
sexuality_count: article hits for LGBTQ/gay query
class_count   : article hits for class/economic inequality query
total_count   : sum of all five axis counts (proxy denominator)
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import time
from datetime import date
from pathlib import Path
from typing import Iterator

import requests

ROOT = Path(__file__).resolve().parents[1]
RAW  = ROOT / "data" / "raw"
OUT  = RAW / "nyt_per_axis_raw.csv"

NYT_BASE = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# --- Keyword query strings per axis ----------------------------------------
# These are broad intentionally: we want article *counts*, not precision retrieval.
AXIS_QUERIES: dict[str, str] = {
    "race":      (
        '"civil rights" OR "racial discrimination" OR "race relations" '
        'OR "systemic racism" OR "police brutality" OR "racial justice"'
    ),
    "gender":    (
        '"gender discrimination" OR "women\'s rights" OR feminism '
        'OR "sexual harassment" OR "gender pay gap" OR "Title IX"'
    ),
    "religion":  (
        '"religious freedom" OR "religious rights" OR evangelical '
        'OR "separation of church" OR "prayer in school" OR "religious liberty"'
    ),
    "sexuality": (
        '"gay rights" OR "LGBTQ" OR "same-sex" OR transgender '
        'OR "homosexual" OR "sexual orientation"'
    ),
    "class": (
        '"income inequality" OR "wealth gap" OR "working class" '
        'OR "labor rights" OR "economic inequality" OR "poverty"'
    ),
}

FIELDNAMES = [
    "year_quarter", "race_count", "gender_count",
    "religion_count", "sexuality_count", "class_count", "total_count",
]


def _quarter_dates(year: int, quarter: int) -> tuple[str, str]:
    """Return (begin_date, end_date) strings in YYYYMMDD format for a quarter."""
    starts = {1: (1, 1), 2: (4, 1), 3: (7, 1), 4: (10, 1)}
    ends   = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}
    sm, sd = starts[quarter]
    em, ed = ends[quarter]
    return f"{year}{sm:02d}{sd:02d}", f"{year}{em:02d}{ed:02d}"


def _query_hits(session: requests.Session, api_key: str,
                query: str, begin: str, end: str, retries: int = 3) -> int:
    """Return article hit count for a keyword query over a date range."""
    params = {
        "q":          query,
        "begin_date": begin,
        "end_date":   end,
        "api-key":    api_key,
    }
    for attempt in range(retries):
        try:
            r = session.get(NYT_BASE, params=params, timeout=30)
            if r.status_code == 429:
                # Rate limited — wait and retry
                wait = 65 * (attempt + 1)
                print(f"  Rate limited. Waiting {wait}s ...", flush=True)
                time.sleep(wait)
                continue
            r.raise_for_status()
            data = r.json()
            # NYT API returns either "meta" or "metadata" depending on version
            meta = data["response"].get("meta") or data["response"].get("metadata", {})
            return int(meta["hits"])
        except (requests.RequestException, KeyError, ValueError) as exc:
            print(f"  Warning: {exc} (attempt {attempt+1}/{retries})", flush=True)
            time.sleep(10)
    return -1  # sentinel: query failed


def _load_existing(path: Path) -> set[str]:
    """Return set of year_quarter values already written to the output CSV."""
    if not path.exists():
        return set()
    with path.open() as f:
        reader = csv.DictReader(f)
        return {row["year_quarter"] for row in reader}


def _iter_quarters(start_year: int, end_year: int) -> Iterator[tuple[int, int]]:
    for yr in range(start_year, end_year + 1):
        for q in range(1, 5):
            # Skip future quarters
            begin, _ = _quarter_dates(yr, q)
            if begin > date.today().strftime("%Y%m%d"):
                return
            yield yr, q


def main() -> None:
    parser = argparse.ArgumentParser(description="NYT per-axis article count retrieval")
    parser.add_argument("--api-key", default=os.environ.get("NYT_API_KEY", ""),
                        help="NYT Article Search API key (or set NYT_API_KEY env var)")
    parser.add_argument("--start-year", type=int, default=1979)
    parser.add_argument("--end-year",   type=int, default=2024)
    parser.add_argument("--sleep",      type=float, default=6.5,
                        help="Seconds between requests (default 6.5 → ~9 req/min)")
    args = parser.parse_args()

    if not args.api_key:
        print("ERROR: NYT API key required.")
        print("  Register free at https://developer.nytimes.com/")
        print("  Then:  python3 nyt_per_axis_query.py --api-key YOUR_KEY")
        print("  Or:    export NYT_API_KEY=YOUR_KEY && python3 nyt_per_axis_query.py")
        sys.exit(1)

    RAW.mkdir(parents=True, exist_ok=True)
    existing = _load_existing(OUT)

    total_quarters = (args.end_year - args.start_year + 1) * 4
    axes = list(AXIS_QUERIES.keys())
    # Total requests = total_quarters × 5 axes
    print(f"NYT per-axis query: {args.start_year}–{args.end_year}, "
          f"{total_quarters} quarters × {len(axes)} axes = "
          f"~{total_quarters * len(axes)} requests")
    print(f"Estimated runtime at {args.sleep}s/request: "
          f"~{total_quarters * len(axes) * args.sleep / 60:.0f} min")
    print(f"Output: {OUT}")
    print(f"Existing rows to skip: {len(existing)}\n", flush=True)

    # Open CSV in append mode so we can resume
    write_header = not OUT.exists() or OUT.stat().st_size == 0
    outfile = OUT.open("a", newline="")
    writer = csv.DictWriter(outfile, fieldnames=FIELDNAMES)
    if write_header:
        writer.writeheader()

    session = requests.Session()
    completed = 0

    try:
        for yr, q in _iter_quarters(args.start_year, args.end_year):
            label = f"{yr}-Q{q}"
            if label in existing:
                continue  # resume: skip already-fetched quarters

            begin, end = _quarter_dates(yr, q)
            counts: dict[str, int] = {}

            for axis in axes:
                hits = _query_hits(session, args.api_key,
                                   AXIS_QUERIES[axis], begin, end)
                counts[axis] = hits
                print(f"  {label} {axis:12s}: {hits:>7,} hits", flush=True)
                time.sleep(args.sleep)

            total = sum(v for v in counts.values() if v >= 0)
            row = {
                "year_quarter":    label,
                "race_count":      counts.get("race", -1),
                "gender_count":    counts.get("gender", -1),
                "religion_count":  counts.get("religion", -1),
                "sexuality_count": counts.get("sexuality", -1),
                "class_count":     counts.get("class", -1),
                "total_count":     total,
            }
            writer.writerow(row)
            outfile.flush()
            completed += 1
            print(f"  → {label} written (total={total:,})\n", flush=True)

    finally:
        outfile.close()
        session.close()

    print(f"\nDone. {completed} new quarters written to {OUT}")
    print("Next step: run  make data-refresh  to preprocess into Paper/data/nyt_per_axis.csv")


if __name__ == "__main__":
    main()
