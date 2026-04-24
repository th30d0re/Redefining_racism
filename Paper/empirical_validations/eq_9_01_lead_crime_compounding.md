---
label: eq:9.1-lead-crime-compounding
new_label: eq:9.1-lead-crime-compounding
chapter: 9
chapter_title: "The Recompile: COINTELPRO, the Variable Swap, and the War on Drugs (1968--1994)"
line: 5153
statement: |
  O_{t+1}^{\text{capacity}} = O_t^{\text{capacity}} \cdot (1 - \alpha_{P_{\text{lead}}})
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "The Lead-Crime Nexus and Spatial Concentration"
phase3_headline: true
target_events: 
  - "Lead gasoline phase-out 1970–1986 and crime decline 1990–2010"
data_sources: 
  - {name: Reyes (2007) — Environmental Policy as Social Policy, type: "peer-reviewed", url: "https://doi.org/10.3386/w12417"}
  - {name: "Aizer & Currie (2019) — Lead and Juvenile Delinquency", type: "peer-reviewed", url: "https://doi.org/10.1257/app.20180026"}
difficulty: M
notebook: "Paper/scripts/eq47_51_lead_crime.ipynb"
data_file: "Paper/data/eq47_51_lead_crime_reyes.csv, Paper/data/eq47_51_lead_crime_aizer.csv, Paper/data/eq47_51_lead_crime_highway.csv"
figure: "Paper/figures/eq47_51_lead_crime.png"
case_study_line: 6344
bib_keys: [reyes2007, aizer_currie, rothstein, mapping_inequality]
falsification: "Falsified if Reyes (2007) blood-lead time-series fails to predict crime-rate decline after 20-year lag in multivariate regression."
---

# Notes

**Description**: Lead-crime compounding: O^capacity(t) reduced by P_lead policy variable in compounding chain

**Equation**: `eq:47` — Chapter 9, equation 1 in chapter (line 5153 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**CS9 (canonical for tract-level replication)**: For equations in the 9.1--9.10 lead-crime and spatial-concentration family, **CS9** (Spatial Confluence, `cs:spatial_confluence`, this registry's companion file `eq_9_10_highway_lead_spatial_concentration.md`, notebook `eq47_51_spatial_overlay.ipynb`) is the **canonical** tract-level replication target. **CS7** remains the **historical, national** block (Reyes, Aizer--Currie, three-panel figure, `eq47_51_lead_crime.ipynb` / `eq47_51_lead_crime.png`). CS7 is not duplicated by CS9; it provides literature-scale evidence while CS9 operationalizes the multi-layer operator at census-tract resolution when `fetch_spatial_data.py` + `make empirical` are run.

**Standalone paper**: The CS9 analysis is developed as a standalone manuscript at `Paper/standalone/spatial_confluence_draft.md` (targeting *Environmental Research* / *Social Science & Medicine* / *PNAS Nexus*).

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
