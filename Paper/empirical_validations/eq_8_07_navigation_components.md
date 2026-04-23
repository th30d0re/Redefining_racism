---
label: eq:8.7-navigation-components
new_label: eq:8.7-navigation-components
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 3927
statement: |
  \gamma_i(q) = \sum_{j \in \mathcal{N}_i} \tfrac{1}{2}\,\|q_i - q_j\|^2, \qquad
  \beta_i(q) = \tfrac{1}{2}\!\!\prod_{(i,j) \in \mathcal{E}_G}\!\! b_{ij}(q),
  \quad b_{ij}(q) = \delta - \|q_i - q_j\|^2,
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: []
data_sources: []
difficulty: S
notebook: ""
case_study_line: 4220
falsification: "Falsified if goal and constraint functions do not bound follower trajectory correctly in containment-model simulation."
---

# Notes

**Description**: Navigation function components: goal function γ_i (proximity to neighbors) and constraint b_ij (distance to boundary)

**Equation**: `eq:navigation-components` — Chapter 8, equation 7 in chapter (line 3927 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
