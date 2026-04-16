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

# pdfLaTeX verbatiminput is ASCII-safe; strip combining marks (e.g. U+0301) from UTF-8 diffs.
sanitize_diff() {
  python3 -c 'import sys, unicodedata
s = sys.stdin.read()
s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
sys.stdout.write(s)'
}

git -C "${REPO}" diff congress/115..congress/118 -- \
  uscode/title-18-crimes-and-criminal-procedure/chapter-044-firearms.md \
  | sanitize_diff > "${OUT}/usc_diff_firearms_congress115-118.diff"

git -C "${REPO}" diff congress/113..congress/118 -- \
  uscode/title-52-voting-and-elections/chapter-103-enforcement-of-voting-rights.md \
  | sanitize_diff > "${OUT}/usc_diff_voting_congress113-118.diff"

echo "Wrote:"
echo "  ${OUT}/usc_diff_firearms_congress115-118.diff"
echo "  ${OUT}/usc_diff_voting_congress113-118.diff"
