#!/usr/bin/env python3
"""
SCOTUS Corpus Audit — build-time lint script.

Usage (standalone):
    python3 Paper/scripts/audit_scotus_corpus.py [--strict]

Usage (from make pdf):
    Add to Makefile after bibtex step:
        python3 Paper/scripts/audit_scotus_corpus.py --strict || exit 1

Exit codes:
    0 — no fatal issues (warnings may still print)
    1 — fatal issues found (cited-but-missing or bib-key-but-no-PDF)

Output buckets:
    (a) FATAL  — cite_key in .tex but case has NO pdf AND NO md in corpus
    (b) FATAL  — cite_key in .tex but case has a pdf bib entry yet no PDF file
    (c) WARN   — case present in corpus but not cited in .tex (orphan candidate)
    (d) WARN   — Tier-1 case is missing an integration memo in case_integration_memos/
    (e) OK     — case has cite_key + pdf + md (fully resolved)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

ROOT = Path(__file__).resolve().parents[1]
TEX_PATH   = ROOT / "Redefining_Racism.tex"
INDEX_PATH = ROOT / "research" / "case_index.yaml"
PDF_DIR    = ROOT / "research" / "ia_scotus_pdfs"
MD_DIR     = ROOT / "research" / "markdown_cases"
MEMO_DIR   = ROOT / "research" / "case_integration_memos"

# Tier-1 cases: (slug, memo_filename) — require integration memo to exist
TIER1_CASES: list[tuple[str, str]] = [
    ("dobbs_v_jackson_women_s_health_organization_2022", "dobbs.md"),
    ("new_york_state_rifle_pistol_association_v_bruen_2022", "bruen.md"),
    ("washington_v_davis_1976", "washington_v_davis.md"),
    ("united_states_v_rahimi_2024", "rahimi.md"),
    ("dred_scott_v_sandford_1857", "dred_scott.md"),
    ("marbury_v_madison_1803", "marbury_v_madison.md"),
    ("village_of_arlington_heights_v_metropolitan_housing_development_corp_1977", "arlington_heights.md"),
    ("deshaney_v_winnebago_county_1989", "deshaney.md"),
    ("loving_v_virginia_1967", "loving_v_virginia.md"),
    ("town_of_castle_rock_v_gonzales_2005", "castle_rock.md"),
    ("perry_v_united_states_1935", "perry.md"),
    ("richmond_newspapers_v_virginia_1980", "richmond_newspapers.md"),
]

# Cite keys that are NOT legal cases (books, datasets, etc.)
NON_CASE_KEYS = {
    "fehrenbacher",   # book about Dred Scott
    "ia_scotus_briefs_2026",  # IA collection resource
    "ia_scotus_collection",   # IA collection resource
}

# Cite keys that refer to cases but have research notes (not PDFs) as primary source
LOWER_COURT_KEYS: set[str] = set()  # Relf/Madrigal have no cite_keys yet


def load_index() -> list[dict]:
    if not INDEX_PATH.exists():
        print(f"[WARN] case_index.yaml not found at {INDEX_PATH}. Run build to generate.")
        return []
    if HAVE_YAML:
        data = yaml.safe_load(INDEX_PATH.read_text())
        return data.get("cases", []) if data else []
    # Fallback: minimal YAML parser for simple key:value
    cases: list[dict] = []
    current: dict = {}
    for line in INDEX_PATH.read_text().splitlines():
        if line.startswith("  - case:"):
            if current:
                cases.append(current)
            current = {"case": line.split(":", 1)[1].strip().strip('"')}
        elif line.startswith("    slug:") and current is not None:
            current["slug"] = line.split(":", 1)[1].strip()
        elif line.startswith("    cite_keys:") and current is not None:
            raw = line.split(":", 1)[1].strip()
            current["cite_keys"] = re.findall(r"[\w_]+", raw)
        elif line.startswith("    pdf_exists:") and current is not None:
            current["pdf_exists"] = line.split(":", 1)[1].strip() == "true"
        elif line.startswith("    md_exists:") and current is not None:
            current["md_exists"] = line.split(":", 1)[1].strip() == "true"
    if current:
        cases.append(current)
    return cases


def extract_cite_keys(tex: str) -> dict[str, int]:
    """Return {key: occurrence_count} for all \cite{...} keys."""
    counts: dict[str, int] = {}
    for raw in re.findall(r"\\cite\{([^}]+)\}", tex):
        for k in raw.split(","):
            k = k.strip()
            if k:
                counts[k] = counts.get(k, 0) + 1
    return counts


def extract_case_mentions(tex: str) -> list[str]:
    """Extract X v. Y style mentions from the .tex source."""
    raw = re.findall(
        r'(?:(?:\\textit|\\textbf|\\emph)\{)?'
        r'([A-Z][A-Za-z\.\-\'\s]{1,40}?\s+v\.?\s+[A-Z][A-Za-z\.\-\'\s]{1,40}?)'
        r'(?:\}|\s*[\(\,\.\;]|\s+\()',
        tex,
    )
    cleaned = []
    for m in raw:
        c = re.sub(r'\s+', ' ', m.strip().rstrip(".,;"))
        if not re.search(r'\d|\\|Lyapunov|Viv\s|Font|Table|Figure|Chapter|Equation|Section', c):
            cleaned.append(c)
    return sorted(set(cleaned))


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit SCOTUS corpus against manuscript citations.")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 if any FATAL issues found.")
    parser.add_argument("--json", action="store_true",
                        help="Emit machine-readable JSON to stdout.")
    args = parser.parse_args()

    if not TEX_PATH.exists():
        print(f"[ERROR] .tex file not found: {TEX_PATH}", file=sys.stderr)
        return 1

    tex = TEX_PATH.read_text(encoding="utf-8")
    cases = load_index()

    # ── Build lookup maps ─────────────────────────────────────────────────────
    cite_counts = extract_cite_keys(tex)
    case_mentions = extract_case_mentions(tex)

    # Map cite_key → case entry
    key_to_case: dict[str, dict] = {}
    for c in cases:
        for k in (c.get("cite_keys") or []):
            key_to_case[k] = c

    # ── Bucket (a): cite_key in .tex, but no PDF and no MD ──────────────────
    fatal_missing: list[dict] = []
    for key, count in cite_counts.items():
        if key in NON_CASE_KEYS or key in LOWER_COURT_KEYS:
            continue
        if key not in key_to_case:
            continue
        c = key_to_case[key]
        slug = c.get("slug", "")
        pdf_ok = c.get("pdf_exists", False) or (PDF_DIR / f"{slug}.pdf").exists()
        md_ok  = c.get("md_exists",  False) or (MD_DIR  / f"{slug}.md").exists()
        if not pdf_ok and not md_ok:
            fatal_missing.append({
                "type": "cited_but_no_corpus",
                "cite_key": key,
                "case": c.get("case"),
                "year": c.get("year"),
                "cited_count": count,
                "slug": slug,
            })

    # ── Bucket (b): bib key exists + case in index, but PDF file is missing ─
    fatal_no_pdf: list[dict] = []
    for key, count in cite_counts.items():
        if key in NON_CASE_KEYS or key in LOWER_COURT_KEYS:
            continue
        if key not in key_to_case:
            continue
        c = key_to_case[key]
        slug = c.get("slug", "")
        # Only flag if we EXPECT a PDF (i.e., it's not a lower-court stub)
        note = c.get("note", "")
        if "stub" in note or "not SCOTUS" in note:
            continue
        pdf_ok = c.get("pdf_exists", False) or (PDF_DIR / f"{slug}.pdf").exists()
        if not pdf_ok:
            fatal_no_pdf.append({
                "type": "cite_key_but_no_pdf",
                "cite_key": key,
                "case": c.get("case"),
                "year": c.get("year"),
                "cited_count": count,
                "slug": slug,
            })

    # ── Bucket (c/new d): Tier-1 cases missing integration memos ────────────
    warn_no_memo: list[dict] = []
    for slug, memo_file in TIER1_CASES:
        memo_path = MEMO_DIR / memo_file
        if not memo_path.exists():
            warn_no_memo.append({
                "type": "tier1_no_memo",
                "slug": slug,
                "expected_memo": str(memo_path.relative_to(ROOT.parent)),
            })

    # ── Bucket (original c): case in corpus but no cite_key in .tex ─────────
    warn_orphan: list[dict] = []
    for c in cases:
        keys = c.get("cite_keys") or []
        if not keys:
            continue
        slug = c.get("slug", "")
        pdf_ok = c.get("pdf_exists", False) or (PDF_DIR / f"{slug}.pdf").exists()
        md_ok  = c.get("md_exists",  False) or (MD_DIR  / f"{slug}.md").exists()
        if (pdf_ok or md_ok) and all(k not in cite_counts for k in keys):
            warn_orphan.append({
                "type": "corpus_but_uncited",
                "cite_keys": keys,
                "case": c.get("case"),
                "year": c.get("year"),
                "slug": slug,
            })

    # ── Bucket (d): fully OK (cited + pdf + md) ──────────────────────────────
    ok_cases: list[dict] = []
    for key, count in cite_counts.items():
        if key in NON_CASE_KEYS or key not in key_to_case:
            continue
        c = key_to_case[key]
        slug = c.get("slug", "")
        pdf_ok = c.get("pdf_exists", False) or (PDF_DIR / f"{slug}.pdf").exists()
        md_ok  = c.get("md_exists",  False) or (MD_DIR  / f"{slug}.md").exists()
        if pdf_ok and md_ok:
            ok_cases.append({"cite_key": key, "case": c.get("case"), "year": c.get("year")})

    # ── Report ────────────────────────────────────────────────────────────────
    fatals = fatal_missing + fatal_no_pdf

    if args.json:
        import json
        print(json.dumps({
            "fatal_missing": fatal_missing,
            "fatal_no_pdf": fatal_no_pdf,
            "warn_orphan": warn_orphan,
            "warn_no_memo": warn_no_memo,
            "ok_count": len(ok_cases),
            "tier1_memos_present": len(TIER1_CASES) - len(warn_no_memo),
            "tier1_total": len(TIER1_CASES),
            "total_cases": len(cases),
            "total_cite_keys": len(cite_counts),
        }, indent=2))
        return 1 if (fatals and args.strict) else 0

    # Human-readable output
    print(f"\n{'='*60}")
    print(f"  SCOTUS Corpus Audit — {TEX_PATH.name}")
    print(f"{'='*60}")
    print(f"  Index: {len(cases)} cases | Cite keys in .tex: {len(cite_counts)}")
    print(f"  Case 'v.' mentions: {len(case_mentions)}")
    print()

    if not fatals:
        print(f"  ✓ No fatal issues")
    else:
        print(f"  ✗ {len(fatals)} FATAL issue(s):")
        for r in fatal_missing:
            print(f"      [CITED_BUT_MISSING]  \\cite{{{r['cite_key']}}} ({r['case']}, {r['year']}) — no PDF, no MD")
        for r in fatal_no_pdf:
            print(f"      [NO_PDF]             \\cite{{{r['cite_key']}}} ({r['case']}, {r['year']}) — MD exists but no PDF")

    if warn_no_memo:
        print(f"\n  ⚠  {len(warn_no_memo)} Tier-1 case(s) missing integration memo:")
        for r in warn_no_memo:
            print(f"      [NO_MEMO]  {r['slug']}")
            print(f"               → expected: {r['expected_memo']}")

    if warn_orphan:
        print(f"\n  ⚠  {len(warn_orphan)} orphan cases (corpus but uncited):")
        for r in warn_orphan:
            print(f"      {r['case']} ({r['year']}) — keys: {r['cite_keys']}")

    print(f"\n  ✓ Fully resolved (cited + pdf + md): {len(ok_cases)}")
    print(f"  ✓ Tier-1 memos present: {len(TIER1_CASES) - len(warn_no_memo)}/{len(TIER1_CASES)}")
    print(f"{'='*60}\n")

    return 1 if (fatals and args.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
