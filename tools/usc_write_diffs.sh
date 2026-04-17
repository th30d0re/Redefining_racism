#!/usr/bin/env bash
# Write git diffs from nickvido/us-code into Paper/usc_snippets/ for LaTeX \verbatiminput.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO="${ROOT}/reference/us-code"
OUT="${ROOT}/Paper/usc_snippets"
mkdir -p "${OUT}"

if [[ ! -d "${REPO}/.git" ]]; then
  echo "Missing clone: ${REPO}" >&2
  exit 1
fi

# pdfLaTeX \verbatiminput: strip combining marks, normalize common Unicode punctuation to ASCII,
# then wrap long OLRC lines so boxes stay inside the text block (see Paper/usc_macros.sty).
sanitize_diff() {
  python3 -c 'import sys, unicodedata
s = sys.stdin.read()
s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
for a, b in (
    ("\u201c", "\""), ("\u201d", "\""),
    ("\u2018", chr(39)), ("\u2019", chr(39)),
    ("\u2014", "--"), ("\u2013", "-"),
    ("\u2026", "..."),
    ("\u00a7", "Sec."),
):
    s = s.replace(a, b)
sys.stdout.write(s)'
}

wrap_diff_for_pdf() {
  local f="$1"
  local tmp="${f}.foldtmp"
  fold -s -w 88 "$f" > "$tmp" && mv "$tmp" "$f"
}

git -C "${REPO}" diff congress/115..congress/118 -- \
  uscode/title-18-crimes-and-criminal-procedure/chapter-044-firearms.md \
  | sanitize_diff > "${OUT}/usc_diff_firearms_congress115-118.diff"
wrap_diff_for_pdf "${OUT}/usc_diff_firearms_congress115-118.diff"

git -C "${REPO}" diff congress/113..congress/118 -- \
  uscode/title-52-voting-and-elections/chapter-103-enforcement-of-voting-rights.md \
  | sanitize_diff > "${OUT}/usc_diff_voting_congress113-118.diff"
wrap_diff_for_pdf "${OUT}/usc_diff_voting_congress113-118.diff"

echo "Wrote:"
echo "  ${OUT}/usc_diff_firearms_congress115-118.diff"
echo "  ${OUT}/usc_diff_voting_congress113-118.diff"
