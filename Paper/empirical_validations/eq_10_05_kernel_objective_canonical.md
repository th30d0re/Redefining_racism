---
label: eq:10.5-kernel-objective-canonical
new_label: eq:10.5-kernel-objective-canonical
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: 6402
statement: |
  \max_{\{P_i\}}\; \mathcal{E}(t) \quad \text{subject to} \quad M_{\text{eff}}(t) < \tau
type: quantitative
tier: 1
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - "Post-Civil Rights Era 1965–2024"
  - "Great Compression 1933–1978 (New Deal psi_m deployment)"
  - "Post-1978 recovery to Gilded Age levels (Delta_max=0)"
data_sources: 
  - {name: "Piketty-Saez-Zucman Distributional National Accounts", type: "peer-reviewed", url: "http://gabriel-zucman.eu/usdina/"}
difficulty: L
notebook: "eq56_kernel_objective.ipynb"
case_study_line: 7477
falsification: "Falsified if a documented period shows sustained Elite wealth-share decline while M_eff(t) < τ without external kinetic intervention."
---

# Notes

**Description**: Canonical kernel objective: maximize E(t) subject to M_eff(t) < τ — full algorithm statement

**Equation**: `eq:56` — Chapter 10, equation 5 in chapter (line 6402 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
