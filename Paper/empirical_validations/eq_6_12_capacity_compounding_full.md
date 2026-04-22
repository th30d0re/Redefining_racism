---
label: eq:6.12-capacity-compounding-full
new_label: eq:6.12-capacity-compounding-full
chapter: 6
chapter_title: "The Enforcement Engine: Slave Patrols, the 13th Amendment, and the Compounding Model (1704--1865)"
line: 3036
statement: |
  O_{1971}^{\text{capacity}} = O_{1450}^{\text{capacity}} \cdot (1-\alpha\, P_{\text{enslavement}})(1-\beta\, P_{\text{13thAmendment}})(1-\gamma\, P_{\text{redlining}})(1-\delta\, P_{\text{WarOnDrugs}})
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Compounding Chain — Cannabis Enforcement, Redlining, and Segregation"
phase3_headline: true
target_events: 
  - ACLU cannabis arrests 2010–2018
  - HOLC redlining maps 1934
  - Mass incarceration 1971–present
data_sources: 
  - {name: ACLU (2020) — A Tale of Two Countries, type: report, url: "https://www.aclu.org/report/tale-two-countries-racially-targeted-arrests-era-marijuana-reform"}
  - {name: Mapping Inequality — HOLC Redlining Maps, type: "public-dataset", url: "https://dsl.richmond.edu/panorama/redlining/"}
  - {name: Rothstein (2017) — The Color of Law, type: "peer-reviewed", url: ""}
  - {name: "Darity & Mullen (2020) — From Here to Equality", type: "peer-reviewed", url: ""}
difficulty: M
notebook: "Paper/scripts/eq33_cannabis_redlining.ipynb"
data_file: "Paper/data/eq33_cannabis_redlining.csv"
figure: "Paper/figures/eq33_cannabis_redlining.png"
case_study_line: 3169
bib_keys: [aclu2020, mapping_inequality, rothstein, blackmon, baptist, darity_mullen]
falsification: Falsified if any one policy shock (α, β, γ, δ) is shown to have zero marginal effect on subsequent Black wealth accumulation in longitudinal data.
---

# Notes

**Description**: Capacity compounding full chain: O_1971 = O_1450 × (1−α·P_enslavement)(1−β·P_13th)(1−γ·P_redlining)(1−δ·P_drugs)

**Equation**: `eq:33` — Chapter 6, equation 12 in chapter (line 3036 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
