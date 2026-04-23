---
label: eq:12.3-judiciary-discrimination-detection
new_label: eq:12.3-judiciary-discrimination-detection
chapter: 12
chapter_title: "The Contradiction: Why Reform Serves the Algorithm"
line: 8017
statement: |
  D(P) = 
  1 & \text{if } P \text{ explicitly invokes racial classification} \\
  0 & \text{if } P \text{ uses proxy variable } x \text{ where } \operatorname{Corr}(x, \text{race}) \to 1
type: structural
tier: 3
status: complete
existing_case_study: true
phase3_headline: false
target_events: 
  - Washington v. Davis (1976) — intent standard
  - McCleskey v. Kemp (1987) — statistical evidence rejected
data_sources: 
  - {name: Washington v. Davis, 426 U.S. 229 (1976), type: "primary-source", url: ""}
  - {name: McCleskey v. Kemp, 481 U.S. 279 (1987), type: "primary-source", url: ""}
difficulty: S
notebook: ""
case_study_line: 9071
falsification: Falsified if judicial detection function produces false positives for proxy discrimination at rates comparable to explicit discrimination.
---

# Notes

**Description**: Judiciary detection function: probability of detecting racial discrimination as function of explicitness

**Equation**: `eq:71` — Chapter 12, equation 3 in chapter (line 8017 in manuscript)

**Classification rationale**: Type=structural, Tier=3 assigned based on mathematical structure and data availability.

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
