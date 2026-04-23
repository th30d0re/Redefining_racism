#!/usr/bin/env python3
"""
extract_case_context.py — TEX paragraph extractor for SCOTUS case integration memos.

Usage:
    python3 Paper/scripts/extract_case_context.py <slug_or_cite_key> [--tex PATH] [--out PATH]

Examples:
    python3 Paper/scripts/extract_case_context.py washington_v_davis_1976
    python3 Paper/scripts/extract_case_context.py bruen
    python3 Paper/scripts/extract_case_context.py "Washington v. Davis"

Outputs a structured markdown file with every .tex paragraph that mentions the case,
annotated with chapter number and section label. Basis for memo section §1 ("What the
book says now").
"""

import re
import sys
import argparse
from pathlib import Path

# ── Project paths ──────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TEX_PATH = REPO_ROOT / "Paper" / "Redefining_Racism.tex"
INDEX_PATH = REPO_ROOT / "Paper" / "research" / "case_index.yaml"
MEMO_DIR = REPO_ROOT / "Paper" / "research" / "case_integration_memos"

# ── Party-name → regex map for common Tier-1 cases ────────────────────────────
# These supplement cite-key matching when a case is referenced by name without \cite{}.
PARTY_NAME_PATTERNS: dict[str, list[str]] = {
    "washington_v_davis_1976":    [r"Washington\s+v\.?\s+Davis", r"purpose[- ]vs?[- ]effect", r"purpose[- ]and[- ]effect"],
    "nysrpa_v_bruen_2022":        [r"Bruen", r"NYSRPA", r"N\.?Y\.?S\.?R\.?P\.?A", r"proper cause", r"historical[- ]tradition"],
    "dobbs_v_jackson_2022":       [r"Dobbs", r"Jackson Women", r"overrul.*Roe", r"Roe.*overrul"],
    "dred_scott_v_sandford_1857": [r"Dred Scott", r"Sandford", r"dredscott"],
    "marbury_v_madison_1803":     [r"Marbury", r"province and duty", r"judicial review"],
    "arlington_heights_1977":     [r"Arlington Heights", r"Village of Arlington"],
    "deshaney_v_winnebago_1989":  [r"DeShaney", r"De\s*Shaney", r"Winnebago", r"affirmative duty", r"Poor Joshua"],
    "loving_v_virginia_1967":     [r"Loving", r"Bazile", r"odious to the Fourteenth"],
    "castle_rock_v_gonzales_2005":[r"Castle Rock", r"Gonzales"],
    "perry_v_united_states_1935": [r"Perry v\.?\s+United States", r"gold clause", r"stupendous catastrophe"],
    "richmond_newspapers_1980":   [r"Richmond Newspapers", r"right of access.*trial", r"open.*trial.*First"],
    "united_states_v_rahimi_2024":[r"Rahimi", r"responsible citizens?", r"kernel stabilization"],
}

# Cite key aliases (IA slug might differ from bib key)
CITE_KEY_ALIASES: dict[str, list[str]] = {
    "washington_v_davis_1976":    ["washington_davis", "washingtondavis", "davis1976"],
    "nysrpa_v_bruen_2022":        ["bruen", "bruen2022", "nysrpa_bruen"],
    "dobbs_v_jackson_2022":       ["dobbs", "dobbs2022"],
    "dred_scott_v_sandford_1857": ["dredscott", "dred_scott", "fehrenbacher"],
    "marbury_v_madison_1803":     ["marbury", "marbury1803"],
    "arlington_heights_1977":     ["arlington_heights", "arlingtonheights", "arlington1977"],
    "deshaney_v_winnebago_1989":  ["deshaney", "de_shaney", "deshaney1989"],
    "loving_v_virginia_1967":     ["loving", "loving1967", "bazile"],
    "castle_rock_v_gonzales_2005":["castle_rock", "castlerock", "gonzales2005"],
    "perry_v_united_states_1935": ["perry", "perry1935", "perry_gold"],
    "richmond_newspapers_1980":   ["richmond_newspapers", "richmond_newspapers_1980", "richmond1980"],
    "united_states_v_rahimi_2024":["rahimi", "rahimi2024"],
}


def resolve_slug(query: str) -> str:
    """Map a query string (cite key, party fragment, or slug) to a canonical slug."""
    q = query.lower().strip()
    # Direct slug match
    for slug in PARTY_NAME_PATTERNS:
        if q == slug or q == slug.replace("_", " "):
            return slug
    # Alias match
    for slug, aliases in CITE_KEY_ALIASES.items():
        if q in [a.lower() for a in aliases]:
            return slug
    # Party name fragment
    for slug in PARTY_NAME_PATTERNS:
        parts = slug.split("_")
        if any(p in q for p in parts if len(p) > 3):
            return slug
    return q  # Return as-is for generic query


def build_combined_regex(slug: str, cite_keys: list[str]) -> re.Pattern:
    """Build a regex that matches any cite key or party name mention."""
    patterns: list[str] = []
    # Cite key patterns: \cite{key} or \cite{key,other}
    for key in cite_keys:
        patterns.append(rf"\\cite\{{[^}}]*\b{re.escape(key)}\b[^}}]*\}}")
        patterns.append(rf"\\cite\w*\{{[^}}]*\b{re.escape(key)}\b[^}}]*\}}")
    # Party name patterns
    for pat in PARTY_NAME_PATTERNS.get(slug, []):
        patterns.append(pat)
    return re.compile("|".join(patterns), re.IGNORECASE) if patterns else re.compile(r"NOMATCH_$")


def parse_chapters(tex: str) -> list[tuple[int, int, str, str]]:
    """
    Return list of (start_line, end_line, chapter_label, section_label) tuples.
    These partition the .tex file so we can annotate which chapter a paragraph is in.
    """
    chapters: list[tuple[int, int, str, str]] = []
    chapter_pat = re.compile(r"^[^%]*\\(?:chapter|section)\*?\{(.+?)\}", re.MULTILINE)
    label_pat = re.compile(r"\\label\{([^}]+)\}")
    lines = tex.splitlines()
    ch_name = "Preamble"
    ch_label = "preamble"
    last_start = 0
    for i, line in enumerate(lines):
        m = chapter_pat.search(line)
        if m:
            if chapters:
                chapters[-1] = (chapters[-1][0], i - 1, chapters[-1][2], chapters[-1][3])
            lm = label_pat.search(lines[i + 1] if i + 1 < len(lines) else "")
            lbl = lm.group(1) if lm else ch_name.lower().replace(" ", "_")[:30]
            chapters.append((i, len(lines), m.group(1)[:60], lbl))
    return chapters


def locate_chapter(line_idx: int, chapters: list[tuple[int, int, str, str]]) -> tuple[str, str]:
    """Return (chapter_name, label) for a given line index."""
    for start, end, name, lbl in reversed(chapters):
        if start <= line_idx:
            return name, lbl
    return "Preamble", "preamble"


def extract_paragraphs(tex: str, pattern: re.Pattern, chapters: list) -> list[dict]:
    """Extract all paragraphs (double-newline separated blocks) that match pattern."""
    # Work at paragraph level — split on double blank lines
    # But track line numbers by building an offset map first
    lines = tex.splitlines()
    line_start: list[int] = []  # character offset of each line
    offset = 0
    for ln in lines:
        line_start.append(offset)
        offset += len(ln) + 1  # +1 for \n

    results: list[dict] = []
    # Split into paragraph blocks while preserving line numbers
    para_re = re.compile(r"\n{2,}")
    para_starts: list[int] = [0]
    for m in para_re.finditer(tex):
        para_starts.append(m.end())

    for p_start in para_starts:
        # Find end of this paragraph
        next_blank = para_re.search(tex, p_start)
        p_end = next_blank.start() if next_blank else len(tex)
        para_text = tex[p_start:p_end].strip()
        if not para_text:
            continue
        if not pattern.search(para_text):
            continue
        # Determine line number
        para_line = 0
        for i, off in enumerate(line_start):
            if off > p_start:
                para_line = max(0, i - 1)
                break
        ch_name, ch_lbl = locate_chapter(para_line, chapters)
        # Skip pure comment blocks
        non_comment_lines = [l for l in para_text.splitlines() if not l.strip().startswith("%")]
        if not non_comment_lines:
            continue
        results.append({
            "line": para_line + 1,
            "chapter": ch_name,
            "label": ch_lbl,
            "text": para_text,
        })

    return results


def format_output(slug: str, cite_keys: list[str], results: list[dict], tex_path: Path) -> str:
    """Format extraction results as structured markdown."""
    lines: list[str] = []
    lines.append(f"# TEX Context Extraction: `{slug}`")
    lines.append(f"\n**Source:** `{tex_path.name}`  ")
    lines.append(f"**Cite keys searched:** {', '.join(f'`{k}`' for k in cite_keys) or '(none)'}  ")
    party_pats = PARTY_NAME_PATTERNS.get(slug, [])
    lines.append(f"**Party-name patterns:** {', '.join(f'`{p}`' for p in party_pats) or '(none)'}  ")
    lines.append(f"**Paragraphs found:** {len(results)}")
    lines.append("\n---\n")

    # Group by chapter
    by_chapter: dict[str, list[dict]] = {}
    for r in results:
        key = r["chapter"]
        by_chapter.setdefault(key, []).append(r)

    for ch, paras in by_chapter.items():
        lines.append(f"\n## Chapter: {ch}")
        lines.append(f"*({len(paras)} hit{'s' if len(paras) != 1 else ''})*\n")
        for p in paras:
            lines.append(f"### Line {p['line']} — `\\label{{{p['label']}}}`")
            lines.append(f"\n```latex")
            lines.append(p["text"])
            lines.append("```\n")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("query", help="Case slug, cite key, or party-name fragment")
    parser.add_argument("--tex", default=str(TEX_PATH), help="Path to .tex file")
    parser.add_argument("--out", default=None, help="Output path (default: stdout or memos dir)")
    parser.add_argument("--print", dest="print_only", action="store_true", help="Print to stdout even if --out not set")
    args = parser.parse_args()

    tex_path = Path(args.tex)
    if not tex_path.exists():
        print(f"ERROR: .tex file not found: {tex_path}", file=sys.stderr)
        return 1

    slug = resolve_slug(args.query)
    cite_keys = CITE_KEY_ALIASES.get(slug, [args.query.lower()])
    pattern = build_combined_regex(slug, cite_keys)

    tex = tex_path.read_text(encoding="utf-8", errors="replace")
    chapters = parse_chapters(tex)
    results = extract_paragraphs(tex, pattern, chapters)

    output = format_output(slug, cite_keys, results, tex_path)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Written to: {out_path}")
    elif args.print_only or not sys.stdout.isatty():
        print(output)
    else:
        # Write to memos dir as a context file
        out_path = MEMO_DIR / f"{slug}_context.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Written to: {out_path}")
        print(f"Paragraphs found: {len(results)}")
        by_ch: dict[str, int] = {}
        for r in results:
            by_ch[r["chapter"]] = by_ch.get(r["chapter"], 0) + 1
        for ch, cnt in by_ch.items():
            print(f"  {cnt:3d}  {ch}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
