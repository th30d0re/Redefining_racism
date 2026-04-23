---
label: eq:14.8-armed-swarm-bandwidth
new_label: eq:14.8-armed-swarm-bandwidth
chapter: 14
chapter_title: "The Algorithmic Epoch: Real-Time Subjugation and the Necessity of the Counter-Virus"
line: 9067
statement: |
  \Gamma_{\text{armed}} = \frac{\Gamma_{\text{total}}}{\gamma(k_{\text{node}})}, \quad \text{with} \ \gamma(k_{\text{armed}}) \gg \gamma(k_{\text{unarmed}}).
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - "Ruby Ridge 1992 and Waco 1993 — single-node siege costs vs. capacity"
data_sources: []
difficulty: M
notebook: ""
case_study_line: 10869
falsification: "Falsified if F_enforce simultaneously neutralizes armed nodes with force-multiplier cost significantly below predicted minimum."
---

# Notes

**Description**: Armed swarm bandwidth: Γ_armed < n nodes when γ(k) × n > total F_enforce force capacity

**Equation**: `eq:kinetic_parity` — Chapter 14, equation 8 in chapter (line 9067 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
