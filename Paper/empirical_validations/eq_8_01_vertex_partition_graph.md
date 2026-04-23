---
label: eq:8.1-vertex-partition-graph
new_label: eq:8.1-vertex-partition-graph
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 3729
statement: |
  \mathcal{V} = \mathcal{V}_L \cup \mathcal{V}_F, \qquad |\mathcal{V}_L| = m, \ |\mathcal{V}_F| = N-m,
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: []
data_sources: []
difficulty: S
notebook: ""
case_study_line: 4020
falsification: Falsified if leader/follower partition fails to predict convergence in any documented network containment model.
---

# Notes

**Description**: Graph vertex partition: V = V_L (leaders/Elite) ∪ V_F (followers/non-Elite)

**Equation**: `eq:35` — Chapter 8, equation 1 in chapter (line 3729 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
