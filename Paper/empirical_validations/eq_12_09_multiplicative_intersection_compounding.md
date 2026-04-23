---
label: eq:12.9-multiplicative-intersection-compounding
new_label: eq:12.9-multiplicative-intersection-compounding
chapter: 12
chapter_title: "The Contradiction: Why Reform Serves the Algorithm"
line: 8463
statement: |
  O_t^{\text{capacity}} = O_{t-1}^{\text{capacity}} \cdot (1 - \alpha_r P_t) \cdot (1 - \alpha_g P_t)
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - "Black women's wage and wealth gap 2000–2024"
data_sources: 
  - {name: "AAUW pay-gap data by race and gender", type: "public-dataset", url: "https://www.aauw.org/resources/research/simple-truth/"}
  - {name: Federal Reserve SCF wealth by race × gender, type: "public-dataset", url: "https://www.federalreserve.gov/econres/scfindex.htm"}
difficulty: M
notebook: ""
case_study_line: 9607
falsification: "Falsified if Black women's wealth gap from white men is not multiplicatively larger than either racial or gender gap alone."
---

# Notes

**Description**: Intersection compounding: effective reduction = (1−α_r)(1−α_g) — multiplicative, not additive

**Equation**: `eq:77` — Chapter 12, equation 9 in chapter (line 8463 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
