---
label: eq:8.17-circular-dispersion-operator
new_label: eq:8.17-circular-dispersion-operator
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 4482
statement: |
  \overline{e^{i\Phi}} = \frac{1}{N}\sum_{j=1}^{N} e^{i\Phi_j}, \qquad
  \Phi_{\text{load}}(t) = 1 - \left|\,\overline{e^{i\Phi}}\,\right| \in [0,1]
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events:
  - "Rolling Φ_load estimation (1948–2020): 8-yr centered mean from ANES solidarity proxy"
  - "Step increase 1948–1964 → 1965–1980: +0.136 (+174%)"
  - "Φ_load era means: 0.078 (pre) → 0.214 (activation) → 0.403 (post)"
  - "Identity fragmentation correlated with multi-axis activation events (STOP ERA, Moral Majority)"
data_sources:
  - {name: "ANES Time Series — cross-group solidarity items", type: "public-dataset", url: "https://electionstudies.org/"}
  - {name: Google Trends, type: "public-dataset", url: "https://trends.google.com/"}
  - {name: "Mardia & Jupp (2000) Directional Statistics", type: "reference", url: ""}
  - {name: "GDELT Global Knowledge Graph v2 (BigQuery public dataset)", type: "public-dataset", url: "https://console.cloud.google.com/bigquery?p=gdelt-bq"}
difficulty: M
notebook: "eq40_45_interference_engine.ipynb"
case_study_line: 4968
falsification: "Falsified if circular dispersion of phase values fails to predict cross-group political mobilization in ANES solidarity data. Operationalized: falsified if Φ_load does not show a positive step increase during 1965–1980."
---

# Notes

**Description**: Circular dispersion operator Φ_load = 1 − |R̄| where R̄ = (1/N)∑exp(iΦ_j) — directional-statistics measure

**Equation**: `eq:45` — Chapter 8, equation 17 in chapter (line 4482 in manuscript)

**Classification rationale**: Type=quantitative, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
