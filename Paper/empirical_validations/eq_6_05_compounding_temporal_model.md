---
label: eq:6.5-compounding-temporal-model
new_label: eq:6.5-compounding-temporal-model
chapter: 6
chapter_title: "The Enforcement Engine: Slave Patrols, the 13th Amendment, and the Compounding Model (1704--1865)"
line: 2997
statement: |
  O_t^{\text{capacity}} = O_{t-1}^{\text{capacity}} \cdot (1 - \alpha P_t)
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - Black wealth trajectory 1865–2024
data_sources: 
  - {name: "Hamilton & Darity (2017) — The Political Economy of Education, Financial Literacy, and the Racial Wealth Gap", type: "peer-reviewed", url: ""}
difficulty: M
notebook: ""
case_study_line: ~3154
falsification: Falsified if policy shock effects on O^capacity are shown to be independent across periods in longitudinal wealth data.
---

# Notes

**Description**: Compounding temporal model: O^capacity(t+1) = O^capacity(t) × (1 − α·P_t)

**Equation**: `eq:30` — Chapter 6, equation 5 in chapter (line 2997 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
