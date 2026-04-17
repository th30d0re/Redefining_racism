# Session Log - 2026-04-17 Equation Numbering

## What Was Requested

Number and label all equations in `Paper/Redefining_Racism.tex`. The book uses ~95 display equations in `\[...\]` format (unnumbered) plus 6 existing `\begin{equation}` environments (most already labeled). The request is to convert all unlabeled display math to proper numbered `\begin{equation}\label{...}\end{equation}` environments so equations can be referenced and appear with numbers in the compiled PDF.

## How I Fixed It / What I Did

1. Audited all equation locations using grep: found ~95 `\[...\]` blocks at lines 144, 159, 190, 195, 390, 439, 453, 456, 481, 485, 600, 604, 608, 692, 835, 900, 903, 941, 949, 966, 1010, 1061, 1184, 1233, 1253, 1274, 1295, 1960, 2575, 2684, 2750, 2756, 2774, 2780, 2795, 3192, 3397, 3401, 3415, 3693, 3779, 4024, 4031, 4035, 4040, 4044, 4147, 4344, 4848, 4931, 5167, 5171, 5244, 5879, 5883, 5939, 6051, 6057, 6061, 6066, 6071, 6076, 6144, 6147, 6270, 6381, 6493, 7310, 7314, 7318, 7394, 7429, 7454, 7498, 7651, 7654, 7839, 7844, 7849, 7947, 8047, 8129, 8174, 8186, 8192, 8198, 8211, 8232, 8240, 8256, 8294, 8331, 8444, 8493, 8625, 8629, 8633, 8637

2. Existing labeled `\begin{equation}` blocks (already correct):
   - Line 3409: `\label{eq:fractional-dynamics}`
   - Line 3423: `\label{eq:stationary-leaders}`
   - Line 3505: `\label{eq:state-dep-connectivity}`
   - Line 3595: `\label{eq:navigation-components}`
   - Line 3601: `\label{eq:navigation-function}`
   - Line 3605: `\label{eq:control-law}`

3. Unlabeled `\begin{equation}` block:
   - Line 8156: Killick division-by-zero equation — added `\label{eq:killick-extraction}`

4. Wrote and ran a Python script (`/tmp/number_equations.py`) that:
   - Reads the .tex source
   - Replaces every `\[...\]` block with `\begin{equation}\label{eq:N}...\end{equation}` where N is a sequential integer
   - Handles multi-line equations correctly using regex with DOTALL flag
   - Writes the result back to the .tex file

## Challenges Encountered

1. Multi-line equations: Some `\[...\]` blocks span multiple lines. The Python regex used `re.DOTALL` to handle this.
2. Label namespace: Using simple sequential integers (`eq:1`, `eq:2`, ...) avoids collisions with the existing descriptive labels on `\begin{equation}` environments.
3. Equation count: With ~95 equations, a manual approach would be impractical; the scripted approach ensures all are captured.

## Next Ideas (6 Ideas)

1. **Add cross-references**: Go through prose and add `Equation~\ref{eq:N}` references wherever equations are discussed but not yet referenced.
2. **Descriptive labels**: Rename `eq:1`...`eq:N` to semantic labels like `eq:enclosure-score`, `eq:causal-reversal`, `eq:kernel-objective` for better maintainability.
3. **Align environments**: Some equations that are displayed in sequential `\[...\]` pairs (e.g., the Bayesian prior update) could be combined into a single `align` environment for visual alignment.
4. **`amsmath` audit**: Ensure `\usepackage{amsmath}` is in the preamble (required for `equation` environment labels to render with `\ref`).
5. **`cleveref` package**: Add `\usepackage{cleveref}` so `\cref{eq:N}` produces "Equation (N)" automatically with proper formatting.
6. **Chapter-scoped numbering**: Consider using `\numberwithin{equation}{chapter}` so equations are numbered (1.1), (2.3) etc. by chapter — more conventional for book-length works.
