"""Query GDELT Global Knowledge Graph for per-axis theme coverage, 1979–2024.

This script queries the GDELT 2.0 Global Knowledge Graph (GKG) BigQuery
public dataset for monthly per-theme article coverage, grouped into four
identity axes (race, gender, religion, sexuality) plus a total-coverage
denominator.  Each axis is normalized as a share of total news coverage
(compositionally bounded), which also closes the open-system problem noted
in the Parseval discussion: GT search-volume indices are not compositionally
bounded, but GDELT per-article theme shares are.

Usage
-----
Option A — BigQuery Python client (requires google-cloud-bigquery):
    python3 Paper/scripts/gdelt_per_axis_query.py --method bigquery

Option B — Manual BigQuery console:
    Copy the SQL from gdelt_query.sql (printed below) into the BigQuery
    console at https://console.cloud.google.com/bigquery, run it against
    the public `gdelt-bq.gdeltv2.gkg` table, and export the result as
    `Paper/data/raw/gdelt_per_axis_raw.csv`.

Output
------
Paper/data/raw/gdelt_per_axis_raw.csv
    Columns: year_month, race_count, gender_count, religion_count,
             sexuality_count, total_count
    Period:  Monthly, 2013-04 to 2024-12 (GKG v2 coverage begins April 2013)
    Source:  GDELT 2.0 GKG BigQuery public dataset

Preprocessing
-------------
Run `make data-refresh` (which calls preprocess_spectral_data.py) after
retrieving the raw CSV.  This normalises each axis to a share of
total_count and writes Paper/data/gdelt_per_axis.csv.

Theme taxonomy
--------------
| Axis       | GDELT Theme Codes (prefix-matched)                           |
|------------|--------------------------------------------------------------|
| Race       | DISCRIMINATION, CIVIL_RIGHTS, RACE_RELATIONS, PROTEST,      |
|            | RACIAL (all subtypes), ETHNICITY                             |
| Gender     | WOMEN, GENDER_DISCRIMINATION, FEMINISM, SEXUAL_HARASSMENT    |
| Religion   | RELIGION (all subtypes), RELIGIOUS_RIGHTS, EVANGELICAL,      |
|            | PRAYER                                                       |
| Sexuality  | LGBTQ, GAY_RIGHTS, TRANSGENDER, HOMOSEXUAL                  |
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

GDELT_SQL = """
-- GDELT GKG v2 per-axis monthly theme coverage, 2013-04 to 2024-12
-- Table: gdelt-bq.gdeltv2.gkg  (GKG v2 coverage begins April 2013)
-- Run in BigQuery console at https://console.cloud.google.com/bigquery
-- Free tier: first 1 TB/month of queries are free.
-- Estimated scan: ~100-300 GB (will use ~0.1-0.3 TB of free quota).
-- Export result as CSV and save to Paper/data/raw/gdelt_per_axis_raw.csv
SELECT
  FORMAT_DATE('%Y-%m', DATE(PARSE_TIMESTAMP('%Y%m%d%H%M%S',
      CAST(DATE AS STRING)))) AS year_month,
  COUNTIF(REGEXP_CONTAINS(LOWER(V2Themes),
      r'discrimination|civil_rights|race_relations|racial|ethnicity'))    AS race_count,
  COUNTIF(REGEXP_CONTAINS(LOWER(V2Themes),
      r'women|gender_discrimination|feminism|sexual_harassment'))          AS gender_count,
  COUNTIF(REGEXP_CONTAINS(LOWER(V2Themes),
      r'religion|religious_rights|evangelical|prayer'))                   AS religion_count,
  COUNTIF(REGEXP_CONTAINS(LOWER(V2Themes),
      r'lgbtq|gay_rights|transgender|homosexual'))                        AS sexuality_count,
  COUNT(*) AS total_count
FROM `gdelt-bq.gdeltv2.gkg`
WHERE
  SourceCommonName IS NOT NULL
  AND DocumentIdentifier IS NOT NULL
  AND DATE >= '20130401000000'
  AND DATE <= '20241231235959'
GROUP BY year_month
ORDER BY year_month
"""

GDELT_SQL_V1 = """
-- GDELT 1.0 GKG (wider historical coverage back to 1979)
-- Table: gdelt-bq.full.events  (fallback if GKGv2 lacks pre-2013 rows)
-- Use the GKG table for theme-level access.
SELECT
  FORMAT_DATE('%Y-%m', PARSE_DATE('%Y%m%d', CAST(SQLDATE AS STRING))) AS year_month,
  COUNTIF(REGEXP_CONTAINS(Actor1EthnicCode, r'.+'))   AS race_proxy_count,
  COUNT(*) AS total_count
FROM `gdelt-bq.full.events`
WHERE
  SQLDATE BETWEEN 19790101 AND 20121231
GROUP BY year_month
ORDER BY year_month
"""


def _print_sql() -> None:
    print("\n" + "=" * 72)
    print("GDELT GKG BigQuery SQL (copy into console at bigquery.cloud.google.com)")
    print("=" * 72)
    print(GDELT_SQL)
    print("=" * 72 + "\n")
    print("Export the result as CSV and save to:")
    print(f"  {RAW / 'gdelt_per_axis_raw.csv'}\n")
    print("Then run:  make data-refresh")


def _run_bigquery() -> None:
    try:
        from google.cloud import bigquery  # type: ignore[import]
    except ImportError:
        print("ERROR: google-cloud-bigquery not installed.")
        print("Install with:  pip install google-cloud-bigquery")
        print("Or use --method console and run the SQL manually.")
        sys.exit(1)

    print("Connecting to BigQuery public dataset (gdelt-bq.gdeltv2.gkg)...")
    print("This uses the BigQuery free tier (1 TB/month).")
    print("Estimated query size: ~50–200 GB depending on date range.")

    client = bigquery.Client()
    RAW.mkdir(parents=True, exist_ok=True)
    out = RAW / "gdelt_per_axis_raw.csv"

    job = client.query(GDELT_SQL)
    df = job.to_dataframe()
    df.to_csv(out, index=False)
    print(f"Wrote {len(df)} rows to {out}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Retrieve GDELT per-axis theme coverage data."
    )
    parser.add_argument(
        "--method",
        choices=["console", "bigquery"],
        default="console",
        help="'console' prints SQL for manual execution; 'bigquery' runs via Python client.",
    )
    args = parser.parse_args()

    if args.method == "console":
        _print_sql()
    else:
        _run_bigquery()


if __name__ == "__main__":
    main()
