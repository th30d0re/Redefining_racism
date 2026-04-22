---
label: eq:1.10-effective-coherence
new_label: eq:1.10-effective-coherence
chapter: 1
chapter_title: "Redefining Racism"
line: 665
statement: |
  M_{\text{eff}}(t) = M(t) - \lambda \Phi_{\text{load}}(t), \quad M_{\text{eff}}(t) > \tau
type: quantitative
tier: 2
status: pending
existing_case_study: false
phase3_headline: false
target_events: 
  - "Bacon's Rebellion 1676 — cross-racial solidarity peak"
  - Civil Rights Movement 1955–1968
data_sources: 
  - {name: "ANES cross-racial coalition data 1948–2020", type: "public-dataset", url: "https://electionstudies.org/"}
difficulty: M
notebook: ""
case_study_line: null
falsification: "Falsified if a crash event occurs when M_eff(t) < τ, or if no crash occurs when M_eff(t) > τ persistently."
---

# Notes

**Description**: Effective class coherence M_eff = M(t) − λΦ_load(t); crash when M_eff > τ

**Equation**: `eq:10` — Chapter 1, equation 10 in chapter (line 665 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
