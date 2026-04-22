#!/usr/bin/env python3
"""
Split PDFs over 200 MB into chunks under 200 MB for NotebookLM upload.
Output goes to split_pdfs/ subfolder.
"""

import os
import math
import tempfile
import shutil
from pathlib import Path
from pypdf import PdfReader, PdfWriter

SOURCE_DIR = Path(__file__).parent
OUTPUT_DIR = SOURCE_DIR / "split_pdfs"
# Use true megabytes (1 MB = 1,000,000 bytes), NOT mebibytes (1 MiB = 1,048,576 bytes)
# NotebookLM enforces a hard 200 MB limit using decimal MB.
# Target 175 MB per chunk for a comfortable margin.
MAX_SIZE_MB = 200
MAX_SIZE_BYTES = MAX_SIZE_MB * 1_000_000
TARGET_MB = 175
TARGET_BYTES = TARGET_MB * 1_000_000

OUTPUT_DIR.mkdir(exist_ok=True)

def get_file_size_mb(path):
    """Return size in true megabytes (1 MB = 1,000,000 bytes)."""
    return os.path.getsize(path) / 1_000_000

def split_pdf(pdf_path: Path):
    size_mb = get_file_size_mb(pdf_path)
    if size_mb <= MAX_SIZE_MB:
        return

    stem = pdf_path.stem
    print(f"\n→ {stem} ({size_mb:.0f} MB)")

    reader = PdfReader(str(pdf_path))
    total_pages = len(reader.pages)
    file_size = os.path.getsize(pdf_path)

    # Estimate pages per chunk targeting 175 true MB (1 MB = 1,000,000 bytes)
    bytes_per_page = file_size / total_pages
    pages_per_chunk = max(1, int(TARGET_BYTES / bytes_per_page))

    num_chunks = math.ceil(total_pages / pages_per_chunk)
    print(f"   Pages: {total_pages}, ~{bytes_per_page/1024:.0f} KB/page → {pages_per_chunk} pages/chunk → {num_chunks} parts")

    for chunk_idx in range(num_chunks):
        start = chunk_idx * pages_per_chunk
        end = min(start + pages_per_chunk, total_pages)

        writer = PdfWriter()
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        part_num = chunk_idx + 1
        out_name = f"{stem}_part{part_num:02d}_of{num_chunks:02d}.pdf"
        out_path = OUTPUT_DIR / out_name

        # Write to temp first, then verify size and move
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp_path = Path(tmp.name)

        writer.write(str(tmp_path))
        actual_size_mb = get_file_size_mb(tmp_path)

        if actual_size_mb > MAX_SIZE_MB:
            # Part is still too big — subdivide further on retry pass
            print(f"   ⚠  Part {part_num} is {actual_size_mb:.1f} MB (over limit), will re-split")
            tmp_path.unlink(missing_ok=True)
            # Recursively handle oversized chunk
            sub_chunks = math.ceil((end - start) / 2)
            _split_range(reader, stem, start, end, sub_chunks, chunk_idx, num_chunks)
        else:
            shutil.move(str(tmp_path), str(out_path))
            print(f"   ✓  {out_name} — {actual_size_mb:.1f} MB (pages {start+1}–{end})")

def _split_range(reader, stem, page_start, page_end, pages_per_chunk, parent_chunk, parent_total):
    """Recursively split a range if a chunk came out too big."""
    total_in_range = page_end - page_start
    num_sub = math.ceil(total_in_range / pages_per_chunk)
    for sub_idx in range(num_sub):
        s = page_start + sub_idx * pages_per_chunk
        e = min(s + pages_per_chunk, page_end)
        writer = PdfWriter()
        for p in range(s, e):
            writer.add_page(reader.pages[p])
        label = f"part{parent_chunk+1:02d}s{sub_idx+1:02d}_of{parent_total:02d}"
        out_name = f"{stem}_{label}.pdf"
        out_path = OUTPUT_DIR / out_name
        writer.write(str(out_path))
        size_mb = get_file_size_mb(out_path)
        print(f"   ✓  {out_name} — {size_mb:.1f} MB (pages {s+1}–{e})")

def main():
    pdfs = sorted(SOURCE_DIR.glob("*.pdf"))
    over_limit = [(p, get_file_size_mb(p)) for p in pdfs if get_file_size_mb(p) > MAX_SIZE_MB]

    print(f"Found {len(over_limit)} PDFs over {MAX_SIZE_MB} MB to split:")
    for p, mb in over_limit:
        print(f"  {p.name}: {mb:.0f} MB")

    for pdf_path, _ in over_limit:
        split_pdf(pdf_path)

    print("\n✅ Done! Split PDFs saved to:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
