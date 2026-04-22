---
label: eq:8.14-net-solidarity-signal
new_label: eq:8.14-net-solidarity-signal
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 4370
statement: |
  S_{\text{total}}(t) = S_{\text{class}}(t) + \sum_{k=1}^{K} A_k(t)\sin(2\pi f_k t + \varphi_k) + \eta(t)
type: structural
tier: 1
status: complete
existing_case_study: true
phase3_headline: false
target_events:
  - "Total political-attention variance decomposition (2004–2024 Google Trends; 1965–2024 Congressional Record)"
  - "Rolling Parseval conservation test: CV(P_total) < 0.30 in both datasets"
  - "Stacked band-power decomposition: P_class + P_id + P_noise across rolling windows"
data_sources:
  - {name: Google Trends, type: "public-dataset", url: "https://trends.google.com/"}
  - {name: GovInfo Congressional Record, type: "public-dataset", url: "https://www.govinfo.gov/app/collection/crec"}
  - {name: ANES Cumulative Data File, type: "public-dataset", url: "https://electionstudies.org/"}
  - {name: "GDELT Global Knowledge Graph v2 (BigQuery public dataset)", type: "public-dataset", url: "https://console.cloud.google.com/bigquery?p=gdelt-bq"}
  - {name: "Internet Archive SCOTUS PDFs (55 opinions, 1873–2018)", type: "public-dataset", url: "https://archive.org/details/usscourt"}
difficulty: M
notebook: "eq40_45_interference_engine.ipynb"
case_study_line: 4968
falsification: "Falsified if net solidarity signal cannot be measured as distinct from identity-axis signals in political-attention time series."
---

# Notes

**Description**: Net class-solidarity signal S_class = Re[∑_j A_j exp(i(2πf_class t + Φ_j))]

**Equation**: `eq:42` — Chapter 8, equation 14 in chapter (line 4370 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
