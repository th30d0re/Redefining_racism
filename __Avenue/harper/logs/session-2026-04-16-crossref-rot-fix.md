# Session Log - 2026-04-16 - Cross-Reference Rot Fix

## What Was Wrong / What Was Requested

Following the prior cohesion audit, the user said "proceed" — accepting the
ranked recommendations starting with Fix #1: **stale hard-coded `Chapter~N`
cross-references**.

Before this session, `Paper/Redefining_Racism.tex` contained **~90 in-text
references** of the form `Chapter~N` or `Chapter N` that were authored against
an older chapter ordering. Many pointed to the wrong chapter because the
manuscript had been reorganized several times (Kinship moved in, Gendered Axis
inserted between Bacon and Enforcement, etc.). Specific examples:

- "the Haitian Theorem (formally defined in Chapter~8)" → theorem is actually
  in current Ch. 9
- "slave patrols documented in Chapter~5" → slave patrols are actually in
  current Ch. 6
- "Variable Swap documented in Chapter~7" appearing *inside* Ch. 8, pointing
  at an earlier sub-section of the same chapter

Only three chapters (`ch:portugal`, `ch:kinship`, `ch:gendered`) had existing
`\label{}` anchors; the other nine chapters had no labels at all, so fixing
the refs also required establishing the label system.

## How I Fixed It / What I Did

### 1. Verified current chapter numbering
Ran a structural audit of `\chapter{}` commands. Current ordering (after file
grew by ~53 lines since the audit):

| # | Title | Label |
|---|---|---|
| 1 | Redefining Racism | `ch:redefining` |
| 2 | Version 1.0: Portugal | `ch:portugal` (existed) |
| 3 | Bacon's Rebellion / Constitutional Patch | `ch:bacon` |
| 4 | Architecture of Kinship | `ch:kinship` (existed) |
| 5 | Gendered Axis | `ch:gendered` (existed) |
| 6 | Enforcement Engine | `ch:enforcement` |
| 7 | Containment / Puppet Class | `ch:containment` |
| 8 | Complete Algorithm (1968–Present) | `ch:complete` |
| 9 | Contradiction / Reform Paradox | `ch:contradiction` |
| 10 | Global Containment Field | `ch:global` |
| 11 | Structural Synthesis | `ch:synthesis` |
| 12 | Conclusion | `ch:conclusion` |

### 2. Added missing `\label{ch:...}` anchors
Inserted nine new chapter labels (left the three pre-existing ones alone to
avoid breaking anything that might already reference them).

### 3. Fixed stale in-text references
Replaced hard-coded `Chapter~N` with `Chapter~\ref{ch:...}` in all ~55
in-text locations where the target chapter had shifted, plus ~15 locations
where the ref was correct but needed to be converted to the label-based form
for future-proofing.

Key corrections by intended target:

- Ch. 5 "In Chapter~5" (compounding) → `ch:enforcement` (Ch. 6)
- Ch. 6 "Variable Swap documented in Chapter~6" → `ch:complete` (Ch. 8)
- Ch. 9 "arms asymmetry documented in Chapter~9" → `ch:complete` (Ch. 8)
- Ch. 4 "gendered axis analysis in Chapter~4" → `ch:gendered` (Ch. 5)
- Ch. 8 "Haitian Theorem (formally defined in Chapter~8)" → `ch:contradiction` (Ch. 9)
- Ch. 7 "reform paradox that Chapter~7 will formalize" → `ch:contradiction` (Ch. 9)
- Ch. 5 "Chapter~5 documents" (sex ratios) → `ch:kinship` (Ch. 4)
- Ch. 8 "documented in Chapter~8 (spatial proxy etc.)" → `ch:complete` / same-chapter self-reference rephrased as "earlier in this chapter"
- Ch. 9 refs to Framer's 21 confessions → `ch:contradiction` (Ch. 9) — those are actually located in Ch. 9's *Two-Party Theory* subsection (line 7547), not in Ch. 8
- Ch. 5/6/7 labels in the appendix Era-Level Calibration table and in every
  tcolorbox runtime-log title
- One citation at the end of the bibliography references "Chapter~5" of an
  *external* book (Brill Handbook on African Customary Law) — left as-is

### 4. Compiled and verified
`latexmk -pdf` completed cleanly:
- 551 pages, output written to `Redefining_Racism.pdf`
- **Zero** undefined-reference warnings
- **Zero** duplicate-label warnings
- One pre-existing unresolved citation (`sheidlower_fword`) — not caused by
  this session
- Verified `.aux` file: all 12 chapter labels resolved to their intended
  numbers.

## Challenges Encountered

1. **Mis-identified forward reference.** Initially rewrote the Ch. 8 reference
   "Chapter~9's analysis of the Framers' twenty-one confessions" as
   "this chapter's earlier analysis" assuming the confessions were in Ch. 8.
   A grep revealed the *Two-Party Theory* subsection with the 21 statements
   actually lives inside Ch. 9 (line 7547+). Reverted to `\ref{ch:contradiction}`.
2. **Same-chapter self-references that still read as inter-chapter refs.**
   Several Ch. 8 paragraphs said "documented in Chapter~7" when they actually
   referred to an *earlier section of Ch. 8 itself* (Variable Swap, spatial
   proxy, Prohibition isomorphism). Resolved by rewording to "earlier in this
   chapter" rather than faking a cross-chapter reference.
3. **`\ref{}` inside `tcolorbox` `title=` argument.** Was a latent risk
   because tcolorbox titles are moving arguments and `\ref` must expand in
   a way hyperref supports. Plain `\ref{ch:...}` compiled without issue
   (no `\protect` needed under the current package stack).
4. **File growing mid-session.** Line numbers shifted while inserting
   `\label{}` calls. Re-ran `grep -nE '^\\chapter'` after each batch of
   insertions to keep coordinates current.
5. **External-book reference disambiguation.** The bibliography entry for
   the Brill Handbook contains "Chapter~5" — had to preserve this because
   it references a different book, not our manuscript.
6. **Distinguishing "Chapter~N as label" from "Chapter N as narrative text"**.
   A few mentions of "21-Chapter Compendium" or "Chapter 13 of [external]"
   needed to be sifted out. The final grep returned exactly one match
   (the external bibliographic reference) — clean.

## Next Ideas (6 Ideas)

1. **Section-level labels for internal forward/backward references.**
   Do the same label treatment for key named sections (e.g., the Haitian
   Theorem, the Variable Swap, the Two-Party Theory) so "earlier in this
   chapter" can become a specific `\Cref{sec:haitian_theorem}` reference
   that survives any future subsection reorganization.
2. **Proceed to Fix #2 — split Ch. 8 "The Complete Algorithm".**
   At 2767+ lines, it is ~4× the length of any other chapter and buries
   the 5-tier reveal. Proposed break into: 8a Recompile (COINTELPRO/War on
   Drugs) · 8b Full Algorithm (Broken Windows/Cannibalization/5-Tier) ·
   8c Kinetic Guarantee (Guns/2A/Disarmament Timeline).
3. **Proceed to Fix #3 — absorb or demote Ch. 11 Structural Synthesis.**
   74 lines, largely duplicative of Ch. 8 + the Conclusion. Either fold
   unique content into the Conclusion or demote to an appendix table.
4. **Add `\Cref{}`/`cleveref` package.** Instead of hand-writing "Chapter~"
   before every `\ref{}`, `\Cref{ch:complete}` would auto-produce
   "Chapter~8" with consistent capitalization and spacing.
5. **Add `\part{}` divisions.** Split manuscript into Part I Diagnostic
   Model (Chs. 1–3), Part II Racial Partition (Chs. 6–8), Part III
   Gendered Partition (Chs. 4–5), Part IV Terminal Findings (Chs. 9–12)
   to formalize the thematic intercalation and give readers a navigational
   hand-rail.
6. **Automated cross-ref linter.** Write a small `tools/check_chapter_refs.sh`
   that greps for any new occurrence of `Chapter[~ ][0-9]` to flag future
   backsliding during editing.
