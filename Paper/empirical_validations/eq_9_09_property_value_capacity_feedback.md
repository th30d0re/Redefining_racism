---
label: eq:9.9-property-value-capacity-feedback
new_label: eq:9.9-property-value-capacity-feedback
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5507
statement: |
  V_{t+1} \propto \text{Community capacity}(t)
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Property-Tax Feedback Loop and School Lead Exposure"
phase3_headline: false
target_events: 
  - Redlined neighborhood property value trajectories 1940–2020
  - HOLC-D tracts appreciated at 52% of HOLC-A rates since 1940
data_sources: 
  - {name: Mapping Inequality HOLC maps + ACS property value data, type: "public-dataset", url: "https://dsl.richmond.edu/panorama/redlining/"}
  - {name: American Community Survey (ACS) longitudinal property value data, type: "public-dataset", url: "https://data.census.gov/"}
difficulty: M
notebook: "Paper/scripts/eq_funding_propval_feedback.ipynb"
data_file: "Paper/data/eq_funding_propval_feedback.csv"
figure: "Paper/figures/eq_funding_propval_feedback.png"
case_study_line: 6340
bib_keys: [tel_nces, edbuild_23b, tel_gao, tel_dore, tel_asce, aizer_currie, san_antonio_v_rodriguez, mapping_inequality]
falsification: Falsified if property values in subsequent periods are shown to be independent of community economic capacity in longitudinal housing data.
---

# Notes

**Description**: V_{t+1} ∝ community capacity(t) — property values feed back through community economic capacity

**Equation**: `eq:propval` — Chapter 9, equation 9 in chapter (line 5507 in manuscript)

**Classification rationale**: Tier=1 — ACS longitudinal property values; Mapping Inequality HOLC spatial overlay; documented 1940–2020 appreciation differential confirming the feedback mechanism.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
