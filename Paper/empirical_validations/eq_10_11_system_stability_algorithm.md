---
label: eq:10.11-system-stability-algorithm
new_label: eq:10.11-system-stability-algorithm
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: 6492
statement: |
  \text{Dynamic Equivalent:} \quad \max \mathcal{E}(t) \quad \text{subject to} \quad M_{\text{eff}}(t)=M(t)-\lambda\Phi_{\text{load}}(t)<\tau
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: []
data_sources: []
difficulty: S
notebook: ""
case_study_line: 7405
falsification: Falsified if system stability is maintained when extraction/resistance ratio is not optimized.
---

# Notes

**Description**: Algorithm stability: five-tier hierarchy + suppression envelope maintains Max/Min ratio → stability

**Equation**: `eq:62` — Chapter 10, equation 11 in chapter (line 6492 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
