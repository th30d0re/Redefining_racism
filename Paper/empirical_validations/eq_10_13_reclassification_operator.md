---
label: eq:10.13-reclassification-operator
new_label: eq:10.13-reclassification-operator
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: 6758
statement: |
  \mathcal{R}(x_i) =  I_{\text{buffer}} & \text{if } K(x_i) \leq K_{\text{tolerated}} \text{ and } \mathrm{comply}(x_i) = 1 \\ O_{\text{final}} & \text{if } K(x_i) > K_{\text{tolerated}} \text{ or } \mathrm{comply}(x_i) = 0
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - "Obama-era Black professional class reclassification"
  - "Post-9/11 Arab-American reclassification"
data_sources: []
difficulty: M
notebook: ""
case_study_line: 7734
falsification: Falsified if the operator fails to predict observed ideological sorting in any documented historical reclassification case.
---

# Notes

**Description**: Reclassification operator R: maps individual x from tier based on K(x) vs K_tolerated and comply(x)

**Equation**: `eq:reclassification` — Chapter 10, equation 13 in chapter (line 6758 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
