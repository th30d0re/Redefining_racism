---
label: eq:10.16-financial-repression-condition
new_label: eq:10.16-financial-repression-condition
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: ~7800
statement: |
  r_{\text{real}}(t) = i(t) - \pi(t) < 0 \quad \Longrightarrow \quad \delta_E(t) = \pi(t) - i(t) > 0
type: quantitative
tier: 1
status: complete
existing_case_study: true
phase3_headline: true
target_events:
  - "US 1945-1980 (Reinhart-Sbrancia primary window)"
  - "UK 1945-1980 (3-4% GDP/year liquidation)"
  - "Post-1971 fiat architecture (unanchored inflation regime)"
data_sources:
  - {name: "FRED 10Y Treasury Constant Maturity Rate (GS10)", type: "primary", url: "https://fred.stlouisfed.org/series/GS10"}
  - {name: "FRED CPI-U All Items (CPIAUCSL)", type: "primary", url: "https://fred.stlouisfed.org/series/CPIAUCSL"}
  - {name: "IMF World Economic Outlook: Gross Government Debt/GDP", type: "primary", url: "https://www.imf.org/en/Publications/WEO"}
  - {name: "Reinhart & Sbrancia 2015 (Economic Policy, 12-country panel)", type: "peer-reviewed", url: "https://doi.org/10.1093/epolic/eiv011"}
difficulty: L
notebook: "eq10_15_17_financial_repression.ipynb"
case_study_line: ~7825
falsification: "Falsified if: (1) real interest rates remain positive throughout the 1945-1980 window (eliminating the delta_E extraction channel), OR (2) controlling for real rates eliminates the observed wealth-share divergence between E and I_buffer, OR (3) cumulative debt liquidation is < 15% of initial debt/GDP over the 1945-1980 window. Actual documented value (~40-60%) exceeds falsification threshold by 2.5-4x."
---

# Notes

**Description**: The financial repression extraction condition: when $P_{\text{uppet}}$ engineers nominal interest rates below the inflation rate ($r_{\text{real}} < 0$), the extraction increment $\delta_E(t) = \pi(t) - i(t) > 0$ is the annual real purchasing power silently transferred from nominal-instrument holders ($I_{\text{buffer}}$, $O$) to hard-asset holders ($E$). This is the stealth extraction subroutine within the Temporal Enclosure ($X_{\text{temporal}}$) mechanism.

**Numerical prediction**: Average annual extraction increment $\delta_E \approx 2.9\%$ (US) and $4.1\%$ (UK) across 1945-1980. Cumulative liquidation $\approx 40-60\%$ of 1945 debt/GDP ratio. Real rates negative in $\sim$50% of years during 1945-1980.

**Classification rationale**: Type=quantitative (directly measurable from FRED/IMF primary data); Tier=1 (Federal Reserve and IMF primary data with direct correspondence to equation variables; independently replicated in peer-reviewed Reinhart-Sbrancia 2015).

**Relationship to existing equations**:
- Direct operationalization of $\mathcal{E}_{X_{\text{temporal}}}(t)$ in Eq. 10.17.
- Provides the mechanism by which $\dot{\psi}(t) < 0$ (Eq. 10.18) manifests as measurable $\psi_m$ decay.
- The 1971 Nixon Shock (Interface Swap III) removed the Bretton Woods constraint on $D_{\text{sovereign}}$ expansion, allowing $\delta_E(t)$ to compound indefinitely.

**Figure**: `Paper/figures/eq10_15_17_real_rates_1945_1980.png` — twin-axis: real rate timeseries + cumulative liquidation.

**Next steps**:
- [x] Verify LaTeX statement matches manuscript
- [x] Notebook built: eq10_15_17_financial_repression.ipynb
- [x] Case study written in manuscript (cs:reinhart_sbrancia)
