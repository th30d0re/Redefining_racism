#!/usr/bin/env python3
"""
Download new SCOTUS case PDFs (Tier 1 + 2 + 3) and convert to markdown via markitdown.

Run from the repository root:
    python3 Paper/scripts/download_new_scotus_cases.py [--tiers 1 2 3] [--dry-run]

The script:
  1. Searches Internet Archive `us-supreme-court` collection for each case.
  2. Falls back to hard-coded URLs (LOC, CourtListener, SCOTUS.gov) for cases not on IA.
  3. Saves PDFs to Paper/research/ia_scotus_pdfs/{slug}_{year}.pdf.
  4. Converts with markitdown → Paper/research/markdown_cases/{slug}_{year}.md.
  5. Logs results to a JSON manifest appended to Paper/research/ia_scotus_pdfs/download_manifest.json.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR  = ROOT / "research" / "ia_scotus_pdfs"
MD_DIR   = ROOT / "research" / "markdown_cases"
MANIFEST = PDF_DIR / "download_manifest.json"

ADV  = "https://archive.org/advancedsearch.php"
META = "https://archive.org/metadata/{identifier}"
DL   = "https://archive.org/download/{identifier}/{filename}"

# ── Case registry ─────────────────────────────────────────────────────────────
# Each entry: (case_name, year, tier, cite_keys, cluster, chapters, url_override_or_None, lucene_override_or_None)

CASES: list[dict] = [
    # ── Tier 1 ──────────────────────────────────────────────────────────────
    {
        "case": "Dred Scott v. Sandford",
        "year": 1857,
        "tier": 1,
        "cite_keys": ["dredscott", "fehrenbacher"],
        "cluster": "racial_classification",
        "chapters": ["ch1", "ch2", "ch10"],
        "url": "https://tile.loc.gov/storage-services/service/ll/usrep/usrep060/usrep060393/usrep060393.pdf",
    },
    {
        "case": "Loving v. Virginia",
        "year": 1967,
        "tier": 1,
        "cite_keys": ["loving_v_virginia_record_1967", "bazile_opinion_1965"],
        "cluster": "reconstruction_amendments",
        "chapters": ["ch3"],
        "lucene": 'title:Loving AND title:Virginia AND year:1967',
    },
    {
        "case": "DeShaney v. Winnebago County",
        "year": 1989,
        "tier": 1,
        "cite_keys": ["deshaney"],
        "cluster": "carceral_enforcement",
        "chapters": ["ch6", "ch10", "ch13"],
        "lucene": 'title:DeShaney AND title:Winnebago',
    },
    {
        "case": "Town of Castle Rock v. Gonzales",
        "year": 2005,
        "tier": 1,
        "cite_keys": ["castlerock"],
        "cluster": "carceral_enforcement",
        "chapters": ["ch6", "ch10", "ch13"],
        "lucene": 'title:"Castle Rock" AND title:Gonzales AND year:2005',
    },
    {
        "case": "Washington v. Davis",
        "year": 1976,
        "tier": 1,
        "cite_keys": ["tel_wash_v_davis"],
        "cluster": "intent_doctrine",
        "chapters": ["ch11"],
        "lucene": 'title:Washington AND title:Davis AND year:1976',
    },
    {
        "case": "Village of Arlington Heights v. Metropolitan Housing Development Corp.",
        "year": 1977,
        "tier": 1,
        "cite_keys": ["tel_arlington_heights"],
        "cluster": "intent_doctrine",
        "chapters": ["ch11"],
        "lucene": 'title:"Arlington Heights" AND title:Metropolitan AND year:1977',
    },
    {
        "case": "New York State Rifle & Pistol Association v. Bruen",
        "year": 2022,
        "tier": 1,
        "cite_keys": ["bruen"],
        "cluster": "second_amendment",
        "chapters": ["ch10"],
        "url": "https://www.supremecourt.gov/opinions/21pdf/20-843_7j80.pdf",
    },
    {
        "case": "Dobbs v. Jackson Women's Health Organization",
        "year": 2022,
        "tier": 1,
        "cite_keys": ["dobbs"],
        "cluster": "gendered_kernel",
        "chapters": ["ch4", "ch18"],
        "url": "https://www.supremecourt.gov/opinions/21pdf/19-1392_6j37.pdf",
    },
    # ── Tier 1 — additional cite-key cases found during extraction ──────────
    {
        "case": "Marbury v. Madison",
        "year": 1803,
        "tier": 1,
        "cite_keys": ["marbury_1803"],
        "cluster": "reconstruction_amendments",
        "chapters": ["ch11"],
        "url": "https://tile.loc.gov/storage-services/service/ll/usrep/usrep005/usrep005137/usrep005137.pdf",
    },
    {
        "case": "Perry v. United States",
        "year": 1935,
        "tier": 1,
        "cite_keys": ["perry_v_us_1935"],
        "cluster": "macroeconomics_finance",
        "chapters": ["ch13"],
        "lucene": 'title:Perry AND title:"United States" AND year:1935',
    },
    {
        "case": "Richmond Newspapers v. Virginia",
        "year": 1980,
        "tier": 1,
        "cite_keys": ["richmond_newspapers_1980"],
        "cluster": "first_amendment",
        "chapters": ["ch6_fn"],
        "lucene": 'title:"Richmond Newspapers" AND title:Virginia AND year:1980',
    },
    {
        "case": "United States v. Rahimi",
        "year": 2024,
        "tier": 1,
        "cite_keys": ["rahimi2024"],
        "cluster": "second_amendment",
        "chapters": ["ch10"],
        "url": "https://www.supremecourt.gov/opinions/23pdf/22-915_7425.pdf",
    },
    # ── Tier 2 ──────────────────────────────────────────────────────────────
    {
        "case": "Bradwell v. Illinois",
        "year": 1873,
        "tier": 2,
        "cite_keys": [],
        "cluster": "gendered_kernel",
        "chapters": ["ch4"],
        "lucene": 'title:Bradwell AND title:Illinois AND year:1873',
    },
    {
        "case": "Muller v. Oregon",
        "year": 1908,
        "tier": 2,
        "cite_keys": [],
        "cluster": "gendered_kernel",
        "chapters": ["ch4"],
        "lucene": 'title:Muller AND title:Oregon AND year:1908',
    },
    {
        "case": "Reed v. Reed",
        "year": 1971,
        "tier": 2,
        "cite_keys": [],
        "cluster": "gendered_kernel",
        "chapters": ["ch4"],
        "lucene": 'title:Reed AND title:Reed AND year:1971',
    },
    {
        "case": "Roe v. Wade",
        "year": 1973,
        "tier": 2,
        "cite_keys": [],
        "cluster": "gendered_kernel",
        "chapters": ["ch4"],
        "lucene": 'title:Roe AND title:Wade AND year:1973',
    },
    {
        "case": "Relf v. Weinberger",
        "year": 1974,
        "tier": 2,
        "cite_keys": [],
        "cluster": "gendered_kernel",
        "chapters": ["ch4"],
        # D.C. Circuit case — not in SCOTUS collection; use CourtListener
        "url": "https://storage.courtlistener.com/recap/gov.uscourts.dcd.69484/gov.uscourts.dcd.69484.1.0.pdf",
    },
    {
        "case": "Madrigal v. Quilligan",
        "year": 1978,
        "tier": 2,
        "cite_keys": [],
        "cluster": "gendered_kernel",
        "chapters": ["ch4"],
        # Federal district court (C.D. Cal.) — use CourtListener
        "url": "https://storage.courtlistener.com/recap/gov.uscourts.cacd.49795/gov.uscourts.cacd.49795.1.0.pdf",
    },
    {
        "case": "Obergefell v. Hodges",
        "year": 2015,
        "tier": 2,
        "cite_keys": [],
        "cluster": "buffer_class_expansion",
        "chapters": ["ch13"],
        "url": "https://www.supremecourt.gov/opinions/14pdf/14-556_3204.pdf",
    },
    # ── Tier 3 — Bundle A: Intent-Doctrine Complex ──────────────────────────
    {
        "case": "Personnel Administrator of Massachusetts v. Feeney",
        "year": 1979,
        "tier": 3,
        "cite_keys": [],
        "cluster": "intent_doctrine",
        "chapters": ["ch11"],
        "lucene": 'title:Feeney AND title:Massachusetts AND year:1979',
    },
    {
        "case": "Mobile v. Bolden",
        "year": 1980,
        "tier": 3,
        "cite_keys": [],
        "cluster": "voting_rights",
        "chapters": ["ch7"],
        "lucene": 'title:Bolden AND title:Mobile AND year:1980',
    },
    {
        "case": "City of Richmond v. J.A. Croson Co.",
        "year": 1989,
        "tier": 3,
        "cite_keys": [],
        "cluster": "affirmative_action",
        "chapters": ["ch11"],
        "lucene": 'title:Richmond AND title:Croson AND year:1989',
    },
    {
        "case": "Adarand Constructors v. Pena",
        "year": 1995,
        "tier": 3,
        "cite_keys": [],
        "cluster": "affirmative_action",
        "chapters": ["ch11"],
        "lucene": 'title:Adarand AND title:Pena AND year:1995',
    },
    # ── Tier 3 — Bundle B: Affirmative-Action Terminal Arc ──────────────────
    {
        "case": "Gratz v. Bollinger",
        "year": 2003,
        "tier": 3,
        "cite_keys": [],
        "cluster": "affirmative_action",
        "chapters": ["ch11"],
        "lucene": 'title:Gratz AND title:Bollinger AND year:2003',
    },
    {
        "case": "Schuette v. Coalition to Defend Affirmative Action",
        "year": 2014,
        "tier": 3,
        "cite_keys": [],
        "cluster": "affirmative_action",
        "chapters": ["ch11"],
        "lucene": 'title:Schuette AND year:2014',
    },
    {
        "case": "Students for Fair Admissions v. Harvard",
        "year": 2023,
        "tier": 3,
        "cite_keys": [],
        "cluster": "affirmative_action",
        "chapters": ["ch11"],
        "url": "https://www.supremecourt.gov/opinions/22pdf/20-1199_hgdj.pdf",
    },
    # ── Tier 3 — Bundle C: Use-of-Force Doctrine ────────────────────────────
    {
        "case": "Tennessee v. Garner",
        "year": 1985,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch6"],
        "lucene": 'title:Garner AND title:Tennessee AND year:1985',
    },
    {
        "case": "Graham v. Connor",
        "year": 1989,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch6"],
        "lucene": 'title:Graham AND title:Connor AND year:1989',
    },
    {
        "case": "Whren v. United States",
        "year": 1996,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch6", "ch9"],
        "lucene": 'title:Whren AND title:"United States" AND year:1996',
    },
    {
        "case": "Scott v. Harris",
        "year": 2007,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch6"],
        "lucene": 'title:Scott AND title:Harris AND year:2007',
    },
    {
        "case": "Rodriguez v. United States",
        "year": 2015,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch6"],
        "lucene": 'title:Rodriguez AND title:"United States" AND year:2015',
    },
    # ── Tier 3 — Bundle D: Juvenile-Sentencing Trilogy ──────────────────────
    {
        "case": "Roper v. Simmons",
        "year": 2005,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch9"],
        "lucene": 'title:Roper AND title:Simmons AND year:2005',
    },
    {
        "case": "Graham v. Florida",
        "year": 2010,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch9"],
        "lucene": 'title:Graham AND title:Florida AND year:2010',
    },
    {
        "case": "Miller v. Alabama",
        "year": 2012,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch9"],
        "lucene": 'title:Miller AND title:Alabama AND year:2012',
    },
    {
        "case": "Ramos v. Louisiana",
        "year": 2020,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch9"],
        "url": "https://www.supremecourt.gov/opinions/19pdf/18-5924_o75q.pdf",
    },
    # ── Tier 3 — Bundle E: VRA Post-Shelby Arc ──────────────────────────────
    {
        "case": "Rucho v. Common Cause",
        "year": 2019,
        "tier": 3,
        "cite_keys": [],
        "cluster": "voting_rights",
        "chapters": ["ch7"],
        "url": "https://www.supremecourt.gov/opinions/18pdf/18-422_9ol1.pdf",
    },
    {
        "case": "Brnovich v. Democratic National Committee",
        "year": 2021,
        "tier": 3,
        "cite_keys": [],
        "cluster": "voting_rights",
        "chapters": ["ch7"],
        "url": "https://www.supremecourt.gov/opinions/20pdf/19-1257_g204.pdf",
    },
    {
        "case": "Allen v. Milligan",
        "year": 2023,
        "tier": 3,
        "cite_keys": [],
        "cluster": "voting_rights",
        "chapters": ["ch7"],
        "url": "https://www.supremecourt.gov/opinions/22pdf/21-1086_1co6.pdf",
    },
    {
        "case": "Moore v. Harper",
        "year": 2023,
        "tier": 3,
        "cite_keys": [],
        "cluster": "voting_rights",
        "chapters": ["ch7"],
        "url": "https://www.supremecourt.gov/opinions/22pdf/21-1271_3f14.pdf",
    },
    # ── Tier 3 — Bundle F: Batson-Purkett Terminal Arc ──────────────────────
    {
        "case": "Flowers v. Mississippi",
        "year": 2019,
        "tier": 3,
        "cite_keys": [],
        "cluster": "jury_selection",
        "chapters": ["ch9"],
        "url": "https://www.supremecourt.gov/opinions/18pdf/17-9572_k537.pdf",
    },
    # ── Tier 3 — Bundle G: Religious-Exemption / Dobbs-Era Counter-Reform ───
    {
        "case": "Trump v. Hawaii",
        "year": 2018,
        "tier": 3,
        "cite_keys": [],
        "cluster": "racial_classification",
        "chapters": ["ch13"],
        "url": "https://www.supremecourt.gov/opinions/17pdf/17-965_h315.pdf",
    },
    {
        "case": "Kennedy v. Bremerton School District",
        "year": 2022,
        "tier": 3,
        "cite_keys": [],
        "cluster": "first_amendment",
        "chapters": ["ch18"],
        "url": "https://www.supremecourt.gov/opinions/21pdf/21-418_i425.pdf",
    },
    {
        "case": "303 Creative LLC v. Elenis",
        "year": 2023,
        "tier": 3,
        "cite_keys": [],
        "cluster": "first_amendment",
        "chapters": ["ch18"],
        "url": "https://www.supremecourt.gov/opinions/22pdf/21-476_c185.pdf",
    },
    # ── Tier 3 — Bundle H: Excessive-Fines / Civil-Asset Architecture ───────
    {
        "case": "Timbs v. Indiana",
        "year": 2019,
        "tier": 3,
        "cite_keys": [],
        "cluster": "carceral_enforcement",
        "chapters": ["ch9"],
        "url": "https://www.supremecourt.gov/opinions/18pdf/17-1091_5536.pdf",
    },
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _slug(name: str) -> str:
    return re.sub(r"[^\w]+", "_", name.lower()).strip("_")


def _curl(url: str, dest: Path, timeout: int = 120) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["curl", "-fsSL", "--retry", "3", "--retry-delay", "2",
         "--max-time", str(timeout), "-o", str(dest), url],
        check=True, capture_output=True,
    )


def _ia_search(lucene: str) -> list[dict]:
    params = urllib.parse.urlencode({
        "q": f"({lucene}) AND collection:(us-supreme-court)",
        "fl[]": "identifier,title,year",
        "rows": 5,
        "output": "json",
    })
    result = subprocess.run(
        ["curl", "-fsSL", "--max-time", "30", f"{ADV}?{params}"],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(result.stdout)
    return data.get("response", {}).get("docs", [])


def _ia_pick_pdf(identifier: str) -> tuple[str, str] | None:
    result = subprocess.run(
        ["curl", "-fsSL", "--max-time", "30",
         META.format(identifier=urllib.parse.quote(identifier))],
        capture_output=True, text=True, check=True,
    )
    meta = json.loads(result.stdout)
    pdfs = [f for f in (meta.get("files") or []) if f.get("name", "").lower().endswith(".pdf")]
    if not pdfs:
        return None
    exact = f"{identifier}.pdf"
    for f in pdfs:
        if f["name"] == exact:
            return identifier, exact
    best = max(pdfs, key=lambda f: int(f.get("size") or 0))
    return identifier, best["name"]


def _year_ok(doc: dict, year: int) -> bool:
    y = doc.get("year")
    if not y:
        return True
    try:
        return abs(int(str(y)) - year) <= 1
    except (ValueError, TypeError):
        return True


def _markitdown(pdf: Path, md: Path) -> None:
    result = subprocess.run(
        ["markitdown", str(pdf)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr[:500])
    md.parent.mkdir(parents=True, exist_ok=True)
    md.write_text(result.stdout, encoding="utf-8")


# ── Main ─────────────────────────────────────────────────────────────────────

def process_case(entry: dict, dry_run: bool) -> dict:
    case  = entry["case"]
    year  = entry["year"]
    tier  = entry["tier"]
    slug  = _slug(case)
    pdf   = PDF_DIR / f"{slug}_{year}.pdf"
    md    = MD_DIR  / f"{slug}_{year}.md"

    result: dict = {
        "case": case,
        "year": year,
        "tier": tier,
        "slug": f"{slug}_{year}",
        "cite_keys": entry.get("cite_keys", []),
        "cluster": entry.get("cluster", ""),
        "chapters": entry.get("chapters", []),
        "status": "pending",
    }

    # Skip if already done
    if pdf.exists() and pdf.stat().st_size > 4096 and md.exists() and md.stat().st_size > 512:
        result["status"] = "skipped_exists"
        result["pdf"] = str(pdf.relative_to(ROOT))
        result["md"]  = str(md.relative_to(ROOT))
        print(f"[skip]  {case} ({year})")
        return result

    if dry_run:
        result["status"] = "dry_run"
        print(f"[dry]   {case} ({year}) -> {slug}_{year}")
        return result

    # ── Download PDF ─────────────────────────────────────────────────────────
    url = entry.get("url")
    lucene = entry.get("lucene")

    if not pdf.exists() or pdf.stat().st_size <= 4096:
        if url:
            print(f"[url]   {case} ({year})")
            try:
                _curl(url, pdf)
                result["source"] = "direct_url"
                result["pdf_url"] = url
            except subprocess.CalledProcessError as e:
                result["status"] = f"download_error: {e.stderr[:200]}"
                return result
        elif lucene:
            docs = _ia_search(lucene)
            # prefer year-matched hit
            docs_ok = [d for d in docs if _year_ok(d, year)] or docs
            if not docs_ok:
                result["status"] = "no_search_results"
                print(f"[miss]  {case} ({year}) — no IA results for: {lucene}")
                return result
            best = docs_ok[0]
            identifier = best["identifier"]
            picked = _ia_pick_pdf(identifier)
            if not picked:
                result["status"] = "no_pdf_in_item"
                print(f"[miss]  {case} ({year}) — no PDF in item {identifier}")
                return result
            _, fname = picked
            dl_url = DL.format(
                identifier=urllib.parse.quote(identifier),
                filename=urllib.parse.quote(fname),
            )
            print(f"[ia]    {case} ({year}) -> {identifier}")
            try:
                _curl(dl_url, pdf, timeout=300)
                result["source"] = "internet_archive"
                result["identifier"] = identifier
                result["pdf_url"] = dl_url
            except subprocess.CalledProcessError as e:
                result["status"] = f"download_error: {e.stderr[:200]}"
                return result
        else:
            result["status"] = "no_source_configured"
            return result

    if not pdf.exists() or pdf.stat().st_size <= 4096:
        result["status"] = "download_empty"
        return result

    result["pdf"] = str(pdf.relative_to(ROOT))
    result["pdf_bytes"] = pdf.stat().st_size

    # ── Convert to markdown ───────────────────────────────────────────────────
    if not md.exists() or md.stat().st_size <= 512:
        print(f"[md]    converting {pdf.name}")
        try:
            _markitdown(pdf, md)
        except Exception as e:  # noqa: BLE001
            result["status"] = f"markitdown_error: {e}"
            result["pdf"] = str(pdf.relative_to(ROOT))
            return result

    result["status"] = "ok"
    result["md"] = str(md.relative_to(ROOT))
    result["md_bytes"] = md.stat().st_size
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Download + convert new SCOTUS cases.")
    parser.add_argument("--tiers", nargs="+", type=int, default=[1, 2, 3],
                        help="Which tiers to process (default: 1 2 3)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    active = [c for c in CASES if c["tier"] in args.tiers]
    print(f"Processing {len(active)} cases (tiers: {args.tiers})")

    # Load existing manifest
    existing: list[dict] = []
    if MANIFEST.exists():
        try:
            existing = json.loads(MANIFEST.read_text())
        except json.JSONDecodeError:
            pass
    already_slugs = {e.get("slug") for e in existing}

    new_results: list[dict] = []
    for entry in active:
        slug = f"{_slug(entry['case'])}_{entry['year']}"
        if slug in already_slugs:
            print(f"[skip]  {entry['case']} ({entry['year']}) — already in manifest")
            continue
        res = process_case(entry, dry_run=args.dry_run)
        new_results.append(res)
        # persist after each case
        MANIFEST.write_text(json.dumps(existing + new_results, indent=2), encoding="utf-8")
        time.sleep(0.4)

    ok = sum(1 for r in new_results if r["status"] in ("ok", "skipped_exists"))
    total = len(new_results)
    print(f"\nDone. {ok}/{total} cases succeeded.")
    failed = [r for r in new_results if r["status"] not in ("ok", "skipped_exists", "dry_run")]
    if failed:
        print("Failed:")
        for r in failed:
            print(f"  {r['case']} ({r['year']}): {r['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
