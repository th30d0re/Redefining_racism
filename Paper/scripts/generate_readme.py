#!/usr/bin/env python3
"""
generate_readme.py — Regenerate Paper/empirical_validations/README.md
from the YAML frontmatter of all eq_*.md files.

Usage:
    python3 Paper/scripts/generate_readme.py
    (or via `make readme`)
"""

import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml not installed — run: pip install pyyaml")

SCRIPT_DIR  = Path(__file__).resolve().parent
PAPER_DIR   = SCRIPT_DIR.parent
VAL_DIR     = PAPER_DIR / "empirical_validations"
README_PATH = VAL_DIR / "README.md"

# ── YAML frontmatter loader ────────────────────────────────────────────────────

_FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

_SEQ_RE = re.compile(r'^eq_\d+_(\d+)_')

def load_md(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = _FM_RE.match(text)
    if not m:
        raise ValueError(f"No YAML frontmatter in {path}")
    data = yaml.safe_load(m.group(1))
    data["_file"] = path.name
    # Populate seq from filename if missing or null in YAML
    if not data.get("seq"):
        ms = _SEQ_RE.match(path.name)
        if ms:
            data["seq"] = int(ms.group(1))
    return data


def short_type(t: str) -> str:
    return {"quantitative": "qua", "structural": "str", "ordinal": "ord"}.get(t, t[:3])


def main() -> None:
    print(f"Reading {VAL_DIR} …")
    records = sorted(
        [load_md(p) for p in VAL_DIR.glob("eq_*.md")],
        key=lambda r: (r.get("chapter", 0), r.get("_file", "")),
    )
    n = len(records)
    phase3  = [r for r in records if r.get("phase3_headline")]
    others  = [r for r in records if not r.get("phase3_headline")]

    by_type = {}
    by_tier = {}
    for r in records:
        by_type[r.get("type", "?")] = by_type.get(r.get("type", "?"), 0) + 1
        by_tier[r.get("tier", 0)]   = by_tier.get(r.get("tier", 0), 0) + 1

    today = date.today().isoformat()

    # ── Summary table ──────────────────────────────────────────────────────────
    summary = f"""\
# Equation Registry — Prioritized Work Queue

> **T4 Deliverable** — Built by `Paper/scripts/scan_equations.py`  
> Last generated: {today}  
> Manuscript: `Paper/Redefining_Racism.tex` ({n} labeled equations across 19 numbered chapters)

---

## Summary Table

| Metric | Count |
|--------|-------|
| **Total labeled equations** | {n} |
| Phase 3 headline equations | {len(phase3)} |
| Remaining equations | {len(others)} |
| Type: quantitative | {by_type.get('quantitative', 0)} |
| Type: structural | {by_type.get('structural', 0)} |
| Type: ordinal | {by_type.get('ordinal', 0)} |
| Tier 1 (peer-reviewed quantitative) | {by_tier.get(1, 0)} |
| Tier 2 (public dataset + author computation) | {by_tier.get(2, 0)} |
| Tier 3 (ordinal estimate / structural) | {by_tier.get(3, 0)} |

---

## Priority Queue — Phase 3 ({len(phase3)} Headline Equations)

These {len(phase3)} equations are the single canonical headline equation per Phase 3 numbered group.
Each represents a full quantitative or ordinal case study to be written as a
`\\subsection*{{Case Study: …}}` block in the manuscript.
All 12 groups are now complete. Group 6 (Interference Engine, `eq:40`) was completed in T5/T6 via `Paper/scripts/eq40_45_interference_engine.ipynb`.

| # | Label | File | Type | Tier | Difficulty | Existing CS |
|---|-------|------|------|------|------------|-------------|
"""

    for idx, r in enumerate(phase3, 1):
        cs = "✓" if r.get("status") == "complete" else ""
        summary += (
            f"| {idx} | `{r['label']}` | `{r['_file']}` "
            f"| {short_type(r.get('type','?'))} "
            f"| {r.get('tier','?')} "
            f"| {r.get('difficulty','?')} "
            f"| {cs} |\n"
        )

    summary += "\n---\n\n## Priority Queue — Remaining Equations (Chapter Order)\n\n"
    summary += "| Ch | Seq | Label | File | Type | Tier | Difficulty | Existing CS |\n"
    summary += "|----|-----|-------|------|------|------|------------|-------------|\n"

    for r in others:
        cs = "✓" if r.get("status") == "complete" else ""
        summary += (
            f"| {r.get('chapter','?')} "
            f"| {str(r.get('seq','?')).zfill(2)} "
            f"| `{r['label']}` "
            f"| `{r['_file']}` "
            f"| {short_type(r.get('type','?'))} "
            f"| {r.get('tier','?')} "
            f"| {r.get('difficulty','?')} "
            f"| {cs} |\n"
        )

    summary += """
---

## Status Legend

| Status | Meaning |
|--------|---------|
| `pending` | Not yet started |
| `in_progress` | Case study being written |
| `complete` | Case study written and verified |

---

## Tier Definitions

| Tier | Label | Criteria |
|------|-------|----------|
| 1 | Peer-reviewed quantitative | Falsifiable with published dataset + regression/estimate |
| 2 | Public dataset + author computation | Open data available; case study writable without new collection |
| 3 | Ordinal estimate / structural | Qualitative ordering claim; narrative calibration acceptable |

---

## Type Definitions

| Type | Symbol | Meaning |
|------|--------|---------|
| quantitative | qua | Directly measurable with numeric data |
| structural | str | Relational / causal / set-theoretic claim |
| ordinal | ord | Relative ordering claim (no cardinal scale required) |

---

## Calibration Anchor Methodology

Each case study must provide:
1. **Event(s)**: Historical period(s) where the equation's prediction is most visible
2. **Dataset**: Primary or secondary source providing the numeric signal
3. **Estimate**: Point or range estimate for each variable in the equation
4. **Falsification test**: One condition under which the equation would be disconfirmed

---

## File Naming Convention

```
eq_<chapter>_<seq:02d>_<short_name>.md
```

- `chapter` — zero-indexed chapter number (0 = front matter / methodology appendix)
- `seq` — 1-indexed per-chapter sequence number
- `short_name` — snake_case slug derived from the label or classification

`new_label` in each file gives the T7-target label format: `eq:<chapter>.<seq>-<slug>`
"""

    README_PATH.write_text(summary, encoding="utf-8")
    print(f"  README → {README_PATH}")
    print(f"  Phase 3 headline: {len(phase3)}  |  Remaining: {len(others)}  |  Total: {n}")


if __name__ == "__main__":
    main()
