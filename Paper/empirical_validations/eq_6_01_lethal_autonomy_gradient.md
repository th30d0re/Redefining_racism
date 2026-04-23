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
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - LEOSA statutory analysis (18 U.S.C. §926B)
  - Mulford Act (1967) — disarmament of Black Panthers
  - Sullivan Law (1911) — discretionary licensing
data_sources: 
  - {name: "LEOSA — 18 U.S.C. §926B statutory text", type: "legislation", url: ""}
  - {name: Mulford Act (1967) — California Assembly Bill 1591, type: "legislation", url: ""}
  - {name: Sullivan Law (1911 N.Y. Laws ch. 195), type: "legislation", url: ""}
  - {name: "Mapping Police Violence (MPV) — police killings database by race", type: "database", url: "https://mappingpoliceviolence.org/"}
  - {name: "Fatal Encounters — national database of deaths during police interactions", type: "database", url: "https://fatalencounters.org/"}
difficulty: M
notebook: ""
case_study_line: ~2889
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
