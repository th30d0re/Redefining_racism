---
label: eq:13.9-infeasible-constraint-set
new_label: eq:13.9-infeasible-constraint-set
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: 8771
statement: |
  \nexists\; S:\quad \mathcal{E}(S) > 0 \;\;\wedge\;\; \mathcal{L}(S) = \text{valid} \quad \text{when } F^* > F^L
type: structural
tier: 3
status: complete
existing_case_study: false
phase3_headline: false
target_events: 
  - "US failure at Môle Saint-Nicolas 1891"
data_sources: []
difficulty: S
notebook: ""
case_study_line: 10075
falsification: Falsified if E_global achieves both extraction success and legitimation validity simultaneously under Firmin conditions.
---

# Notes

**Description**: Infeasible constraint set: no strategy S with E(S)>0 AND L(S)=valid when Firmin conditions hold

**Equation**: `eq:86` — Chapter 13, equation 9 in chapter (line 8771 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
