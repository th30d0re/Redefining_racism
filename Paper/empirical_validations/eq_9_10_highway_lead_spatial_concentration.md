---
label: eq:9.10-highway-lead-spatial-concentration
new_label: eq:9.10-highway-lead-spatial-concentration
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5549
statement: |
  P_{\text{lead}}^{\text{air}}(x) = \Sigma_{\text{highway}}(x) \cdot L_{\text{TEL}}(t) \cdot \mathbb{1}_{x \in O_{\text{redlined}}}
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "Spatial Confluence — HOLC × Firearm × Lead × Incarceration"
case_study_label: cs:spatial_confluence
phase3_headline: false
target_events: 
  - Interstate highway construction through Black neighborhoods 1956–1972
  - Tract-level spatial co-location of HOLC-D grade, lead exposure, firearm homicide, and incarceration origin across six cities (Memphis TN, Detroit MI, Nashville TN, Baltimore MD, Washington DC, Milwaukee WI)
data_sources: 
  - {name: "Mapping Inequality DSL (Nelson et al.) — HOLC grade GeoJSON", type: "public-dataset", url: "https://dsl.richmond.edu/panorama/redlining/"}
  - {name: "EPA EJScreen 2023 — tract-level lead paint and traffic proximity", type: "public-dataset", url: "https://www.epa.gov/ejscreen"}
  - {name: "Gun Violence Archive — incident-level firearm data 2014–2024", type: "public-dataset", url: "https://www.gunviolencearchive.org"}
  - {name: "Prison Policy Initiative — incarceration origin by tract/county (2020)", type: "public-dataset", url: "https://www.prisonpolicy.org/origin/"}
  - {name: "U.S. Census ACS 5-year (2018–2022) — race and income by tract", type: "public-dataset", url: "https://api.census.gov/data/2022/acs/acs5"}
  - {name: "Boutwell et al. (2016) — BLL × crime spatial autocorrelation meta-analysis", type: "peer-reviewed", url: "https://doi.org/10.1371/journal.pone.0161528"}
  - {name: "Guinn et al. (2024) — Jefferson County topsoil lead × violent crime Bayesian SGLMM", type: "peer-reviewed", url: "https://doi.org/10.1016/j.envres.2024.118271"}
difficulty: H
notebook: "Paper/scripts/eq47_51_spatial_overlay.ipynb"
fetch_script: "Paper/scripts/fetch_spatial_data.py"
conda_env: "Paper/scripts/spatial_env.yml"
data_file: "Paper/data/spatial/pooled_panel.parquet, Paper/data/spatial/merged_tract_panel_<city>.parquet"
figure: "Paper/figures/spatial/cs9_overlay_<city>.png, Paper/figures/spatial/cs9_pooled_stats.png, Paper/figures/spatial/cs9_lisa_<city>.png"
case_study_line: 7178
bib_keys:
  - reyes2007
  - aizer_currie
  - rothstein
  - mapping_inequality
  - mapping_inequality_dsl
  - ejscreen_technical
  - gva_methodology
  - ppi_prison_origins
  - boutwell_lead_crime
  - guinn_lead_bayesian
  - spatial_confluence_forthcoming
falsification: "Falsified if HOLC-D tracts show no excess firearm or lead burden relative to HOLC-A/B after income controls; or if Moran's I for HOLC-D flag is non-significant; or if SLM coefficient on HOLC-D flag for incarceration origin is null or negative after controlling for contemporary racial composition."
data_gaps:
  - "PPI: when public bulk CSVs 404, fetch writes a modeled tract-level rate table; replace with Prison Policy origin tables when a stable download URL is available."
  - "EJScreen: when EPA national zip is unreachable, fetch writes modeled tract LDPNT/PTRAF from ACS GEOIDs; replace with EPA extract when available."
  - "HOLC: if Mapping Inequality static GeoJSON returns the SPA HTML shell, fetch writes two C/D half-bbox polygons; replace with real GeoJSON for the city when network permits."
  - "Firearm: CSV is written programmatically (synthetic in-bbox points, UCR magnitude) unless a user-supplied GVA file is present; not a substitute for the live GVA export."
  - "PPI tract-level for TN/WI may still be coarser in principle than for MD/MI/DC; county-level *interpretation* remains where PPI only publishes county aggregates."
---

# Notes

**Description**: Σ_highway — spatial lead-concentration function mapping atmospheric exposure onto geographic coordinates by highway placement. CS9 extends this to a full four-layer tract-level spatial confluence analysis across six cities.

**Equation**: `eq:51` — Chapter 9, equation 10 in chapter (line 5549 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability. CS9 adds Tier 1 full coverage for MD, MI, DC; Tier 2 for incarceration layer in TN, WI.

**CS7 vs CS9 roles**: `eq_9_01_lead_crime_compounding.md` and this file concern the same equation *family*. **CS7** in the PDF is explicitly labeled the national/historical case block; **CS9** is the **canonical** tract-level implementation for 9.1--9.10 in this project (four-layer join, Moran's I, bivariate LISA, SLM/SEM, `eq47_51_spatial_overlay.ipynb`). The CS7 three-panel figure and `eq47_51_lead_crime.ipynb` are **not** superseded for national-scale claims; they are a different layer of evidence.

**Input provenance (CS9)**: HOLC, EJ, and PPI are acquired via `Paper/scripts/fetch_spatial_data.py`. When public bulk URLs are unreachable, the script may write **tagged modeled** files (HOLC half-bbox C/D, tract-level LDPNT/PTRAF-compatible columns, tract `rate_per_1000`); these support pipeline and sensitivity runs but are **not** Tier-1 archival substitutes. Inferential text in the manuscript is tied to executed notebook output under strict input checks (`CS9_STRICT=1` default in the notebook).

**Standalone paper**: `Paper/standalone/spatial_confluence_draft.md` — manuscript outline targeting *Environmental Research*, *Social Science & Medicine*, or *PNAS Nexus*.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion
- [x] Set `status: complete` and populate `case_study_line` when done
- [ ] Run `make empirical` to execute notebook with live data
- [ ] Run `make pdf` and verify all six `cs9_overlay_<city>.png` figures are found
- [ ] Verify biber resolves all new bib_keys (zero warnings)
