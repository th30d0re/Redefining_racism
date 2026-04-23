---
label: eq:10.14-kinetic-power-distribution
new_label: eq:10.14-kinetic-power-distribution
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: 6792
statement: |
  \text{Kinetic}(I_{\text{buffer}} \cup O_{\text{racialized}} \setminus O_{\text{incarcerated}}) \gg \text{Kinetic}(F_{\text{enforce}} \cup E)
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - Contemporary US gun ownership by occupation/race
data_sources: 
  - {name: Pew Research Center — Gun Ownership Survey 2017, type: "public-dataset", url: "https://www.pewresearch.org/social-trends/2017/06/22/americas-complex-relationship-with-guns/"}
difficulty: M
notebook: ""
case_study_line: 7768
falsification: "Falsified if kinetic power is not concentrated in F_enforce as a proportion of total non-Elite capacity."
---

# Notes

**Description**: Total kinetic power of non-Elite: P_total = P_F_enforce + P_I_buffer + P_O — distribution across tiers

**Equation**: `eq:64` — Chapter 10, equation 14 in chapter (line 6792 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
