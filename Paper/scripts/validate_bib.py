#!/usr/bin/env python3
"""
validate_bib.py
===============
Standalone validator for Paper/references.bib.  Flags entries that likely
contain conversion artefacts: statute numbers parsed as years, full
descriptive text in author fields, missing titles, etc.

Usage (from repository root):
    python3 Paper/scripts/validate_bib.py
    python3 Paper/scripts/validate_bib.py --bib Paper/references.bib
    python3 Paper/scripts/validate_bib.py --strict   # exit 1 on any warning

Exit codes:
    0 — no warnings (or --strict not set)
    1 — warnings found and --strict was passed
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_BIB = REPO_ROOT / "Paper" / "references.bib"

# ---------------------------------------------------------------------------
# Entry parser
# ---------------------------------------------------------------------------

@dataclass
class BibEntry:
    key:    str
    etype:  str
    fields: dict[str, str] = field(default_factory=dict)
    raw:    str = ''

    def get(self, name: str) -> str:
        return self.fields.get(name, '')


def parse_bib(text: str) -> list[BibEntry]:
    """Parse BibLaTeX text into a list of BibEntry objects."""
    entries: list[BibEntry] = []
    for em in re.finditer(r'@(\w+)\{(\w+),(.*?)\n\}', text, re.DOTALL):
        etype = em.group(1).lower()
        key   = em.group(2)
        body  = em.group(3)
        raw   = em.group(0)

        flds: dict[str, str] = {}
        for fm in re.finditer(r'(\w+)\s+=\s+\{(.*?)\}(?:,|$)', body, re.DOTALL):
            fname = fm.group(1).lower()
            fvals = fm.group(2).strip()
            flds[fname] = fvals

        entries.append(BibEntry(key=key, etype=etype, fields=flds, raw=raw))
    return entries


# ---------------------------------------------------------------------------
# Validation checks
# ---------------------------------------------------------------------------

@dataclass
class Warning:
    key:      str
    severity: str   # 'ERROR' | 'WARN' | 'INFO'
    message:  str

    def __str__(self) -> str:
        return f'  [{self.severity}] {self.key}: {self.message}'


def check_year(e: BibEntry) -> list[Warning]:
    """Flag years outside 1400–2030 (statute numbers, page numbers parsed as years)."""
    ws: list[Warning] = []
    year = e.get('year')
    if year and re.fullmatch(r'\d{4}', year):
        y = int(year)
        if not (1400 <= y <= 2030):
            ws.append(Warning(
                e.key, 'ERROR',
                f'year={y} is outside 1400–2030 — probable statute number or '
                f'page number extracted as year (raw entry contains Stat. or similar)'
            ))
        elif y < 1450 and e.etype not in ('misc',):
            ws.append(Warning(
                e.key, 'WARN',
                f'year={y} is very early — verify against source'
            ))
    return ws


def check_author(e: BibEntry) -> list[Warning]:
    """Flag malformed author fields."""
    ws: list[Warning] = []
    author = e.get('author')

    if not author:
        if e.etype not in ('online',):
            ws.append(Warning(e.key, 'WARN', 'missing author field'))
        return ws

    # Strip double braces for length check
    plain = author.strip('{}')

    # Length check — full descriptive text in author
    if len(plain) > 120:
        ws.append(Warning(
            e.key, 'ERROR',
            f'author is {len(plain)} chars — probable full descriptive text, '
            f'not just a name (first 80: {plain[:80]!r})'
        ))

    # Author == "Unknown"
    if plain == 'Unknown':
        if e.etype == 'misc' and 'v.' in e.get('title'):
            hint = '{Supreme Court of the United States}'
        else:
            hint = '{Anonymous} or the issuing body'
        ws.append(Warning(
            e.key, 'WARN',
            f'author=Unknown — replace with {hint}'
        ))

    # Author contains URL
    if re.search(r'https?://|www\.', plain):
        ws.append(Warning(
            e.key, 'ERROR',
            'author field contains URL — probable extraction error'
        ))

    # Author contains LaTeX section comment markers (%%--) — bib parser leak
    if r'\%' in plain or '%%' in plain or '---' in plain:
        ws.append(Warning(
            e.key, 'ERROR',
            'author field contains LaTeX comment markers or dashes — '
            'section comment leaked into field'
        ))

    # Too many commas within a single name segment (biber "too many commas").
    # Correct: "Last, First and Last2, First2" — 1 comma per name → OK.
    # Incorrect: "Last, First, Middle" — 2 commas in one name → biber error.
    # We split on ' and ' and check each segment independently.
    if not plain.startswith('{'):
        for segment in re.split(r'\s+and\s+', plain, flags=re.IGNORECASE):
            if segment.count(',') >= 2:
                ws.append(Warning(
                    e.key, 'WARN',
                    f'name segment {segment[:60]!r} has {segment.count(",") } commas '
                    f'— biber may reject as "too many commas"; consider double-brace protection'
                ))
                break

    return ws


def check_title(e: BibEntry) -> list[Warning]:
    """Flag missing or suspicious titles."""
    ws: list[Warning] = []
    title = e.get('title')

    if not title:
        ws.append(Warning(e.key, 'ERROR', 'missing title field'))
        return ws

    # Title and author are identical (full description dumped into both)
    if title == e.get('author').strip('{}'):
        ws.append(Warning(
            e.key, 'WARN',
            'title == author — both fields contain the same full description text'
        ))

    # Title ends with comma (truncation artefact)
    if title.rstrip().endswith(','):
        ws.append(Warning(
            e.key, 'WARN',
            f'title ends with comma — probable truncation artefact: {title[-30:]!r}'
        ))

    return ws


def check_url(e: BibEntry) -> list[Warning]:
    """Flag entries with URL in non-url fields."""
    ws: list[Warning] = []
    for fname in ('author', 'title', 'journal', 'publisher', 'institution'):
        val = e.get(fname)
        if val and re.search(r'https?://', val):
            ws.append(Warning(
                e.key, 'WARN',
                f'URL found in field {fname!r} — should be in url field'
            ))
    return ws


def check_type_consistency(e: BibEntry) -> list[Warning]:
    """Flag type inconsistencies."""
    ws: list[Warning] = []

    # @article should have journal
    if e.etype == 'article' and not e.get('journal'):
        ws.append(Warning(e.key, 'WARN', '@article missing journal field'))

    # @book should have publisher
    if e.etype == 'book' and not e.get('publisher'):
        ws.append(Warning(e.key, 'WARN', '@book missing publisher field'))

    # @report should have institution
    if e.etype == 'report' and not e.get('institution'):
        ws.append(Warning(e.key, 'WARN', '@report missing institution field'))

    # @online should have url
    if e.etype == 'online' and not e.get('url'):
        ws.append(Warning(e.key, 'WARN', '@online missing url field'))

    return ws


ALL_CHECKS = [check_year, check_author, check_title, check_url, check_type_consistency]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Validate Paper/references.bib for conversion artefacts.',
    )
    parser.add_argument(
        '--bib', type=Path, default=DEFAULT_BIB,
        metavar='BIB_FILE',
        help=f'Path to the .bib file to validate (default: {DEFAULT_BIB})'
    )
    parser.add_argument(
        '--strict', action='store_true',
        help='Exit with code 1 if any warnings are found'
    )
    parser.add_argument(
        '--errors-only', action='store_true',
        help='Print only ERROR-severity issues'
    )
    args = parser.parse_args()

    if not args.bib.exists():
        sys.exit(f'ERROR: {args.bib} not found.')

    text    = args.bib.read_text(encoding='utf-8')
    entries = parse_bib(text)
    print(f'Validating {len(entries)} entries in {args.bib}')

    all_warnings: list[Warning] = []
    for entry in entries:
        for check in ALL_CHECKS:
            all_warnings.extend(check(entry))

    if args.errors_only:
        all_warnings = [w for w in all_warnings if w.severity == 'ERROR']

    errors = [w for w in all_warnings if w.severity == 'ERROR']
    warns  = [w for w in all_warnings if w.severity == 'WARN']

    print(f'\n--- Results: {len(errors)} ERROR(s), {len(warns)} WARN(s) ---')
    if all_warnings:
        for w in sorted(all_warnings, key=lambda x: (x.severity, x.key)):
            print(w)
    else:
        print('  No issues found.')

    # Summary by entry type
    from collections import Counter
    type_counts = Counter(e.etype for e in entries)
    print('\n--- Entry type distribution ---')
    for t, n in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f'  {t:<12} {n:>4}')

    if args.strict and all_warnings:
        sys.exit(1)


if __name__ == '__main__':
    main()
