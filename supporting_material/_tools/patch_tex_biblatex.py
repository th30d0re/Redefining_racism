#!/usr/bin/env python3
"""Insert biblatex + replace Works cited block with \\printbibliography."""
from __future__ import annotations

import re
import sys
from pathlib import Path

# biblatex must load before hyperref; \usepackage{bookmark} pulls in hyperref.
BIBLATEX_SNIPPET = r"""
\usepackage[backend=biber,style=authortitle,maxbibnames=99,doi=false,isbn=false,url=true]{biblatex}
\addbibresource{BIBFILE}
"""

WORKS_START = re.compile(
    r"\\paragraph\{\\texorpdfstring\{\\textbf\{Works\s*\n\s*cited\}\}\{Works cited\}\}\\label\{works-cited\}\s*\n",
    re.MULTILINE,
)

END_DOC = r"\end{document}"


def bib_filename_for(tex_path: Path) -> str:
    stem = tex_path.stem
    return re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_") + ".bib"


def patch_tex(tex_path: Path) -> bool:
    text = tex_path.read_text(encoding="utf-8")
    if r"\usepackage{biblatex}" in text or r"\usepackage[backend=biber" in text:
        print(f"Already patched: {tex_path}")
        return False
    bibfile = bib_filename_for(tex_path)
    bib_path = tex_path.parent / bibfile
    if not bib_path.is_file():
        print(f"Missing {bib_path}", file=sys.stderr)
        return False
    insert = BIBLATEX_SNIPPET.replace("BIBFILE", bibfile)
    tight_then_bookmark = (
        "\\providecommand{\\tightlist}{%\n"
        "  \\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}\n"
        "\\usepackage{bookmark}"
    )
    if tight_then_bookmark in text:
        text = text.replace(
            tight_then_bookmark,
            "\\providecommand{\\tightlist}{%\n"
            "  \\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}"
            + insert
            + "\n\\usepackage{bookmark}",
            1,
        )
    elif r"\usepackage{bookmark}" in text:
        text = text.replace(
            r"\usepackage{bookmark}",
            insert + "\n\\usepackage{bookmark}",
            1,
        )
    else:
        print(f"No anchor for biblatex: {tex_path}", file=sys.stderr)
        return False
    m = WORKS_START.search(text)
    if not m:
        print(f"No Works cited paragraph: {tex_path}", file=sys.stderr)
        return False
    start = m.start()
    end = text.find(END_DOC, start)
    if end == -1:
        print(f"No end document: {tex_path}", file=sys.stderr)
        return False
    replacement = (
        "\\nocite{*}\n"
        "\\printbibliography[title={Works cited},sorting=none]\n"
        "\\label{works-cited}\n\n"
    )
    text = text[:start] + replacement + text[end:]
    tex_path.write_text(text, encoding="utf-8")
    print(f"Patched {tex_path.name} -> {bibfile}")
    return True


def main() -> int:
    for arg in sys.argv[1:]:
        patch_tex(Path(arg).resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
