---
label: eq:9.4-redlining-containment-field
new_label: eq:9.4-redlining-containment-field
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5476
statement: |
  P_{\text{lead}}^{v}(x) \propto \mathbb{1}_{x \in \text{Redlined}} \quad \text{for each vector } v \in \{\text{air}, \text{water}, \text{school}\}
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Lead-Crime Nexus and Spatial Concentration"
phase3_headline: false
target_events: 
  - HOLC redlining 1934–1968 and lead exposure mapping
data_sources: 
  - {name: Mapping Inequality HOLC maps, type: "public-dataset", url: "https://dsl.richmond.edu/panorama/redlining/"}
  - {name: Rothstein (2017) — The Color of Law, type: "peer-reviewed", url: ""}
difficulty: M
notebook: "Paper/scripts/eq47_51_lead_crime.ipynb"
data_file: "Paper/data/eq47_51_lead_crime_reyes.csv, Paper/data/eq47_51_lead_crime_aizer.csv, Paper/data/eq47_51_lead_crime_highway.csv"
figure: "Paper/figures/eq47_51_lead_crime.png"
case_study_line: 5744
bib_keys: [reyes2007, aizer_currie, rothstein, mapping_inequality]
falsification: "Falsified if HOLC map grades show no statistically significant correlation with lead exposure levels in matched same-city tract comparison."
---

# Notes

**Description**: Redlining containment field: each lead vector's intensity = f(HOLC grade) — spatial amplification by race

**Equation**: `eq:50` — Chapter 9, equation 4 in chapter (line 5476 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
