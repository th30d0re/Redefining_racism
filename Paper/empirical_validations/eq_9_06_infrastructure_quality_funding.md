---
label: eq:9.6-infrastructure-quality-funding
new_label: eq:9.6-infrastructure-quality-funding
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5504
statement: |
  \text{Infrastructure quality}(t) \propto \text{School funding}(t)
type: quantitative
tier: 2
status: complete
existing_case_study: true
case_study_title: "The Property-Tax Feedback Loop and School Lead Exposure"
phase3_headline: false
target_events: 
  - School infrastructure disparities 2000–2020
  - ASCE 2021 Infrastructure Report Card D+ grade for schools
data_sources: 
  - {name: NCES School Facility Condition Survey, type: "public-dataset", url: "https://nces.ed.gov/"}
  - {name: ASCE 2021 Report Card for America's Infrastructure — Schools, type: "report", url: "https://infrastructurereportcard.org/cat-item/schools-infrastructure/"}
difficulty: M
notebook: "Paper/scripts/eq_funding_propval_feedback.ipynb"
data_file: "Paper/data/eq_funding_propval_feedback.csv"
figure: "Paper/figures/eq_funding_propval_feedback.png"
case_study_line: 6337
bib_keys: [tel_nces, tel_asce, edbuild_23b]
falsification: "Falsified if school infrastructure quality is shown to be unrelated to per-pupil spending in NCES facility condition data."
---

# Notes

**Description**: Infrastructure quality(t) ∝ school funding(t) — per-pupil spending drives facility condition

**Equation**: `eq:infra` — Chapter 9, equation 6 in chapter (line 5504 in manuscript)

**Classification rationale**: Tier=2 — illustrative. ASCE grade is an aggregate ordinal measure; building-age gap is an illustrative comparison from the national distribution rather than a regression coefficient controlling for all confounders.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
