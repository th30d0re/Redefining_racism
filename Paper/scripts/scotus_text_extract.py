"""Extract keyword counts from SCOTUS opinion PDFs for spectral analysis.

Reads all 55 SCOTUS opinion PDFs from Paper/research/ia_scotus_pdfs/ and:
  1. Extracts full text from each opinion using pdfplumber.
  2. Splits majority vs. dissent sections by pattern-matching dissent headers.
  3. Counts keyword occurrences per opinion using five basket definitions.
  4. Normalises counts per 1,000 words of opinion text.
  5. Writes Paper/data/raw/scotus_keyword_counts_raw.csv.

Run:
    python3 Paper/scripts/scotus_text_extract.py

Requires:
    pip install pdfplumber   (already in Paper/scripts/requirements.txt)

Split PDFs in Paper/research/ia_scotus_pdfs/split_pdfs/ are concatenated
before extraction using their *_part01_of*.pdf naming convention.

Keyword baskets (per-1000-words, case-insensitive):
    class:    union, strike, minimum wage, labor, working class
    race:     racism, racial, discrimination, segregation, civil rights
    gender:   gender, sex discrimination, women, feminist, sexual harassment
    religion: religion, religious, evangelical, prayer, establishment clause
    sexuality:homosexual, gay, lesbian, transgender, same-sex
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import pdfplumber  # type: ignore[import]
except ImportError:
    sys.exit(
        "ERROR: pdfplumber not installed.\n"
        "Install with:  pip install pdfplumber\n"
        "or:            pip install -r Paper/scripts/requirements.txt"
    )

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR  = ROOT / "research" / "ia_scotus_pdfs"
SPLIT_DIR = PDF_DIR / "split_pdfs"
MANIFEST  = PDF_DIR / "download_manifest.json"
RAW_OUT   = ROOT / "data" / "raw" / "scotus_keyword_counts_raw.csv"

KEYWORD_BASKETS: dict[str, list[str]] = {
    "class":    ["union", "strike", "minimum wage", "labor", "working class"],
    "race":     ["racism", "racial", "discrimination", "segregation", "civil rights"],
    "gender":   ["gender", "sex discrimination", "women", "feminist", "sexual harassment"],
    "religion": ["religion", "religious", "evangelical", "prayer", "establishment clause"],
    "sexuality":["homosexual", "gay", "lesbian", "transgender", "same-sex"],
}

DISSENT_PATTERN = re.compile(
    r"(justice|mr\.?\s*justice|chief justice)\s+\w+[\w\s]*,\s*(dissenting|dissent)",
    re.IGNORECASE,
)


def _count_keywords(text: str, baskets: dict[str, list[str]]) -> dict[str, int]:
    t = text.lower()
    return {axis: sum(t.count(kw.lower()) for kw in kws) for axis, kws in baskets.items()}


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


MAX_PAGES = 120  # cap per PDF to avoid multi-hour runs on 800-page image PDFs


def _extract_text_from_pdf(pdf_path: Path) -> str:
    """Return page-concatenated text (up to MAX_PAGES) from a PDF.

    Many pre-1950 SCOTUS PDFs from the Internet Archive are scanned-image
    documents with no embedded text layer.  pdfplumber will open them fine but
    return empty strings for every page.  Capping at MAX_PAGES prevents hours-long
    spins on such files.  If fewer than 20 words are found across all sampled
    pages, the file is treated as an image-only PDF and an empty string is returned.
    """
    pages: list[str] = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            sample = pdf.pages[:MAX_PAGES]
            for page in sample:
                txt = page.extract_text()
                if txt:
                    pages.append(txt)
                    if sum(len(p) for p in pages) > 500_000:
                        # Safety cap: ~500 kB of text is plenty for keyword counting
                        break
            if total_pages > MAX_PAGES:
                print(f"    (capped at {MAX_PAGES}/{total_pages} pages)", flush=True)
    except Exception as exc:
        print(f"  WARNING: could not read {pdf_path.name}: {exc}", flush=True)
    return "\n".join(pages)


def _split_majority_dissent(full_text: str) -> tuple[str, str]:
    """Return (majority_text, dissent_text) by finding the first dissent header."""
    match = DISSENT_PATTERN.search(full_text)
    if match:
        split_pos = match.start()
        return full_text[:split_pos], full_text[split_pos:]
    return full_text, ""


def _load_manifest() -> list[dict]:
    if not MANIFEST.exists():
        raise FileNotFoundError(f"Download manifest not found: {MANIFEST}")
    with MANIFEST.open() as fh:
        return json.load(fh)


def _resolve_pdf_paths(record: dict) -> list[Path]:
    """Return ordered list of PDF parts for a given manifest record.

    Single PDFs return a one-element list.  Split PDFs (identified by the
    presence of split_pdfs/ parts in the split directory) return all parts
    sorted by part number so they can be concatenated in order.
    """
    saved_as = record.get("saved_as", "")
    if not saved_as:
        return []
    base = ROOT / saved_as
    if base.exists():
        return [base]
    stem = base.stem
    parts = sorted(SPLIT_DIR.glob(f"{stem}_part*.pdf"))
    if parts:
        return parts
    return []


def _concat_text(paths: list[Path]) -> str:
    return "\n".join(_extract_text_from_pdf(p) for p in paths)


def process_all() -> pd.DataFrame:
    manifest = _load_manifest()
    rows: list[dict] = []

    for record in manifest:
        case_name = record.get("case", "unknown")
        year      = int(record.get("year", 0))
        pdfs      = _resolve_pdf_paths(record)

        if not pdfs:
            print(f"  SKIP {case_name} ({year}): no PDF found", flush=True)
            continue

        print(f"  Processing: {case_name} ({year})", flush=True)
        full_text = _concat_text(pdfs)

        if not full_text.strip():
            print(f"    SKIP: no extractable text (likely scanned-image PDF)", flush=True)
            continue

        majority_text, dissent_text = _split_majority_dissent(full_text)

        for is_dissent, text in [(False, majority_text), (True, dissent_text)]:
            if not text.strip():
                continue
            total_words = _word_count(text)
            if total_words < 50:
                continue
            counts  = _count_keywords(text, KEYWORD_BASKETS)
            per_1k  = {
                f"{axis}_per_1k": round(cnt / total_words * 1000, 4)
                for axis, cnt in counts.items()
            }
            rows.append({
                "case_name":        case_name,
                "year":             year,
                "total_words":      total_words,
                "class_count":      counts["class"],
                "race_count":       counts["race"],
                "gender_count":     counts["gender"],
                "religion_count":   counts["religion"],
                "sexuality_count":  counts["sexuality"],
                "is_dissent":       is_dissent,
                **per_1k,
            })

    df = pd.DataFrame(rows)
    df = df.sort_values(["year", "case_name", "is_dissent"]).reset_index(drop=True)
    return df


def main() -> None:
    RAW_OUT.parent.mkdir(parents=True, exist_ok=True)
    print(f"Extracting SCOTUS keyword counts from PDFs in:\n  {PDF_DIR}\n")
    df = process_all()
    header_lines = [
        "# raw: SCOTUS per-1k-word keyword counts for 55 opinions (1873-2018)",
        "# source: Internet Archive SCOTUS PDF collection",
        "# extraction_tool: pdfplumber",
        "# keyword_baskets: class / race / gender / religion / sexuality",
        "# is_dissent: True = dissent section; False = majority section",
        "# generated_by: Paper/scripts/scotus_text_extract.py",
    ]
    with RAW_OUT.open("w") as fh:
        for line in header_lines:
            fh.write(line + "\n")
        df.to_csv(fh, index=False)
    print(f"\nWrote {len(df)} rows to {RAW_OUT}")
    print("Next step:  make data-refresh   (runs preprocess_spectral_data.py)")


if __name__ == "__main__":
    main()
