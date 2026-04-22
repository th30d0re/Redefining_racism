---
label: eq:6.11-capacity-chain-1971
new_label: eq:6.11-capacity-chain-1971
chapter: 6
chapter_title: "The Enforcement Engine: Slave Patrols, the 13th Amendment, and the Compounding Model (1704--1865)"
line: 3033
statement: |
  O_{1971}^{\text{capacity}} = O_{1934}^{\text{capacity}} \cdot (1 - \delta\, P_{\text{WarOnDrugs}})
type: quantitative
tier: 1
status: pending
existing_case_study: false
phase3_headline: false
target_events: 
  - War on Drugs 1971–present
  - Rockefeller Drug Laws 1973
data_sources: 
  - {name: ACLU (2020) — Cannabis Arrests Report, type: report, url: "https://www.aclu.org/report/tale-two-countries-racially-targeted-arrests-era-marijuana-reform"}
  - {name: BJS Drug Offense Incarceration Statistics, type: "public-dataset", url: "https://www.bjs.gov/"}
difficulty: M
notebook: "nb_ch06_eq11_capacity_chain_1971.ipynb"
case_study_line: null
falsification: Falsified if War on Drugs enforcement shows no differential impact on O_racialized capacity in incarceration and wealth data.
---

# Notes

**Description**: Compounding chain step 4: O_1971 = O_1934 × (1 − δ·P_WarOnDrugs)

**Equation**: `eq:hist4` — Chapter 6, equation 11 in chapter (line 3033 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
