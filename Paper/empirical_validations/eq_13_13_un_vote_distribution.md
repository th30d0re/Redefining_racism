---
label: eq:13.13-un-vote-distribution
new_label: eq:13.13-un-vote-distribution
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: 8854
statement: |
  \text{Vote}_{\text{UN}}(x) =  \text{No} & \text{if } x \in E_{\text{imperial}} \\[4pt] \text{Abstain} & \text{if } x \in I_{\text{buffer}}^{\text{global}} \\[4pt] \text{Yes} & \text{if } x \in O_{\text{global}}
type: structural
tier: 3
status: pending
existing_case_study: false
phase3_headline: false
target_events: 
  - UN Security Council voting patterns on Haiti resolutions
data_sources: 
  - {name: UN Digital Library — UNSC vote records, type: "public-dataset", url: "https://digitallibrary.un.org/"}
difficulty: S
notebook: ""
case_study_line: null
falsification: "Falsified if UN Security Council voting distribution fails to map onto the international 5-tier hierarchy."
---

# Notes

**Description**: UN vote distribution maps onto international 5-tier hierarchy with mathematical precision

**Equation**: `eq:90` — Chapter 13, equation 13 in chapter (line 8854 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
