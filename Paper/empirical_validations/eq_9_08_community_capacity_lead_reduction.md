---
label: eq:9.8-community-capacity-lead-reduction
new_label: eq:9.8-community-capacity-lead-reduction
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5506
statement: |
  \text{Community capacity}(t) = O_t^{\text{capacity}} \cdot (1 - \alpha \cdot P_{\text{lead}}^{\text{school}}(t))
type: quantitative
tier: 2
status: complete
existing_case_study: true
case_study_title: "The Property-Tax Feedback Loop and School Lead Exposure"
phase3_headline: false
target_events: 
  - "Aizer-Currie (2019) Rhode Island cohort: each 1 μg/dL BLL reduction → 17% suspension reduction, 22% detention reduction"
data_sources: 
  - {name: "Aizer & Currie (2019) — Lead and Juvenile Delinquency", type: "peer-reviewed", url: "https://doi.org/10.1257/app.20180026"}
difficulty: M
notebook: "Paper/scripts/eq_funding_propval_feedback.ipynb"
data_file: "Paper/data/eq_funding_propval_feedback.csv"
figure: "Paper/figures/eq_funding_propval_feedback.png"
case_study_line: 6340
bib_keys: [aizer_currie, tel_gao, edbuild_23b]
falsification: Falsified if community economic capacity is shown to be independent of school lead exposure after controlling for income.
---

# Notes

**Description**: Community capacity(t) = O^capacity_t × (1 − α·P_lead^school(t)) — lead exposure reduces community capacity

**Equation**: `eq:community` — Chapter 9, equation 8 in chapter (line 5506 in manuscript)

**Classification rationale**: Tier=2 — Aizer & Currie peer-reviewed sibling fixed-effects estimate (α ≈ 0.17–0.22 per μg/dL) is well-identified, but the translation from suspension/detention rate to "community capacity" involves an ordinal interpretation of the framework mapping.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
