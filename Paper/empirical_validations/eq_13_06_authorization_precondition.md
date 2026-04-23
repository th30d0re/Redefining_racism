---
label: eq:13.6-authorization-precondition
new_label: eq:13.6-authorization-precondition
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: 8746
statement: |
  \text{Valid\_negotiation}(t) =  1 & \text{if } A_{\text{auth}} = 1 \\ 0 & \text{if } A_{\text{auth}} = 0
type: structural
tier: 3
status: complete
existing_case_study: false
phase3_headline: false
target_events: 
  - "US Môle Saint-Nicolas failure 1891 (Frederick Douglass as envoy)"
data_sources: []
difficulty: S
notebook: ""
case_study_line: 10050
falsification: Falsified if E_global achieves extraction without satisfying authorization precondition under active legitimation constraint.
---

# Notes

**Description**: Authorization precondition A_auth ∈ {0,1} — diplomatic authorization required by L before extraction

**Equation**: `eq:83` — Chapter 13, equation 6 in chapter (line 8746 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
