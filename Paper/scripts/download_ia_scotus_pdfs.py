#!/usr/bin/env python3
"""
Download one primary PDF per case from Internet Archive collection us-supreme-court,
using targets from Paper/research/internet_archive_scotus_pull_list.md (Quick-Reference table).

Resolves items via archive.org advancedsearch.php, then picks identifier.pdf or largest .pdf.
Writes manifest JSON alongside downloads.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_PATH = ROOT / "research" / "internet_archive_scotus_pull_list.md"
OUT_DIR = ROOT / "research" / "ia_scotus_pdfs"
MANIFEST_PATH = OUT_DIR / "download_manifest.json"

ADV_SEARCH = "https://archive.org/advancedsearch.php"
META = "https://archive.org/metadata/{identifier}"
DOWNLOAD = "https://archive.org/download/{identifier}/{filename}"

# Cases where `us-supreme-court` search does not resolve: direct PDF URL + short source tag.
# Yick Wo: official U.S. Reports volume 118 from Library of Congress (not party-indexed on IA).
# Foster: slip opinion bundle on IA (full microfilm docket not indexed under "Chatman").
EXTERNAL_PDF_URLS: dict[str, tuple[str, str]] = {
    "Yick Wo v. Hopkins": (
        "https://tile.loc.gov/storage-services/service/ll/usrep/usrep118/usrep118356/usrep118356.pdf",
        "loc_usrep118356",
    ),
    "Foster v. Chatman": (
        "https://archive.org/download/14-8349-6k-47/14-8349_6k47.pdf",
        "ia_14-8349_slip",
    ),
}

# Manual fixes: case name (exact as in MD) -> lucene query WITHOUT collection prefix
LUCENE_OVERRIDES: dict[str, str] = {
    "Civil Rights Cases": 'title:Stanley AND title:Murray AND year:1883',
    "United States v. Reese": 'title:Reese AND title:United AND year:1875',
    # per_scotus index uses 1875 for this volume; closest to 1876 decision
    "Slaughterhouse Cases": "title:Slaughterhouse",
    "United States v. Reynolds": 'title:Reynolds AND title:United AND year:1914',
    "United States v. Armstrong": "title:Armstrong AND year:1996",
    "United States v. Bhagat Singh Thind": "title:Thind AND year:1923",
    "Harper v. Virginia State Board of Elections": 'title:"Harper v. Virginia" AND title:Elections',
    "South Carolina v. Katzenbach": 'title:"South Carolina" AND title:Katzenbach',
    "Green v. County School Board": 'title:Green AND title:"New Kent County"',
    "Jones v. Alfred H. Mayer Co.": "title:Mayer AND title:Jones AND year:1968",
    "San Antonio ISD v. Rodriguez": "title:Rodriguez AND title:San Antonio AND year:1973",
    "Regents of University of California v. Bakke": "title:Bakke AND title:Regents AND year:1978",
    "Parents Involved v. Seattle": 'title:"Parents Involved"',
    "District of Columbia v. Heller": "title:Heller AND title:Columbia AND year:2008",
    "NLRB v. Jones & Laughlin Steel": "title:Laughlin AND title:Jones AND year:1937",
    "McLaurin v. Oklahoma State Regents": "title:McLaurin AND year:1950",
    "Williams v. Mississippi": "title:Williams AND title:Mississippi AND year:1898",
}


def _curl_bytes(url: str, timeout: int = 300) -> bytes:
    """Fetch URL via curl (uses system trust store; avoids broken Python SSL on some macOS installs)."""
    return subprocess.run(
        ["curl", "-fsSL", "--max-time", str(timeout), "-A", "RedefiningRacismResearch/1.0", url],
        check=True,
        capture_output=True,
    ).stdout


def http_get_json(url: str, timeout: int = 120) -> dict:
    return json.loads(_curl_bytes(url, timeout=timeout).decode("utf-8"))


def parse_quick_reference(md_text: str) -> list[tuple[str, int, str]]:
    """Return list of (case_name, year, url_query_decoded) from Quick-Reference table only."""
    rows: list[tuple[str, int, str]] = []
    in_table = False
    for line in md_text.splitlines():
        # Must match the summary table (not cluster tables that include Citation column).
        if re.match(r"^\|\s*Case\s*\|\s*Year\s*\|\s*Direct Search\s*\|", line.strip()):
            in_table = True
            continue
        if not in_table:
            continue
        if re.match(r"^\|\s*-+", line.strip()):
            continue
        if not line.strip().startswith("|"):
            break
        m = re.match(
            r"\|\s*([^|]+?)\s*\|\s*(\d{4})\s*\|\s*\[archive\.org\]\(https://archive\.org/search\?query=([^)]+)\)",
            line.strip(),
        )
        if not m:
            continue
        name = m.group(1).strip()
        year = int(m.group(2))
        q = urllib.parse.unquote_plus(m.group(3).strip())
        rows.append((name, year, q))
    return rows


def derive_lucene(case_name: str, _fallback_query: str) -> str:
    if case_name in LUCENE_OVERRIDES:
        return LUCENE_OVERRIDES[case_name]
    parts = re.split(r"\s+[Vv]\.\s+", case_name, maxsplit=1)
    if len(parts) == 2:
        left, right = parts[0].strip(), parts[1].strip()
        lu = left.lower().replace(".", "")
        if lu in ("united states", "u s", "us"):
            # US v X -> distinctive token from defendant
            tokens = _significant_tokens(right)
            if not tokens:
                tokens = _significant_tokens(left)
        else:
            tokens = _significant_tokens(left)[:1] + _significant_tokens(right)[:1]
            tokens = [t for t in tokens if t]
    else:
        tokens = _significant_tokens(case_name)[:2]
    if not tokens:
        return _fallback_query.replace(" ", " AND ")
    clauses = [f"title:{_escape_solr(t)}" for t in tokens[:3]]
    return " AND ".join(clauses)


def _escape_solr(s: str) -> str:
    if not s:
        return s
    if " " in s or "&" in s:
        return '"' + s.replace('"', r"\"") + '"'
    return s


_STOP = {
    "the",
    "a",
    "an",
    "of",
    "and",
    "for",
    "in",
    "on",
    "at",
    "to",
    "v",
    "ex",
    "rel",
    "alias",
    "track",
    "no",
    "nos",
    "case",
    "cases",
    "board",
    "state",
    "states",
    "united",
    "city",
    "county",
    "election",
    "elections",
    "department",
    "commission",
    "committee",
    "community",
    "schools",
    "steel",
    "fec",
    "nfib",
}


def _significant_tokens(phrase: str) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9'\-]*", phrase)
    out: list[str] = []
    for w in words:
        wl = w.lower()
        if wl in _STOP or len(w) < 2:
            continue
        out.append(w)
    return out


def search_ia(lucene_inner: str, rows: int = 50) -> list[dict]:
    q = f"collection:us-supreme-court AND ({lucene_inner})"
    params = urllib.parse.urlencode({"q": q, "fl": "identifier,title,year", "rows": str(rows), "output": "json"})
    data = http_get_json(f"{ADV_SEARCH}?{params}")
    return data.get("response", {}).get("docs", [])


def pick_best(docs: list[dict], target_year: int, case_name: str) -> dict | None:
    if not docs:
        return None
    name_l = case_name.lower()
    tokens = set(_significant_tokens(case_name.replace(" v. ", " ").replace(" v ", " ")))

    def score(d: dict) -> float:
        title = (d.get("title") or "").lower()
        y = d.get("year")
        s = 0.0
        for t in tokens:
            if len(t) > 2 and t in title:
                s += 5.0
        if y is not None:
            try:
                yi = int(y)
                s -= abs(yi - target_year) * 0.8
                if str(target_year) in d.get("title", ""):
                    s += 12.0
            except (TypeError, ValueError):
                pass
        # Prefer microfilm items with U.S. citation in title for 20th+ century
        if target_year >= 1950 and "u.s." in title and "micro_" in (d.get("identifier") or ""):
            s += 4.0
        if name_l.split(" v. ")[0][:4] in title[:80]:
            s += 2.0
        return s

    ranked = sorted(docs, key=score, reverse=True)
    return ranked[0]


def pick_pdf_file(files: list[dict], identifier: str) -> tuple[str, str] | None:
    pdfs = [f for f in files if f.get("name", "").lower().endswith(".pdf")]
    if not pdfs:
        return None
    exact = f"{identifier}.pdf"
    for f in pdfs:
        if f.get("name") == exact:
            return f["name"], exact
    best = max(pdfs, key=lambda f: int(f.get("size") or 0))
    return best["name"], best["name"]


def download_file(url: str, dest: Path, timeout: int = 600) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = _curl_bytes(url, timeout=timeout)
    dest.write_bytes(data)


def main() -> int:
    md = MD_PATH.read_text(encoding="utf-8")
    cases = parse_quick_reference(md)
    if not cases:
        print("No cases parsed from markdown.", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []

    for case_name, year, fallback_q in cases:
        slug = re.sub(r"[^\w]+", "_", case_name.lower()).strip("_")
        dest = OUT_DIR / f"{slug}_{year}.pdf"
        entry: dict = {
            "case": case_name,
            "year": year,
            "status": "pending",
        }
        if dest.exists() and dest.stat().st_size > 4096:
            entry["status"] = "skipped_exists"
            entry["saved_as"] = str(dest.relative_to(ROOT))
            entry["bytes"] = dest.stat().st_size
            manifest.append(entry)
            print(f"[skip] {case_name} ({year})", flush=True)
            MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            time.sleep(0.05)
            continue

        if case_name in EXTERNAL_PDF_URLS:
            ext_url, ext_tag = EXTERNAL_PDF_URLS[case_name]
            entry["lucene"] = f"EXTERNAL:{ext_tag}"
            try:
                print(f"[external {ext_tag}] {case_name}", flush=True)
                download_file(ext_url, dest, timeout=300)
                entry["status"] = "ok_external"
                entry["pdf_url"] = ext_url
                entry["external_source"] = ext_tag
                entry["saved_as"] = str(dest.relative_to(ROOT))
                entry["bytes"] = dest.stat().st_size
            except Exception as exc:  # noqa: BLE001
                entry["status"] = f"download_error: {exc}"
                entry["pdf_url"] = ext_url
            manifest.append(entry)
            MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            time.sleep(0.2)
            continue

        lucene = derive_lucene(case_name, fallback_q)
        entry["lucene"] = lucene
        docs = search_ia(lucene)
        best = pick_best(docs, year, case_name)
        if not best:
            entry["status"] = "no_search_results"
            manifest.append(entry)
            MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            time.sleep(0.35)
            continue

        ident = best["identifier"]
        entry["identifier"] = ident
        entry["picked_title"] = best.get("title")

        try:
            meta = http_get_json(META.format(identifier=urllib.parse.quote(ident)))
        except (subprocess.CalledProcessError, json.JSONDecodeError, OSError) as e:
            entry["status"] = f"metadata_error: {e}"
            manifest.append(entry)
            MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            time.sleep(0.35)
            continue

        picked = pick_pdf_file(meta.get("files") or [], ident)
        if not picked:
            entry["status"] = "no_pdf_in_item"
            manifest.append(entry)
            MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            time.sleep(0.35)
            continue

        fname, _src_name = picked
        url = DOWNLOAD.format(identifier=urllib.parse.quote(ident), filename=urllib.parse.quote(fname))
        try:
            print(f"[get] {case_name} -> {ident} ({fname[:60]}...)", flush=True)
            download_file(url, dest, timeout=900)
            entry["status"] = "ok"
            entry["pdf_url"] = url
            entry["saved_as"] = str(dest.relative_to(ROOT))
            entry["bytes"] = dest.stat().st_size
        except Exception as exc:  # noqa: BLE001
            entry["status"] = f"download_error: {exc}"
            entry["pdf_url"] = url

        manifest.append(entry)
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        time.sleep(0.35)

    ok = sum(1 for m in manifest if m.get("status") in ("ok", "ok_external", "skipped_exists"))
    print(f"Done. {ok}/{len(manifest)} PDFs present (ok + ok_external + skipped) under {OUT_DIR}")
    print(f"Manifest: {MANIFEST_PATH}")
    return 0 if ok == len(manifest) else 0


if __name__ == "__main__":
    raise SystemExit(main())
