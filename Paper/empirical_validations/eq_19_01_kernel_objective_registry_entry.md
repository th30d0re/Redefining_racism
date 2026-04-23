---
label: eq:19.1-kernel-objective-registry-entry
new_label: eq:19.1-kernel-objective-registry-entry
chapter: 19
chapter_title: "Equation Registry and Era-Level Calibration"
line: 9854
statement: |
  \max_{\{P_i\}}\; \mathcal{E}(t) \quad \text{subject to} \quad M_{\text{eff}}(t) = M(t) - \lambda\,\Phi_{\text{load}}(t) < \tau
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: []
data_sources: []
difficulty: S
notebook: ""
case_study_line: 11717
falsification: "Redundant with eq:5 and eq:56; falsified by the same conditions as those equations."
---

# Notes

**Description**: Registry restatement of kernel objective: max E(t) s.t. M_eff(t) < τ

**Equation**: `eq:94` — Chapter 19, equation 1 in chapter (line 9854 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
