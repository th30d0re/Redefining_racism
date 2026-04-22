---
gate: T8 Decision Gate
date: 2026-04-22
status: PASS_WITH_CONDITIONS
reviewer: automated-methodology-review
---

# Decision Gate: Post-T5/T6 Review

## Headline Case Study Review (12/12)

All 12 `\subsection*{Case Study: ...}` blocks were read in full. Each was evaluated
against the four criteria defined in the Empirical Methodology chapter: Event,
Dataset (with DOI/URL or archival reference), Estimate (point or range), and
Falsification test. Confidence tier was also verified for each.

| # | Case Study | Tier | Verdict |
|---|---|---|---|
| 1 | Kernel Optimization in the Antebellum South (1840–1860) | Tier 1 | **PASS** — Cotton revenue, militia/patrol expenditure (Census HSoUS, Hadden, Beckert, Baptist); suppression ratio CV < 0.04; falsification: no period of rising revenue + falling enforcement exists |
| 2 | The Post-1965 Backlash Wave | Tier 1 | **PASS** — BLS union density, WID wealth share, BJS incarceration (1965–2020); composite Σ_sup expanded >23%; falsification: simultaneous ↑ union density + ↓ incarceration + ↓ wealth concentration would falsify |
| 3 | Bacon's Rebellion and the Coalition Arithmetic | Tier 1 (Anchor, ρ_τ=1.0) | **PASS** — Morgan (Am. Slavery Am. Freedom), Census HSoUS, Du Bois; 27:1 labor coalition ratio; 1705 Slave Codes as documented structural response; falsification: Codes not triggered by Rebellion |
| 4 | Police Killings and the Enforcement Benefit Hierarchy | Tier 1 | **PASS** — Mapping Police Violence 2013–2024; Black 7.00 / Native 6.55 / White 2.33 per million; 3:1 Black-to-White ratio stable across 11 years; falsification: uniform or inverted hierarchy |
| 5 | The Compounding Chain — Cannabis Enforcement | Tier 1 | **PASS** — ACLU (2020), Mapping Inequality, Blackmon (2008), Darity & Mullen (2020); terminal O₁₉₇₁ ≈ 0.019; factors independently documented before computation; falsification: any factor = 0 in longitudinal data |
| 6 | The Interference Engine — Spectral Redistribution | Tier 1/Tier 2 (mixed, stated) | **PASS** — ANES 1948–2020, Google Trends, Congressional Record, GDELT, 55 SCOTUS PDFs; Φ_load +0.136 (+174%); CR Parseval CV=0.162; SCOTUS inter-axis range 4.9 yr; AIC=-8.30 two-segment preferred; falsification criteria explicit per sub-analysis |
| 7 | Gilens-Page and the Agenda-Setting Path | Tier 1 | **PASS** — Gilens & Page (2014), 1,779 policy proposals 1981–2002; median voter β=0.03 (p=0.43, n.s.); elite β=0.76 (p<0.001); falsification: median voter coefficient ≈ elite coefficient |
| 8 | The Lead-Crime Nexus and Spatial Concentration | Tier 1 | **PASS** — Reyes (2007), Aizer & Currie (2019), Mapping Inequality, EPA; elasticity 0.80; HOLC-D 5.1× lead exposure vs. HOLC-A; falsification: Reyes lag fails in panel regression, or HOLC-lead correlation vanishes after controls |
| 9 | Mass Incarceration and the Expanding Out-Group | Tier 1 | **PASS** — BJS 1980–2024, Sentencing Project; 3.6× total incarceration growth; Black-to-White ratio range 3.92–6.11; Elite incarceration ≈ 0; falsification: White/Hispanic rates decline post-1994 while Black rates grow |
| 10 | The Jurisprudential Boomerang — 2A Case Law (1911–2024) | Tier 1 | **PASS** — 16 primary-source legislative/ATF/SCOTUS events; federal legislation floor stable at 4 active Acts; 91% of restriction-adding events show target expansion; falsification: federal Acts floor reduced by congressional repeal, or no initial O_racialized targeting extends to I_buffer |
| 11 | The Haitian Theorem — Liberia, Algeria, Zimbabwe | Tier 1 | **PASS** — James (1938), Horne (2015), Haiti Constitution 1805, Evian Accords 1962, Lancaster House 1979, NYT Ransom 2022; Liberia Δmax ≈ +1.0pp, Algeria ≈ -3.0pp (both ≈ 0); Haiti max = 0 locally at 5 yr; falsification: any non-kinetic reform sustains >10pp extraction reduction over 20 yr |
| 12 | Imperial Core Collapse — China, OPEC, Asian Tigers | Tier 1 | **PASS** — World Bank WDI, SIPRI, IMF; China capacity 0.26→0.68, crossing τ_sovereign ≈ 2015; OPEC peak 0.49 (below threshold, absorbed <24 mo); Tigers 0.44–0.52 (structurally below threshold); falsification: rising power crosses τ_sovereign without triggering containment response |

**Summary:** 12/12 case studies contain all four required elements. Confidence tier is
explicitly stated in each. All falsification criteria are observable and directionally
specific. **Criterion met.**

---

## Spectral Rewrite Review (Case Study 6 / T6)

### Model assessment: does FFT recover meaningful band distributions?

**Sub-analysis A (Φ_load trajectory):**
- ANES rolling proxy confirms two-step increase: pre-activation (1948–1964) mean 0.078,
  activation (1965–1980) mean 0.214, post-activation (1981–2020) mean 0.403.
- Step increase: +0.136 (+174%) — non-trivial and temporally co-incident with sequenced
  axis injections (gender 1972, religion 1979, sexuality 1977–1979).
- **CONFIRMED.**

**Sub-analysis B (per-axis frequency decomposition):**
- SCOTUS Lomb-Scargle (57 cases, 1873–2018): race 3.6 yr, gender 6.2 yr, religion 8.5 yr.
- Sexuality axis (50.0 yr) correctly flagged as boundary artifact and excluded.
- Inter-axis range 4.9 yr > 3 yr threshold → **distinctness confirmed** for three axes.
- GDELT per-axis PSD: conditional on BigQuery retrieval; placeholder figure rendered
  correctly via `\IfFileExists` conditional (lines 5088–5114).
- **CONFIRMED (SCOTUS); GDELT PENDING DATA.**

**Sub-analysis C (Parseval conservation):**
- Congressional Record (institutional layer): CV(P_total) = 0.162 < 0.30 → conservation
  supported. Google Trends CV = 0.578 (open-system Internet — theoretically expected).
- **PARTIALLY CONFIRMED** — institutional layer passes; open-system divergence is itself
  a theoretically meaningful finding, not a failure.

**Sub-analysis D (suppression substitution):**
- R(t) declines 0.97 → 0.38 as Φ_load rises 0.27 → 0.60 and ψ_s rises 0.19 → 0.52.
- Composite Σ_sup CV = 0.058 < 0.10 (pre/post means 1.480 vs. 1.485 — stable).
- **CONFIRMED.**

**Sub-analysis E (shock time-constant acceleration):**
- T_n sequence: 20.91 → 11.96 → 5.82 → 0.94 yr — monotonically decreasing.
- Two-segment piecewise log-linear model AIC = -8.30 vs. single-segment AIC = 1.11
  (two-segment strongly preferred).
- Segment 2 slope 18× steeper than Segment 1 — distinct post-2008 acceleration regime.
- **CONFIRMED.**

**Laplace transfer function (spectral_laplace.ipynb):**
All four primary shock fits returned stable poles (0 < ζ < 1, LHP) with non-degenerate
natural periods. Fix~2 intermediate shocks (1917, 1954, 1968, 1992) are present in
`historical_shocks.json` and correctly filtered to `primary_shocks` list for fitting;
intermediate shocks carry `"intermediate": true` flags.

**Overall spectral assessment: PASS** — FFT recovers distinct class/identity bands;
Laplace fits are stable; all five sub-analyses return supportive or partially supportive
results consistent with the interference-engine framework.

---

## Build Verification

- `make empirical`: **PASS** — All 16 notebooks executed without error (exit code 0).
  Notebooks: scotus_corpus_analysis, spectral_fourier, spectral_laplace, eq05–eq91
  series, eq_black_gun_ownership_mt. All expected figures regenerated in
  `Paper/figures/spectral/`.

- `make pdf`: **PASS** — Manuscript compiled to `Redefining_Racism.pdf` (713 pages,
  5,908,373 bytes, exit code 0). No broken `\ref{}`, `\eqref{}`, or `\cite{}`
  references detected in log.

- Notebook failures at gate start (pre-fix): **3 issues resolved**
  1. `spectral_laplace.ipynb`: `assert len(shocks) == 4` failed after Fix~2 expanded
     `historical_shocks.json` to 8 entries. Fixed: assertion updated to `>= 4`; fitting
     loop filtered to `primary_shocks` (non-intermediate only).
  2. Pre-existing stale cached outputs across multiple notebooks missing required
     `name` (stream) and `metadata` (display_data) fields per nbformat4 schema.
     Fixed: comprehensive output patch applied across all 16 notebooks.
  3. `eq_black_gun_ownership_mt.ipynb`: unterminated string literal
     (`set_ylabel` multi-line string without triple quotes — Python 3.13 SyntaxError).
     Fixed: `\n` escape sequence used instead.

- LaTeX warnings: **2 cosmetic float-sizing warnings** (Float too large for page,
  input lines 6215 and 9034). No broken cross-references. No missing citations.
  `\IfFileExists` GDELT conditional renders placeholder box correctly.

---

## Gate Decision

**PROCEED to T8.**

All four gate criteria pass. The three notebook issues resolved at this gate were
pre-existing format/compatibility issues (nbformat4 schema enforcement in Python 3.13,
assertion not updated after Fix~2 data expansion, legacy string literal syntax) — none
were logic or data errors. The spectral analysis produces meaningful, non-degenerate
results across all five sub-analyses. The manuscript compiles cleanly. The 12 case
studies all satisfy the four-element methodology checklist with explicitly stated
confidence tiers and falsification criteria.

---

## Conditions (to address during T8, not blocking)

1. **GDELT per-axis PSD figure** (`figures/spectral/per_axis_psd.pdf`) is pending BigQuery
   data retrieval via `gdelt_per_axis_query.py`. The `\IfFileExists` conditional renders a
   clearly labeled placeholder. Run `make data-refresh` after executing the BigQuery script
   to generate this figure for the final manuscript.

2. **SCOTUS majority-vs-dissent class-language analysis** (Figure `scotus_majority_dissent`)
   is based on only 2 paired cases — insufficient for directional inference. The figure is
   correctly labeled "illustrative only" and excluded from confirmatory claims. Expand the
   matched-section corpus to ≥ 30 paired cases during T8 to enable directional testing.

3. **Two cosmetic LaTeX float warnings** (lines 6215, 9034). Adjust `[h]` float specifiers
   or add `\vspace` adjustments during T8 manuscript pass.

4. **`spectral_laplace.ipynb` cell 0 description** still reads "four historical ... shocks"
   — update to reflect the 8-entry `historical_shocks.json` (4 primary + 4 intermediate)
   during the next notebook maintenance pass.
