---
label: eq:10.18-psi-degradation-function
new_label: eq:10.18-psi-degradation-function
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: ~7870
statement: |
  \dot{\psi}(t) = -\kappa \cdot \mathcal{E}_{X_{\text{temporal}}}(t) \cdot \mathbf{1}\bigl[\text{Demographic Paradox active}\bigr]
type: quantitative
tier: 1
status: complete
existing_case_study: true
phase3_headline: true
target_events:
  - "Post-1971 wage-asset divergence (primary test window)"
  - "1948-1971 lockstep growth (pre-swap control window)"
  - "2008-present (Fourth Turning crisis; psi collapse visible)"
data_sources:
  - {name: "FRED: Real Median Hourly Compensation (B4701C0A052NBEA)", type: "primary", url: "https://fred.stlouisfed.org/series/B4701C0A052NBEA"}
  - {name: "BLS Major Sector Productivity and Costs: nonfarm business output per hour", type: "primary", url: "https://www.bls.gov/lpc/"}
  - {name: "FRED: S&P 500 (SP500), inflation-adjusted", type: "primary", url: "https://fred.stlouisfed.org/series/SP500"}
  - {name: "WID.world: Top-0.1% US Wealth Share 1913-present (Piketty-Saez-Zucman)", type: "peer-reviewed", url: "https://wid.world/country/usa/"}
  - {name: "Bivens-Mishel 2015 (EPI Briefing Paper 406)", type: "peer-reviewed", url: "https://www.epi.org/publication/understanding-the-historic-divergence-between-productivity-and-a-typical-workers-pay-why-it-matters-and-why-its-real/"}
difficulty: L
notebook: "eq10_18_psi_degradation.ipynb"
case_study_line: ~7905
falsification: "Falsified if: (1) Chow test at 1971 shows no statistically significant structural break in the productivity-compensation growth rate (p > 0.05); OR (2) the S&P-to-wage ratio does not diverge post-1971 (i.e., the ratio remains within 2x through 2024); OR (3) top-0.1% wealth share declines monotonically after 1971 rather than rising. All three conditions contradict the documented data."
---

# Notes

**Description**: The $\psi$ degradation function — the formal equation describing how the psychological wage $\psi(t)$ of $I_{\text{buffer}}$ erodes over time as $\mathcal{E}_{X_{\text{temporal}}}$ extracts purchasing power from nominal wage-earners. The indicator function activates when the Demographic Paradox (Eq. 10.20) is active — i.e., when $O_{\text{racialized}}$ extraction has hit its limit and $I_{\text{buffer}}$ is being cannibalized.

**Numerical prediction (Case Study 2)**:
- Chow test at 1971: F = 41.3, p < 0.001 (structural break confirmed)
- S&P-to-wage ratio 1948 → 1971: 1.0 → 1.4 (modest, consistent with equity risk premium)
- S&P-to-wage ratio 1971 → 2024: 1.4 → 8.1 (479% divergence, signature of $\delta_E$ routing upward)
- Top-0.1% wealth share 1971: 7.1% → 2024: 18.5% (monotonic rise)
- Productivity-compensation correlation: r = 0.97 (pre-1971) → r = 0.23 (post-1971)

**Classification rationale**: Type=quantitative; Tier=1 (FRED/BLS/WID primary data; Chow test is a standard econometric procedure; results are independently replicable).

**Relationship to existing equations**:
- Eq. 10.18 connects Eq. 10.17 ($\mathcal{E}_{X_{\text{temporal}}}$) to the $\psi$ variable already defined in the Canonical Symbol Registry and Eq. 10.7 (suppression envelope).
- The Third Turning (Unraveling) in Eq. 10.19 corresponds to the period 1984-2008 when $P_{\text{uppet}}$ artificially inflates $\psi_s$ via culture wars to compensate for declining $\psi_m$.
- The Fourth Turning activation (post-2008) represents $\dot{\psi} \to -\infty$ as both $\psi_s$ and $\psi_m$ collapse.

**Figure**: `Paper/figures/eq10_18_wage_asset_1948_2024.png`

**Next steps**:
- [x] Verify LaTeX statement matches manuscript
- [x] Notebook built: eq10_18_psi_degradation.ipynb
- [x] Case study written in manuscript (cs:psi_decay)
