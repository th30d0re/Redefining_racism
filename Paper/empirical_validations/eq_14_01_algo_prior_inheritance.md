---
label: eq:14.1-algo-prior-inheritance
new_label: eq:14.1-algo-prior-inheritance
chapter: 14
chapter_title: "The Algorithmic Epoch: Real-Time Subjugation and the Necessity of the Counter-Virus"
line: 8967
statement: |
  P_{\text{algo}} = \arg\min_{P} \; \mathcal{L}(P; \mathcal{H}) \quad \Longrightarrow \quad |O_{\text{racialized}} \cap P_{\text{algo}}| \gg |I \cap P_{\text{algo}}|
type: quantitative
tier: 2
status: complete
existing_case_study: false
phase3_headline: false
target_events: 
  - COMPAS recidivism algorithm analysis 2016
  - Facial recognition racial accuracy disparities
data_sources: 
  - {name: Angwin et al. (2016) — Machine Bias (ProPublica), type: journalism, url: "https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing"}
  - {name: "Buolamwini & Gebru (2018) — Gender Shades", type: "peer-reviewed", url: "https://doi.org/10.1145/3287560.3287596"}
difficulty: M
notebook: ""
case_study_line: 10757
falsification: "Falsified if ML systems trained on pre-2024 US data show no racial disparity in predictive outputs relative to ground truth after controlling for relevant covariates."
---

# Notes

**Description**: Algorithmic prior inheritance: P_algo trained on H (historical dataset produced under compounding chain) inherits extraction priors

**Equation**: `eq:algo_prior_inheritance` — Chapter 14, equation 1 in chapter (line 8967 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
