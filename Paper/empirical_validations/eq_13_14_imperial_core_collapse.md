---
label: eq:13.14-imperial-core-collapse
new_label: eq:13.14-imperial-core-collapse
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: 8888
statement: |
  \text{Either} \quad F_{\text{enforce}}^{\text{global}} \rightarrow 0 \quad \text{or} \quad O_{\text{bloc}}^{\text{capacity}}(t) > \tau_{\text{sovereign}} \;\;\forall\; t
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "Imperial Core Collapse — China, OPEC, and the Asian Tigers"
phase3_headline: true
target_events: 
  - China WTO entry 2001 (capacity trajectory 1978–2024)
  - OPEC oil embargo 1973 (peak disruption; petrodollar containment 1974–1975)
  - Asian financial crisis 1997 and IMF response
  - South Korea, Taiwan, Singapore developmental trajectories (1965–2024)
data_sources: 
  - {name: "World Bank Development Indicators — GDP trajectory for rising economies", type: "public-dataset", url: "https://data.worldbank.org/"}
  - {name: "SIPRI Military Expenditure Database", type: "public-dataset", url: "https://www.sipri.org/databases/milex"}
  - {name: "IMF historical lending and conditionality data", type: "public-dataset", url: "https://www.imf.org/en/Data"}
  - {name: "Naughton (2007) The Chinese Economy", type: "peer-reviewed", url: ""}
  - {name: "Yergin (2011) The Quest", type: "peer-reviewed", url: ""}
  - {name: "Amsden (1989) Asia's Next Giant", type: "peer-reviewed", url: ""}
  - {name: "Acemoglu & Robinson (2012) — Why Nations Fail", type: "peer-reviewed", url: ""}
difficulty: L
notebook: "Paper/scripts/eq91_imperial_core_collapse.ipynb"
data_file: "Paper/data/eq91_imperial_core_collapse.csv"
figure: "Paper/figures/eq91_imperial_core_collapse.png"
case_study_line: 9208
bib_keys: [world_bank_wdi, sipri_milex, naughton2007, yergin2011, amsden1989, acemoglu_robinson]
falsification: Falsified if documented rising powers (China, OPEC, Asian Tigers) achieved core status without triggering debt/sanction/military responses from incumbent core.
---

# Notes

**Description**: Imperial core collapse condition: rising O_global challenges extraction ceiling — liberation requires kinetic or structural parity

**Equation**: `eq:91` — Chapter 13, equation 14 in chapter (line 8888 in manuscript)

**Result**: China crosses τ_sovereign (0.60) around 2015; reaches 0.68 by 2024. Containment response escalating (chip embargo, TSMC restrictions, QUAD). OPEC peaks at 0.49 (1973) — below threshold; contained within 24 months via petrodollar recycling. Asian Tigers structurally below τ_sovereign across all dimensions (range: 0.22–0.52). Condition 1 (F_enforce^global → 0): no historical instance. CONFIRMED.
