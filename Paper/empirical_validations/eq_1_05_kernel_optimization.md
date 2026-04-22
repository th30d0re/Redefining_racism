---
label: eq:1.5-kernel-optimization
new_label: eq:1.5-kernel-optimization
chapter: 1
chapter_title: "Redefining Racism"
line: 486
statement: |
  \max \mathcal{E}(t) \quad \text{subject to} \quad M(t) < \tau
type: quantitative
tier: 1
status: pending
existing_case_study: false
phase3_headline: true
target_events: 
  - "Antebellum South 1840–1860 (cotton output vs. slave-rebellion suppression budget)"
  - "Post-Civil Rights Era 1965–2020 (Elite wealth share vs. reform pressure)"
data_sources: 
  - {name: Piketty, Saez, Zucman — Distributional National Accounts, type: "peer-reviewed", url: "http://gabriel-zucman.eu/usdina/"}
  - {name: Gilens and Page (2014) — Testing Theories of American Politics, type: "peer-reviewed", url: "https://doi.org/10.1017/S1537592714001595"}
difficulty: L
notebook: "nb_ch01_eq05_kernel_optimization.ipynb"
case_study_line: null
falsification: "Falsified if a documented period shows sustained decline in Elite extraction share while M(t) < τ without kernel-level intervention."
---

# Notes

**Description**: Predatory min-max: maximize extraction E(t) subject to class-coherence risk M(t) < τ

**Equation**: `eq:5` — Chapter 1, equation 5 in chapter (line 486 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
