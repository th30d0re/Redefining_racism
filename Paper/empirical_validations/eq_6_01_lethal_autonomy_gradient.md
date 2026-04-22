---
label: eq:6.1-lethal-autonomy-gradient
new_label: eq:6.1-lethal-autonomy-gradient
chapter: 6
chapter_title: "The Enforcement Engine: Slave Patrols, the 13th Amendment, and the Compounding Model (1704--1865)"
line: 2762
statement: |
  \text{Lethal Autonomy}(F_{\text{enforce}}) \gg \text{Lethal Autonomy}(I_{\text{buffer}}) \gg \text{Lethal Autonomy}(O) = 0
type: quantitative
tier: 2
status: pending
existing_case_study: false
phase3_headline: false
target_events: 
  - Police killings 2013–2024
  - LEOSA statutory analysis
data_sources: 
  - {name: Mapping Police Violence database 2013–2024, type: "public-dataset", url: "https://mappingpoliceviolence.us/"}
  - {name: Fatal Encounters database, type: "public-dataset", url: "https://fatalencounters.org/"}
difficulty: M
notebook: ""
case_study_line: null
falsification: Falsified if Mapping Police Violence data shows parity in police killings per capita across racial groups after controlling for encounter rates.
---

# Notes

**Description**: Lethal Autonomy gradient: LA(F_enforce) >> LA(I_buffer) >> LA(O_racialized) = 0 — measurable via MPV killings-per-capita by racial group

**Equation**: `eq:26` — Chapter 6, equation 1 in chapter (line 2762 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
