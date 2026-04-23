---
label: eq:13.17-elite-asset-continuity-invariant
new_label: eq:13.17-elite-asset-continuity-invariant
chapter: 13
chapter_title: "The Global Containment Field: Scaling the Algorithm"
line: ~10215
statement: |
  \forall\; \mathrm{SWAP} : \quad \Delta_E \geq 0, \quad \text{where} \quad \Delta_E = \mathrm{Assets}(E,\, \mathcal{A}_{\text{new}}) - \mathrm{Assets}(E,\, \mathcal{A}_{\text{old}})
type: quantitative
tier: 1
status: complete
existing_case_study: true
phase3_headline: true
target_events:
  - "1933-1940: Top-0.1% dips 1929-1933; recovers to 22.4% by 1940 (post-swap)"
  - "1944-1955: US top-0.1% rises from 10.3% to 13.2%; UK declines (architecture transfer)"
  - "1971-2024: Top-0.1% rises monotonically from 7.1% to 18.5%"
data_sources:
  - {name: "WID.world: Top-0.1% US Wealth Share 1913-present (Piketty-Saez-Zucman)", type: "peer-reviewed", url: "https://wid.world/country/usa/"}
  - {name: "WID.world: Top-0.1% UK Income Share 1913-present", type: "peer-reviewed", url: "https://wid.world/country/gb/"}
  - {name: "WID.world: Top-0.1% French Wealth Share (1944 context)", type: "peer-reviewed", url: "https://wid.world/country/fr/"}
  - {name: "Piketty-Saez-Zucman 2018 (QJE)", type: "peer-reviewed", url: "https://doi.org/10.1093/qje/qjx043"}
difficulty: L
notebook: "eq13_16_interface_swap_matrix.ipynb"
case_study_line: ~10320
falsification: "Falsified if the top-0.1% US wealth share declines STRUCTURALLY (> 3 percentage points, sustained > 5 years without subsequent recovery) across any of the three swap windows. Three independent tests: (1) 1933-1940 window; (2) 1944-1955 window; (3) 1971-1985 window. Condition not met in any window: (1) Depression trough recovers fully by 1940; (2) US top-0.1% rises; (3) top-0.1% rises monotonically to present. The $Delta_E geq 0$ invariant holds in all three independent tests."
---

# Notes

**Description**: The Elite Asset Continuity Invariant — the hard mathematical constraint that defines every Polymorphic Interface Swap: across every architectural reboot, $E$'s aggregate asset base must be preserved or expanded. The liabilities liquidated to fund the swap are sourced entirely from $I_{\text{buffer}}$ (nominal bond holdings, savings, pension accounts) and $O$ (labor obligations, public services), never from $E$'s hard-asset base.

**This is the capstone equation of the Interface Swap Typology** — the claim that unifies all three historical proofs into a single invariant. It is the macrofinancial equivalent of the existing $\Delta\max = 0$ invariant (Eq. 10.5, kernel objective), extending the non-decreasing elite-extraction claim from the domestic annual level to the generational architectural-reboot level.

**Numerical results (Case Study 5)**:
- **1933-1940 window**: Top-0.1% dips from 21.3% (1929) to 18.1% (1933, Depression trough); recovers to 22.4% (1940, exceeding pre-Depression level). Median wealth declines and does not recover to equivalent real purchasing power until late 1940s. $\Delta_E > 0$.
- **1944-1955 window**: US top-0.1% rises from 10.3% to 13.2%. UK top-0.1% declines as Imperial Preference dismantled (architecture transfer from British to American elite). Global $\Delta_E > 0$ for the dominant architecture holder.
- **1971-2024 window**: Top-0.1% rises monotonically from 7.1% to 18.5% (161% increase over 53 years). No reversal > 3 pp sustained > 5 years. $\Delta_E \gg 0$.

**Classification rationale**: Type=quantitative; Tier=1 (WID.world is a continuously maintained, peer-reviewed distributional accounting database with annual observations spanning 111 years of US data; independently replicated across multiple research teams).

**Relationship to existing equations**:
- Eq. 13.17 is the inter-epoch analogue of $\Delta\max = 0$ (Eq. 10.5): both state that $E$'s extraction share is preserved across every system adaptation.
- Together, Eq. 10.5 and Eq. 13.17 form a complete two-level invariant: within each architectural epoch ($\Delta\max = 0$) and across architectural reboots ($\Delta_E \geq 0$).
- The Perry v. US judicial retreat is the legal mechanism by which the 1933 $\Delta_E \geq 0$ was enforced: the court acknowledged illegality but denied remedy, ensuring E bore no net loss from the swap.

**Figure**: `Paper/figures/eq13_16_top01_across_swaps.png` (3-panel faceted figure)

**Next steps**:
- [x] Verify LaTeX statement matches manuscript
- [x] Notebook built: eq13_16_interface_swap_matrix.ipynb
- [x] Case study written in manuscript (cs:delta_e_invariant)
- [x] Figure referenced in manuscript
