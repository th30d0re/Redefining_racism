---
label: eq:14.17-botnet-load-theorem
new_label: eq:14.17-botnet-load-theorem
chapter: 14
chapter_title: "The Algorithmic Epoch: Real-Time Subjugation and the Necessity of the Counter-Virus"
line: 9234
statement: |
  n(t) > \Gamma_{\text{armed}} \quad \wedge \quad \mathcal{N}(t) \to H_{\max}.
type: quantitative
tier: 2
status: complete
existing_case_study: false
phase3_headline: false
target_events: 
  - George Floyd protests 2020 — 550+ cities simultaneously
data_sources: 
  - {name: ACLED — 2020 US protest dataset, type: "public-dataset", url: "https://acleddata.com/"}
difficulty: M
notebook: ""
case_study_line: 11051
falsification: "Falsified if enforcement grid contains a swarm with n > Γ_armed nodes and high N(t) in any documented mobilization."
---

# Notes

**Description**: Botnet Load Theorem: enforcement fails when n(t) > Γ_armed AND N(t) > N_threshold

**Equation**: `eq:botnet_load` — Chapter 14, equation 17 in chapter (line 9234 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
