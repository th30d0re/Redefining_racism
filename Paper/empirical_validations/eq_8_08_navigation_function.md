---
label: eq:8.8-navigation-function
new_label: eq:8.8-navigation-function
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 3933
statement: |
  \varphi_i(q) = \frac{\gamma_i(q)}{\bigl(\gamma_i(q)^k + \beta_i(q)\bigr)^{1/k}},
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: []
data_sources: []
difficulty: S
notebook: ""
case_study_line: 4223
falsification: "Falsified if φ_i fails to produce convergence in any graph satisfying the containment model's connectivity conditions."
---

# Notes

**Description**: Navigation function φ_i = γ_i / (γ_i^k + β_i)^{1/k} — bounded-above function for containment convergence

**Equation**: `eq:navigation-function` — Chapter 8, equation 8 in chapter (line 3933 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
