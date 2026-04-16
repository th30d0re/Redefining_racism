#!/usr/bin/env bash
# With no arguments: write preset diffs into Paper/usc_snippets/ (see usc_write_diffs.sh).
# With three arguments: print a sanitized unified diff to stdout:
#   usc_diff.sh TAG_A TAG_B uscode/relative/path.md > out.diff
# Example:
#   usc_diff.sh congress/115 congress/118 uscode/title-18-crimes-and-criminal-procedure/chapter-044-firearms.md
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO="${ROOT}/reference/us-code"

sanitize_diff() {
  python3 -c 'import sys, unicodedata
s = sys.stdin.read()
s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
sys.stdout.write(s)'
}

if [[ $# -eq 0 ]]; then
  exec "${ROOT}/tools/usc_write_diffs.sh"
fi

if [[ $# -ne 3 ]]; then
  echo "Usage: $0" >&2
  echo "       $0 TAG_A TAG_B PATH_UNDER_USCODE   (diff printed to stdout)" >&2
  exit 1
fi

if [[ ! -d "${REPO}/.git" ]]; then
  echo "Missing clone: ${REPO}" >&2
  exit 1
fi

git -C "${REPO}" diff "$1..$2" -- "$3" | sanitize_diff
