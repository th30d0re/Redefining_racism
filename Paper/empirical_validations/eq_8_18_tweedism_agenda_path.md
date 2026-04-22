---
label: eq:8.18-tweedism-agenda-path
new_label: eq:8.18-tweedism-agenda-path
chapter: 8
chapter_title: "Tweedism and the Puppet Class: The Algorithmic Filter on Democracy"
line: 4680
statement: |
  x_0 \rightarrow x_1 \rightarrow x_2 \rightarrow \cdots \rightarrow x_m
type: quantitative
tier: 1
status: complete
existing_case_study: true
case_study_title: "Gilens-Page and the Agenda-Setting Path"
phase3_headline: true
target_events: 
  - "Gilens-Page 1,779 policy votes 1981–2002"
data_sources: 
  - {name: "Gilens & Page (2014) — Testing Theories of American Politics", type: "peer-reviewed", url: "https://doi.org/10.1017/S1537592714001595"}
  - {name: Gilens (2012) — Affluence and Influence, type: "peer-reviewed", url: ""}
difficulty: M
notebook: "Paper/scripts/eq46_gilens_page.ipynb"
data_file: "Paper/data/eq46_gilens_page.csv"
figure: "Paper/figures/eq46_gilens_page.png"
case_study_line: 4844
bib_keys: [gilens, gilens_book]
falsification: "Falsified if Gilens-Page analysis shows median voter preferences predict policy outcomes as strongly as top-quintile preferences."
---

# Notes

**Description**: Tweedism agenda path: P_uppet sequences votes from x_0 toward x* moving terminal policy away from class-optimal

**Equation**: `eq:46` — Chapter 8, equation 18 in chapter (line 4680 in manuscript)

**Classification rationale**: Phase 3 headline — full quantitative case study target.

**Next steps**:
- [x] Verify LaTeX statement above matches manuscript
- [x] Confirm target_events and data_sources
- [x] Write falsification criterion (if placeholder)
- [x] Set `status: in_progress` when case study work begins
- [x] Set `status: complete` and populate `case_study_line` when done
