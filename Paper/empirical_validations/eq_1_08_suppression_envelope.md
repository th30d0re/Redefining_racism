---
label: eq:1.8-suppression-envelope
new_label: eq:1.8-suppression-envelope
chapter: 1
chapter_title: "Redefining Racism"
line: 657
statement: |
  \Sigma_{\text{sup}}(t) = \psi_s(t) + \psi_m(t) + R(t) + \Phi_{\text{load}}(t)
type: quantitative
tier: 2
status: pending
existing_case_study: false
phase3_headline: true
target_events: 
  - "Post-1965 backlash wave — union density, wealth share, incarceration rate"
  - Civil Rights era 1955–1975
data_sources: 
  - {name: BLS Union Membership Historical Series, type: "public-dataset", url: "https://www.bls.gov/news.release/union2.toc.htm"}
  - {name: "Saez-Zucman wealth concentration series", type: "peer-reviewed", url: "http://gabriel-zucman.eu/usdina/"}
difficulty: M
notebook: ""
case_study_line: null
falsification: Falsified if M(t) consistently exceeds Σ_sup(t) for extended periods without triggering a crash or interface swap.
---

# Notes

**Description**: Suppression envelope Σ_sup = ψ_s(t) + ψ_m(t) + R(t) + Φ_load(t)

**Equation**: `eq:8` — Chapter 1, equation 8 in chapter (line 657 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
