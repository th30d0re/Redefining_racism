# Session Log - 2026-04-17 (Guyana fact-check and integration)

## What Was Wrong / What Was Requested

User provided a social-media transcript about Guyana's oil boom and ExxonMobil contract, plus Gemini's suggestion to integrate it into the book. Requested: (1) fact-check the transcript, (2) implement the integration.

---

## Fact-Check Results

### ✅ GDP per capita: ~$6,000 (2019) → ~$34,000 (2025–26)
- **2019**: World Bank / Worldometer: **$6,279** — transcript says "about $6,000" ✅ accurate
- **2025–26**: IMF/World Bank: **$32,330–$34,307** — transcript says "$34,000" ✅ accurate (top of current range)
- World Bank 2024 figure: $29,675 — the $34k is a 2025/2026 projection

### ✅ Growth rates of ~44% per year
- Real GDP growth: **62.3% (2022), 37.2% (2023), 45.3% (2024)** — 44% is a reasonable approximation of the 2023–24 range ✅ accurate in order of magnitude; technically the 2022 spike was much higher

### ✅ 11 billion barrels
- The Stabroek Block resource base is confirmed at **~11 billion oil-equivalent barrels** as of February 2026 (Ministry of Natural Resources + ExxonMobil) ✅ accurate
- Note: "resource base" vs. "proved reserves" — technically distinct but 11B is the publicly confirmed figure

### ✅ ExxonMobil/Chevron getting 85%, Guyana getting 14.5%
This is the most important claim and it is **confirmed and well-documented**:
- **2% royalty** on gross production → Guyana
- **75% cost recovery cap** → companies (no ring-fencing = entire block's costs aggregated, keeping this at ceiling)
- **25% profit oil split 50/50** → 12.5% to Guyana + 12.5% to companies
- **Total Guyana take: 14.5%** — confirmed by IEEFA (Institute for Energy Economics and Financial Analysis), Oil & Gas Governance Network, Kaieteur News, Stabroek News ✅ accurate
- **Additional extraction**: Government of Guyana pays ExxonMobil's income taxes FROM Guyana's oil revenue (Article 15.4 of PSA) — the transcript does NOT mention this, and it makes the actual Guyanese take even lower than 14.5%
- ExxonMobil consortium reported **$10.4 billion profit** from Guyana operations
- Production as of Feb 2026: **918,000 barrels/day**, approaching 1M bpd

### ✅ "Never equal negotiating" / asymmetrical power
- The contract was signed in 2016 when Guyana was a lower-income country with no oil production history ✅ structurally accurate
- ExxonMobil's market cap vastly exceeds Guyana's GDP — no ring-fencing is a major concession rarely seen in comparable contracts

### ✅ Local elite / Puppet Class getting rich
- Documented in Guyanese media and academic literature: political contractors, middlemen ✅ accurate as structural claim

### ✅ Dependency trap / Dutch disease risk
- The economy is shifting toward extraction/export rather than industrial diversification ✅ accurately describes "resource curse" / Dutch disease dynamics

### ✅ Sanctions/destabilization/coups if demanding sovereignty
- No active intervention yet in Guyana specifically, but the pattern is historically documented (Iran 1953, Chile 1973, Venezuela, Bolivia, etc.) ✅ accurate as structural prediction; appropriately hedged in the transcript as "this is when pressure comes"

### ⚠️ "$34K GDP per capita = Guyanese people are rich"
- The transcript **does not** claim this but readers might infer it — important to note that GDP per capita is a national aggregate; most wealth flows through the oil sector and Puppet Class, not ordinary citizens. Inequality is severe.

### ⚠️ "One of the richest countries in South America"
- By GDP per capita: **true** — Guyana is now approaching or surpassing several South American nations by this metric
- By lived experience / wealth distribution: **misleading** — most Guyanese do not see $34K equivalent in real income; the per-capita figure reflects oil revenues largely captured by the sector and government

---

## How I Fixed It / What I Did

1. Fact-checked all claims (see above)
2. Added `\subsection{The Guyana Oil Trap: Corporate Imperialism as Modern Interface Swap}` to the Imperial Extraction Archive (after the Congo and India subsections, before the Peripheral Revolt section)
3. Variable mapping: Eglobal (ExxonMobil/Chevron), Puppet Class (local political elite), Fenforce global (sanctions/destabilization threat), Pdependency, cost-recovery asymmetry as modern version of sovereign debt trap
4. Added government-pays-company-taxes detail (not in transcript — strengthens the argument)
5. Added bibliography entries: IEEFA PSA summary, Kaieteur News, Stabroek News letter, Oil & Gas Governance Network
6. Updated Episode 16 podcast prompt
7. Compiled PDF — clean build

## Challenges Encountered

- The 14.5% claim sounds like an oversimplification but is actually the precise mathematical output of the contract — the mechanism needed careful explanation
- GDP per capita figure can be weaponized to argue "Guyana is doing well" — required framing about distribution inequality
- Need to distinguish resource base (11B barrels) from proved reserves (lower figure)

## Next Ideas (6 Ideas)

1. Add a formal equation showing the PSA extraction ratio as a Predatory Min-Max instantiation: max(E_global) = 0.855 * Revenue, min(O_global) = 0.145 * Revenue with no floor
2. Connect to the $P_debt$ variable: the cost-recovery mechanism functions like a perpetual sovereign debt — companies keep accumulating recoverable costs so the 75% ceiling is never breached
3. Add Venezuela as a counter-case: when Venezuela nationalized and demanded 85%+ for the state, F_enforce activated (sanctions, coup attempt, destabilization) — confirms the pressure prediction
4. Quantify: ExxonMobil consortium's $10.4B profit from Guyana = roughly 3x Guyana's entire pre-oil GDP
5. The government-pays-company-taxes detail is the Dexter Taylor / ex post facto mechanism applied to resource extraction: the "tax" is paid by the victim to the extractor
6. Add to Episode 8 (Compounding Chain) as well — the Guyana contract is a live instance of the P_debt sovereign ransom replicated in corporate form
