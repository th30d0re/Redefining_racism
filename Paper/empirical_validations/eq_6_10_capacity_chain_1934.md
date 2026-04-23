---
label: eq:6.10-capacity-chain-1934
new_label: eq:6.10-capacity-chain-1934
chapter: 6
chapter_title: "The Enforcement Engine: Slave Patrols, the 13th Amendment, and the Compounding Model (1704--1865)"
line: 3032
statement: |
  O_{1934}^{\text{capacity}} = O_{1865}^{\text{capacity}} \cdot (1 - \gamma\, P_{\text{redlining}})
type: quantitative
tier: 1
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - HOLC redlining 1934–1968
  - Fair Housing Act 1968
data_sources: 
  - {name: Mapping Inequality — HOLC Redlining Maps, type: "public-dataset", url: "https://dsl.richmond.edu/panorama/redlining/"}
  - {name: Rothstein (2017) — The Color of Law, type: "peer-reviewed", url: ""}
difficulty: M
notebook: "eq_hist3_redlining_capacity.ipynb"
case_study_line: ~3199
falsification: "Falsified if redlining-exposed tracts show no differential wealth accumulation decline relative to non-redlined areas in HOLC map data."
---

# Notes

**Description**: Compounding chain step 3: O_1934 = O_1865 × (1 − γ·P_redlining)

**Equation**: `eq:hist3` — Chapter 6, equation 10 in chapter (line 3032 in manuscript)

**Classification rationale**: Type=quantitative, Tier=1 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
