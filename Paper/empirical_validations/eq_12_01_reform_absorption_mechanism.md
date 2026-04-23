---
label: eq:12.1-reform-absorption-mechanism
new_label: eq:12.1-reform-absorption-mechanism
chapter: 12
chapter_title: "The Contradiction: Why Reform Serves the Algorithm"
line: 7811
statement: |
  \min(t+1) = \min(t) - \epsilon \cdot \Delta|O_{\text{racialized}} \cap P'|
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - Civil Rights Act 1964 — reduced min without touching max
  - 13th Amendment — interface swap
data_sources: 
  - {name: "Piketty-Saez top income share data", type: "peer-reviewed", url: "http://gabriel-zucman.eu/usdina/"}
difficulty: S
notebook: ""
case_study_line: 8859
falsification: Falsified if a documented reform reduces Elite extraction share (max) rather than just reducing resistance pressure (min).
---

# Notes

**Description**: Reform absorption: policy reform reduces min(M) not max(E) — extraction share preserved

**Equation**: `eq:69` — Chapter 12, equation 1 in chapter (line 7811 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
