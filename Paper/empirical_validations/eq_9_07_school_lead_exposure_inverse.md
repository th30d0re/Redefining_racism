---
label: eq:9.7-school-lead-exposure-inverse
new_label: eq:9.7-school-lead-exposure-inverse
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5505
statement: |
  P_{\text{lead}}^{\text{school}}(t) \propto \frac{1}{\text{Infrastructure quality}(t)}
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Property-Tax Feedback Loop and School Lead Exposure"
phase3_headline: false
target_events: 
  - Michigan school lead pipe replacement program 2016–2024
  - GAO-18-382 (2018) — 37% of tested schools found elevated lead
data_sources: 
  - {name: EPA 3Ts for Reducing Lead in Drinking Water in Schools, type: "public-dataset", url: "https://www.epa.gov/ground-water-and-drinking-water/3ts-reducing-lead-drinking-water-schools"}
  - {name: GAO-18-382 (2018) — K-12 Education: Lead Testing of School Drinking Water, type: "report", url: ""}
  - {name: "Dore et al. (2019) — Sampling in Schools and Daycares to Assess Lead in Drinking Water", type: "peer-reviewed", url: ""}
difficulty: M
notebook: "Paper/scripts/eq_funding_propval_feedback.ipynb"
data_file: "Paper/data/eq_funding_propval_feedback.csv"
figure: "Paper/figures/eq_funding_propval_feedback.png"
case_study_line: 6337
bib_keys: [tel_gao, tel_dore, tel_nces, edbuild_23b]
falsification: "Falsified if school infrastructure quality is shown to be unrelated to lead exposure rates in NCES or EPA school-building data."
---

# Notes

**Description**: P_lead^school(t) ∝ 1/infrastructure quality(t) — degraded infrastructure increases lead exposure in schools

**Equation**: `eq:lead_school` — Chapter 9, equation 7 in chapter (line 5505 in manuscript)

**Classification rationale**: Tier=1 — GAO-18-382 stratified national survey; EPA 3Ts data; Doré et al. peer-reviewed building-age effect on first-draw lead concentrations.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
