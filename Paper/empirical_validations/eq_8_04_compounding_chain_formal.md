---
label: eq:8.4-compounding-chain-formal
new_label: eq:8.4-compounding-chain-formal
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 3747
statement: |
  O_{1971}^{\text{capacity}} = O_{1450}^{\text{capacity}} \cdot (1-\alpha P_{\text{enslavement}})(1-\beta P_{\text{13thAmendment}})(1-\gamma P_{\text{redlining}})(1-\delta P_{\text{WarOnDrugs}})
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - Black wealth accumulation trajectory 1865–2024
data_sources: 
  - {name: Federal Reserve SCF racial wealth data, type: "public-dataset", url: "https://www.federalreserve.gov/econres/scfindex.htm"}
difficulty: M
notebook: "Paper/scripts/eq33_cannabis_redlining.ipynb"
case_study_line: 3187
falsification: "Falsified if multiplicative chain prediction diverges significantly from observed wealth-gap trajectory in longitudinal data."
---

# Notes

**Description**: Formal fractional compounding chain — multiplicative capacity reduction over policy sequence

**Equation**: `eq:37` — Chapter 8, equation 4 in chapter (line 3747 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Cross-reference**: The compounding chain formula (`eq:37`) is fully validated by the `eq:33` (Cannabis/Redlining) case study. The eq:33 case study (manuscript line 3187, notebook `Paper/scripts/eq33_cannabis_redlining.ipynb`) applies the four-factor multiplicative chain with independently documented shock values ($\alpha$=enslavement, $\beta$=13th Amendment exception, $\gamma$=HOLC redlining, $\delta$=War on Drugs) and computes the terminal capacity $O_{1971} \approx 0.019$. This constitutes an empirical validation of `eq:37`'s mathematical structure. See `eq_6_12_capacity_compounding_full.md` for the headline registry entry.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
