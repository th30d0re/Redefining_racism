---
label: eq:8.11-mittag-leffler-stability
new_label: eq:8.11-mittag-leffler-stability
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 4111
statement: |
  \|x(t)\| \leq \bigl\{\, m[x(t_0)]\, E_{\alpha,1}\!\bigl(-\lambda(t-t_0)^{\alpha}\bigr)\bigr\}^{b},
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - Black intergenerational wealth mobility 1865–2024
data_sources: 
  - {name: Chetty et al. (2018) — Race and Economic Opportunity in the United States, type: "peer-reviewed", url: "https://doi.org/10.1093/qje/qjy007"}
difficulty: M
notebook: ""
case_study_line: 4402
falsification: "Falsified if social-mobility data for α ∈ (0,1) shows exponential rather than Mittag-Leffler (slower) decay of displacement."
---

# Notes

**Description**: Mittag-Leffler asymptotic stability for α ∈ (0,1): ‖q_i(t) − conv(V_L)‖ ≤ m·E_α(−λt^α)·‖q_i(0)‖^b

**Equation**: `eq:39` — Chapter 8, equation 11 in chapter (line 4111 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
