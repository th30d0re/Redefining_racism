#!/usr/bin/env python3
"""
split_large_markdown_cases.py

Splits markdown case files that exceed NotebookLM's 500,000-word limit.
Splits at natural paragraph breaks, saving each part to:
  Paper/research/markdown_cases/split/{case_name}_part1.md
  Paper/research/markdown_cases/split/{case_name}_part2.md
  ...

Usage:
    python3 split_large_markdown_cases.py [--dry-run] [--limit 480000]
"""

import os
import sys
import argparse
from pathlib import Path

WORD_LIMIT = 480_000  # Conservative threshold (under NotebookLM's 500K cap)
CASES_DIR = Path(__file__).parent.parent / "research" / "markdown_cases"
SPLIT_DIR = CASES_DIR / "split"


def count_words(text: str) -> int:
    return len(text.split())


def split_into_parts(text: str, word_limit: int) -> list[str]:
    """
    Split text into chunks of at most word_limit words,
    breaking only at paragraph boundaries (blank lines).
    """
    paragraphs = text.split("\n\n")
    parts = []
    current_words = 0
    current_chunk: list[str] = []

    for para in paragraphs:
        para_words = count_words(para)

        # If a single paragraph is itself over the limit, we must force-split it
        if para_words > word_limit:
            # Flush current chunk first
            if current_chunk:
                parts.append("\n\n".join(current_chunk))
                current_chunk = []
                current_words = 0

            # Force-split the monster paragraph by sentence (fallback: by lines)
            lines = para.split("\n")
            sub_chunk: list[str] = []
            sub_words = 0
            for line in lines:
                lw = count_words(line)
                if sub_words + lw > word_limit and sub_chunk:
                    parts.append("\n".join(sub_chunk))
                    sub_chunk = []
                    sub_words = 0
                sub_chunk.append(line)
                sub_words += lw
            if sub_chunk:
                current_chunk = ["\n".join(sub_chunk)]
                current_words = sub_words
            continue

        if current_words + para_words > word_limit and current_chunk:
            parts.append("\n\n".join(current_chunk))
            current_chunk = []
            current_words = 0

        current_chunk.append(para)
        current_words += para_words

    if current_chunk:
        parts.append("\n\n".join(current_chunk))

    return parts


def process_file(md_path: Path, word_limit: int, dry_run: bool, split_dir: Path) -> dict:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    total_words = count_words(text)

    result = {
        "file": md_path.name,
        "total_words": total_words,
        "over_limit": total_words > word_limit,
        "parts_created": [],
    }

    if total_words <= word_limit:
        return result

    parts = split_into_parts(text, word_limit)
    case_stem = md_path.stem

    if not dry_run:
        split_dir.mkdir(parents=True, exist_ok=True)

    for i, part_text in enumerate(parts, start=1):
        part_name = f"{case_stem}_part{i}.md"
        part_path = split_dir / part_name
        part_words = count_words(part_text)

        # Prepend a header so each part is self-identified
        header = (
            f"# {case_stem.replace('_', ' ').title()} — Part {i} of {len(parts)}\n\n"
            f"> **Source file:** `{md_path.name}`  \n"
            f"> **Part {i}/{len(parts)}** — {part_words:,} words\n\n"
            "---\n\n"
        )
        full_content = header + part_text

        if not dry_run:
            part_path.write_text(full_content, encoding="utf-8")

        result["parts_created"].append({
            "name": part_name,
            "words": part_words,
            "path": str(part_path),
        })

    return result


def main():
    parser = argparse.ArgumentParser(description="Split large markdown case files for NotebookLM upload")
    parser.add_argument("--dry-run", action="store_true", help="Report what would be split without writing files")
    parser.add_argument("--limit", type=int, default=WORD_LIMIT, help=f"Word limit per part (default: {WORD_LIMIT:,})")
    parser.add_argument("--cases-dir", type=Path, default=CASES_DIR, help="Directory containing markdown case files")
    parser.add_argument("--split-dir", type=Path, default=SPLIT_DIR, help="Output directory for split files")
    args = parser.parse_args()

    md_files = sorted(args.cases_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {args.cases_dir}")
        sys.exit(1)

    print(f"NotebookLM word limit: {args.limit:,}")
    print(f"Scanning {len(md_files)} markdown files in {args.cases_dir}")
    print(f"Split output → {args.split_dir}")
    if args.dry_run:
        print("DRY RUN — no files will be written\n")
    print()

    over_limit = []
    near_limit = []
    ok = []

    for md_path in md_files:
        text = md_path.read_text(encoding="utf-8", errors="replace")
        wc = count_words(text)
        if wc > args.limit:
            over_limit.append((md_path, wc))
        elif wc > args.limit * 0.9:
            near_limit.append((md_path, wc))
        else:
            ok.append((md_path, wc))

    print(f"{'='*60}")
    print(f"❌ OVER LIMIT ({len(over_limit)} files — will be split)")
    print(f"{'='*60}")
    for path, wc in sorted(over_limit, key=lambda x: -x[1]):
        print(f"  {wc:>10,} words  {path.name}")
    print()

    if near_limit:
        print(f"{'='*60}")
        print(f"⚠️  NEAR LIMIT ({len(near_limit)} files — may work but watch these)")
        print(f"{'='*60}")
        for path, wc in sorted(near_limit, key=lambda x: -x[1]):
            print(f"  {wc:>10,} words  {path.name}")
        print()

    print(f"{'='*60}")
    print(f"✅ OK ({len(ok)} files — under limit, upload as-is)")
    print(f"{'='*60}")
    for path, wc in sorted(ok, key=lambda x: -x[1]):
        print(f"  {wc:>10,} words  {path.name}")
    print()

    if not over_limit:
        print("Nothing to split. All files are within the word limit.")
        return

    print(f"{'='*60}")
    print(f"Splitting {len(over_limit)} files...")
    print(f"{'='*60}")

    total_parts_created = 0
    for md_path, _ in over_limit:
        result = process_file(md_path, args.limit, args.dry_run, args.split_dir)
        n = len(result["parts_created"])
        total_parts_created += n
        action = "Would create" if args.dry_run else "Created"
        print(f"\n  {md_path.name}  ({result['total_words']:,} words)")
        for part in result["parts_created"]:
            print(f"    {action} → {part['name']}  ({part['words']:,} words)")

    print()
    if args.dry_run:
        print(f"DRY RUN complete. Would create {total_parts_created} part files in {args.split_dir}")
    else:
        print(f"Done. Created {total_parts_created} part files in {args.split_dir}")
        print()
        print("Upload the files in the 'split/' folder to NotebookLM instead of the originals.")
        print("Each part is self-labeled with its case name and part number.")


if __name__ == "__main__":
    main()
