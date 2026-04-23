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
  - "PPI tract-level data unavailable for TN (Memphis, Nashville) and WI (Milwaukee) — county-level fallback used; attenuates within-county spatial contrast."
  - "GVA incident data (2014–2024) requires manual bulk export from GVA query interface; pre-2014 covered by CDC WONDER county-level firearm mortality."
---

# Notes

**Description**: Σ_highway — spatial lead-concentration function mapping atmospheric exposure onto geographic coordinates by highway placement. CS9 extends this to a full four-layer tract-level spatial confluence analysis across six cities.

**Equation**: `eq:51` — Chapter 9, equation 10 in chapter (line 5549 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability. CS9 adds Tier 1 full coverage for MD, MI, DC; Tier 2 for incarceration layer in TN, WI.

**CS9 upgrade**: This registry entry now covers the full CS9 "Spatial Confluence" case study (`\label{cs:spatial_confluence}`), which extends the CS7 lead-crime analysis to a four-layer tract-level spatial pipeline. The original CS7 analysis (three-panel figure `eq47_51_lead_crime.png`, notebook `eq47_51_lead_crime.ipynb`) is preserved; CS9 adds the spatial join pipeline, choropleth figures, Moran's I / bivariate LISA / SLM-SEM statistics, and pooled forest plot.

**Standalone paper**: `Paper/standalone/spatial_confluence_draft.md` — manuscript outline targeting *Environmental Research*, *Social Science & Medicine*, or *PNAS Nexus*.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion
- [x] Set `status: complete` and populate `case_study_line` when done
- [ ] Run `make empirical` to execute notebook with live data
- [ ] Run `make pdf` and verify all six `cs9_overlay_<city>.png` figures are found
- [ ] Verify biber resolves all new bib_keys (zero warnings)
