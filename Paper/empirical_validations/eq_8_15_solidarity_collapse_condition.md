---
label: eq:8.15-solidarity-collapse-condition
new_label: eq:8.15-solidarity-collapse-condition
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 4375
statement: |
  P_{\text{class}}(t) = \int_{f^{-}_{\text{class}}}^{f^{+}_{\text{class}}} |\hat{S}_{\text{total}}(f,t)|^2\,df > \tau
type: structural
tier: 1
status: complete
existing_case_study: true
phase3_headline: false
target_events:
  - "Integrated class-band PSD from Google Trends (2004–2024)"
  - "Integrated class-band PSD from Congressional Record (1965–2024)"
  - "Parseval conservation test confirms P_class + P_id + P_noise ≈ const"
data_sources:
  - {name: Google Trends, type: "public-dataset", url: "https://trends.google.com/"}
  - {name: GovInfo Congressional Record, type: "public-dataset", url: "https://www.govinfo.gov/app/collection/crec"}
  - {name: "GDELT Global Knowledge Graph v2 (BigQuery public dataset)", type: "public-dataset", url: "https://console.cloud.google.com/bigquery?p=gdelt-bq"}
difficulty: S
notebook: "eq40_45_interference_engine.ipynb"
case_study_line: 4968
falsification: "Falsified if M(t) remains above τ even when S_class approaches zero across all subgroups simultaneously. Operationalized: falsified if CV(P_total) > 0.30 in both datasets."
---

# Notes

**Description**: Collapse condition: S_class → 0 when ∑_j A_j exp(iΦ_j) → 0 — solidarity collapses under maximum dispersion

**Equation**: `eq:43` — Chapter 8, equation 15 in chapter (line 4375 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
