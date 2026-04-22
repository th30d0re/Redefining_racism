---
label: eq:8.13-subgroup-compound-phase
new_label: eq:8.13-subgroup-compound-phase
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 4366
statement: |
  S_{\text{id}}(t) = \sum_{k=1}^{K} A_k(t)\,\sin\bigl(2\pi f_k\,t + \varphi_k\bigr)
type: structural
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events:
  - "Identity-axis frequency decomposition across race/gender/religion proxies (2004–2024)"
  - "Aggregate identity-band dominant period: ~2.1 yr (GT), ~2.5 yr (CR)"
  - "GDELT per-axis PSD: per-axis dominant periods and distinctness test (1979–2024)"
  - "SCOTUS Lomb-Scargle: per-axis dominant periods across 145-year institutional corpus"
  - "SCOTUS majority vs. dissent class-language divergence"
data_sources:
  - {name: Google Trends, type: "public-dataset", url: "https://trends.google.com/"}
  - {name: GovInfo Congressional Record, type: "public-dataset", url: "https://www.govinfo.gov/app/collection/crec"}
  - {name: "GDELT Global Knowledge Graph v2 (BigQuery public dataset)", type: "public-dataset", url: "https://console.cloud.google.com/bigquery?p=gdelt-bq"}
  - {name: "Internet Archive SCOTUS PDFs (55 opinions, 1873–2018)", type: "public-dataset", url: "https://archive.org/details/usscourt"}
difficulty: M
notebook: "eq40_45_interference_engine.ipynb"
case_study_line: 4968
falsification: "Falsified if compound phase Φ_j fails to predict subgroup political alignment in ANES cross-tabulation data. When per-axis basket data becomes available: falsified if per-axis dominant periods cluster at a single f rather than distinct f_k values."
---

# Notes

**Description**: Compound phase Φ_j = ∑_k φ_{k,j} — subgroup j's cumulative phase shift across identity axes k

**Equation**: `eq:41` — Chapter 8, equation 13 in chapter (line 4366 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
- [x] GDELT per-axis PSD analysis implemented in eq40_45_interference_engine.ipynb Section B
- [x] SCOTUS Lomb-Scargle analysis implemented in scotus_corpus_analysis.ipynb Analysis 2
