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
case_study_title: "The Lead-Crime Nexus and Spatial Concentration"
phase3_headline: false
target_events: 
  - Interstate highway construction through Black neighborhoods 1956–1972
data_sources: 
  - {name: Rothstein (2017) — The Color of Law (highway displacement chapters), type: "peer-reviewed", url: ""}
  - {name: EPA National Emissions Inventory, type: "public-dataset", url: "https://www.epa.gov/air-emissions-inventories"}
difficulty: M
notebook: "Paper/scripts/eq47_51_lead_crime.ipynb"
data_file: "Paper/data/eq47_51_lead_crime_reyes.csv, Paper/data/eq47_51_lead_crime_aizer.csv, Paper/data/eq47_51_lead_crime_highway.csv"
figure: "Paper/figures/eq47_51_lead_crime.png"
case_study_line: 5744
bib_keys: [reyes2007, aizer_currie, rothstein, mapping_inequality]
falsification: "Falsified if spatial concentration of automotive lead is not correlated with highway placement in redlined vs. non-redlined areas."
---

# Notes

**Description**: Σ_highway — spatial lead-concentration function mapping atmospheric exposure onto geographic coordinates by highway placement

**Equation**: `eq:51` — Chapter 9, equation 10 in chapter (line 5549 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
