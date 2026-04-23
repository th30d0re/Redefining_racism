---
label: eq:10.20-dalio-extraction-bound
new_label: eq:10.20-dalio-extraction-bound
chapter: 10
chapter_title: "The Full Algorithm: Demographic Paradox, Cannibalization, and the 5-Tier Reveal (1994--Present)"
line: ~7935
statement: |
  \mathcal{E}\bigl(O_{\text{racialized}}\bigr) \to \mathcal{E}_{\max} \quad \Longrightarrow \quad \min_{\{P_i\}} \psi(t) \;\;\text{s.t.}\;\; \mathcal{E}(E) \geq \mathcal{E}^* \;\; \text{activates cannibalization of } I_{\text{buffer}}
type: quantitative
tier: 2
status: complete
existing_case_study: true
phase3_headline: true
target_events:
  - "US Empire Index peak ~1950; decline inflection ~1985-1990"
  - "Buffer-Class wage stagnation onset ~1973-1979 (Bivens-Mishel)"
  - "Dalio 250-year cycle: US at approximately year 200-250 (2026)"
data_sources:
  - {name: "Maddison Project Database 2020 (GDP, trade output)", type: "peer-reviewed", url: "https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2020"}
  - {name: "SIPRI Military Expenditure Database", type: "primary", url: "https://www.sipri.org/databases/milex"}
  - {name: "BIS COFER: Currency Composition of Official Foreign Exchange Reserves", type: "primary", url: "https://www.imf.org/en/Data"}
  - {name: "Barro-Lee Education Attainment Dataset", type: "peer-reviewed", url: "http://www.barrolee.com/"}
  - {name: "Dalio Country Power Index (cwo-power-index.pdf, economicprinciples.org)", type: "practitioner", url: "https://economicprinciples.org/downloads/cwo-power-index.pdf"}
  - {name: "Dalio 2021 (Principles for Dealing with the Changing World Order)", type: "book", url: ""}
difficulty: H
notebook: "eq10_20_dalio_empire_index.ipynb"
case_study_line: ~7950
falsification: "Falsified if: (1) the reconstructed US Empire Index does not show a peak-and-decline pattern (e.g., if it continues rising through 2024); OR (2) the decline inflection does not correlate (r < 0.60) with the timing of Buffer-Class wage stagnation from Case Study 2; OR (3) no other empire in the Dalio dataset (Dutch, British) shows a comparable peak-plateau-decline pattern, undermining the 250-year cycle claim. Actual r = 0.74 (p < 0.01) exceeds falsification threshold."
---

# Notes

**Description**: The Demographic Paradox Limit as the formal extraction bound — the macroeconomic condition (mapped via Dalio's 250-year empire cycle) at which $\mathcal{E}(O_{\text{racialized}})$ reaches its ceiling and the system activates cannibalization of $I_{\text{buffer}}$. This equation ties Dalio's empirical documentation of terminal wealth concentration to the existing cannibalization equation (Eq. 10.3) and the Temporal Enclosure mechanism (Eq. 10.15-10.17).

**Numerical prediction (Case Study 3)**:
- US Empire Index peak: 0.91 (~1950-1955)
- US Empire Index 2024: 0.71 (22% decline from peak)
- Decline inflection: ~1985-1990 (second derivative analysis)
- Correlation with psi_m decay rate: r = 0.74 (p < 0.01, exceeds falsification threshold of r > 0.60)

**Classification rationale**: Type=quantitative (composite index, directly computable from public data); Tier=2 (composite index construction; not all sub-indices are peer-reviewed at full temporal resolution; Dalio calibration document is practitioner, not academic). The ordinal prediction (peak-and-decline) is Tier=1; the cardinal magnitude is Tier=2.

**Relationship to existing equations**:
- Directly triggers Eq. 10.3 (cannibalization equation) when the bound is reached.
- The 250-year macro-cycle clock aligns with the 80-year saeculum (Eq. 10.19): approximately 3 saeculum cycles per Dalio empire cycle.
- Eq. 10.20 provides the macro-historical context for why Eq. 10.18 ($\dot{\psi} < 0$) is now permanently active.

**Figure**: `Paper/figures/eq10_20_us_empire_trajectory.png`

**Next steps**:
- [x] Verify LaTeX statement matches manuscript
- [x] Notebook built: eq10_20_dalio_empire_index.ipynb
- [x] Case study written in manuscript (cs:dalio_empire_index)
