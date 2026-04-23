---
label: eq:13.16-polymorphic-reboot-operator
new_label: eq:13.16-polymorphic-reboot-operator
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: ~10210
statement: |
  \mathcal{A}_{\text{old}} \;\xrightarrow{\;P_{\text{uppet}}\;}\; \mathcal{A}_{\text{new}} \quad \text{subject to} \quad \mathrm{Assets}(E,\, \mathcal{A}_{\text{new}}) \;\geq\; \mathrm{Assets}(E,\, \mathcal{A}_{\text{old}})
type: structural
tier: 2
status: complete
existing_case_study: true
phase3_headline: false
target_events:
  - "1933-1935: A_old = classical gold standard; A_new = Federal Reserve fiat (domestic)"
  - "1944: A_old = fragmented colonial blocs; A_new = dollar hegemony + IMF/World Bank"
  - "1971: A_old = dollar-gold peg (Bretton Woods); A_new = global floating fiat"
data_sources:
  - {name: "Gowa 1983 (Closing the Gold Window)", type: "peer-reviewed book", url: ""}
  - {name: "Bordo & Eichengreen 1993", type: "peer-reviewed", url: ""}
  - {name: "Perry v. United States, 294 U.S. 330 (1935)", type: "legal", url: ""}
  - {name: "WID.world: Top-0.1% US and UK Wealth Shares (1913-present)", type: "peer-reviewed", url: "https://wid.world/"}
difficulty: H
notebook: "eq13_16_interface_swap_matrix.ipynb"
case_study_line: ~10310
falsification: "Falsified if Assets(E, A_new) < Assets(E, A_old) across any of the three documented swap events — i.e., if E's asset base declined permanently following any Interface Swap. Case Study 5 tests this directly using WID top-0.1% wealth share. The only documented temporary decline (1929-1933 Depression trough) preceded and motivated the 1933 swap; post-swap recovery to 22.4% (1940) confirms Assets(E, A_new) > Assets(E, A_old)."
---

# Notes

**Description**: The Polymorphic Reboot Operator — the transition function that maps a failing extraction architecture $\mathcal{A}_{\text{old}}$ to a new one $\mathcal{A}_{\text{new}}$ under $P_{\text{uppet}}$ direction, subject to the hard constraint that $E$'s asset base is preserved or expanded. This is the formal mathematical statement of why Interface Swaps are not system failures but system upgrades.

**Classification rationale**: Type=structural (the operator is a formal transition function); Tier=2 (the historical case studies validate the transition qualitatively; the quantitative $\Delta_E \geq 0$ test in Eq. 13.17 is Tier=1 via WID data). The operator itself is definitional; its validation is through Case Study 5.

**Key feature — law-breaking as kernel function**: In all three historical instances, the reboot operator required $P_{\text{uppet}}$ to break established law:
- 1933: EO 6102 (confiscation), Congressional nullification of gold clauses (contract law), Perry v. US (Supreme Court retreat)
- 1944: Dismantling of British Imperial Preference treaties
- 1971: Unilateral suspension of Bretton Woods gold convertibility commitment

This is not incidental but constitutive: the reboot operator can only function by overriding the legal architecture that protected $I_{\text{buffer}}$'s claims on the old system. Law is the interface; the kernel is the extraction function.

**Relationship to existing equations**:
- Eq. 13.16 generalizes the Interface Swap concept already introduced in Ch.1 (Eq. 1.6-1.7) to the macrofinancial domain.
- The output $\mathcal{A}_{\text{new}}$ of each historical swap becomes the $\mathcal{A}_{\text{old}}$ input for the next swap, creating a sequential upgrade chain: gold standard → Bretton Woods → floating fiat.
- Each swap increases the capacity of $X_{\text{temporal}}$ (Eq. 10.15): floating fiat provides maximum $D_{\text{sovereign}}$ scaling.

**Next steps**:
- [x] Verify LaTeX statement matches manuscript
- [x] Notebook built: eq13_16_interface_swap_matrix.ipynb
- [x] Three historical case studies written in manuscript
- [x] Interface Swap Matrix table (Table 13.x) written
