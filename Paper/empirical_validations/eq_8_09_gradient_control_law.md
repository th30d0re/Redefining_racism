---
label: eq:8.9-gradient-control-law
new_label: eq:8.9-gradient-control-law
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 3937
statement: |
  u_i = -K_i\, \nabla_{q_i}\,\varphi_i(q), \qquad K_i > 0.
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: []
data_sources: []
difficulty: S
notebook: ""
case_study_line: 4228
falsification: "Falsified if negative gradient of φ_i fails to drive convergence in any simulation with K_i > 0 and valid graph."
---

# Notes

**Description**: Control law: u_i = −K_i ∇_{q_i} φ_i(q), K_i > 0 — negative gradient descent on navigation function

**Equation**: `eq:control-law` — Chapter 8, equation 9 in chapter (line 3937 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
