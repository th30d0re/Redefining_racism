---
label: eq:10.17-temporal-extraction-rate
new_label: eq:10.17-temporal-extraction-rate
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: ~7810
statement: |
  \mathcal{E}_{X_{\text{temporal}}}(t) = \frac{d D_{\text{sovereign}}}{dt} \cdot \delta_E(t) \cdot \mathbf{1}[r(t) < g(t)]
type: quantitative
tier: 1
status: complete
existing_case_study: true
phase3_headline: false
target_events:
  - "US 1945-1980 (Reinhart-Sbrancia primary window)"
  - "Post-1971 fiat scaling (unconstrained D_sovereign growth)"
  - "Japan BOJ carry-trade model (Lustig-Sleet-Zhang)"
data_sources:
  - {name: "FRED: Federal Debt Total Public Debt as % of GDP (GFDEGDQ188S)", type: "primary", url: "https://fred.stlouisfed.org/series/GFDEGDQ188S"}
  - {name: "FRED: Real GDP Growth Rate (A191RL1A225NBEA)", type: "primary", url: "https://fred.stlouisfed.org/series/A191RL1A225NBEA"}
  - {name: "Reinhart-Sbrancia 2015", type: "peer-reviewed", url: "https://doi.org/10.1093/epolic/eiv011"}
  - {name: "Lustig-Sleet-Zhang NBER WP 31028 (2023)", type: "peer-reviewed", url: "https://www.nber.org/papers/w31028"}
difficulty: M
notebook: "eq10_15_17_financial_repression.ipynb"
case_study_line: ~7825
falsification: "Falsified if the indicator function 1[r < g] is inactive during documented periods of high sovereign debt accumulation — i.e., if debt expands when r > g, making the extraction channel mathematically closed. Post-1980 periods with r > g (early 1980s Volcker shock) provide a natural control window."
---

# Notes

**Description**: The instantaneous temporal extraction rate — the rate at which $X_{\text{temporal}}$ extracts from $L_{\text{future}}$. The extraction is active only when the $r < g$ condition holds (real interest rate below growth rate), which Reinhart-Sbrancia document as the dominant operating condition for advanced economies during 1945-1980. Lustig-Sleet-Zhang extend this to the Japan BOJ carry-trade model showing national-scale implementation.

**Relationship to existing equations**:
- $\mathcal{E}_{X_{\text{temporal}}}(t)$ is a component of the overall extraction objective $\mathcal{E}(t)$ in Eq. 10.5.
- The indicator function $\mathbf{1}[r < g]$ was switched permanently into a more favorable (to $E$) state by the 1971 Nixon Shock (Eq. 13.15-13.17), which removed the gold constraint on $D_{\text{sovereign}}$ expansion.
- The Volcker shock (1980-1982, $r > g$) provides a natural falsification window: the indicator function should deactivate, halting the extraction channel. Documented: real wealth-share growth of $E$ slows during 1980-1983 before resuming.

**Next steps**:
- [x] Verify LaTeX statement matches manuscript
- [x] Notebook built: eq10_15_17_financial_repression.ipynb
