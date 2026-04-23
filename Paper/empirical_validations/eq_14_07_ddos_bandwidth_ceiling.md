---
label: eq:14.7-ddos-bandwidth-ceiling
new_label: eq:14.7-ddos-bandwidth-ceiling
chapter: 14
chapter_title: "The Algorithmic Epoch: Real-Time Subjugation and the Necessity of the Counter-Virus"
line: 9059
statement: |
  n > \Gamma \quad \Longrightarrow \quad \text{Localized enforcement superiority fails at} \ (n - \Gamma) \ \text{nodes.}
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - "George Floyd protests 2020 — simultaneous multi-city mobilization vs. National Guard capacity"
data_sources: 
  - {name: "Armed Conflict Location & Event Data (ACLED) — US protests 2020", type: "public-dataset", url: "https://acleddata.com/"}
difficulty: M
notebook: ""
case_study_line: 10858
falsification: "Falsified if F_enforce simultaneously suppresses n > Γ nodes in any documented distributed mobilization event."
---

# Notes

**Description**: DDoS bandwidth ceiling: n > Γ simultaneous nodes exceeds F_enforce concentrated-force ceiling

**Equation**: `eq:ddos_bandwidth` — Chapter 14, equation 7 in chapter (line 9059 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
