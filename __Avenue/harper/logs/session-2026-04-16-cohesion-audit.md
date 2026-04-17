# Session Log — 2026-04-16 — Book Cohesion Audit

## What Was Wrong / What Was Requested

User asked for a cohesion review of `Paper/Redefining_Racism.tex` (9,356 lines, 16 chapters) after a round of substantial edits, and asked whether chapters should be split, merged, or reordered.

## How I Fixed It / What I Did

No edits performed yet. Produced a structural audit using chapter/section/subsection grep passes:

- Counted lines between `\chapter` boundaries to measure chapter balance.
- Enumerated 99 `\section{...}` and ~100 `\subsection{...}` blocks to identify over‑stuffed chapters.
- Scanned all hard‑coded `Chapter~N` / `Chapter N` references for cross‑reference rot introduced by prior re‑orderings.
- Compared `\chapter{Structural Synthesis}` (Ch. 11, 74 lines) against Chapters 6 and 8 to confirm topical overlap.
- Checked preface/conclusion against actual chapter content to find stale "Chapter~X" attributions.

Key diagnostic findings delivered to the user:

1. **Chapter imbalance** — Ch. 7 is 1,310 lines, Ch. 8 is 2,767 lines (~30% of the book), Ch. 11 is 74 lines and redundant.
2. **Chapter 8 split proposal**: 8A (COINTELPRO / War on Drugs / Manufactured Crisis, 4241–5490), 8B (Broken Windows / 5‑Tier Reveal / Cannibalization, 5491–6113), 8C (Disarmament Timeline / Second Amendment, 6117–7007). The existing "Rhetorical Bridge" section at 6990 confirms the pivot.
3. **Chapter 7 Tweedism section** (3161–4165) is ~1,000 lines flat-packed under one `\section`; promote to chapter or restructure with more subsections.
4. **Chapter 11 is redundant** with Ch. 6 and Ch. 8; recommended absorbing its evidence table into an appendix.
5. **Cross-reference rot**: ~15–20 `Chapter~N` references point at wrong numbers after prior re‑orderings (e.g., 268, 429, 775, 1086, 1704, 2893, 3144, 5418, 5782, 6115, 6202, 6216, 6259, 6276, 6316, 6917, 6935, 6939, 6947, 8047). Recommended `\label{ch:...}` + `\ref`/`\autoref` migration.
6. **Narrative flow**: Ch. 4–5 (gendered axis) intercalates between Ch. 3 (1676–1787) and Ch. 6 (1704–1865), breaking the timeline. Recommended adding Parts I–IV to justify the thematic break.
7. Minor: Preface's "each variable at the moment it is invented" promise is honored for $O, I_{\text{buffer}}, P_{\text{uppet}}, F_{\text{enforce}}$ but not $\psi$; Conclusion references "three theorems" that are not formally wrapped in `theorem` environments despite `\newtheorem` being declared.

Delivered a ranked action list:
1. Fix cross-reference rot (low-risk, high-impact).
2. Split Chapter 8 (biggest readability win).
3. Absorb / remove Chapter 11.
4. Promote or restructure Ch. 7 Tweedism.
5. Add Part I–IV structure.
6. Preface/Conclusion nits.

## Challenges Encountered

1. The Grep tool has an internal pagination ceiling (≈100 matches) — had to switch to `grep -nE` in the shell to get the full list of ~134 structural headings.
2. Visually estimating section‑span from line numbers is an imperfect proxy for rendered page count; some sections contain dense tables/figures that will be denser in PDF, while others are mostly prose with heavy inline code.
3. Cross-reference rot detection is hand-audited — there's no static check in the repo that would have caught `Chapter~7` vs `Chapter~8` drift automatically.
4. Chapter 11 looked redundant from titles alone, but had to verify by cross‑reading it against Chapter 6 (13A loophole) and Chapter 8 (War on Drugs, environmental) before recommending removal.
5. The gender/kinship intercalation (Ch. 4–5) is a real trade‑off: Option A (Parts) is low‑risk, Option B (move before Ch. 2) breaks the preface's ordering promise.
6. Some `\section` titles contain `\texorpdfstring{}` and math ($O_{\text{racialized}}$) that complicate automatic TOC extraction.

## Next Ideas (6 Ideas)

1. **Automated cross-ref lint**: add a `tools/check_chapter_refs.sh` that greps for `Chapter~\d+` and reports any chapter number that doesn't match an actual `\chapter{...}` ordinal. Wire into the existing Makefile.
2. **Label-migration pass**: mechanically insert `\label{ch:<slug>}` under every `\chapter{}` and replace `Chapter~N` with `\autoref{ch:<slug>}` — one‑time pain, permanent immunity.
3. **Part structure + running head redesign**: once Parts I–IV exist, adjust `fancyhdr` so `\leftmark` shows the Part/Chapter and `\rightmark` shows the Section, improving wayfinding in a long print book.
4. **Formalize the three theorems**: wrap Concession, Haitian, and Imperial Core Theorems in `theorem` environments with `\label{thm:concession}` etc., and have the Conclusion `\ref` them. This turns the climactic claims into citable objects.
5. **Split-preview branch**: do the Chapter 8 split on a throwaway git branch first, compile the PDF, and diff page counts / TOC only before merging — lets the user see layout impact before committing.
6. **Reading‑time heatmap**: write a small script that estimates minutes per chapter (words / 250 wpm) and emits a CSV or Markdown chart. Would make imbalances (like Ch. 8 = ~30% of book) visible to future reviewers at a glance and would replace the crude line-count proxy used in this audit.
