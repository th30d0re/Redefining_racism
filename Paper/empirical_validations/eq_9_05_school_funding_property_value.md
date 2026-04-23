---
label: eq:9.5-school-funding-property-value
new_label: eq:9.5-school-funding-property-value
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5503
statement: |
  \text{School funding}(t) \propto V_t
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Property-Tax Feedback Loop and School Lead Exposure"
phase3_headline: false
target_events: 
  - "San Antonio v. Rodriguez (1973) upholding property-tax school funding"
data_sources: 
  - {name: NCES Public School Finance Survey, type: "public-dataset", url: "https://nces.ed.gov/"}
  - {name: EdBuild (2019) — 23 Billion, type: report, url: "https://edbuild.org/content/23-billion"}
difficulty: M
notebook: "Paper/scripts/eq_funding_propval_feedback.ipynb"
data_file: "Paper/data/eq_funding_propval_feedback.csv"
figure: "Paper/figures/eq_funding_propval_feedback.png"
case_study_line: 6340
bib_keys: [tel_nces, edbuild_23b, tel_gao, tel_dore, tel_asce, aizer_currie, san_antonio_v_rodriguez]
falsification: Falsified if school funding is shown to be independent of property values in a national dataset controlling for state equalization formulas.
---

# Notes

**Description**: School funding(t) ∝ V_t — property-value-based school funding formula

**Equation**: `eq:funding` — Chapter 9, equation 5 in chapter (line 5503 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on peer-reviewed EdBuild data, NCES national dataset, and Supreme Court precedent in Rodriguez (1973).

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
