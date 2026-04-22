---
label: eq:1.11-phase-loading
new_label: eq:1.11-phase-loading
chapter: 1
chapter_title: "Redefining Racism"
line: 752
statement: |
  \Phi_j = \sum_{k=1}^{K} \phi_{k,j}, \qquad
  \Phi_{\text{load}}(t) = \operatorname{Dispersion}\!\left(\{\Phi_j\}_{j=1}^{N}\right) = 1 - \left|\frac{1}{N}\sum_{j=1}^{N} e^{i\Phi_j}\right| \in [0,1]
type: quantitative
tier: 3
status: pending
existing_case_study: false
phase3_headline: false
target_events: 
  - "Post-Civil Rights fragmentation 1968–1990"
  - "Identity-politics polarization 1990–2020"
data_sources: 
  - {name: ANES Time Series Study 1948–2020, type: "public-dataset", url: "https://electionstudies.org/"}
  - {name: Pew Research Political Polarization Series, type: "public-dataset", url: "https://www.pewresearch.org/politics/"}
difficulty: M
notebook: ""
case_study_line: null
falsification: "Falsified if survey-measured cross-group solidarity remains high when Φ_load is high in ANES or Pew polarization data."
---

# Notes

**Description**: Phase-loading Φ_load = 1 − |mean(exp(iΦ_j))| — circular dispersion measuring destructive interference across subgroups

**Equation**: `eq:11` — Chapter 1, equation 11 in chapter (line 752 in manuscript)

**Classification rationale**: Type=quantitative, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
