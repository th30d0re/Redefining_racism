---
label: eq:9.3-multi-vector-lead-exposure
new_label: eq:9.3-multi-vector-lead-exposure
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5472
statement: |
  P_{\text{lead}} = P_{\text{lead}}^{\text{air}} + P_{\text{lead}}^{\text{water}} + P_{\text{lead}}^{\text{school}}
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Lead-Crime Nexus and Spatial Concentration"
phase3_headline: false
target_events: 
  - Flint water crisis 2014–2019
  - Detroit school lead exposure study
data_sources: 
  - {name: EPA Air Quality Monitoring Data, type: "public-dataset", url: "https://www.epa.gov/outdoor-air-quality-data"}
  - {name: Mapping Inequality HOLC maps, type: "public-dataset", url: "https://dsl.richmond.edu/panorama/redlining/"}
difficulty: M
notebook: "Paper/scripts/eq47_51_lead_crime.ipynb"
data_file: "Paper/data/eq47_51_lead_crime_reyes.csv, Paper/data/eq47_51_lead_crime_aizer.csv, Paper/data/eq47_51_lead_crime_highway.csv"
figure: "Paper/figures/eq47_51_lead_crime.png"
case_study_line: 5744
bib_keys: [reyes2007, aizer_currie, rothstein, mapping_inequality]
falsification: "Falsified if cumulative lead exposure from all three vectors is not significantly higher in redlined areas than non-redlined areas."
---

# Notes

**Description**: Multi-vector lead exposure: P_lead = P_air + P_water + P_institutional_plumbing, all concentrated by redlining

**Equation**: `eq:49` — Chapter 9, equation 3 in chapter (line 5472 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
