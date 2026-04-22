---
label: eq:9.1-lead-crime-compounding
new_label: eq:9.1-lead-crime-compounding
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5153
statement: |
  O_{t+1}^{\text{capacity}} = O_t^{\text{capacity}} \cdot (1 - \alpha_{P_{\text{lead}}})
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Lead-Crime Nexus and Spatial Concentration"
phase3_headline: true
target_events: 
  - "Lead gasoline phase-out 1970–1986 and crime decline 1990–2010"
data_sources: 
  - {name: Reyes (2007) — Environmental Policy as Social Policy, type: "peer-reviewed", url: "https://doi.org/10.3386/w12417"}
  - {name: "Aizer & Currie (2019) — Lead and Juvenile Delinquency", type: "peer-reviewed", url: "https://doi.org/10.1257/app.20180026"}
difficulty: M
notebook: "Paper/scripts/eq47_51_lead_crime.ipynb"
data_file: "Paper/data/eq47_51_lead_crime_reyes.csv, Paper/data/eq47_51_lead_crime_aizer.csv, Paper/data/eq47_51_lead_crime_highway.csv"
figure: "Paper/figures/eq47_51_lead_crime.png"
case_study_line: 5744
bib_keys: [reyes2007, aizer_currie, rothstein, mapping_inequality]
falsification: "Falsified if Reyes (2007) blood-lead time-series fails to predict crime-rate decline after 20-year lag in multivariate regression."
---

# Notes

**Description**: Lead-crime compounding: O^capacity(t) reduced by P_lead policy variable in compounding chain

**Equation**: `eq:47` — Chapter 9, equation 1 in chapter (line 5153 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
