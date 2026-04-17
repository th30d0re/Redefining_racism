# Session Log - 2026-04-16 (Master Vocabulary Scrub)

## What Was Wrong / What Was Requested

User flagged that Appendix B1 is titled "Master Equation" and asked that the
"master"-family vocabulary be eliminated anywhere it is a metaphorical import from
the oppressive structure the paper is diagnosing, rather than a direct reference
to that structure.

Rule of thumb: if the paper is diagnosing slavery/oppression, we shouldn't let the
vocabulary of that system leak into neutral technical or figurative phrasing.

## How I Fixed It / What I Did

1. Grepped `Paper/Redefining_Racism.tex` for all `master`-family tokens
   (case-insensitive): found 9 occurrences.

2. Triaged each occurrence into three buckets:

   **Scrub (metaphorical leaks):**
   - L8155 `\section{Master Equation: The Predatory Min-Max Function}` (Appendix B1 header)
     -> `\section{Canonical Equation: The Predatory Min-Max Function}`
   - L8157 two instances of "master equation" in the appendix prose -> "canonical equation"
   - L8159 `\begin{definition}[The Predatory Min-Max Function --- Master Entry]`
     -> `--- Canonical Entry`
   - L5736 cross-reference "see also Appendix~\ref{sec:equation_registry} for the master
     equation entry" -> "canonical equation entry"
   - L2148 "performance of mastery" (in the White Masculine Wound subsection of §5.14)
     -> "performance of domination"
   - L4317 "a masterclass in disproportionate state violence" (Hampton assassination
     forensic prose) -> "a textbook case of disproportionate state violence"
   - L7687 "a masterclass in using the system's own rules as a defensive weapon"
     (Firmin/Haiti 1891 prose) -> "a textbook demonstration of using the system's own
     rules as a defensive weapon"

   **Keep (direct references to the oppression apparatus):**
   - L1205 "stationmasters" -- Underground Railroad's deliberate railway-code lexicon
     (conductor/station/stationmaster/passenger). Altering this distorts historical
     accuracy.
   - L1918 `"Head and master"` laws -- the actual statutory name of the Louisiana/
     Southern legal doctrine being diagnosed; already in quotes.

   **Borderline, default keep:**
   - L6368 "brewmasters" -- German/guild brewery occupational term, parallel to
     *postmaster*, *concertmaster*. Standard professional vocabulary, not
     oppression-coded.

3. Naming choice for the Appendix B1 rename: "Canonical Equation" was chosen because
   - it echoes the already-present phrase "reproduced here as the canonical reference"
     in the appendix prose itself, and
   - it matches the naming of the immediately following §B.2, which is already titled
     "Canonical Symbol Registry," so the appendix's internal vocabulary becomes
     self-consistent.

4. Executed seven StrReplace edits.

5. Re-grepped -- zero residual matches for `aster equation|aster Equation|aster entry|
   aster Entry|erformance of mastery|asterclass`.

6. Ran `latexmk -pdf -interaction=nonstopmode -halt-on-error` -- clean build, 541 pages,
   PDF regenerated. Only log warning is the pre-existing `sheidlower_fword` missing
   citation on line 1998, unrelated to this scrub.

## Challenges Encountered

1. Distinguishing direct-reference uses from metaphorical leaks. The "Head and master"
   laws are the actual statutory doctrine being diagnosed and therefore must be named
   precisely, while "master equation" is an imported physics metaphor that has no
   analytical content in this paper -- it only carries the connotations of hierarchical
   dominance the paper is arguing against.

2. Choosing a replacement for "Master Equation" that doesn't tautologize with the
   existing phrasing. "Governing Equation" was rejected because the text already
   calls the Predatory Min-Max Function "the governing optimization algorithm" and
   the resulting phrase would be circular. "Canonical Equation" was selected because
   it matches the pre-existing "canonical reference" phrasing and the adjacent
   "Canonical Symbol Registry" section title.

3. "Brewmasters" required a judgment call. Left in because it is a guild occupational
   term rather than a vocabulary import from the slavery/oppression lexicon. Flagged
   for user review in case a strict scrub is preferred.

## Next Ideas (6 Ideas)

1. Do a parallel sweep for other oppression-vocabulary metaphors that may have leaked
   into technical phrasing: `slave` (as in "slave clock," "slave process"), `dummy`,
   `blacklist`/`whitelist`, `hang` (as in "the process hangs"), `kill` (in the process-
   management sense vs. the forensic sense the paper uses deliberately).
2. Add a brief footnote to Appendix B explaining the deliberate avoidance of "master
   equation" terminology, so readers who expect that physics vocabulary see the
   reasoning rather than wondering at the absence.
3. Fix the pre-existing `sheidlower_fword` missing bibliography entry on line 1998.
4. Audit figure captions and table headers for the same vocabulary class -- these are
   the spots where imported technical terminology tends to slip through an author's
   pass.
5. Consider whether the Underground Railroad "stationmaster" passages warrant an
   explicit author's note clarifying why that specific term is retained, since a
   reader doing a casual CTRL-F might flag it as inconsistent with the scrub elsewhere.
6. Build a small style-guide document (or extend `Docs/` if one exists) codifying the
   paper's vocabulary-hygiene rule: the diagnostic vocabulary of the diagnosed system
   is permissible only when directly naming or quoting that system, never as
   metaphorical import elsewhere. This would make future edits self-policing.
