---
label: eq:8.12-class-alignment-base-waves
new_label: eq:8.12-class-alignment-base-waves
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 4359
statement: |
  S_{\text{class}}(t) = A_{\text{class}}(t)\,\sin\bigl(2\pi f_{\text{class}}\,t + \varphi_{\text{class}}\bigr)
type: structural
tier: 1
status: complete
existing_case_study: true
phase3_headline: true
target_events:
  - "Google Trends class-signal index (2004–2024)"
  - "Congressional Record class-word frequency (1965–2024)"
  - "ANES economic-salience item (1948–2020)"
  - "GDELT GKG per-axis theme coverage (1979–2024, monthly)"
  - "SCOTUS corpus class-language share trend (1873–2018, 55 opinions)"
  - "Parseval conservation rolling-window test (10-yr GT, 20-yr CR)"
  - "Shock time-constant sequence 1865–2020 (log-space OLS, two-segment model)"
data_sources:
  - {name: Google Trends, type: "public-dataset", url: "https://trends.google.com/"}
  - {name: GovInfo Congressional Record, type: "public-dataset", url: "https://www.govinfo.gov/app/collection/crec"}
  - {name: ANES Cumulative Data File, type: "public-dataset", url: "https://electionstudies.org/"}
  - {name: "Historical backlash proxies (Foner 1988, Trelease 1971, Carter 1996, SPLC/ADL)", type: "secondary-dataset", url: ""}
  - {name: "GDELT Global Knowledge Graph v2 (BigQuery public dataset)", type: "public-dataset", url: "https://console.cloud.google.com/bigquery?p=gdelt-bq"}
  - {name: "Internet Archive SCOTUS PDFs (55 opinions, 1873–2018)", type: "public-dataset", url: "https://archive.org/details/usscourt"}
difficulty: M
notebook: "eq40_45_interference_engine.ipynb"
case_study_line: 4968
falsification: "Falsified if class alignment signal is not measurable as a distinct frequency in ANES or Congressional Record political-attention data."
---

# Notes

**Description**: Base class-alignment waves for I_buffer and O_racialized at shared frequency f_class

**Equation**: `eq:40` — Chapter 8, equation 12 in chapter (line 4359 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
