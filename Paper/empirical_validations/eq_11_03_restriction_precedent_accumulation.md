---
label: eq:11.3-restriction-precedent-accumulation
new_label: eq:11.3-restriction-precedent-accumulation
chapter: 11
chapter_title: "The Kinetic Guarantee: Arms Asymmetry, the Second Amendment, and the Disarmament Timeline"
line: 7982
statement: |
  \mathcal{R}_{t+1} = \mathcal{R}_t \cup \{r_t\}
type: structural
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Jurisprudential Boomerang — 2A Case Law as Target Expansion (1911–2024)"
phase3_headline: false
target_events:
  - All 16 events (1911–2024), three classes: legislation, ATF admin rules, SCOTUS rulings
  - Federal legislation count (Acts of Congress): monotonically non-decreasing floor, currently 4 (NFA, GCA, Hughes, Brady)
  - Net restriction count: two-directional arc — peaks at 7 (1994), dips to 4 (post-Bruen 2022), rises to 6 (2024)
data_sources:
  - {name: "Primary legislation and ruling texts (11 events)", type: "primary-source", url: ""}
difficulty: M
notebook: "Paper/scripts/eq65_68_2a_case_law.ipynb"
data_file: "Paper/data/eq65_68_2a_case_law.csv"
figure:
  - "Paper/figures/eq65_68_fig_a_legislation.png"
  - "Paper/figures/eq65_68_fig_b_net_restriction.png"
  - "Paper/figures/eq65_68_2a_case_law.png"
case_study_line: 7992
bib_keys: [sullivanlaw, nfa1934, mulford1967, gca1968, hughes1986, brady1993, awb1994, heller, mcdonald, bruen, rahimi2024]
falsification: "Falsified if any documented legislative or ruling event reduced cumulative restriction precedent count."
---

# Notes

**Description**: Restriction precedent accumulation: each event deposits r_t into doctrine; R_t monotonically non-decreasing

**Equation**: `eq:67` — Chapter 11, equation 3 in chapter (line 7982 in manuscript)

**Result**: 16 events (1911–2024). Federal legislation floor R_t = 4 active Acts of Congress; monotonically non-decreasing within the legislative sub-path (AWB lapse is the AWB's own sunset clause, not a repeal of NFA/GCA/Hughes/Brady). Net restriction count = 6 terminal (2024). ATF administrative rules add 3 new events (2018, 2022, 2023) demonstrating the boomerang's executive mechanism — doctrinal apparatus built for O_racialized management repurposed against I_buffer without congressional action.
