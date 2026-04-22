---
label: eq:13.1-global-compounding-capacity
new_label: eq:13.1-global-compounding-capacity
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: 8619
statement: |
  O_{\text{global}}^{\text{capacity}}(t) = O_{\text{global}}^{\text{capacity}}(t_0) \cdot \prod_{i} (1 - \alpha_i P_i^{\text{imperial}})
type: quantitative
tier: 2
status: pending
existing_case_study: false
phase3_headline: false
target_events: 
  - "Haiti post-independence 1804–2024"
  - "Congo post-colonialism 1960–2024"
data_sources: 
  - {name: World Bank development indicators — GDP per capita time series, type: "public-dataset", url: "https://data.worldbank.org/"}
  - {name: IMF historical debt data, type: "public-dataset", url: "https://www.imf.org/en/Data"}
difficulty: M
notebook: ""
case_study_line: null
falsification: "Falsified if post-colonial nation's capacity trajectory shows exponential recovery rather than Mittag-Leffler slow recovery after independence."
---

# Notes

**Description**: Global South compounding: O_global capacity reduced by colonial extraction chain (same multiplicative logic as domestic)

**Equation**: `eq:79` — Chapter 13, equation 1 in chapter (line 8619 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
