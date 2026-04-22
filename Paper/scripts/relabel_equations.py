#!/usr/bin/env python3
"""
relabel_equations.py — Equation label migration for Redefining_Racism.tex

Two-phase design:
  Phase A (registry-driven)  — reads label → new_label pairs from registry .md
                                frontmatter and applies them.
  Phase B (auto-completion)  — discovers any remaining \label{eq:...} that do
                                not yet conform to the hybrid scheme
                                eq:<chapter>.<seq>[-<descriptor>], generates
                                labels from chapter position, and applies them.

Coverage validation runs after Phase A mapping is built: the script hard-fails
before writing anything if any non-conforming label is unmapped.

Usage:
    python3 Paper/scripts/relabel_equations.py           # apply changes
    python3 Paper/scripts/relabel_equations.py --dry-run # audit only
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
REGISTRY_DIR = PROJECT_ROOT / "Paper" / "empirical_validations"
MANUSCRIPT = PROJECT_ROOT / "Paper" / "Redefining_Racism.tex"

# Regex that matches the target hybrid label scheme:  eq:8.17-some-descriptor
# or eq:8.17 (no descriptor).
HYBRID_RE = re.compile(r"^eq:\d+\.\d+(-[\w-]+)?$")


# ---------------------------------------------------------------------------
# YAML frontmatter parser (no external deps)
# ---------------------------------------------------------------------------
def parse_frontmatter(text: str) -> dict[str, str]:
    """Extract scalar key:value pairs from the first YAML frontmatter block."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip().strip('"').strip("'")
    return result


# ---------------------------------------------------------------------------
# Phase A: build registry-driven mapping
# ---------------------------------------------------------------------------
def build_registry_mapping(
    registry_dir: Path,
) -> dict[str, tuple[str, Path]]:
    """Return {old_label: (new_label, md_path)} for registry files that have
    a non-empty new_label different from label."""
    mapping: dict[str, tuple[str, Path]] = {}
    for md_path in sorted(registry_dir.glob("*.md")):
        if md_path.name == "README.md":
            continue
        text = md_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        old = fm.get("label", "")
        new = fm.get("new_label", "")
        if not old or not new or old == new:
            continue
        if old in mapping:
            existing_new, existing_path = mapping[old]
            if existing_new != new:
                print(
                    f"WARNING: conflicting new_label for '{old}': "
                    f"'{existing_new}' ({existing_path.name}) vs "
                    f"'{new}' ({md_path.name}) — keeping first",
                    file=sys.stderr,
                )
            continue
        mapping[old] = (new, md_path)
    return mapping


# ---------------------------------------------------------------------------
# Manuscript label discovery
# ---------------------------------------------------------------------------
_LABEL_RE = re.compile(r"\\label\{(eq:[^}]+)\}")


def extract_all_labels(text: str) -> list[str]:
    """Return all eq:... label strings found in the manuscript (preserving order,
    deduplicating)."""
    seen: set[str] = set()
    result: list[str] = []
    for m in _LABEL_RE.finditer(text):
        lbl = m.group(1)
        if lbl not in seen:
            seen.add(lbl)
            result.append(lbl)
    return result


# ---------------------------------------------------------------------------
# Phase B: chapter detection and auto-label generation
# ---------------------------------------------------------------------------
_CHAPTER_RE = re.compile(r"^\\chapter\{", re.MULTILINE)


def build_chapter_map(text: str) -> dict[str, int]:
    """Return {label: chapter_number} for every eq: label in the manuscript.
    Chapter number is the 1-based count of \\chapter{ occurrences before the
    label's first appearance.  Chapter 0 = before any \\chapter declaration."""
    # Collect chapter start positions
    chapter_starts: list[int] = [m.start() for m in _CHAPTER_RE.finditer(text)]

    def chapter_at(pos: int) -> int:
        # Binary-search for how many chapter_starts are <= pos
        lo, hi = 0, len(chapter_starts)
        while lo < hi:
            mid = (lo + hi) // 2
            if chapter_starts[mid] <= pos:
                lo = mid + 1
            else:
                hi = mid
        return lo  # 1-based chapter count

    result: dict[str, int] = {}
    for m in _LABEL_RE.finditer(text):
        lbl = m.group(1)
        if lbl not in result:
            result[lbl] = chapter_at(m.start())
    return result


def _slug(old_label: str) -> str:
    """Derive a descriptor slug from a legacy label name."""
    name = old_label.removeprefix("eq:")
    name = re.sub(r"[_\s]+", "-", name)
    name = re.sub(r"[^a-z0-9\-]", "", name.lower())
    name = re.sub(r"-+", "-", name).strip("-")
    return name or "eq"


def build_auto_mapping(
    unmapped_labels: list[str],
    chapter_map: dict[str, int],
    all_hybrid_labels: set[str],
) -> dict[str, str]:
    """Generate {old_label: new_hybrid_label} for unmapped non-conforming labels.

    Sequence numbers are assigned by finding the highest existing sequence number
    for each chapter across ALL labels already in hybrid form (both from previous
    registry migration passes and already-present hybrid labels in the manuscript),
    then incrementing from the per-chapter maximum.
    """
    chapter_max: dict[int, int] = {}
    hybrid_seq_re = re.compile(r"^eq:(\d+)\.(\d+)")

    for lbl in all_hybrid_labels:
        m = hybrid_seq_re.match(lbl)
        if m:
            ch, seq = int(m.group(1)), int(m.group(2))
            chapter_max[ch] = max(chapter_max.get(ch, 0), seq)

    auto: dict[str, str] = {}
    for old in unmapped_labels:
        ch = chapter_map.get(old, 0)
        chapter_max[ch] = chapter_max.get(ch, 0) + 1
        seq = chapter_max[ch]
        slug = _slug(old)
        new_lbl = f"eq:{ch}.{seq}-{slug}"
        auto[old] = new_lbl

    return auto


# ---------------------------------------------------------------------------
# Coverage validation (hard-fail)
# ---------------------------------------------------------------------------
def validate_coverage(
    all_labels: list[str],
    full_map: dict[str, str],
    dry_run: bool,
) -> None:
    """Exit with a non-zero status if any non-conforming label is unmapped."""
    missing = [
        lbl
        for lbl in all_labels
        if not HYBRID_RE.match(lbl) and lbl not in full_map
    ]
    if missing:
        print(
            "\nCOVERAGE ERROR — the following labels are not in the hybrid scheme"
            " and have no mapping:\n",
            file=sys.stderr,
        )
        for lbl in missing:
            print(f"  {lbl}", file=sys.stderr)
        print(
            "\nMigration aborted. Add these labels to the registry or ensure the"
            " auto-generation logic covers them.",
            file=sys.stderr,
        )
        sys.exit(1)


# ---------------------------------------------------------------------------
# Sort substitutions longest-first (prevents partial-match collisions)
# ---------------------------------------------------------------------------
def sorted_pairs(mapping: dict[str, str]) -> list[tuple[str, str]]:
    """Return (old, new) pairs sorted by descending len(old)."""
    return sorted(mapping.items(), key=lambda t: len(t[0]), reverse=True)


# ---------------------------------------------------------------------------
# Manuscript replacement (plain-string, four LaTeX contexts)
# ---------------------------------------------------------------------------
def replace_in_manuscript(
    manuscript: Path,
    pairs: list[tuple[str, str]],
    dry_run: bool,
) -> int:
    """Apply all (old, new) substitutions to the manuscript.  Returns count."""
    text = manuscript.read_text(encoding="utf-8")
    total = 0

    for old, new in pairs:
        subs = [
            (f"\\label{{{old}}}", f"\\label{{{new}}}"),
            (f"\\ref{{{old}}}", f"\\ref{{{new}}}"),
            (f"\\eqref{{{old}}}", f"\\eqref{{{new}}}"),
            (f"eq.~\\ref{{{old}}}", f"eq.~\\ref{{{new}}}"),
        ]
        label_subs = 0
        for find_str, replace_str in subs:
            count = text.count(find_str)
            if count:
                if not dry_run:
                    text = text.replace(find_str, replace_str)
                label_subs += count
        if label_subs:
            print(
                f"  {old!r:50s} → {new!r:50s}  "
                f"({label_subs} site{'s' if label_subs != 1 else ''})"
            )
        total += label_subs

    if not dry_run:
        manuscript.write_text(text, encoding="utf-8")
    return total


# ---------------------------------------------------------------------------
# Registry .md update (Phase A labels only)
# ---------------------------------------------------------------------------
def update_registry_files(
    registry_pairs: dict[str, tuple[str, Path]],
    dry_run: bool,
) -> int:
    """Update label: field in each registry .md file to the new hybrid value."""
    updated = 0
    for old, (new, md_path) in registry_pairs.items():
        text = md_path.read_text(encoding="utf-8")
        new_text = re.sub(
            r"(?m)^(label:\s*)" + re.escape(old) + r"(\s*)$",
            r"\g<1>" + new + r"\g<2>",
            text,
        )
        if new_text != text:
            if not dry_run:
                md_path.write_text(new_text, encoding="utf-8")
            updated += 1
    return updated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Relabel equations in Redefining_Racism.tex and registry files."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned substitutions without writing any files.",
    )
    args = parser.parse_args()
    dry_run: bool = args.dry_run

    mode = "DRY RUN" if dry_run else "APPLY"
    print(f"\n{'='*72}")
    print(f"  relabel_equations.py — {mode}")
    print(f"{'='*72}\n")

    # ── Phase A: registry-driven mapping ────────────────────────────────────
    print("Phase A: Building registry-driven mapping …")
    registry_map = build_registry_mapping(REGISTRY_DIR)
    print(f"  {len(registry_map)} registry pairs loaded.\n")

    # ── Discover all manuscript labels ─────────────────────────────────────
    manuscript_text = MANUSCRIPT.read_text(encoding="utf-8")
    all_labels = extract_all_labels(manuscript_text)
    print(f"Manuscript labels discovered: {len(all_labels)}")

    # Split into already-conforming vs. non-conforming
    non_conforming = [lbl for lbl in all_labels if not HYBRID_RE.match(lbl)]
    already_hybrid = [lbl for lbl in all_labels if HYBRID_RE.match(lbl)]
    print(f"  Already hybrid : {len(already_hybrid)}")
    print(f"  Non-conforming : {len(non_conforming)}\n")

    # ── Phase B: auto-generate labels for registry-unmapped non-conforming ──
    registry_old_labels = set(registry_map.keys())
    auto_unmapped = [lbl for lbl in non_conforming if lbl not in registry_old_labels]

    if auto_unmapped:
        print("Phase B: Auto-generating labels for unmapped non-conforming equations …")
        chapter_map = build_chapter_map(manuscript_text)
        # Seed chapter_max from ALL labels already in hybrid form:
        # - labels that are already hybrid in the manuscript (previous migration)
        # - new labels that Phase A will produce (from registry mapping)
        all_hybrid: set[str] = set(already_hybrid)
        all_hybrid.update(new for new, _ in registry_map.values())
        auto_map = build_auto_mapping(auto_unmapped, chapter_map, all_hybrid)
        for old, new in auto_map.items():
            print(f"  AUTO {old!r:45s} → {new!r}")
        print()
    else:
        auto_map = {}
        print("Phase B: No unmapped non-conforming labels — skipping.\n")

    # ── Build full substitution map ─────────────────────────────────────────
    full_map: dict[str, str] = {}
    for old, (new, _) in registry_map.items():
        full_map[old] = new
    full_map.update(auto_map)

    # ── Coverage validation (hard-fail) ────────────────────────────────────
    print("Coverage validation …")
    validate_coverage(all_labels, full_map, dry_run)
    print("  ✓ All non-conforming labels are covered.\n")

    # ── Apply substitutions ─────────────────────────────────────────────────
    pairs = sorted_pairs(full_map)

    print(
        f"{'[DRY RUN] ' if dry_run else ''}"
        f"Substituting in manuscript: {MANUSCRIPT.name}"
    )
    total = replace_in_manuscript(MANUSCRIPT, pairs, dry_run)
    print(f"\n  Total substitution sites: {total}\n")

    # ── Update registry files (Phase A only) ───────────────────────────────
    print(
        f"{'[DRY RUN] ' if dry_run else ''}"
        "Updating label fields in registry .md files …"
    )
    updated = update_registry_files(registry_map, dry_run)
    print(f"  Registry files updated: {updated} / {len(registry_map)}\n")

    if dry_run:
        print("Dry run complete — no files were modified.")
    else:
        print("Migration complete.")
        print(f"  Manuscript : {MANUSCRIPT}")
        print(f"  Registry   : {updated} files updated in {REGISTRY_DIR}")
        if auto_map:
            print(f"  Auto-gen   : {len(auto_map)} new hybrid labels generated")
        print("\nNext: run `make pdf` (or latexmk directly) to verify zero undefined-reference warnings.")

    print(f"\n{'='*72}\n")


if __name__ == "__main__":
    main()
