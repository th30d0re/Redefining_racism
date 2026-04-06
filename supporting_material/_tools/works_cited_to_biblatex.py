#!/usr/bin/env python3
"""
Extract the pandoc-style 'Works cited' paragraph from a supporting-material
.tex file and emit a BibLaTeX .bib (mostly @online) plus print the \\addbibresource basename.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

URLDATE = "2026-04-05"

START_MARKERS = (
    r"\paragraph{\texorpdfstring{\textbf{Works",
    r"\paragraph{\textbf{Works cited}}",
)


def find_works_block(text: str) -> tuple[str, int, int] | None:
    start = -1
    for m in START_MARKERS:
        i = text.find(m)
        if i != -1:
            start = i
            break
    if start == -1:
        return None
    label_pos = text.find(r"\label{works-cited}", start)
    if label_pos == -1:
        return None
    body_start = text.find("\n", label_pos)
    if body_start == -1:
        return None
    body_start += 1
    end = text.find(r"\end{document}", body_start)
    if end == -1:
        return None
    return text[body_start:end].strip(), start, end


def latex_title_cleanup(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip().rstrip(",").strip()
    s = re.sub(r"\\textbar\{\}", "|", s)
    s = re.sub(r"\\ldots\b", "...", s)
    s = s.replace("\\&", "&")
    s = re.sub(r"\\%", "%", s)
    s = re.sub(r"`+", "'", s)
    return s


def bib_title_field(s: str) -> str:
    s = latex_title_cleanup(s)
    s = s.replace("{", "{{").replace("}", "}}")
    s = s.replace("%", r"\%")
    s = s.replace("&", r"\&")
    s = s.replace("#", r"\#")
    return s


def url_cleanup(raw: str) -> str:
    u = raw.strip().rstrip(").,;")
    u = u.replace(r"\_", "_")
    u = u.replace(r"\&", "&")
    return u


def preprocess_glued_numbers(block: str) -> str:
    """Insert newlines before ' N. ' when run together with prior URL/text (pandoc export)."""
    block = re.sub(r"(\S)\s+(\d{1,3})\.\s+", r"\1\n\2. ", block)
    return block


def parse_numbered_entries(block: str) -> list[tuple[int, str]]:
    block = preprocess_glued_numbers(block)
    entries: list[tuple[int, str]] = []
    current_num: int | None = None
    current_lines: list[str] = []
    for line in block.splitlines():
        line_st = line.strip()
        if not line_st:
            continue
        m = re.match(r"^(\d+)\.\s*(.*)$", line_st)
        if m:
            if current_num is not None:
                entries.append((current_num, " ".join(current_lines)))
            current_num = int(m.group(1))
            rest = m.group(2).strip()
            current_lines = [rest] if rest else []
        else:
            current_lines.append(line_st)
    if current_num is not None:
        entries.append((current_num, " ".join(current_lines)))
    return entries


def split_title_url(blob: str) -> tuple[str, str]:
    m = re.search(r"(https?://\S+)", blob)
    if not m:
        return latex_title_cleanup(blob), ""
    url = url_cleanup(m.group(1))
    title = blob[: m.start()]
    return latex_title_cleanup(title), url


def safe_bib_key(prefix: str, num: int) -> str:
    p = re.sub(r"[^a-z0-9_]", "_", prefix.lower())
    p = re.sub(r"_+", "_", p).strip("_")[:40]
    return f"{p}_ref_{num:03d}"


def write_bib(path: Path, prefix: str, entries: list[tuple[int, str]]) -> None:
    lines = [
        "% Auto-generated from Works cited — edit in .bib and cite with \\cite{key} as needed.",
        f"% urldate={URLDATE}",
        "",
    ]
    for num, blob in entries:
        title, url = split_title_url(blob)
        if not title and url:
            title = url
        key = safe_bib_key(prefix, num)
        if url:
            lines.append(f"@online{{{key},")
            lines.append(f"  title   = {{{bib_title_field(title)}}},")
            lines.append(f"  url     = {{{url}}},")
            lines.append(f"  urldate = {{{URLDATE}}},")
            lines.append("}")
        else:
            lines.append(f"@misc{{{key},")
            lines.append(f"  note = {{{bib_title_field(title)}}},")
            lines.append("}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: works_cited_to_biblatex.py <file.tex> [file2.tex ...]")
        return 1
    for arg in sys.argv[1:]:
        tex_path = Path(arg).resolve()
        text = tex_path.read_text(encoding="utf-8")
        found = find_works_block(text)
        if not found:
            print(f"SKIP (no Works cited block): {tex_path}", file=sys.stderr)
            continue
        block, _, _ = found
        entries = parse_numbered_entries(block)
        if not entries:
            print(f"SKIP (no entries): {tex_path}", file=sys.stderr)
            continue
        stem = tex_path.stem
        prefix = re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_")
        bib_name = prefix + ".bib"
        bib_path = tex_path.parent / bib_name
        write_bib(bib_path, prefix, entries)
        print(f"Wrote {len(entries)} entries -> {bib_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
