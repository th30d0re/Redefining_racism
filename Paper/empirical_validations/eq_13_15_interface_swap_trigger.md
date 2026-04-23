---
label: eq:13.15-interface-swap-trigger
new_label: eq:13.15-interface-swap-trigger
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: ~10200
statement: |
  D_{\text{sovereign}}(t) > \bar{D} \quad \Longrightarrow \quad P_{\text{uppet}} \;\text{executes}\; \mathrm{SWAP}\bigl(\mathcal{A}_{\text{old}} \to \mathcal{A}_{\text{new}}\bigr)
type: quantitative
tier: 1
status: complete
existing_case_study: true
phase3_headline: true
target_events:
  - "1933: Classical gold standard architecture; deflationary crisis forcing swap"
  - "1944: Bretton Woods compilation replacing fragmented colonial blocs"
  - "1971: Dollar-gold peg; cover ratio collapse to 22% triggers Nixon Shock"
data_sources:
  - {name: "Federal Reserve H.4.1: Historical Gold Stock Data (1945-present)", type: "primary", url: "https://www.federalreserve.gov/releases/h41/"}
  - {name: "FRED: Foreign-Held US Treasury Securities (FDHBFIN)", type: "primary", url: "https://fred.stlouisfed.org/series/FDHBFIN"}
  - {name: "Bordo & Eichengreen 1993 (A Retrospective on the Bretton Woods System)", type: "peer-reviewed", url: ""}
  - {name: "Bordo & Irwin NBER WP 17749 (Nixon Shock retrospective)", type: "peer-reviewed", url: "https://www.nber.org/papers/w17749"}
difficulty: M
notebook: "eq13_15_17_nixon_cover_ratio.ipynb"
case_study_line: ~10280
falsification: "Falsified if the gold-cover ratio was still above 80% at the time of the Nixon Shock (August 1971) — which would indicate the decoupling was strategically elective rather than architecturally forced by D_sovereign > D-bar. Documented: cover ratio was ~22% in July 1971, well below any plausible D-bar threshold. For 1933: falsified if gold-clause enforcement would not have caused a debt crisis (i.e., if the debt/GDP trajectory was sustainable without nullification). Historical record confirms it was not."
---

# Notes

**Description**: The Interface Swap trigger condition — the formal threshold at which accumulated $X_{\text{temporal}}$ debt ($D_{\text{sovereign}}$) exceeds the architecture's stability constraint $\bar{D}$, forcing $P_{\text{uppet}}$ to execute a controlled demolition of the failing architecture and reboot onto a new substrate.

**Primary test case (Case Study 4)**: Nixon Shock 1971.
- 1949 cover ratio: ~175% (US gold reserves well exceed foreign dollar claims)
- 1956 cover ratio: ~134% (shortfall of $6.5B in free gold emerging)
- 1965 cover ratio: falls below 100% for the first time; De Gaulle demands conversion
- July 1971: cover ratio = ~22%; UK requests conversion of $3B
- August 15, 1971: Nixon unilaterally suspends convertibility

**Relationship to existing equations**:
- $D_{\text{sovereign}}$ is the primary output of Eq. 10.15-10.17 ($X_{\text{temporal}}$ accumulation).
- The swap trigger activates the Polymorphic Reboot Operator (Eq. 13.16).
- The 1933 swap was triggered by the deflation paradox: gold clauses made real debt unpayable ($\bar{D}$ enforced by price dynamics rather than nominal accumulation).
- The 1944 swap was triggered by the geopolitical architecture's instability (WWII kinetic event), not by $D_{\text{sovereign}}$ alone.

**Figure**: `Paper/figures/eq13_15_17_cover_ratio_collapse.png`

**Next steps**:
- [x] Verify LaTeX statement matches manuscript
- [x] Notebook built: eq13_15_17_nixon_cover_ratio.ipynb
- [x] Case study written in manuscript (cs:nixon_cover)
