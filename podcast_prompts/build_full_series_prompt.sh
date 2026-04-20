#!/usr/bin/env bash
# Rebuild 00_ROOT_The_Open_Source_Republic.md from:
#   - 00_ROOT_SERIES_FRAGMENT.md (shared series block only)
#   - Episode_01 … Episode_18 (verbatim), in broadcast order
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

OUT="00_ROOT_The_Open_Source_Republic.md"
FRAG="00_ROOT_SERIES_FRAGMENT.md"

if [[ ! -f "$FRAG" ]]; then
  echo "error: missing $FRAG" >&2
  exit 1
fi

{
  shopt -s nullglob
  cat "$FRAG"
  echo ""
  echo "## Verbatim episode prompts (Episodes 1–18)"
  echo ""
  echo "The sections below are the **complete** contents of each \`Episode_NN_*.md\` file, concatenated in broadcast order."
  echo ""
  for n in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18; do
    matches=( Episode_${n}_*.md )
    if [[ ${#matches[@]} -ne 1 ]]; then
      echo "error: expected exactly one Episode_${n}_*.md, got ${#matches[@]}: ${matches[*]-}" >&2
      exit 1
    fi
    f="${matches[0]}"
    echo ""
    echo "---"
    echo ""
    echo "### FILE: \`$f\` (verbatim full text follows)"
    echo ""
    echo "---"
    echo ""
    cat "$f"
  done
} > "${OUT}.tmp"
mv "${OUT}.tmp" "$OUT"
echo "wrote $OUT ($(wc -l < "$OUT") lines)"
