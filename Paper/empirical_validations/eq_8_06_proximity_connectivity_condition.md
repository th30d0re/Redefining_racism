---
label: eq:8.6-proximity-connectivity-condition
new_label: eq:8.6-proximity-connectivity-condition
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 3837
statement: |
  \|q_i(t) - q_j(t)\|^2 \leq \delta.
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: []
data_sources: []
difficulty: S
notebook: ""
case_study_line: 4128
falsification: "Falsified if social-affinity graph connectivity is shown to be independent of proximity in documented community-level data."
---

# Notes

**Description**: State-dependent connectivity: edge (i,j) exists iff ‖q_i − q_j‖² ≤ δ

**Equation**: `eq:state-dep-connectivity` — Chapter 8, equation 6 in chapter (line 3837 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
