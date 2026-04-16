#!/usr/bin/env python3
"""
Extract U.S. Code excerpts from nickvido/us-code Markdown into LaTeX snippets.

Run from repo root: python3 tools/usc_extract.py
Requires: reference/us-code checkout (optionally at a git tag).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
USCODE = ROOT / "reference" / "us-code" / "uscode"


def git_checkout_tag(us_code_dir: Path, tag: str | None) -> None:
    if not tag:
        return
    r = subprocess.run(
        ["git", "-C", str(us_code_dir), "checkout", "--quiet", tag],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        print(f"git checkout {tag} failed: {r.stderr}", file=sys.stderr)
        sys.exit(1)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw = parts[1]
    body = parts[2].lstrip("\n")
    meta: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for line in fm_raw.splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            if key is not None:
                meta[key] = "\n".join(buf).strip()
            key, val = m.group(1), m.group(2)
            buf = [val] if val else []
        elif key is not None and line.startswith((" ", "\t")):
            buf.append(line.strip())
        elif key is not None:
            meta[key] = "\n".join(buf).strip()
            key = None
    if key is not None:
        meta[key] = "\n".join(buf).strip()
    # Fold folded scalars (source: >-) into one line; strip YAML block indicators
    src = meta.get("source", "")
    if src:
        src = " ".join(src.split())
        src = re.sub(r"^>-\s*", "", src).strip()
        meta["source"] = src
    return meta, body


def extract_section_block(body: str, section_id: str) -> str:
    """Text from <a id="section-X"> through the line before the next section anchor."""
    pat = re.compile(
        rf'<a id="{re.escape(section_id)}"></a>\s*\n(.*?)(?=\n<a id="section-|\Z)',
        re.DOTALL,
    )
    m = pat.search(body)
    if not m:
        raise ValueError(f"Section anchor {section_id!r} not found")
    return m.group(1).strip()


def strip_statutory_notes(block: str) -> str:
    idx = block.find("\n### Statutory Notes")
    if idx != -1:
        return block[:idx].strip()
    return block.strip()


def extract_subsection(block: str, start: str, end: str | None) -> str:
    """Extract from a line starting with start (e.g. '**(g)**') through line before end (e.g. '**(h)**')."""
    lines = block.splitlines()
    out: list[str] = []
    capturing = False
    for line in lines:
        if not capturing:
            if line.strip().startswith(start):
                capturing = True
                out.append(line)
            continue
        if end and line.strip().startswith(end):
            break
        out.append(line)
    return "\n".join(out).strip()


def md_link_to_latex(m: re.Match[str]) -> str:
    label, url = m.group(1), m.group(2)
    label_esc = latex_escape(label, link_child=True)
    if url.startswith("http"):
        return rf"\href{{{latex_escape_url(url)}}}{{{label_esc}}}"
    return label_esc


def latex_escape_url(url: str) -> str:
    return (
        url.replace("\\", r"\textbackslash{}")
        .replace("%", r"\%")
        .replace("#", r"\#")
    )


def latex_escape(s: str, *, link_child: bool = False) -> str:
    if not link_child:
        s = (
            s.replace("\\", r"\textbackslash{}")
            .replace("{", r"\{")
            .replace("}", r"\}")
            .replace("#", r"\#")
            .replace("$", r"\$")
            .replace("%", r"\%")
            .replace("&", r"\&")
            .replace("_", r"\_")
            .replace("~", r"\textasciitilde{}")
            .replace("^", r"\textasciicircum{}")
        )
    return s


_PH = "@@@USCPH{}@@@"  # unlikely in federal statutes; protects LaTeX during escape


def md_to_latex(text: str) -> str:
    """Convert a Markdown statute chunk to LaTeX; escape prose without mangling inserted commands."""
    slots: list[str] = []
    slot_i = 0

    def push_latex(latex: str) -> str:
        nonlocal slot_i
        token = _PH.format(slot_i)
        slots.append(latex)
        slot_i += 1
        return token

    def sub_link(m: re.Match[str]) -> str:
        return push_latex(md_link_to_latex(m))

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", sub_link, text)

    def sub_bold_paren(m: re.Match[str]) -> str:
        inner = latex_escape(m.group(1), link_child=True)
        return push_latex(r"\textbf{(" + inner + ")}")

    text = re.sub(r"\*\*\(([^)]+)\)\*\*", sub_bold_paren, text)

    def sub_bold(m: re.Match[str]) -> str:
        inner = latex_escape(m.group(1), link_child=True)
        return push_latex(r"\textbf{" + inner + "}")

    text = re.sub(r"\*\*([^*]+)\*\*", sub_bold, text)

    lines_out: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("### "):
            heading = stripped[4:].strip()
            lines_out.append(r"\medskip\textbf{" + latex_escape(heading) + r"}\\")
            continue
        if stripped.startswith("## "):
            heading = stripped[3:].strip()
            lines_out.append(r"\textbf{" + latex_escape(heading) + r"}\\")
            continue
        lines_out.append(latex_escape(line))
    merged = "\n".join(lines_out)
    for i, latex in enumerate(slots):
        merged = merged.replace(_PH.format(i), latex)
    return merged


def emit_snippet(
    out_path: Path,
    title: str,
    cite: str,
    source_url: str,
    tag: str,
    body_latex: str,
    label: str,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    url_esc = latex_escape_url(source_url) if source_url else ""
    cap = (
        r"\textbf{Primary text} --- Title~" + latex_escape(title, link_child=True)
        + ", "
        + cite
        + r" (OLRC via \texttt{nickvido/us-code}, tag \texttt{"
        + latex_escape(tag, link_child=True)
        + "})"
    )
    src_line = (
        r"\textit{Source:} \url{" + url_esc + r"}\par\medskip" if url_esc else ""
    )
    # Label is emitted once in the appendix (see Redefining_Racism.tex) to avoid
    # duplicate \\label errors when the same snippet is \\input{} inline and again in the appendix.
    _ = label
    content = f"""% AUTO-GENERATED by tools/usc_extract.py — do not edit by hand
\\begingroup\\small
\\begin{{historicalsource}}[{{{cap}}}]
{src_line}{body_latex}
\\end{{historicalsource}}
\\endgroup
"""
    out_path.write_text(content, encoding="utf-8")


# (output_stem, md_path under uscode/, section_anchor, mode, mode_arg, title, cite, label)
SNIPPETS: list[tuple[str, str, str, str, str | None, str, str, str]] = [
    (
        "usc_18_922g",
        "title-18-crimes-and-criminal-procedure/chapter-044-firearms.md",
        "section-922",
        "subsection",
        "g|h",
        "18",
        r"\S~922(g)",
        "apx:usc:18:922g",
    ),
    (
        "usc_18_922o",
        "title-18-crimes-and-criminal-procedure/chapter-044-firearms.md",
        "section-922",
        "subsection",
        "o|p",
        "18",
        r"\S~922(o)",
        "apx:usc:18:922o",
    ),
    (
        "usc_18_926b",
        "title-18-crimes-and-criminal-procedure/chapter-044-firearms.md",
        "section-926b",
        "section_to_notes",
        None,
        "18",
        r"\S~926B",
        "apx:usc:18:926b",
    ),
    (
        "usc_18_521",
        "title-18-crimes-and-criminal-procedure/chapter-026-criminal-street-gangs.md",
        "section-521",
        "section_to_notes",
        None,
        "18",
        r"\S~521",
        "apx:usc:18:521",
    ),
    (
        "usc_18_241",
        "title-18-crimes-and-criminal-procedure/chapter-013-civil-rights.md",
        "section-241",
        "section_to_notes",
        None,
        "18",
        r"\S~241",
        "apx:usc:18:241",
    ),
    (
        "usc_18_242",
        "title-18-crimes-and-criminal-procedure/chapter-013-civil-rights.md",
        "section-242",
        "section_to_notes",
        None,
        "18",
        r"\S~242",
        "apx:usc:18:242",
    ),
    (
        "usc_42_2000d",
        "title-42-the-public-health-and-welfare/chapter-021-civil-rights.md",
        "section-2000d",
        "section_to_notes",
        None,
        "42",
        r"\S~2000d",
        "apx:usc:42:2000d",
    ),
    (
        "usc_52_10301",
        "title-52-voting-and-elections/chapter-103-enforcement-of-voting-rights.md",
        "section-10301",
        "section_to_notes",
        None,
        "52",
        r"\S~10301",
        "apx:usc:52:10301",
    ),
    (
        "usc_50_1801abc",
        "title-50-war-and-national-defense/chapter-036-foreign-intelligence-surveillance.md",
        "section-1801",
        "subsection",
        "a|d",
        "50",
        r"\S~1801(a)--(c) (excerpt)",
        "apx:usc:50:1801abc",
    ),
    # --- Phase 2 additions ---
    (
        "usc_18_1581",
        "title-18-crimes-and-criminal-procedure/chapter-077-peonage-slavery-and-trafficking-in-persons.md",
        "section-1581",
        "section_to_notes",
        None,
        "18",
        r"\S~1581 (Peonage)",
        "apx:usc:18:1581",
    ),
    (
        "usc_18_1589",
        "title-18-crimes-and-criminal-procedure/chapter-077-peonage-slavery-and-trafficking-in-persons.md",
        "section-1589",
        "section_to_notes",
        None,
        "18",
        r"\S~1589 (Forced labor)",
        "apx:usc:18:1589",
    ),
    (
        "usc_21_812b",
        "title-21-food-and-drugs/chapter-013-drug-abuse-prevention-and-control.md",
        "section-812",
        "subsection",
        "b|c",
        "21",
        r"\S~812(b) (Controlled Substances scheduling criteria)",
        "apx:usc:21:812b",
    ),
    (
        "usc_21_841a",
        "title-21-food-and-drugs/chapter-013-drug-abuse-prevention-and-control.md",
        "section-841",
        "subsection",
        "a|b",
        "21",
        r"\S~841(a) (Prohibited acts)",
        "apx:usc:21:841a",
    ),
    (
        "usc_18_3559c",
        "title-18-crimes-and-criminal-procedure/chapter-227-sentences.md",
        "section-3559",
        "subsection",
        "c|d",
        "18",
        r"\S~3559(c) (Three-strikes mandatory life imprisonment)",
        "apx:usc:18:3559c",
    ),
    (
        "usc_18_981a",
        "title-18-crimes-and-criminal-procedure/chapter-046-forfeiture.md",
        "section-981",
        "subsection",
        "a|b",
        "18",
        r"\S~981(a) (Civil forfeiture)",
        "apx:usc:18:981a",
    ),
    (
        "usc_18_1761",
        "title-18-crimes-and-criminal-procedure/chapter-085-prison-made-goods.md",
        "section-1761",
        "section_to_notes",
        None,
        "18",
        r"\S~1761 (Prison-made goods)",
        "apx:usc:18:1761",
    ),
    (
        "usc_8_ch7",
        "title-08-aliens-and-nationality/chapter-007-exclusion-of-chinese.md",
        "section-262-to-297",
        "section_with_notes",
        None,
        "8",
        r"\S\S~262--297 (Exclusion of Chinese --- Repealed)",
        "apx:usc:8:ch7",
    ),
    (
        "usc_18_2511",
        "title-18-crimes-and-criminal-procedure/chapter-119-wire-and-electronic-communications-interception-and-interception-of-oral-communications.md",
        "section-2511",
        "section_to_notes",
        None,
        "18",
        r"\S~2511 (Wiretap prohibition)",
        "apx:usc:18:2511",
    ),
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="annual/2025", help="Git tag in reference/us-code")
    ap.add_argument(
        "--us-code-dir",
        type=Path,
        default=ROOT / "reference" / "us-code",
        help="Path to nickvido/us-code clone",
    )
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "Paper" / "usc_snippets",
        help="Output directory for .tex snippets",
    )
    args = ap.parse_args()
    us_code_dir: Path = args.us_code_dir
    if not (us_code_dir / "uscode").is_dir():
        print(f"Missing {us_code_dir / 'uscode'}", file=sys.stderr)
        sys.exit(1)
    git_checkout_tag(us_code_dir, args.tag)

    for stem, rel, sec_id, mode, mode_arg, title, cite, label in SNIPPETS:
        path = us_code_dir / "uscode" / rel
        if not path.is_file():
            print(f"SKIP missing file: {path}", file=sys.stderr)
            continue
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        source = meta.get("source", "").replace("\n", " ").strip()
        if mode == "full_body":
            inner = body.strip()
        else:
            block = extract_section_block(body, sec_id)
            if mode == "section_to_notes":
                inner = strip_statutory_notes(block)
            elif mode == "section_with_notes":
                inner = block
            elif mode == "subsection":
                assert mode_arg
                start_l, end_l = mode_arg.split("|")
                start = f"**({start_l})"
                end = f"**({end_l})" if end_l else None
                inner = extract_subsection(strip_statutory_notes(block), start, end)
            else:
                raise ValueError(mode)
        latex_body = md_to_latex(inner)
        emit_snippet(args.out_dir / f"{stem}.tex", title, cite, source, args.tag, latex_body, label)

    print(f"Wrote snippets to {args.out_dir} (tag {args.tag})")


if __name__ == "__main__":
    main()
