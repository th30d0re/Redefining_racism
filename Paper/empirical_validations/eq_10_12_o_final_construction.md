---
label: eq:10.12-o-final-construction
new_label: eq:10.12-o-final-construction
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: 6601
statement: |
  O_{\text{final}} = \text{Everyone} \setminus E
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "Mass Incarceration and the Expanding Out-Group"
phase3_headline: true
target_events: 
  - US mass incarceration 1994–present
data_sources: 
  - {name: Bureau of Justice Statistics incarceration by race series, type: "public-dataset", url: "https://www.bjs.gov/"}
  - {name: The Sentencing Project — Racial Disparity Reports, type: report, url: "https://www.sentencingproject.org/"}
  - {name: Alexander (2010) — The New Jim Crow, type: "peer-reviewed", url: ""}
difficulty: M
notebook: "Paper/scripts/eq63_mass_incarceration.ipynb"
data_file: "Paper/data/eq63_mass_incarceration.csv"
figure: "Paper/figures/eq63_mass_incarceration.png"
case_study_line: 6828
bib_keys: [bjs_incarceration_race, sentencing_project, alexander, pfaff_2017]
falsification: "Falsified if modern mass-incarceration demographics fail to reproduce the O set construction predicted by the algorithm."
---

# Notes

**Description**: O_final set construction: modern mass-incarceration demographics reproduce 1676 out-group definition

**Equation**: `eq:63` — Chapter 10, equation 12 in chapter (line 6601 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
