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
status: pending
existing_case_study: false
phase3_headline: false
target_events: 
  - Michigan school lead pipe replacement program 2016–2024
data_sources: 
  - {name: EPA 3Ts for Reducing Lead in Drinking Water in Schools, type: "public-dataset", url: "https://www.epa.gov/ground-water-and-drinking-water/3ts-reducing-lead-drinking-water-schools"}
difficulty: M
notebook: "nb_ch09_eq07_school_lead_exposure_inverse.ipynb"
case_study_line: null
falsification: "Falsified if school infrastructure quality is shown to be unrelated to lead exposure rates in NCES or EPA school-building data."
---

# Notes

**Description**: P_lead^school(t) ∝ 1/infrastructure quality(t) — degraded infrastructure increases lead exposure in schools

**Equation**: `eq:lead_school` — Chapter 9, equation 7 in chapter (line 5505 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
