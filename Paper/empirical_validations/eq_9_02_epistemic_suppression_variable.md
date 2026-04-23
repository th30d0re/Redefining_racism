---
label: eq:9.2-epistemic-suppression-variable
new_label: eq:9.2-epistemic-suppression-variable
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5236
statement: |
  O_{t_0 + \Delta t_{\text{suppress}}}^{\text{capacity}} = O_{t_0}^{\text{capacity}} \cdot (1 - \alpha_{P_{\text{lead}}})^{\Delta t_{\text{suppress}}}
type: quantitative
tier: 2
status: complete
existing_case_study: true
case_study_title: "The Lead-Crime Nexus and Spatial Concentration"
phase3_headline: false
target_events: 
  - "Lead industry cover-up 1926–1970"
  - "Clair Patterson's research suppression"
data_sources: 
  - {name: Kitman (2000) — The Secret History of Lead (The Nation), type: journalism, url: "https://www.typeinvestigations.org/investigation/2000/03/02/secret-history-lead/"}
  - {name: Michaels (2008) — Doubt Is Their Product, type: "peer-reviewed", url: ""}
difficulty: M
notebook: "Paper/scripts/eq47_51_lead_crime.ipynb"
data_file: "Paper/data/eq47_51_lead_crime_reyes.csv, Paper/data/eq47_51_lead_crime_aizer.csv, Paper/data/eq47_51_lead_crime_highway.csv"
figure: "Paper/figures/eq47_51_lead_crime.png"
case_study_line: 6344
bib_keys: [reyes2007, aizer_currie, kitman_lead, tel_ethyl]
falsification: "Falsified if documented lead industry cover-up timeline shows no correlation with delay in regulatory response."
---

# Notes

**Description**: Epistemic suppression variable P_epistemic: corporate/governmental actions delaying lead-harm knowledge — extends P_lead compounding duration

**Equation**: `eq:48` — Chapter 9, equation 2 in chapter (line 5236 in manuscript)

**Classification rationale**: Tier 2 — illustrative instantiation. The 48-year suppression window (1925–1973) is bounded by two verifiable dates, but the "additional exposed births" calculation is an order-of-magnitude estimate rather than a regression-identified causal quantity.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
