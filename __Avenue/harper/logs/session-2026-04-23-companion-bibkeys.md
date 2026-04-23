# Session Log - 2026-04-23 (companion BibLaTeX keys)

## What Was Wrong / What Was Requested

`Paper/Empirical_Validation_Companion.tex` used `\textcite{...}` keys that did not exist in `Paper/references.bib`, breaking T10 acceptance (unresolved citations / build).

## How I Fixed It / What I Did

1. Replaced every mismatched `\textcite` key in the companion with the corresponding `references.bib` entry key:
   - `gilens_page2014` → `gilens`
   - `morgan1975` → `morgan_american_slavery`
   - `dubois1935` → `dubois`
   - `rothstein2017` → `rothstein`
   - `darity_mullen2020` → `darity_mullen`
   - `blackmon2008` → `blackmon`
   - `gilens2012` → `gilens_book`
   - `aizer_currie2019` → `aizer_currie`
   - `alexander2010` → `alexander`
   - `reinhart_sbrancia2015` → `reinhart_sbrancia_2015`
   - `bivens_mishel2015` → `bivens_mishel_2015`
   - `james_black_jacobins1938` → `james_black_jacobins`
   - `bordo_eichengreen1993` → `bordo_eichengreen_1993`
   - `piketty_saez_zucman2018` → `piketty_saez_zucman_2018`
2. Left already-correct keys unchanged: `aclu2020`, `reyes2007`, `winkler2011`, `cottrol_diamond1991`, `fanon1961`, `moyo2009`, `horne2015`, `naughton2007`, `yergin2011`, `amsden1989`.
3. Added `@book{zinn1980}` (Howard Zinn, 1980) to `references.bib` — no prior entry matched the companion’s Zinn citation.
4. Updated the closing “Note on citation completeness” paragraph so listed keys match the manuscript/bib.
5. Ran `make companion`; final `Empirical_Validation_Companion.log` contains no “undefined” citations or “Empty bibliography”; `Empirical_Validation_Companion.blg` has no WARN/ERROR.

## Challenges Encountered

1. First LaTeX passes log “Citation … undefined” until Biber runs; verification used the **final** `.log` after latexmk completed.

## Next Ideas (6 Ideas)

1. Add a `make check-companion-cites` script that greps `\textcite{key}` keys and asserts each key exists in `references.bib`.
2. Consider `\usepackage[backend=biber,style=authoryear,]{biblatex}` with `maxcitenames=2` for shorter in-text cites if needed.
3. Fix duplicate `figure` hypertarget warnings from repeated `tcolorbox` figure environments (separate hygiene task).
4. Optionally add `crossref` from `zinn1980` to a reprint edition if ISBN is required later.
5. Run the same cite-key audit on `Redefining_Racism.tex` periodically via CI.
6. Document canonical bib key naming (underscore vs year suffix) in `Paper/research/README.md`.
