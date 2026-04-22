#!/usr/bin/env python3
"""
convert_bibliography.py
=======================
Extracts the \\thebibliography block from a LaTeX source file and converts
every \\bibitem entry into a well-formed BibLaTeX entry, writing the result
to Paper/references.bib.

Usage (from repository root):
    python3 Paper/scripts/convert_bibliography.py

    # Explicit alternate source (e.g. a pre-migration backup):
    python3 Paper/scripts/convert_bibliography.py --source Paper/Redefining_Racism_BACKUP_pre_restructure.tex

Output:
    Paper/references.bib          — the BibLaTeX database
    Summary printed to stdout     — total entries, type distribution,
                                    flagged/validation-warning entries
"""

import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Paths (relative to repo root)
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Repository-local source candidates in deterministic priority order.
# No /tmp or other machine-local paths — all candidates live under REPO_ROOT.
_REPO_CANDIDATES = [
    REPO_ROOT / "Paper" / "Redefining_Racism.tex",
    REPO_ROOT / "Paper" / "Redefining_Racism_BACKUP_pre_restructure.tex",
]

BIB_FILE = REPO_ROOT / "Paper" / "references.bib"


def _pick_tex_source(explicit: Path | None = None) -> Path:
    """
    Return the TeX source that contains a \\thebibliography block.

    Priority:
      1. Explicit path passed via ``--source`` (must be under REPO_ROOT).
      2. Repository candidates in order (_REPO_CANDIDATES).

    Raises SystemExit with a helpful message if no valid source is found.
    """
    candidates = ([explicit] if explicit else []) + _REPO_CANDIDATES
    for candidate in candidates:
        if not candidate.exists():
            continue
        if r'\begin{thebibliography}' in candidate.read_text(encoding='utf-8'):
            return candidate

    sources_tried = '\n  '.join(str(c) for c in candidates)
    sys.exit(
        'ERROR: No TeX source containing \\thebibliography found.\n'
        f'Tried:\n  {sources_tried}\n'
        'Pass an explicit source with --source <path> or restore the bibliography block.'
    )


# ---------------------------------------------------------------------------
# LaTeX cleaning helpers
# ---------------------------------------------------------------------------

def strip_latex_commands(text: str) -> str:
    """Remove or simplify common LaTeX markup in field values."""
    # \textit{...} / \textbf{...} / \emph{...} → bare content
    text = re.sub(r'\\(?:textit|textbf|emph|textrm|textsc)\{([^}]*)\}', r'\1', text)
    # \'{x} style accents → x  (rough simplification for BibTeX)
    text = re.sub(r"\\['`^\"~=.]\{?([A-Za-z])\}?", r'\1', text)
    # \v{x} \c{x} \d{x} \b{x} \u{x} \H{x} \t{x} style accents
    text = re.sub(r'\\[vcdbHturkl]\{([A-Za-z])\}', r'\1', text)
    # \'x  (no braces)
    text = re.sub(r"\\['`^\"~=.\\]([A-Za-z])", r'\1', text)
    # Ligature/special chars
    replacements = {
        r'\ae': 'ae', r'\AE': 'AE', r'\oe': 'oe', r'\OE': 'OE',
        r'\aa': 'a',  r'\AA': 'A',  r'\o':  'o',  r'\O':  'O',
        r'\ss': 'ss', r'\l':  'l',  r'\L':  'L',  r'\i':  'i',
        r'\j':  'j',
        r'~':   ' ',  r'\ ':  ' ',
        r'---': '--', r'--':  '--',
        r'\&':  '&',  r'\%':  '%',  r'\$':  '$',
        r'\#':  '#',  r'\_':  '_',
        r'\{':  '{',  r'\}':  '}',
    }
    for latex, plain in replacements.items():
        text = text.replace(latex, plain)
    # Remove remaining \cmd with no argument
    text = re.sub(r'\\[A-Za-z]+\s*', ' ', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_url(text: str):
    """Return the first \\url{...} value found in text, or None."""
    m = re.search(r'\\url\{([^}]+)\}', text)
    return m.group(1) if m else None


def extract_year(text: str):
    """Return the last 4-digit year found in text, or ''."""
    years = re.findall(r'\b(1[4-9]\d{2}|20[012]\d)\b', text)
    return years[-1] if years else ''


def _extract_braced(text: str, start: int) -> str:
    """
    Extract the content of the brace-group starting at text[start] (must be '{').
    Handles arbitrarily nested braces.
    """
    assert text[start] == '{'
    depth = 0
    buf: list[str] = []
    i = start
    while i < len(text):
        ch = text[i]
        if ch == '{':
            depth += 1
            if depth > 1:
                buf.append(ch)
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return ''.join(buf)
            buf.append(ch)
        else:
            buf.append(ch)
        i += 1
    return ''.join(buf)


def extract_title_from_textit(text: str):
    """Return content of the first \\textit{...} block, handling nested braces."""
    m = re.search(r'\\textit(\{)', text)
    if m:
        content = _extract_braced(text, m.start(1))
        return strip_latex_commands(content)
    return ''


def extract_quoted_title(text: str):
    """Return content of the first ``...'' or "..." block (article title)."""
    m = re.search(r'``(.*?)\'\'', text, re.DOTALL)
    if m:
        return strip_latex_commands(m.group(1))
    m = re.search(r'"(.*?)"', text, re.DOTALL)
    if m:
        return strip_latex_commands(m.group(1))
    return ''


def _split_authors_to_and(raw_authors: str) -> str:
    """
    Convert a comma-separated author string to BibLaTeX 'and'-separated format.

    Input examples:
      "Piketty, T., Saez, E., and Zucman, G."
      "Acemoglu, D., Johnson, S., and Robinson, J.A."
      "Koper, Christopher S., Daniel J. Woods, and Jeffrey A. Roth"

    Output examples:
      "Piketty, T. and Saez, E. and Zucman, G."
      "Acemoglu, D. and Johnson, S. and Robinson, J.A."
      "Koper, Christopher S. and Daniel J. Woods and Jeffrey A. Roth"
    """
    # Normalise " and " variants
    s = re.sub(r'\s+and\s+', ' @@AND@@ ', raw_authors, flags=re.IGNORECASE)
    s = re.sub(r',\s*$', '', s)  # trailing comma

    # Split on explicit and-markers first
    and_parts = [p.strip() for p in s.split(' @@AND@@ ')]

    result: list[str] = []
    for part in and_parts:
        part = part.strip().rstrip(',')
        # Try to split comma-separated "Last, F., Last2, F2." into individual names
        # Strategy: split on ", " that is followed by a capital letter
        # This separates "Piketty, T., Saez, E." → ["Piketty, T.", " Saez, E."]
        subnames = re.split(r',\s+(?=[A-Z])', part)
        if len(subnames) > 2:
            # Pairs: subnames[0]="Piketty", [1]="T.", [2]="Saez", [3]="E." etc.
            # Re-pair as "Last, First"
            i = 0
            rebuilt: list[str] = []
            while i < len(subnames):
                # Heuristic: next token is a first name / initials (≤ 25 chars)
                # rather than a standalone surname
                if i + 1 < len(subnames) and len(subnames[i + 1]) <= 25:
                    rebuilt.append(f'{subnames[i]}, {subnames[i+1].strip()}')
                    i += 2
                else:
                    rebuilt.append(subnames[i])
                    i += 1
            result.extend(rebuilt)
        else:
            result.append(part)

    return ' and '.join(r.strip() for r in result if r.strip())


def extract_author(raw: str) -> str:
    """
    Best-effort author extraction from the raw \\bibitem text.
    Returns a BibLaTeX-style author string (Last, First and Last, First ...).
    """
    # Take the first logical 'sentence' up to the first period or \\textit
    author_chunk = re.split(r'\\textit|``|\bIn\b|\bAvailable\b', raw, maxsplit=1)[0]
    author_chunk = strip_latex_commands(author_chunk).strip().rstrip('.,;')
    author_chunk = re.sub(r'\s+', ' ', author_chunk)

    if not author_chunk:
        return 'Unknown'

    # If there are multiple commas, try to convert to 'and'-separated format
    if author_chunk.count(',') >= 2:
        author_chunk = _split_authors_to_and(author_chunk)

    return author_chunk


def safe_title_fallback(raw: str, n: int = 80) -> str:
    """
    Produce a safe short title from raw LaTeX without unbalanced braces.
    Strips all \\url{...} and \\cmd{...} before truncating.
    """
    # Remove \url{...} first (before any other processing)
    clean = re.sub(r'\\url\{[^}]*\}', '', raw)
    # Remove \texttt{...} etc.
    clean = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', clean)
    # Strip remaining commands
    clean = strip_latex_commands(clean)
    # Take up to n chars and trim at last space
    if len(clean) > n:
        clean = clean[:n].rsplit(' ', 1)[0]
    return clean.strip(). rstrip('.,;')


def extract_journal(raw: str) -> str:
    """Extract journal/booktitle from \\textit after author line."""
    # Pattern: ``. Journal Title'' or later textit after an article title
    # Journals appear as \textit after the quoted article title
    parts = re.split(r'``[^`]+\'\'', raw, maxsplit=1)
    if len(parts) > 1:
        m = re.search(r'\\textit\{([^}]*)\}', parts[1])
        if m:
            return strip_latex_commands(m.group(1))
    return ''


def extract_volume_issue_pages(raw: str):
    """Return (volume, issue, pages) tuple from raw text."""
    vol = issue = pages = ''
    # vol. N, no. M (YYYY): ppp–ppp  or  N, no. M (YYYY): ppp–ppp
    m = re.search(r'\b(\d+),\s*no[.~\s]+(\d+)[^:]*:\s*([\d\-–]+)', raw)
    if m:
        vol, issue, pages = m.group(1), m.group(2), m.group(3)
        return vol, issue, pages
    # vol N (YYYY): ppp
    m = re.search(r'\b(\d+)\s*\([12]\d{3}\)\s*:\s*([\d\-–]+)', raw)
    if m:
        vol, pages = m.group(1), m.group(2)
        return vol, issue, pages
    return vol, issue, pages


def extract_publisher_location(raw: str):
    """Rough extraction of City: Publisher from book-like entries."""
    # Pattern: City: Publisher (possibly with commas), YEAR
    # Capture everything between City: and the final ,YEAR
    m = re.search(
        r'(?:^|\.)\s*([A-Z][A-Za-z\s.,\']{1,40}?):\s*(.+?),\s*\d{4}',
        raw
    )
    if m:
        location = strip_latex_commands(m.group(1)).strip()
        publisher = strip_latex_commands(m.group(2)).strip()
        # Sanity: location should be short and not contain another colon
        if ':' not in location and len(location) < 50:
            return location, publisher
    return '', ''


# ---------------------------------------------------------------------------
# Classification heuristics
# ---------------------------------------------------------------------------

# Legal patterns — must be actual citation formats, not just "U.S." in agency names
_LEGAL_RE = re.compile(
    r'(?:'
    # Case citations: U.S. (number) or U.S. ___ or F.2d F.3d S.Ct.
    r'\d+\s+U\.S\.[\s_]+\d+'
    r'|U\.S\.\s*\(.*How\.|U\.S\.\s*___'
    r'|\b\d+\s+F\.\d[a-z]+\s+\d+'
    r'|\bS\.Ct\.\s+\d+'
    # Statute citations: Pub. L. 99-308, 26 U.S.C. ch., 50 Stat.
    r'|Pub\.\s*L\.\s*\d'
    r'|\d+\s+U\.S\.C\.'
    r'|\d+\s+Stat\.\s+\d'
    # v. [Capital] — case name pattern
    r'|\\textit\{[^}]*\bv\.\s*[A-Z]'
    # N.Y. Laws / Assembly Bill
    r'|N\.Y\.\s*Laws\s+ch\.'
    r'|Assembly\s+Bill\s+\d'
    # UN resolutions with letter codes
    r'|Resolution\s+A/'
    r')',
    re.IGNORECASE
)

_DOCUMENTARY_RE = re.compile(
    r'\[\s*Documentary\s*\]|\[Film\]|\[Short\s+Film\]|Director\)',
    re.IGNORECASE
)

_ONLINE_RE = re.compile(
    r'\\url\{|youtu\.be|ted\.com|podcast|Podcast|Available at|'
    r'Accessed|\.org/|\.gov/|\.edu/|\.com/',
    re.IGNORECASE
)

_PAPAL_BULL_RE = re.compile(r'Papal\s+Bull', re.IGNORECASE)

_REPORT_RE = re.compile(
    r'\b(?:Report|Survey|Working\s+Paper|Dataset|Data\s+Release|'
    r'Press\s+Release|Bulletin|Technical\s+Note)\b',
    re.IGNORECASE
)

_ARTICLE_SIGNALS = [
    # Quoted title + \textit journal
    re.compile(r'``[^`]+\'\'.*?\\textit\{', re.DOTALL),
    # vol. / no. / page pattern
    re.compile(r'\b(?:vol\.|no\.|pp\.\s*\d|\d+\s*\([12]\d{3}\)\s*:)', re.IGNORECASE),
]


def classify_entry(key: str, raw: str) -> str:
    """Return a BibLaTeX entry type string (without @)."""
    if _PAPAL_BULL_RE.search(raw):
        return 'misc'   # Papal Bull

    if _LEGAL_RE.search(raw):
        # Refine: if it's a statute/act, still misc; if it's a case, misc
        return 'misc'   # Legal Case or Legislation

    if _DOCUMENTARY_RE.search(raw):
        return 'movie'

    has_url = bool(extract_url(raw))

    # Check for article indicators first (even if URL present)
    for sig in _ARTICLE_SIGNALS:
        if sig.search(raw):
            if has_url and not _ONLINE_RE.search(raw):
                return 'article'
            if has_url:
                # Could be online article — use @article with url field
                return 'article'
            return 'article'

    if _ONLINE_RE.search(raw) or has_url:
        return 'online'

    if _REPORT_RE.search(raw):
        return 'report'

    # Book heuristic: has \textit title
    if extract_title_from_textit(raw):
        # Even if publisher parse fails, if there's a year and no URL it's likely a book
        loc, pub = extract_publisher_location(raw)
        entry_year = extract_year(raw)
        if pub or entry_year:
            return 'book'

    return 'misc'


# ---------------------------------------------------------------------------
# Special-key overrides (from plan Step 2)
# ---------------------------------------------------------------------------

_TYPE_OVERRIDES: dict[str, str] = {
    # Papal Bulls
    'dumdiversas':          'misc',
    'romanuspontifex':      'misc',
    # Legal cases
    'dredscott':            'misc',
    'inredebs':             'misc',
    'bruen':                'misc',
    'heller':               'misc',
    'mcdonald':             'misc',
    'caetano':              'misc',
    'bradwell':             'misc',
    'buck':                 'misc',
    'castlerock':           'misc',
    'deshaney':             'misc',
    'smith_v_allwright':    'misc',
    'williams_v_miss':      'misc',
    'tel_wash_v_davis':     'misc',
    'tel_arlington_heights':'misc',
    'tel_sandoval':         'misc',
    'tel_nashville_case':   'misc',
    # Legislation
    'sullivanlaw':          'misc',
    'nfa1934':              'misc',
    'mulford1967':          'misc',
    'gca1968':              'misc',
    'hughes1986':           'misc',
    'brady1993':            'misc',
    'awb1994':              'misc',
    'epsteinact':           'misc',
    'murphy2025nfa':        'misc',
    # UN / International instruments
    'cubaembargo':          'misc',
    'aesbloc':              'misc',
    # Documentary
    'thirteenth':           'movie',
    # Online / podcast / web
    'abulhawa':             'online',
    'biewen':               'online',
    'blscpi':               'online',
    'apolloepstein':        'online',
    'cnn_lacounty':         'online',
    'python_master_slave':  'online',
    'github_main':          'online',
    'tel_nashville':        'online',
    'tel_baltimore':        'online',
    # Reports
    'itpi':                 'report',
    'tel_gao':              'report',
    # Legislation / regulation (misc)
    'sres400_1976':         'misc',
    'fisa_1978':            'misc',
    'tel_lsl':              'misc',
    'tel_title_vi':         'misc',
    # Misc (internal memos, loose citations, manuscripts)
    'lacounty_memo':        'misc',
    'tel_soil_sampling':    'misc',
    'theodore_missing_variable': 'misc',
}

_EXTRA_FIELDS: dict[str, dict[str, str]] = {
    'dumdiversas':          {'type': 'Papal Bull'},
    'romanuspontifex':      {'type': 'Papal Bull'},
    'dredscott':            {'type': 'Legal Case'},
    'inredebs':             {'type': 'Legal Case'},
    'bruen':                {'type': 'Legal Case'},
    'heller':               {'type': 'Legal Case'},
    'mcdonald':             {'type': 'Legal Case'},
    'caetano':              {'type': 'Legal Case'},
    'bradwell':             {'type': 'Legal Case'},
    'buck':                 {'type': 'Legal Case'},
    'castlerock':           {'type': 'Legal Case'},
    'deshaney':             {'type': 'Legal Case'},
    'smith_v_allwright':    {'type': 'Legal Case'},
    'williams_v_miss':      {'type': 'Legal Case'},
    'tel_wash_v_davis':     {'type': 'Legal Case'},
    'tel_arlington_heights':{'type': 'Legal Case'},
    'tel_sandoval':         {'type': 'Legal Case'},
    'tel_nashville_case':   {'type': 'Legal Case'},
    'nfa1934':              {'type': 'Legislation'},
    'mulford1967':          {'type': 'Legislation'},
    'gca1968':              {'type': 'Legislation'},
    'hughes1986':           {'type': 'Legislation'},
    'brady1993':            {'type': 'Legislation'},
    'awb1994':              {'type': 'Legislation'},
    'epsteinact':           {'type': 'Legislation'},
    'murphy2025nfa':        {'type': 'Legislation'},
    'sullivanlaw':          {'type': 'Legislation'},
    'sres400_1976':         {'type': 'Legislation'},
    'fisa_1978':            {'type': 'Legislation'},
    'tel_lsl':              {'type': 'Regulation'},
    'tel_title_vi':         {'type': 'Legislation'},
    'cubaembargo':          {'type': 'UN Resolution'},
    'aesbloc':              {'type': 'Treaty'},
    'lacounty_memo':        {'type': 'Government Memo'},
    'theodore_missing_variable': {'type': 'Unpublished Manuscript'},
}


# ---------------------------------------------------------------------------
# BibLaTeX entry builder
# ---------------------------------------------------------------------------

def build_entry(key: str, raw: str) -> str:
    """Build a BibLaTeX entry string for the given key and raw \\bibitem body."""
    entry_type = _TYPE_OVERRIDES.get(key, classify_entry(key, raw))
    extra = _EXTRA_FIELDS.get(key, {})

    author  = extract_author(raw)
    year    = extract_year(raw)
    url     = extract_url(raw)
    title   = extract_title_from_textit(raw)

    lines: list[str] = [f'@{entry_type}{{{key},']

    def add(field: str, value: str):
        if value:
            # Escape bare % signs (not already escaped)
            value = re.sub(r'(?<!\\)%', r'\\%', value)
            # Protect author fields with remaining multiple commas using double braces
            # to prevent biber "too many commas" parse errors
            if field == 'author' and value.count(',') >= 2:
                lines.append(f'  {field:<12} = {{{{{value}}}}},')
                return
            lines.append(f'  {field:<12} = {{{value}}},')

    fallback_title = safe_title_fallback(raw)

    if entry_type == 'article':
        quoted_title = extract_quoted_title(raw)
        journal      = extract_journal(raw)
        vol, iss, pgs = extract_volume_issue_pages(raw)
        add('author',  author)
        add('title',   quoted_title or title or fallback_title)
        add('journal', journal)
        add('year',    year)
        add('volume',  vol)
        add('number',  iss)
        add('pages',   pgs)
        if url:
            add('url', url)

    elif entry_type == 'book':
        loc, pub = extract_publisher_location(raw)
        add('author',    author)
        add('title',     title or fallback_title)
        add('publisher', pub)
        add('address',   loc)
        add('year',      year)

    elif entry_type in ('online', 'movie'):
        add('author', author)
        add('title',  title or extract_quoted_title(raw) or fallback_title)
        add('year',   year)
        if url:
            add('url', url)
        if entry_type == 'online':
            add('urldate', '2026-04-21')

    elif entry_type == 'report':
        loc, pub = extract_publisher_location(raw)
        add('author',      author)
        add('title',       title or extract_quoted_title(raw) or fallback_title)
        add('institution', pub or author)
        add('year',        year)
        if url:
            add('url', url)

    else:  # misc (legal, papal bull, legislation, fallback)
        add('author', author)
        add('title',  title or extract_quoted_title(raw) or fallback_title)
        add('year',   year)
        if url:
            add('url', url)
        for field, val in extra.items():
            add(field, val)

    lines.append('}')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Main extraction loop
# ---------------------------------------------------------------------------

def extract_bibliography(tex_path: Path) -> list[tuple[str, str]]:
    """
    Return a list of (key, raw_body) pairs from the \\thebibliography block.
    """
    text = tex_path.read_text(encoding='utf-8')

    # Isolate the bibliography block
    bib_start = text.find(r'\begin{thebibliography}')
    bib_end   = text.find(r'\end{thebibliography}')
    if bib_start == -1 or bib_end == -1:
        sys.exit(f'ERROR: Could not locate \\thebibliography block in {tex_path}')

    bib_block = text[bib_start:bib_end]

    # Split on \bibitem{key} boundaries
    # Each item: key followed by body until next \bibitem or end
    pattern = re.compile(r'\\bibitem\{([^}]+)\}\s*', re.DOTALL)
    splits   = pattern.split(bib_block)

    # splits layout: [preamble, key1, body1, key2, body2, ...]
    entries: list[tuple[str, str]] = []
    it = iter(splits[1:])   # skip preamble
    for key, body in zip(it, it):
        # Strip trailing whitespace/comments
        body = body.strip()
        if body:
            entries.append((key, body))

    return entries


def _validate_entries(bib_lines: list[str]) -> list[str]:
    """
    Run a quick validation pass over the generated BibLaTeX text.
    Returns a list of human-readable warning strings.
    """
    warnings: list[str] = []
    bib_text = '\n'.join(bib_lines)

    # Parse each entry for field-level checks
    for em in re.finditer(r'@(\w+)\{(\w+),(.*?)\n\}', bib_text, re.DOTALL):
        etype = em.group(1).lower()
        key   = em.group(2)
        body  = em.group(3)

        def field(name: str) -> str:
            m = re.search(rf'{name}\s+=\s+\{{(.*?)\}}(?:,|\n)', body, re.DOTALL)
            return m.group(1).strip() if m else ''

        author = field('author')
        year   = field('year')
        title  = field('title')

        # 1. Implausible year — statute/citation numbers parsed as years
        if year.isdigit():
            y = int(year)
            if not (1400 <= y <= 2030):
                warnings.append(
                    f'  [{key}] implausible year={y} (statute number? check raw source)'
                )

        # 2. Very long author field (author contains descriptive text)
        if len(author) > 120:
            warnings.append(
                f'  [{key}] author field is {len(author)} chars '
                f'(likely contains full description, not just name)'
            )

        # 3. Author == "Unknown" for entries that have a knowable issuer
        if author.strip('{}') == 'Unknown':
            hint = (
                '{{Supreme Court of the United States}}'
                if etype == 'misc' and 'v.' in title
                else '{{Issuing Body}} or {{Anonymous}}'
            )
            warnings.append(
                f'  [{key}] author=Unknown — consider {hint}'
            )

        # 4. Author contains URL or HTTP
        if 'http' in author or 'www.' in author:
            warnings.append(
                f'  [{key}] author field contains URL — probable extraction error'
            )

        # 5. Missing title
        if not title:
            warnings.append(f'  [{key}] missing title field')

        # 6. Author and title are identical (full description in both)
        if author and title and author.strip('{}') == title.strip('{}'):
            warnings.append(
                f'  [{key}] author == title (both contain full entry description)'
            )

    return warnings


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Convert \\thebibliography entries to BibLaTeX format.',
    )
    parser.add_argument(
        '--source',
        type=Path,
        default=None,
        metavar='TEX_FILE',
        help=(
            'Explicit path to a .tex file containing a \\thebibliography block. '
            'Must be a file under the repository root. '
            'If omitted the script searches repository-local candidates in order.'
        ),
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=BIB_FILE,
        metavar='BIB_FILE',
        help=f'Output .bib file path (default: {BIB_FILE})',
    )
    args = parser.parse_args()

    tex_file = _pick_tex_source(args.source)
    print(f'Source : {tex_file}')
    print(f'Output : {args.output}')

    entries = extract_bibliography(tex_file)
    print(f'Extracted {len(entries)} bibliography entries.')

    type_dist: dict[str, int] = defaultdict(int)
    flagged: list[str] = []

    bib_lines: list[str] = [
        '% references.bib',
        '% Generated by Paper/scripts/convert_bibliography.py',
        '% Manual review required for entries flagged below.',
        '',
    ]

    for key, raw in entries:
        entry_type = _TYPE_OVERRIDES.get(key, classify_entry(key, raw))
        type_dist[entry_type] += 1

        # Flag misc entries not in the override table (potential misclassification)
        if entry_type == 'misc' and key not in _TYPE_OVERRIDES:
            flagged.append(key)

        bib_lines.append(build_entry(key, raw))
        bib_lines.append('')   # blank line between entries

    args.output.write_text('\n'.join(bib_lines), encoding='utf-8')
    print(f'Wrote {args.output}')

    print('\n--- Type Distribution ---')
    for t, n in sorted(type_dist.items(), key=lambda x: -x[1]):
        print(f'  {t:<12} {n:>4}')

    print(f'\n--- Entries flagged for manual review ({len(flagged)}) ---')
    for k in flagged:
        print(f'  {k}')

    # Run built-in validation pass
    validation_warnings = _validate_entries(bib_lines)
    print(f'\n--- Validation warnings ({len(validation_warnings)}) ---')
    for w in validation_warnings:
        print(w)
    if validation_warnings:
        print(
            '\nRun Paper/scripts/validate_bib.py for a full audit of the generated file.'
        )

    print('\nDone. Review flagged/warned entries in Paper/references.bib before compiling.')


if __name__ == '__main__':
    main()
