---
label: eq:10.2-buffer-class-shrinkage
new_label: eq:10.2-buffer-class-shrinkage
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: 6192
statement: |
  I_{\text{buffer}}(t) \subset I_{\text{buffer}}(t-1) \quad \text{and} \quad O(t) \supset O(t-1)
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - "Middle-class squeeze 1973–2024"
  - Gig economy expansion 2010–2024
  - "Pew 2016: middle-income share 61% (1971) → 50% (2015)"
data_sources: 
  - {name: "Pew Research Center — America's Shrinking Middle Class", type: report, url: "https://www.pewresearch.org/social-trends/2016/05/11/americas-shrinking-middle-class-a-close-look-at-changes-within-metropolitan-areas/"}
  - {name: Federal Reserve SCF income/wealth data, type: "public-dataset", url: "https://www.federalreserve.gov/econres/scfindex.htm"}
difficulty: M
notebook: ""
case_study_line: 7055
falsification: "Falsified if Buffer Class size is shown to be expanding rather than contracting in current income-distribution data."
---

# Notes

**Description**: Buffer Class shrinks while broader O grows: dI_buffer/dt < 0 as Demographic Paradox operates

**Equation**: `eq:53` — Chapter 10, equation 2 in chapter (line 6192 in manuscript)

**Classification rationale**: Type=quantitative, Tier=2 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
