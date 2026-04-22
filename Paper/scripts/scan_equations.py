#!/usr/bin/env python3
"""
scan_equations.py — T4 equation registry builder
============================================================
Scans Paper/Redefining_Racism.tex for all \\label{eq:...} instances,
extracts metadata, classifies each equation, and auto-generates one
YAML-frontmatter .md file per equation in Paper/empirical_validations/.

Also writes Paper/scripts/scan_output.json as a working artifact.

Usage:
    python3 Paper/scripts/scan_equations.py
"""

import re
import json
import os
import textwrap
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PAPER_DIR  = SCRIPT_DIR.parent
TEX_FILE   = PAPER_DIR / "Redefining_Racism.tex"
OUT_DIR    = PAPER_DIR / "empirical_validations"
SCAN_JSON  = SCRIPT_DIR / "scan_output.json"

OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Phase 3 headline equation labels — exactly 12 canonical equations ──────────
# One per Phase 3 numbered group (not all equations in each group).
# Source: Tech Plan Phase 3 list, empirical_hardening_and_spectral_rewrite plan.
PHASE3_LABELS = {
    "eq:5",   # 1. kernel optimization max ε s.t. M(t)<τ
    "eq:8",   # 2. suppression envelope (primary of eq:8–10 group)
    "eq:20",  # 3. Bacon inequality (primary of eq:20 + eq:24 group)
    "eq:27",  # 4. lethal autonomy / four-tier benefit ordering (per Tech Plan)
    "eq:33",  # 5. capacity compounding full chain
    "eq:40",  # 6. Interference Engine base wave (deferred to Phase 4)
    "eq:46",  # 7. Tweedism agenda path
    "eq:47",  # 8. lead-crime compounding (primary of eq:47–51 + sub-eq group)
    "eq:63",  # 9. O_final set construction
    "eq:65",  # 10. extraction precondition / kinetic asymmetry (primary of eq:65–68)
    "eq:73",  # 11. Haitian Theorem (primary of eq:73–74)
    "eq:91",  # 12. imperial core collapse condition
}

# ── Known classifications ──────────────────────────────────────────────────────
# Keys: label string (e.g. "eq:5")
# Values: dict with type, tier, difficulty, short_name, description,
#         falsification, target_events, data_sources
KNOWN: dict[str, dict] = {

    # ── Chapter 1 ────────────────────────────────────────────────────────────
    "eq:1": dict(
        short_name="enclosure_score",
        type="structural", tier=3, difficulty="S",
        description="Tri-Modal Enclosure Score S_enc = (1/3)∑e_i averaged over three outlet dimensions",
        falsification="Falsified if a population with all three outlets blocked (e_i=1) shows sustained autonomous mobilization without external support.",
        target_events=["Colonial-era slave societies 1619–1865"],
        data_sources=[],
    ),
    "eq:2": dict(
        short_name="total_enclosure",
        type="structural", tier=3, difficulty="S",
        description="Total enclosure: S_enc = 1.0 when all outlets fully blocked",
        falsification="Falsified if a fully blocked population (e_1=e_2=e_3=1) achieves coordinated resistance without external support.",
        target_events=["Antebellum South 1840–1860"],
        data_sources=[],
    ),
    "eq:3": dict(
        short_name="conventional_causal_arrow",
        type="structural", tier=3, difficulty="S",
        description="Conventional (incorrect) causal arrow: individual prejudice → discriminatory actions → systemic outcomes",
        falsification="Falsified if documented evidence shows individual prejudice predating Elite economic interest in any historical case.",
        target_events=[],
        data_sources=[],
    ),
    "eq:4": dict(
        short_name="elite_causal_arrow",
        type="structural", tier=3, difficulty="S",
        description="Correct causal arrow: Elite economic interests → systemic racialization → interpersonal prejudice",
        falsification="Falsified if racialization systems are shown to emerge without Elite economic interest as primary driver in any documented case.",
        target_events=["15th-century Portugal 1441–1481"],
        data_sources=[
            {"name": "Zurara, Gomes Eanes de. Chronica do Descobrimento e Conquista de Guiné (1453)", "type": "primary-source", "url": ""},
            {"name": "Blackmon, Douglas. Slavery by Another Name (2008)", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:5": dict(
        short_name="kernel_optimization",
        type="quantitative", tier=1, difficulty="L",
        description="Predatory min-max: maximize extraction E(t) subject to class-coherence risk M(t) < τ",
        falsification="Falsified if a documented period shows sustained decline in Elite extraction share while M(t) < τ without kernel-level intervention.",
        target_events=["Antebellum South 1840–1860 (cotton output vs. slave-rebellion suppression budget)", "Post-Civil Rights Era 1965–2020 (Elite wealth share vs. reform pressure)"],
        data_sources=[
            {"name": "Piketty, Saez, Zucman — Distributional National Accounts", "type": "peer-reviewed", "url": "http://gabriel-zucman.eu/usdina/"},
            {"name": "Gilens and Page (2014) — Testing Theories of American Politics", "type": "peer-reviewed", "url": "https://doi.org/10.1017/S1537592714001595"},
        ],
    ),
    "eq:6": dict(
        short_name="interface_strategy_set",
        type="structural", tier=3, difficulty="S",
        description="Set of available interface strategies S ∈ {partition, integration, direct repression, externalization}",
        falsification="Falsified if a documented Elite extraction system used a strategy outside this four-element set.",
        target_events=[],
        data_sources=[],
    ),
    "eq:7": dict(
        short_name="interface_optimizer",
        type="quantitative", tier=2, difficulty="M",
        description="Interface optimizer S* = argmin[C_coercive + C_legitimacy + C_economic] — selects lowest-cost interface strategy",
        falsification="Falsified if a historical interface transition increased net cost C_total relative to available alternatives.",
        target_events=["Jim Crow to War on Drugs transition 1954–1971", "Slavery to Convict Leasing 1865–1880"],
        data_sources=[
            {"name": "Dudziak (2000) — Cold War Civil Rights", "type": "peer-reviewed", "url": ""},
            {"name": "Alexander (2010) — The New Jim Crow", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:8": dict(
        short_name="suppression_envelope",
        type="quantitative", tier=2, difficulty="M",
        description="Suppression envelope Σ_sup = ψ_s(t) + ψ_m(t) + R(t) + Φ_load(t)",
        falsification="Falsified if M(t) consistently exceeds Σ_sup(t) for extended periods without triggering a crash or interface swap.",
        target_events=["Post-1965 backlash wave — union density, wealth share, incarceration rate", "Civil Rights era 1955–1975"],
        data_sources=[
            {"name": "BLS Union Membership Historical Series", "type": "public-dataset", "url": "https://www.bls.gov/news.release/union2.toc.htm"},
            {"name": "Saez-Zucman wealth concentration series", "type": "peer-reviewed", "url": "http://gabriel-zucman.eu/usdina/"},
        ],
    ),
    "eq:9": dict(
        short_name="crash_condition_derivative",
        type="structural", tier=3, difficulty="S",
        description="Crash condition: dM/dt > dΣ_sup/dt — rate of coherence growth exceeds suppression growth",
        falsification="Falsified if a crash event (Bacon's Rebellion, Haitian Revolution) occurs without dM/dt exceeding dΣ_sup/dt in the preceding period.",
        target_events=["Bacon's Rebellion 1676", "Haitian Revolution 1791–1804"],
        data_sources=[],
    ),
    "eq:10": dict(
        short_name="effective_coherence",
        type="quantitative", tier=2, difficulty="M",
        description="Effective class coherence M_eff = M(t) − λΦ_load(t); crash when M_eff > τ",
        falsification="Falsified if a crash event occurs when M_eff(t) < τ, or if no crash occurs when M_eff(t) > τ persistently.",
        target_events=["Bacon's Rebellion 1676 — cross-racial solidarity peak", "Civil Rights Movement 1955–1968"],
        data_sources=[
            {"name": "ANES cross-racial coalition data 1948–2020", "type": "public-dataset", "url": "https://electionstudies.org/"},
        ],
    ),
    "eq:11": dict(
        short_name="phase_loading",
        type="quantitative", tier=3, difficulty="M",
        description="Phase-loading Φ_load = 1 − |mean(exp(iΦ_j))| — circular dispersion measuring destructive interference across subgroups",
        falsification="Falsified if survey-measured cross-group solidarity remains high when Φ_load is high in ANES or Pew polarization data.",
        target_events=["Post-Civil Rights fragmentation 1968–1990", "Identity-politics polarization 1990–2020"],
        data_sources=[
            {"name": "ANES Time Series Study 1948–2020", "type": "public-dataset", "url": "https://electionstudies.org/"},
            {"name": "Pew Research Political Polarization Series", "type": "public-dataset", "url": "https://www.pewresearch.org/politics/"},
        ],
    ),

    # ── Chapter 2 ────────────────────────────────────────────────────────────
    "eq:12": dict(
        short_name="racism_vector",
        type="structural", tier=3, difficulty="S",
        description="Racism as directional vector: magnitude M and state-power direction d_hat_state",
        falsification="Falsified if documented racism operates without a state-power directional component, proceeding purely through decentralized interpersonal acts.",
        target_events=[],
        data_sources=[],
    ),
    "eq:13": dict(
        short_name="status_suppression_allocation",
        type="structural", tier=3, difficulty="S",
        description="Status allocation S_tatus(I) = Base_Humanity + ψ(t) with ψ = ψ_s + ψ_m",
        falsification="Falsified if Buffer Class loyalty is maintained without a non-material compensation component (ψ_s) when material wages are below subsistence.",
        target_events=["Colonial Virginia 1676–1705", "Du Bois Reconstruction analysis 1935"],
        data_sources=[
            {"name": "Du Bois (1935) — Black Reconstruction in America", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:14": dict(
        short_name="psi_null_in_survival",
        type="structural", tier=3, difficulty="S",
        description="Material wage ψ_m = 0 under normal operation; activated only under elevated kinetic threat",
        falsification="Falsified if material wages to Buffer Class are shown to be independent of kinetic threat level in any documented historical period.",
        target_events=["New Deal concessions 1930s", "Civil Rights Act 1964 (preceded by peak civil rights militancy)"],
        data_sources=[],
    ),
    "eq:15": dict(
        short_name="roman_membership_function",
        type="structural", tier=3, difficulty="S",
        description="Roman enslaved class membership: any conquered ethnicity — no phenotypic lock",
        falsification="Falsified if Roman enslaved population is shown to be phenotypically homogeneous across a significant sample of documented cases.",
        target_events=["Roman Republic slave economy 200 BCE–200 CE"],
        data_sources=[
            {"name": "Bradley (1994) — Slavery and Society at Rome", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:16": dict(
        short_name="american_racial_function",
        type="structural", tier=3, difficulty="S",
        description="American enslaved class: phenotype-locked membership — heritable, legally codified, visually self-enforcing",
        falsification="Falsified if documented American slavery assigned status based on non-phenotypic criteria at scale comparable to phenotypic assignment.",
        target_events=["Virginia partus sequitur ventrem law 1662"],
        data_sources=[
            {"name": "Hening's Statutes at Large (Virginia) Vol. 2", "type": "primary-source", "url": "https://www.encyclopediavirginia.org/Hening_s_Statutes_at_Large"},
        ],
    ),
    "eq:17": dict(
        short_name="roman_american_structural_parallel",
        type="structural", tier=3, difficulty="S",
        description="Structural parallel: Roman slavery → American racial slavery with phenotypic lock added",
        falsification="Falsified if the structural mapping between Roman and American slavery is analytically invalid on more than one key architectural dimension.",
        target_events=[],
        data_sources=[],
    ),
    "eq:18": dict(
        short_name="three_tier_portugal_inequality",
        type="ordinal", tier=3, difficulty="S",
        description="Three-tier inequality: Benefit(E_Portugal) > Benefit(I_buffer) > Benefit(O_enslaved)",
        falsification="Falsified if measured material outcomes show Benefit(I_buffer) ≥ Benefit(E) in any documented 15th-century Portuguese colonial case.",
        target_events=["15th-century Portugal 1441–1500"],
        data_sources=[],
    ),
    "eq:19": dict(
        short_name="church_science_feedback_loop",
        type="structural", tier=3, difficulty="S",
        description="Church and Science self-reinforcing feedback loop legitimating racial extraction",
        falsification="Falsified if the religious-scientific legitimation loop is disrupted from within (without external kinetic pressure) in any documented colonial-era case.",
        target_events=["Zurara's Chronica commissioned 1453", "Cartwright's Diseases and Peculiarities 1851"],
        data_sources=[
            {"name": "Cartwright (1851) — Diseases and Peculiarities of the Negro Race", "type": "primary-source", "url": ""},
        ],
    ),

    # ── Chapter 3 ────────────────────────────────────────────────────────────
    "eq:20": dict(
        short_name="bacon_solidarity_condition",
        type="quantitative", tier=1, difficulty="M",
        description="Bacon's Rebellion: cross-racial Labor Class coalition M(t) > τ_Bacon — system crash condition",
        falsification="Falsified if an antebellum cross-racial coalition reached M(t) > τ without subsequent Elite codification of racial partition.",
        target_events=["Bacon's Rebellion 1676", "Jamestown burning 1676"],
        data_sources=[
            {"name": "Morgan (1975) — American Slavery, American Freedom", "type": "peer-reviewed", "url": ""},
            {"name": "Hening's Statutes — Virginia Slave Codes 1705", "type": "primary-source", "url": "https://www.encyclopediavirginia.org/Hening_s_Statutes_at_Large"},
            {"name": "Zinn (1980) — A People's History of the United States Ch. 3", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:21": dict(
        short_name="boundary_enforcement_1691",
        type="structural", tier=3, difficulty="S",
        description="Racial boundary enforcement: legal penalties for cross-racial reproduction (1691 Virginia law)",
        falsification="Falsified if racial boundary enforcement persisted without legal penalty mechanism in any colonial-era American case.",
        target_events=["Virginia anti-miscegenation law 1691"],
        data_sources=[
            {"name": "Hening's Statutes at Large (Virginia) Vol. 3", "type": "primary-source", "url": "https://www.encyclopediavirginia.org/Hening_s_Statutes_at_Large"},
        ],
    ),
    "eq:22": dict(
        short_name="race_destroys_class",
        type="structural", tier=3, difficulty="S",
        description="Race partition destroys class solidarity: E recruited I_buffer against O to prevent cross-class coalition",
        falsification="Falsified if colonial-era racial coding produced class solidarity rather than suppressing it in any documented case.",
        target_events=["Virginia Slave Codes 1705", "Post-Bacon Rebellion racial partition 1676–1710"],
        data_sources=[
            {"name": "Morgan (1975) — American Slavery, American Freedom", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:23": dict(
        short_name="three_tier_post_bacon",
        type="ordinal", tier=3, difficulty="S",
        description="Three-tier post-Bacon inequality: Benefit(E) >> Benefit(I_buffer_white) > Benefit(O_racialized)",
        falsification="Falsified if the post-Bacon ordering shows Buffer Class benefits exceeding Elite benefits in any documented metric.",
        target_events=["Colonial Virginia 1705–1776"],
        data_sources=[],
    ),
    "eq:24": dict(
        short_name="kinetic_necessary_condition",
        type="quantitative", tier=1, difficulty="M",
        description="Kinetic necessary condition: K_E > K_B + K_O for extraction maintenance — Elite must outgun combined non-Elite",
        falsification="Falsified if documented cases show Elite extraction maintained when K_E ≤ K_B + K_O in any sustained historical period.",
        target_events=["Bacon's Rebellion kinetics 1676", "Haitian Revolution kinetic breach 1791–1804", "Post-Civil War disarmament of freedmen"],
        data_sources=[
            {"name": "Morgan (1975) — American Slavery, American Freedom", "type": "peer-reviewed", "url": ""},
            {"name": "Dubois (1935) — Black Reconstruction in America", "type": "peer-reviewed", "url": ""},
        ],
    ),

    # ── Chapter 5 ────────────────────────────────────────────────────────────
    "eq:25": dict(
        short_name="compliance_differential",
        type="quantitative", tier=2, difficulty="M",
        description="Compliance differential V_c(x) - V_r(x) — expected payoff of compliance vs. resistance for subject x",
        falsification="Falsified if V_c(x) ≤ V_r(x) for subjects in documented extraction regimes with no corresponding increase in M(t).",
        target_events=["Antebellum slave resistance economics", "Post-Reconstruction sharecropper compliance"],
        data_sources=[
            {"name": "Baptist (2014) — The Half Has Never Been Told", "type": "peer-reviewed", "url": ""},
        ],
    ),

    # ── Chapter 6 ────────────────────────────────────────────────────────────
    "eq:26": dict(
        short_name="lethal_autonomy_gradient",
        type="quantitative", tier=2, difficulty="M",
        description="Lethal Autonomy gradient: LA(F_enforce) >> LA(I_buffer) >> LA(O_racialized) = 0 — measurable via MPV killings-per-capita by racial group",
        falsification="Falsified if Mapping Police Violence data shows parity in police killings per capita across racial groups after controlling for encounter rates.",
        target_events=["Police killings 2013–2024", "LEOSA statutory analysis"],
        data_sources=[
            {"name": "Mapping Police Violence database 2013–2024", "type": "public-dataset", "url": "https://mappingpoliceviolence.us/"},
            {"name": "Fatal Encounters database", "type": "public-dataset", "url": "https://fatalencounters.org/"},
        ],
    ),
    "eq:27": dict(
        short_name="four_tier_benefit_ordering",
        type="ordinal", tier=3, difficulty="M",
        description="Four-tier benefit ordering: Benefit(E) >> Benefit(F_enforce) > Benefit(I_buffer) > Benefit(O_racialized)",
        falsification="Falsified if comprehensive wealth, health, or carceral data shows Benefit(I_buffer) exceeding Benefit(F_enforce) systematically.",
        target_events=["Contemporary US income/wealth distribution 2000–2024"],
        data_sources=[
            {"name": "Piketty-Saez-Zucman Distributional National Accounts", "type": "peer-reviewed", "url": "http://gabriel-zucman.eu/usdina/"},
            {"name": "BJS incarceration by race series", "type": "public-dataset", "url": "https://www.bjs.gov/"},
        ],
    ),
    "eq:28": dict(
        short_name="thirteenth_amendment_exception",
        type="structural", tier=3, difficulty="S",
        description="13th Amendment exception clause: slavery conditional on crime conviction — extraction re-encoded as criminalization",
        falsification="Falsified if 13th Amendment exception clause is shown to have been applied non-racially in incarceration data across the post-Civil War period.",
        target_events=["Convict leasing 1865–1940", "Black Codes 1865–1877"],
        data_sources=[
            {"name": "Blackmon (2008) — Slavery by Another Name", "type": "peer-reviewed", "url": ""},
            {"name": "Alexander (2010) — The New Jim Crow", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:29": dict(
        short_name="additive_policy_model",
        type="structural", tier=3, difficulty="S",
        description="Naive additive policy model (incorrect baseline): impact = ∑P_i rather than multiplicative compounding",
        falsification="Falsified if additive accumulation predicts compound policy outcomes with equal accuracy to the multiplicative model.",
        target_events=[],
        data_sources=[],
    ),
    "eq:30": dict(
        short_name="compounding_temporal_model",
        type="quantitative", tier=2, difficulty="M",
        description="Compounding temporal model: O^capacity(t+1) = O^capacity(t) × (1 − α·P_t)",
        falsification="Falsified if policy shock effects on O^capacity are shown to be independent across periods in longitudinal wealth data.",
        target_events=["Black wealth trajectory 1865–2024"],
        data_sources=[
            {"name": "Hamilton & Darity (2017) — The Political Economy of Education, Financial Literacy, and the Racial Wealth Gap", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:31": dict(
        short_name="asymmetric_enforcement_multiplier",
        type="quantitative", tier=1, difficulty="M",
        description="Asymmetric multiplier: same behavioral rate B, different policy multiplier α·P_t applied by race",
        falsification="Falsified if ACLU cannabis arrest data shows no racial disparity in policy multiplier when behavioral rate B is held constant.",
        target_events=["ACLU cannabis arrests 2010–2018"],
        data_sources=[
            {"name": "ACLU (2020) — A Tale of Two Countries: Racially Targeted Arrests in the Era of Marijuana Reform", "type": "report", "url": "https://www.aclu.org/report/tale-two-countries-racially-targeted-arrests-era-marijuana-reform"},
        ],
    ),
    "eq:32": dict(
        short_name="policy_sequence_noncommutative",
        type="structural", tier=3, difficulty="S",
        description="Non-commutativity: P_1 then P_2 ≠ P_2 then P_1 — order of extraction policies produces different terminal states",
        falsification="Falsified if order of policy application (P_1 then P_2 vs. P_2 then P_1) produces identical outcomes in any documented policy sequence.",
        target_events=["Enslavement then redlining vs. counterfactual ordering"],
        data_sources=[],
    ),
    "eq:hist1": dict(
        short_name="capacity_chain_1619",
        type="quantitative", tier=2, difficulty="M",
        description="Compounding chain step 1: O_1619 = O_1450 × (1 − α·P_enslavement)",
        falsification="Falsified if O_1619 capacity is non-significantly different from O_1450 after controlling for pre-existing African economic structures.",
        target_events=["Transatlantic slave trade 1619 — first enslaved Africans in Virginia"],
        data_sources=[
            {"name": "Darity & Mullen (2020) — From Here to Equality (reparations calculations)", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:hist2": dict(
        short_name="capacity_chain_1865",
        type="quantitative", tier=2, difficulty="M",
        description="Compounding chain step 2: O_1865 = O_1619 × (1 − β·P_13thAmendment)",
        falsification="Falsified if O_1865 capacity is not reduced from O_1619 as measured by subsequent wealth and land-access data.",
        target_events=["13th Amendment 1865 and Convict Leasing 1865–1940"],
        data_sources=[
            {"name": "Blackmon (2008) — Slavery by Another Name", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:hist3": dict(
        short_name="capacity_chain_1934",
        type="quantitative", tier=1, difficulty="M",
        description="Compounding chain step 3: O_1934 = O_1865 × (1 − γ·P_redlining)",
        falsification="Falsified if redlining-exposed tracts show no differential wealth accumulation decline relative to non-redlined areas in HOLC map data.",
        target_events=["HOLC redlining 1934–1968", "Fair Housing Act 1968"],
        data_sources=[
            {"name": "Mapping Inequality — HOLC Redlining Maps", "type": "public-dataset", "url": "https://dsl.richmond.edu/panorama/redlining/"},
            {"name": "Rothstein (2017) — The Color of Law", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:hist4": dict(
        short_name="capacity_chain_1971",
        type="quantitative", tier=1, difficulty="M",
        description="Compounding chain step 4: O_1971 = O_1934 × (1 − δ·P_WarOnDrugs)",
        falsification="Falsified if War on Drugs enforcement shows no differential impact on O_racialized capacity in incarceration and wealth data.",
        target_events=["War on Drugs 1971–present", "Rockefeller Drug Laws 1973"],
        data_sources=[
            {"name": "ACLU (2020) — Cannabis Arrests Report", "type": "report", "url": "https://www.aclu.org/report/tale-two-countries-racially-targeted-arrests-era-marijuana-reform"},
            {"name": "BJS Drug Offense Incarceration Statistics", "type": "public-dataset", "url": "https://www.bjs.gov/"},
        ],
    ),
    "eq:33": dict(
        short_name="capacity_compounding_full",
        type="quantitative", tier=1, difficulty="M",
        description="Capacity compounding full chain: O_1971 = O_1450 × (1−α·P_enslavement)(1−β·P_13th)(1−γ·P_redlining)(1−δ·P_drugs)",
        falsification="Falsified if any one policy shock (α, β, γ, δ) is shown to have zero marginal effect on subsequent Black wealth accumulation in longitudinal data.",
        target_events=["ACLU cannabis arrests 2010–2018", "HOLC redlining maps 1934", "Mass incarceration 1971–present"],
        data_sources=[
            {"name": "ACLU (2020) — A Tale of Two Countries", "type": "report", "url": "https://www.aclu.org/report/tale-two-countries-racially-targeted-arrests-era-marijuana-reform"},
            {"name": "Mapping Inequality — HOLC Redlining Maps", "type": "public-dataset", "url": "https://dsl.richmond.edu/panorama/redlining/"},
            {"name": "Rothstein (2017) — The Color of Law", "type": "peer-reviewed", "url": ""},
            {"name": "Darity & Mullen (2020) — From Here to Equality", "type": "peer-reviewed", "url": ""},
        ],
    ),

    # ── Chapter 7 ────────────────────────────────────────────────────────────
    "eq:34": dict(
        short_name="pullman_corollary",
        type="structural", tier=3, difficulty="S",
        description="Pullman Corollary: I_buffer exclusion of O_racialized enables Elite weaponization of O against I_buffer",
        falsification="Falsified if a documented case shows I_buffer achieving collective gains through exclusion of O without subsequent Elite weaponization.",
        target_events=["Pullman Strike 1894 — Strikebreaker recruitment from Black workers", "AFL exclusion policies 1881–1935"],
        data_sources=[
            {"name": "Roediger (1991) — The Wages of Whiteness", "type": "peer-reviewed", "url": ""},
        ],
    ),

    # ── Chapter 8 ────────────────────────────────────────────────────────────
    "eq:35": dict(
        short_name="vertex_partition_graph",
        type="structural", tier=3, difficulty="S",
        description="Graph vertex partition: V = V_L (leaders/Elite) ∪ V_F (followers/non-Elite)",
        falsification="Falsified if leader/follower partition fails to predict convergence in any documented network containment model.",
        target_events=[],
        data_sources=[],
    ),
    "eq:36": dict(
        short_name="tier_to_graph_mapping",
        type="structural", tier=3, difficulty="S",
        description="Tier mapping: E → V_L (stationary leaders), I_buffer/O → V_F (followers); authority flows from j to i",
        falsification="Falsified if the tier-to-graph mapping produces inconsistent predictions across two documented historical cases.",
        target_events=[],
        data_sources=[],
    ),
    "eq:fractional-dynamics": dict(
        short_name="fractional_agent_dynamics",
        type="structural", tier=3, difficulty="M",
        description="Fractional-order Caputo dynamics for agent state: ₀D^α q_i(t) = u_i(t), α ∈ (0,1]",
        falsification="Falsified if integer-order dynamics (α=1) predict social-mobility convergence equally well as fractional-order in longitudinal data.",
        target_events=["Black wealth-gap recovery trajectory 1865–2024"],
        data_sources=[
            {"name": "Li et al. — Mittag-Leffler stability results (mathematical)", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:37": dict(
        short_name="compounding_chain_formal",
        type="quantitative", tier=2, difficulty="M",
        description="Formal fractional compounding chain — multiplicative capacity reduction over policy sequence",
        falsification="Falsified if multiplicative chain prediction diverges significantly from observed wealth-gap trajectory in longitudinal data.",
        target_events=["Black wealth accumulation trajectory 1865–2024"],
        data_sources=[
            {"name": "Federal Reserve SCF racial wealth data", "type": "public-dataset", "url": "https://www.federalreserve.gov/econres/scfindex.htm"},
        ],
    ),
    "eq:stationary-leaders": dict(
        short_name="stationary_leader_condition",
        type="structural", tier=3, difficulty="S",
        description="Stationary leaders: ₀D^α q_i(t) = 0 for i ∈ V_L — Elite state admits no user input u_i",
        falsification="Falsified if documented Elite actors show systematic response to u_i (user-level reform inputs) in their own wealth-extraction trajectory.",
        target_events=[],
        data_sources=[],
    ),
    "eq:state-dep-connectivity": dict(
        short_name="proximity_connectivity_condition",
        type="structural", tier=3, difficulty="S",
        description="State-dependent connectivity: edge (i,j) exists iff ‖q_i − q_j‖² ≤ δ",
        falsification="Falsified if social-affinity graph connectivity is shown to be independent of proximity in documented community-level data.",
        target_events=[],
        data_sources=[],
    ),
    "eq:navigation-components": dict(
        short_name="navigation_components",
        type="structural", tier=3, difficulty="S",
        description="Navigation function components: goal function γ_i (proximity to neighbors) and constraint b_ij (distance to boundary)",
        falsification="Falsified if goal and constraint functions do not bound follower trajectory correctly in containment-model simulation.",
        target_events=[],
        data_sources=[],
    ),
    "eq:navigation-function": dict(
        short_name="navigation_function",
        type="structural", tier=3, difficulty="S",
        description="Navigation function φ_i = γ_i / (γ_i^k + β_i)^{1/k} — bounded-above function for containment convergence",
        falsification="Falsified if φ_i fails to produce convergence in any graph satisfying the containment model's connectivity conditions.",
        target_events=[],
        data_sources=[],
    ),
    "eq:control-law": dict(
        short_name="gradient_control_law",
        type="structural", tier=3, difficulty="S",
        description="Control law: u_i = −K_i ∇_{q_i} φ_i(q), K_i > 0 — negative gradient descent on navigation function",
        falsification="Falsified if negative gradient of φ_i fails to drive convergence in any simulation with K_i > 0 and valid graph.",
        target_events=[],
        data_sources=[],
    ),
    "eq:38": dict(
        short_name="convex_hull_convergence",
        type="structural", tier=3, difficulty="S",
        description="Integer-order convergence theorem: for α=1, followers converge to convex hull of stationary leaders",
        falsification="Falsified if followers fail to converge to Elite convex hull in any graph with required connectivity and α=1.",
        target_events=[],
        data_sources=[],
    ),
    "eq:39": dict(
        short_name="mittag_leffler_stability",
        type="structural", tier=3, difficulty="M",
        description="Mittag-Leffler asymptotic stability for α ∈ (0,1): ‖q_i(t) − conv(V_L)‖ ≤ m·E_α(−λt^α)·‖q_i(0)‖^b",
        falsification="Falsified if social-mobility data for α ∈ (0,1) shows exponential rather than Mittag-Leffler (slower) decay of displacement.",
        target_events=["Black intergenerational wealth mobility 1865–2024"],
        data_sources=[
            {"name": "Chetty et al. (2018) — Race and Economic Opportunity in the United States", "type": "peer-reviewed", "url": "https://doi.org/10.1093/qje/qjy007"},
        ],
    ),
    "eq:40": dict(
        short_name="class_alignment_base_waves",
        type="structural", tier=3, difficulty="M",
        description="Base class-alignment waves for I_buffer and O_racialized at shared frequency f_class",
        falsification="Falsified if class alignment signal is not measurable as a distinct frequency in ANES or Congressional Record political-attention data.",
        target_events=["Class-solidarity measurement 1948–2020 (ANES)"],
        data_sources=[
            {"name": "ANES Time Series Study", "type": "public-dataset", "url": "https://electionstudies.org/"},
        ],
    ),
    "eq:41": dict(
        short_name="subgroup_compound_phase",
        type="structural", tier=3, difficulty="M",
        description="Compound phase Φ_j = ∑_k φ_{k,j} — subgroup j's cumulative phase shift across identity axes k",
        falsification="Falsified if compound phase Φ_j fails to predict subgroup political alignment in ANES cross-tabulation data.",
        target_events=["Post-Civil Rights identity fragmentation 1968–1990"],
        data_sources=[],
    ),
    "eq:42": dict(
        short_name="net_solidarity_signal",
        type="structural", tier=3, difficulty="M",
        description="Net class-solidarity signal S_class = Re[∑_j A_j exp(i(2πf_class t + Φ_j))]",
        falsification="Falsified if net solidarity signal cannot be measured as distinct from identity-axis signals in political-attention time series.",
        target_events=[],
        data_sources=[],
    ),
    "eq:43": dict(
        short_name="solidarity_collapse_condition",
        type="structural", tier=3, difficulty="S",
        description="Collapse condition: S_class → 0 when ∑_j A_j exp(iΦ_j) → 0 — solidarity collapses under maximum dispersion",
        falsification="Falsified if M(t) remains above τ even when S_class approaches zero across all subgroups simultaneously.",
        target_events=[],
        data_sources=[],
    ),
    "eq:44": dict(
        short_name="interference_control_objective",
        type="structural", tier=3, difficulty="S",
        description="Interference engine control objective: minimize S_class by maximizing Φ_load via axis-specific phase injection",
        falsification="Falsified if observed interference engine output increases S_class rather than decreasing it in any documented post-reform period.",
        target_events=[],
        data_sources=[],
    ),
    "eq:45": dict(
        short_name="circular_dispersion_operator",
        type="quantitative", tier=3, difficulty="M",
        description="Circular dispersion operator Φ_load = 1 − |R̄| where R̄ = (1/N)∑exp(iΦ_j) — directional-statistics measure",
        falsification="Falsified if circular dispersion of phase values fails to predict cross-group political mobilization in ANES solidarity data.",
        target_events=["Identity fragmentation 1968–2024"],
        data_sources=[
            {"name": "ANES Time Series — cross-group solidarity items", "type": "public-dataset", "url": "https://electionstudies.org/"},
        ],
    ),
    "eq:46": dict(
        short_name="tweedism_agenda_path",
        type="quantitative", tier=1, difficulty="M",
        description="Tweedism agenda path: P_uppet sequences votes from x_0 toward x* moving terminal policy away from class-optimal",
        falsification="Falsified if Gilens-Page analysis shows median voter preferences predict policy outcomes as strongly as top-quintile preferences.",
        target_events=["Gilens-Page 1,779 policy votes 1981–2002"],
        data_sources=[
            {"name": "Gilens & Page (2014) — Testing Theories of American Politics", "type": "peer-reviewed", "url": "https://doi.org/10.1017/S1537592714001595"},
            {"name": "Gilens (2012) — Affluence and Influence", "type": "peer-reviewed", "url": ""},
        ],
    ),

    # ── Chapter 9 ────────────────────────────────────────────────────────────
    "eq:47": dict(
        short_name="lead_crime_compounding",
        type="quantitative", tier=1, difficulty="M",
        description="Lead-crime compounding: O^capacity(t) reduced by P_lead policy variable in compounding chain",
        falsification="Falsified if Reyes (2007) blood-lead time-series fails to predict crime-rate decline after 20-year lag in multivariate regression.",
        target_events=["Lead gasoline phase-out 1970–1986 and crime decline 1990–2010"],
        data_sources=[
            {"name": "Reyes (2007) — Environmental Policy as Social Policy", "type": "peer-reviewed", "url": "https://doi.org/10.3386/w12417"},
            {"name": "Aizer & Currie (2019) — Lead and Juvenile Delinquency", "type": "peer-reviewed", "url": "https://doi.org/10.1257/app.20180026"},
        ],
    ),
    "eq:48": dict(
        short_name="epistemic_suppression_variable",
        type="quantitative", tier=2, difficulty="M",
        description="Epistemic suppression variable P_epistemic: corporate/governmental actions delaying lead-harm knowledge — extends P_lead compounding duration",
        falsification="Falsified if documented lead industry cover-up timeline shows no correlation with delay in regulatory response.",
        target_events=["Lead industry cover-up 1926–1970", "Clair Patterson's research suppression"],
        data_sources=[
            {"name": "Kitman (2000) — The Secret History of Lead (The Nation)", "type": "journalism", "url": ""},
            {"name": "Michaels (2008) — Doubt Is Their Product", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:49": dict(
        short_name="multi_vector_lead_exposure",
        type="quantitative", tier=1, difficulty="M",
        description="Multi-vector lead exposure: P_lead = P_air + P_water + P_institutional_plumbing, all concentrated by redlining",
        falsification="Falsified if cumulative lead exposure from all three vectors is not significantly higher in redlined areas than non-redlined areas.",
        target_events=["Flint water crisis 2014–2019", "Detroit school lead exposure study"],
        data_sources=[
            {"name": "EPA Air Quality Monitoring Data", "type": "public-dataset", "url": "https://www.epa.gov/outdoor-air-quality-data"},
            {"name": "Mapping Inequality HOLC maps", "type": "public-dataset", "url": "https://dsl.richmond.edu/panorama/redlining/"},
        ],
    ),
    "eq:50": dict(
        short_name="redlining_containment_field",
        type="quantitative", tier=1, difficulty="M",
        description="Redlining containment field: each lead vector's intensity = f(HOLC grade) — spatial amplification by race",
        falsification="Falsified if HOLC map grades show no statistically significant correlation with lead exposure levels in matched same-city tract comparison.",
        target_events=["HOLC redlining 1934–1968 and lead exposure mapping"],
        data_sources=[
            {"name": "Mapping Inequality HOLC maps", "type": "public-dataset", "url": "https://dsl.richmond.edu/panorama/redlining/"},
            {"name": "Rothstein (2017) — The Color of Law", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:funding": dict(
        short_name="school_funding_property_value",
        type="quantitative", tier=1, difficulty="M",
        description="School funding(t) ∝ V_t — property-value-based school funding formula",
        falsification="Falsified if school funding is shown to be independent of property values in a national dataset controlling for state equalization formulas.",
        target_events=["San Antonio v. Rodriguez (1973) upholding property-tax school funding"],
        data_sources=[
            {"name": "NCES Public School Finance Survey", "type": "public-dataset", "url": "https://nces.ed.gov/"},
            {"name": "EdBuild (2019) — 23 Billion", "type": "report", "url": "https://edbuild.org/content/23-billion"},
        ],
    ),
    "eq:infra": dict(
        short_name="infrastructure_quality_funding",
        type="quantitative", tier=2, difficulty="M",
        description="Infrastructure quality(t) ∝ school funding(t) — per-pupil spending drives facility condition",
        falsification="Falsified if school infrastructure quality is shown to be unrelated to per-pupil spending in NCES facility condition data.",
        target_events=["School infrastructure disparities 2000–2020"],
        data_sources=[
            {"name": "NCES School Facility Condition Survey", "type": "public-dataset", "url": "https://nces.ed.gov/"},
        ],
    ),
    "eq:lead_school": dict(
        short_name="school_lead_exposure_inverse",
        type="quantitative", tier=1, difficulty="M",
        description="P_lead^school(t) ∝ 1/infrastructure quality(t) — degraded infrastructure increases lead exposure in schools",
        falsification="Falsified if school infrastructure quality is shown to be unrelated to lead exposure rates in NCES or EPA school-building data.",
        target_events=["Michigan school lead pipe replacement program 2016–2024"],
        data_sources=[
            {"name": "EPA 3Ts for Reducing Lead in Drinking Water in Schools", "type": "public-dataset", "url": "https://www.epa.gov/ground-water-and-drinking-water/3ts-reducing-lead-drinking-water-schools"},
        ],
    ),
    "eq:community": dict(
        short_name="community_capacity_lead_reduction",
        type="quantitative", tier=2, difficulty="M",
        description="Community capacity(t) = O^capacity_t × (1 − α·P_lead^school(t)) — lead exposure reduces community capacity",
        falsification="Falsified if community economic capacity is shown to be independent of school lead exposure after controlling for income.",
        target_events=["Aizer-Currie lead-cognition study outcomes"],
        data_sources=[
            {"name": "Aizer & Currie (2019) — Lead and Juvenile Delinquency", "type": "peer-reviewed", "url": "https://doi.org/10.1257/app.20180026"},
        ],
    ),
    "eq:propval": dict(
        short_name="property_value_capacity_feedback",
        type="quantitative", tier=1, difficulty="M",
        description="V_{t+1} ∝ community capacity(t) — property values feed back through community economic capacity",
        falsification="Falsified if property values in subsequent periods are shown to be independent of community economic capacity in longitudinal housing data.",
        target_events=["Redlined neighborhood property value trajectories 1940–2024"],
        data_sources=[
            {"name": "Mapping Inequality HOLC maps + ACS property value data", "type": "public-dataset", "url": "https://dsl.richmond.edu/panorama/redlining/"},
        ],
    ),
    "eq:51": dict(
        short_name="highway_lead_spatial_concentration",
        type="quantitative", tier=1, difficulty="M",
        description="Σ_highway — spatial lead-concentration function mapping atmospheric exposure onto geographic coordinates by highway placement",
        falsification="Falsified if spatial concentration of automotive lead is not correlated with highway placement in redlined vs. non-redlined areas.",
        target_events=["Interstate highway construction through Black neighborhoods 1956–1972"],
        data_sources=[
            {"name": "Rothstein (2017) — The Color of Law (highway displacement chapters)", "type": "peer-reviewed", "url": ""},
            {"name": "EPA National Emissions Inventory", "type": "public-dataset", "url": "https://www.epa.gov/air-emissions-inventories"},
        ],
    ),

    # ── Chapter 10 ───────────────────────────────────────────────────────────
    "eq:52": dict(
        short_name="outgroup_racialized_subset",
        type="structural", tier=3, difficulty="S",
        description="O_racialized is strict subset of O (broader out-group) — original extraction pool is not the whole out-group",
        falsification="Falsified if O_racialized is shown to be coextensive with O rather than a strict subset in current demographic data.",
        target_events=["Contemporary US population demographics 2000–2024"],
        data_sources=[
            {"name": "US Census Bureau demographic data", "type": "public-dataset", "url": "https://www.census.gov/"},
        ],
    ),
    "eq:53": dict(
        short_name="buffer_class_shrinkage",
        type="quantitative", tier=2, difficulty="M",
        description="Buffer Class shrinks while broader O grows: dI_buffer/dt < 0 as Demographic Paradox operates",
        falsification="Falsified if Buffer Class size is shown to be expanding rather than contracting in current income-distribution data.",
        target_events=["Middle-class squeeze 1973–2024", "Gig economy expansion 2010–2024"],
        data_sources=[
            {"name": "Pew Research Center — America's Shrinking Middle Class", "type": "report", "url": "https://www.pewresearch.org/social-trends/2016/05/11/americas-shrinking-middle-class-a-close-look-at-changes-within-metropolitan-areas/"},
            {"name": "Federal Reserve SCF income/wealth data", "type": "public-dataset", "url": "https://www.federalreserve.gov/econres/scfindex.htm"},
        ],
    ),
    "eq:54": dict(
        short_name="cannibalization_equation",
        type="structural", tier=3, difficulty="M",
        description="Cannibalization: Elite absorbs Buffer Class benefits as extraction zone expands beyond O_racialized",
        falsification="Falsified if documented Elite extraction rate increases without corresponding Buffer Class income decline in same period.",
        target_events=["Reagan-era income redistribution 1980–1990", "Post-2008 recovery wealth concentration"],
        data_sources=[
            {"name": "Saez-Zucman wealth share series", "type": "peer-reviewed", "url": "http://gabriel-zucman.eu/usdina/"},
        ],
    ),
    "eq:55": dict(
        short_name="predatory_minmax_full_definition",
        type="structural", tier=3, difficulty="S",
        description="Full Predatory Min-Max Function definition with five-tier population partition",
        falsification="Falsified if the five-tier hierarchy fails to map onto any contemporary national extraction system.",
        target_events=[],
        data_sources=[],
    ),
    "eq:56": dict(
        short_name="kernel_objective_canonical",
        type="quantitative", tier=1, difficulty="L",
        description="Canonical kernel objective: maximize E(t) subject to M_eff(t) < τ — full algorithm statement",
        falsification="Falsified if a documented period shows sustained Elite wealth-share decline while M_eff(t) < τ without external kinetic intervention.",
        target_events=["Post-Civil Rights Era 1965–2024"],
        data_sources=[
            {"name": "Piketty-Saez-Zucman Distributional National Accounts", "type": "peer-reviewed", "url": "http://gabriel-zucman.eu/usdina/"},
        ],
    ),
    "eq:57": dict(
        short_name="effective_resistance_variable",
        type="structural", tier=3, difficulty="S",
        description="Effective resistance M_eff = M(t) − λΦ_load(t) — interference-engine-adjusted class coherence",
        falsification="Falsified if M_eff fails to capture the difference between raw class coherence and interference-engine dampening in ANES data.",
        target_events=[],
        data_sources=[],
    ),
    "eq:58": dict(
        short_name="suppression_envelope_canonical",
        type="quantitative", tier=2, difficulty="M",
        description="Canonical suppression envelope: Σ_sup = {ψ_s, ψ_m, R(t), Φ_load} — full toolkit",
        falsification="Falsified if documented suppression tools outside this set constitute the primary mechanism in any documented case.",
        target_events=[],
        data_sources=[],
    ),
    "eq:59": dict(
        short_name="crash_condition_canonical",
        type="structural", tier=3, difficulty="S",
        description="Canonical crash condition: M_eff(t) > τ — kernel destabilizes",
        falsification="Falsified if crash events occur in documented cases without M_eff(t) > τ.",
        target_events=["Bacon's Rebellion 1676", "Haitian Revolution 1791–1804"],
        data_sources=[],
    ),
    "eq:60": dict(
        short_name="tier_benefit_ordering_canonical",
        type="ordinal", tier=3, difficulty="S",
        description="Tier benefit ordering: Benefit(E) >> Benefit(P_uppet) > Benefit(F_enforce) > Benefit(I_buffer) >> Benefit(O)",
        falsification="Falsified if any two-tier comparison fails to show stated ordering in comprehensive cross-national income and carceral data.",
        target_events=[],
        data_sources=[],
    ),
    "eq:61": dict(
        short_name="system_objective_extraction_ratio",
        type="structural", tier=3, difficulty="S",
        description="System objective: Max(Extraction) / Min(Resistance_class) → System Stability",
        falsification="Falsified if documented extraction systems show this ratio declining without kernel-level intervention.",
        target_events=[],
        data_sources=[],
    ),
    "eq:62": dict(
        short_name="system_stability_algorithm",
        type="structural", tier=3, difficulty="S",
        description="Algorithm stability: five-tier hierarchy + suppression envelope maintains Max/Min ratio → stability",
        falsification="Falsified if system stability is maintained when extraction/resistance ratio is not optimized.",
        target_events=[],
        data_sources=[],
    ),
    "eq:63": dict(
        short_name="o_final_construction",
        type="quantitative", tier=2, difficulty="M",
        description="O_final set construction: modern mass-incarceration demographics reproduce 1676 out-group definition",
        falsification="Falsified if modern mass-incarceration demographics fail to reproduce the O set construction predicted by the algorithm.",
        target_events=["US mass incarceration 1994–present"],
        data_sources=[
            {"name": "Bureau of Justice Statistics incarceration by race series", "type": "public-dataset", "url": "https://www.bjs.gov/"},
            {"name": "The Sentencing Project — Racial Disparity Reports", "type": "report", "url": "https://www.sentencingproject.org/"},
            {"name": "Alexander (2010) — The New Jim Crow", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:reclassification": dict(
        short_name="reclassification_operator",
        type="structural", tier=3, difficulty="M",
        description="Reclassification operator R: maps individual x from tier based on K(x) vs K_tolerated and comply(x)",
        falsification="Falsified if the operator fails to predict observed ideological sorting in any documented historical reclassification case.",
        target_events=["Obama-era Black professional class reclassification", "Post-9/11 Arab-American reclassification"],
        data_sources=[],
    ),
    "eq:64": dict(
        short_name="kinetic_power_distribution",
        type="quantitative", tier=2, difficulty="M",
        description="Total kinetic power of non-Elite: P_total = P_F_enforce + P_I_buffer + P_O — distribution across tiers",
        falsification="Falsified if kinetic power is not concentrated in F_enforce as a proportion of total non-Elite capacity.",
        target_events=["Contemporary US gun ownership by occupation/race"],
        data_sources=[
            {"name": "Pew Research Center — Gun Ownership Survey 2017", "type": "public-dataset", "url": "https://www.pewresearch.org/social-trends/2017/06/22/americas-complex-relationship-with-guns/"},
        ],
    ),

    # ── Chapter 11 ───────────────────────────────────────────────────────────
    "eq:65": dict(
        short_name="extraction_precondition",
        type="ordinal", tier=3, difficulty="S",
        description="Extraction precondition: L_E >> L_O — Elite lethal capacity must dominate Out-group for extraction maintenance",
        falsification="Falsified if a documented extraction system maintained stability with L_E ≤ L_O.",
        target_events=["Antebellum South arms asymmetry", "Colonial militia vs. enslaved population ratio"],
        data_sources=[],
    ),
    "eq:66": dict(
        short_name="disarmament_agenda_path",
        type="structural", tier=3, difficulty="M",
        description="Disarmament agenda path: P_uppet sequences gun-control votes sold to I_buffer as controls on O_racialized",
        falsification="Falsified if documented gun-control legislation passed under high Φ_load shows no racial targeting pattern.",
        target_events=["Mulford Act 1967 (targeting Black Panthers)", "Gun Control Act 1968"],
        data_sources=[
            {"name": "Harcourt (2006) — Language of the Gun", "type": "peer-reviewed", "url": ""},
            {"name": "California Assembly Bill 1591 (Mulford Act) 1967", "type": "primary-source", "url": ""},
        ],
    ),
    "eq:67": dict(
        short_name="restriction_precedent_accumulation",
        type="structural", tier=3, difficulty="S",
        description="Restriction precedent r_t deposited into doctrine with each disarmament step",
        falsification="Falsified if restriction precedents deposited fail to expand in scope in subsequent judicial periods.",
        target_events=["Heller (2008) → McDonald (2010) → Bruen (2022) case law trajectory"],
        data_sources=[
            {"name": "District of Columbia v. Heller, 554 U.S. 570 (2008)", "type": "primary-source", "url": ""},
            {"name": "New York State Rifle & Pistol Ass'n v. Bruen, 597 U.S. 1 (2022)", "type": "primary-source", "url": ""},
        ],
    ),
    "eq:68": dict(
        short_name="restriction_scope_expansion",
        type="structural", tier=3, difficulty="M",
        description="Restriction scope expansion over time: r_{t+1} ⊃ r_t — doctrine expands beyond original rationale",
        falsification="Falsified if Second Amendment case law shows restriction scope declining over time rather than expanding.",
        target_events=["Second Amendment jurisprudence timeline 1968–2024"],
        data_sources=[
            {"name": "Second Amendment case law database (Georgetown Law)", "type": "primary-source", "url": ""},
        ],
    ),

    # ── Chapter 12 ───────────────────────────────────────────────────────────
    "eq:69": dict(
        short_name="reform_absorption_mechanism",
        type="structural", tier=3, difficulty="S",
        description="Reform absorption: policy reform reduces min(M) not max(E) — extraction share preserved",
        falsification="Falsified if a documented reform reduces Elite extraction share (max) rather than just reducing resistance pressure (min).",
        target_events=["Civil Rights Act 1964 — reduced min without touching max", "13th Amendment — interface swap"],
        data_sources=[
            {"name": "Piketty-Saez top income share data", "type": "peer-reviewed", "url": "http://gabriel-zucman.eu/usdina/"},
        ],
    ),
    "eq:70": dict(
        short_name="concession_theorem",
        type="quantitative", tier=2, difficulty="M",
        description="Concession Theorem: Elite permits reforms at rate proportional to min threat — never sufficient to alter max",
        falsification="Falsified if Elite-initiated reforms consistently exceed the minimum required to prevent kinetic threshold breach.",
        target_events=["New Deal concessions 1930s (preceded by labor militancy)", "Great Society 1964–1968 (preceded by Civil Rights militancy)"],
        data_sources=[
            {"name": "Piven & Cloward (1977) — Poor People's Movements", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:71": dict(
        short_name="judiciary_discrimination_detection",
        type="structural", tier=3, difficulty="S",
        description="Judiciary detection function: probability of detecting racial discrimination as function of explicitness",
        falsification="Falsified if judicial detection function produces false positives for proxy discrimination at rates comparable to explicit discrimination.",
        target_events=["Washington v. Davis (1976) — intent standard", "McCleskey v. Kemp (1987) — statistical evidence rejected"],
        data_sources=[
            {"name": "Washington v. Davis, 426 U.S. 229 (1976)", "type": "primary-source", "url": ""},
            {"name": "McCleskey v. Kemp, 481 U.S. 279 (1987)", "type": "primary-source", "url": ""},
        ],
    ),
    "eq:72": dict(
        short_name="proxy_discrimination_equivalence",
        type="structural", tier=3, difficulty="S",
        description="Proxy discrimination: P_proxy with Corr(x, race) → 1 achieves same partition as P_explicit",
        falsification="Falsified if P_proxy achieves racial separation at rates significantly below P_explicit with similar enforcement investment.",
        target_events=["War on Drugs racial disparities vs. Jim Crow explicit racial targeting"],
        data_sources=[
            {"name": "Alexander (2010) — The New Jim Crow", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:73": dict(
        short_name="haitian_theorem_nonkinetic",
        type="quantitative", tier=1, difficulty="M",
        description="Haitian Theorem: ∀ R_i ∈ R (non-kinetic reforms): Δmax(R_i) = 0 — no reform changes Elite extraction share",
        falsification="Falsified if any documented non-kinetic reform achieves Δmax < 0 (sustained reduction in Elite extraction share) in the 1450–2026 dataset.",
        target_events=["Civil Rights Act 1964", "Reconstruction Amendments 1865–1870", "13th Amendment 1865"],
        data_sources=[
            {"name": "Piketty-Saez top income share series 1913–2024", "type": "peer-reviewed", "url": "http://gabriel-zucman.eu/usdina/"},
            {"name": "Darity & Mullen (2020) — From Here to Equality", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:74": dict(
        short_name="haitian_theorem_kinetic",
        type="quantitative", tier=1, difficulty="M",
        description="Haitian Theorem kinetic: kinetic action → Δmax < 0 (at least temporarily); followed by debt/sanction imposition",
        falsification="Falsified if any documented kinetic event fails to produce at least temporary Δmax < 0, or if no post-kinetic debt/sanction imposition follows.",
        target_events=["Haitian Revolution 1791–1804 and 150M franc indemnity", "Haitian debt 1825–1947"],
        data_sources=[
            {"name": "NYT 'The Ransom' (2022) — Haiti independence debt investigation", "type": "journalism", "url": "https://www.nytimes.com/2022/05/20/world/americas/haiti-history-colonized-france.html"},
            {"name": "James (1938) — The Black Jacobins", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:75": dict(
        short_name="gendered_outgroup_set",
        type="structural", tier=3, difficulty="S",
        description="Gendered out-group set O_gendered — women partitioned along gender axis by same extraction logic",
        falsification="Falsified if O_gendered is shown to be structured differently from O_racialized in its extraction mechanics.",
        target_events=["Coverture law period 1600–1920", "Eugenics programs 1907–1970s"],
        data_sources=[],
    ),
    "eq:76": dict(
        short_name="intersection_double_partition",
        type="structural", tier=3, difficulty="S",
        description="Intersection: Black woman ∈ O_racialized ∩ O_gendered — simultaneous double partition",
        falsification="Falsified if intersection O_racialized ∩ O_gendered does not show compounded extraction rates relative to either component alone.",
        target_events=[],
        data_sources=[
            {"name": "Crenshaw (1989) — Demarginalizing the Intersection of Race and Sex", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:77": dict(
        short_name="multiplicative_intersection_compounding",
        type="quantitative", tier=2, difficulty="M",
        description="Intersection compounding: effective reduction = (1−α_r)(1−α_g) — multiplicative, not additive",
        falsification="Falsified if Black women's wealth gap from white men is not multiplicatively larger than either racial or gender gap alone.",
        target_events=["Black women's wage and wealth gap 2000–2024"],
        data_sources=[
            {"name": "AAUW pay-gap data by race and gender", "type": "public-dataset", "url": "https://www.aauw.org/resources/research/simple-truth/"},
            {"name": "Federal Reserve SCF wealth by race × gender", "type": "public-dataset", "url": "https://www.federalreserve.gov/econres/scfindex.htm"},
        ],
    ),
    "eq:78": dict(
        short_name="nonviolence_mandate_function",
        type="structural", tier=3, difficulty="S",
        description="Nonviolence mandate as algorithmic constraint: prevents O from achieving kinetic parity while M increases",
        falsification="Falsified if documented liberation movements adopting nonviolence achieve Δmax < 0 without external kinetic pressure.",
        target_events=["Civil Rights nonviolence doctrine vs. kinetic threshold analysis"],
        data_sources=[
            {"name": "Carson (1981) — In Struggle: SNCC and the Black Awakening of the 1960s", "type": "peer-reviewed", "url": ""},
        ],
    ),

    # ── Chapter 13 ───────────────────────────────────────────────────────────
    "eq:79": dict(
        short_name="global_compounding_capacity",
        type="quantitative", tier=2, difficulty="M",
        description="Global South compounding: O_global capacity reduced by colonial extraction chain (same multiplicative logic as domestic)",
        falsification="Falsified if post-colonial nation's capacity trajectory shows exponential recovery rather than Mittag-Leffler slow recovery after independence.",
        target_events=["Haiti post-independence 1804–2024", "Congo post-colonialism 1960–2024"],
        data_sources=[
            {"name": "World Bank development indicators — GDP per capita time series", "type": "public-dataset", "url": "https://data.worldbank.org/"},
            {"name": "IMF historical debt data", "type": "public-dataset", "url": "https://www.imf.org/en/Data"},
        ],
    ),
    "eq:80": dict(
        short_name="global_predatory_minmax",
        type="structural", tier=3, difficulty="S",
        description="Global Predatory Min-Max Function: same E/P_uppet/F_enforce/I_buffer/O hierarchy at international scale",
        falsification="Falsified if documented international economic relationships fail to map onto the five-tier extraction hierarchy.",
        target_events=["IMF structural adjustment programs 1980–2000"],
        data_sources=[
            {"name": "Klein (2007) — The Shock Doctrine", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:81": dict(
        short_name="externalized_enforcement_envelope",
        type="structural", tier=3, difficulty="S",
        description="Externalized enforcement: F_enforce active coercive envelope imported via multinational security missions",
        falsification="Falsified if Haiti's domestic coercive capacity is shown to be structurally independent of external enforcement alignment.",
        target_events=["MINUSTAH UN mission 2004–2017", "US military interventions in Haiti 1915–1934, 1994, 2004"],
        data_sources=[
            {"name": "UN MINUSTAH mission records", "type": "primary-source", "url": "https://peacekeeping.un.org/mission/past/minustah/"},
        ],
    ),
    "eq:killick-extraction": dict(
        short_name="killick_extraction_equation",
        type="structural", tier=3, difficulty="S",
        description="Killick extraction equation — indemnity/debt imposition formula post-kinetic breach (Haitian case)",
        falsification="Falsified if the extraction equation fails to predict subsequent debt imposition after kinetic breach in any post-colonial case.",
        target_events=["Haitian independence debt 1825", "Haitian self-immolation Crête-à-Pierrot 1802"],
        data_sources=[
            {"name": "NYT 'The Ransom' (2022)", "type": "journalism", "url": "https://www.nytimes.com/2022/05/20/world/americas/haiti-history-colonized-france.html"},
        ],
    ),
    "eq:82": dict(
        short_name="legitimation_constraint_set",
        type="structural", tier=3, difficulty="S",
        description="Legitimation Constraint Set L — procedural rules E_global has committed to as basis for institutional authority",
        falsification="Falsified if E_global actors consistently operate outside their stated legitimation constraints without institutional cost.",
        target_events=["US Môle Saint-Nicolas negotiations with Haiti 1891"],
        data_sources=[],
    ),
    "eq:83": dict(
        short_name="authorization_precondition",
        type="structural", tier=3, difficulty="S",
        description="Authorization precondition A_auth ∈ {0,1} — diplomatic authorization required by L before extraction",
        falsification="Falsified if E_global achieves extraction without satisfying authorization precondition under active legitimation constraint.",
        target_events=["US Môle Saint-Nicolas failure 1891 (Frederick Douglass as envoy)"],
        data_sources=[],
    ),
    "eq:84": dict(
        short_name="coercion_legitimacy_frontier",
        type="structural", tier=3, difficulty="M",
        description="Coercion-legitimacy frontier C_max — maximum coercion compatible with claiming a 'freely negotiated' agreement",
        falsification="Falsified if observed coercion levels in 'voluntary' agreements consistently exceed C_max without triggering legitimation challenges.",
        target_events=["IMF loan conditionality negotiations", "World Bank structural adjustment programs"],
        data_sources=[],
    ),
    "eq:85": dict(
        short_name="firmin_extraction_threshold",
        type="structural", tier=3, difficulty="S",
        description="Firmin Extraction Threshold F* — minimum coercive force E_global requires to compel O_global compliance",
        falsification="Falsified if E_global achieves extraction with deployed force below F* in any documented coercion case.",
        target_events=["Haitian resistance to US Môle demands 1891"],
        data_sources=[],
    ),
    "eq:86": dict(
        short_name="infeasible_constraint_set",
        type="structural", tier=3, difficulty="S",
        description="Infeasible constraint set: no strategy S with E(S)>0 AND L(S)=valid when Firmin conditions hold",
        falsification="Falsified if E_global achieves both extraction success and legitimation validity simultaneously under Firmin conditions.",
        target_events=["US failure at Môle Saint-Nicolas 1891"],
        data_sources=[],
    ),
    "eq:87": dict(
        short_name="asymmetric_leverage_ratio",
        type="structural", tier=3, difficulty="M",
        description="Asymmetric counter-leverage: structurally weaker actor constrains stronger by invoking stronger's own legitimation architecture",
        falsification="Falsified if a weaker actor's invocation of E_global's legitimation architecture generates no constraint on stronger actor's behavior.",
        target_events=["Anténor Firmin's 'De l'égalité des races humaines' (1885) as legitimation counter-strategy"],
        data_sources=[
            {"name": "Firmin (1885) — De l'égalité des races humaines", "type": "primary-source", "url": ""},
        ],
    ),
    "eq:88": dict(
        short_name="legitimation_abandonment_condition",
        type="structural", tier=3, difficulty="S",
        description="Legitimation abandonment: when extraction value exceeds legitimacy dependence, E_global drops L as operating constraint",
        falsification="Falsified if E_global maintains legitimation constraints even when extraction value clearly exceeds institutional legitimacy value.",
        target_events=["US 1915 occupation of Haiti (abandoning Monroe Doctrine constraints)"],
        data_sources=[],
    ),
    "eq:89": dict(
        short_name="global_containment_strategy",
        type="structural", tier=3, difficulty="S",
        description="Global containment: same interface options as domestic — partition, integration, repression, externalization at international scale",
        falsification="Falsified if global containment strategies differ structurally from the domestic min-max function's interface options.",
        target_events=["IMF conditionality as 'integration', sanctions as 'repression'"],
        data_sources=[],
    ),
    "eq:90": dict(
        short_name="un_vote_distribution",
        type="structural", tier=3, difficulty="S",
        description="UN vote distribution maps onto international 5-tier hierarchy with mathematical precision",
        falsification="Falsified if UN Security Council voting distribution fails to map onto the international 5-tier hierarchy.",
        target_events=["UN Security Council voting patterns on Haiti resolutions"],
        data_sources=[
            {"name": "UN Digital Library — UNSC vote records", "type": "public-dataset", "url": "https://digitallibrary.un.org/"},
        ],
    ),
    "eq:91": dict(
        short_name="imperial_core_collapse",
        type="quantitative", tier=1, difficulty="L",
        description="Imperial core collapse condition: rising O_global challenges extraction ceiling — liberation requires kinetic or structural parity",
        falsification="Falsified if documented rising powers (China, OPEC, Asian Tigers) achieved core status without triggering debt/sanction/military responses from incumbent core.",
        target_events=["China WTO entry 2001", "OPEC oil embargo 1973", "Asian financial crisis 1997 and IMF response", "Post-colonial Algeria 1962–1980"],
        data_sources=[
            {"name": "World Bank development indicators — GDP trajectory for rising economies", "type": "public-dataset", "url": "https://data.worldbank.org/"},
            {"name": "IMF historical lending and conditionality data", "type": "public-dataset", "url": "https://www.imf.org/en/Data"},
            {"name": "Acemoglu & Robinson (2012) — Why Nations Fail", "type": "peer-reviewed", "url": ""},
        ],
    ),

    # ── Chapter 14 ───────────────────────────────────────────────────────────
    "eq:algo_prior_inheritance": dict(
        short_name="algo_prior_inheritance",
        type="quantitative", tier=2, difficulty="M",
        description="Algorithmic prior inheritance: P_algo trained on H (historical dataset produced under compounding chain) inherits extraction priors",
        falsification="Falsified if ML systems trained on pre-2024 US data show no racial disparity in predictive outputs relative to ground truth after controlling for relevant covariates.",
        target_events=["COMPAS recidivism algorithm analysis 2016", "Facial recognition racial accuracy disparities"],
        data_sources=[
            {"name": "Angwin et al. (2016) — Machine Bias (ProPublica)", "type": "journalism", "url": "https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing"},
            {"name": "Buolamwini & Gebru (2018) — Gender Shades", "type": "peer-reviewed", "url": "https://doi.org/10.1145/3287560.3287596"},
        ],
    ),
    "eq:realtime_proximity": dict(
        short_name="realtime_proximity_estimate",
        type="quantitative", tier=2, difficulty="M",
        description="Real-time proximity estimate: G(t) tracks cross-class solidarity ties with Φ_load(t) as interference index",
        falsification="Falsified if real-time social-affinity graph G(t) shows no correlation with Φ_load in social-media network data.",
        target_events=["Social media political polarization 2008–2024"],
        data_sources=[
            {"name": "Twitter/X political affinity graph data (academic dataset)", "type": "public-dataset", "url": ""},
        ],
    ),
    "eq:orthogonal_vector": dict(
        short_name="orthogonal_vector_injection",
        type="structural", tier=3, difficulty="S",
        description="Orthogonal vector injection: E operator selects identity axis, amplifies stimulus, redistributes coalition energy from class to identity axis",
        falsification="Falsified if documented interference engine operations increase class-axis coalition energy rather than redistributing it to identity axes.",
        target_events=["Southern Strategy 1968 — race axis injection", "Culture wars 1990s — gender/sexuality axis"],
        data_sources=[],
    ),
    "eq:damped_oscillator": dict(
        short_name="correction_signal_damping",
        type="structural", tier=3, difficulty="S",
        description="Scale-correction signal damping: ψ_correction(t) is damped toward zero by induced damping coefficient Δ(t) via trauma-absorption mechanism",
        falsification="Falsified if scale-accurate counter-signals are shown to reduce identity-axis amplitude in documented media-correction episodes.",
        target_events=["'All Lives Matter' response to BLM as correction absorption"],
        data_sources=[],
    ),
    "eq:optical_enclosure": dict(
        short_name="optical_enclosure",
        type="structural", tier=3, difficulty="S",
        description="Optical Enclosure: E, P_uppet, F_enforce, I_buffer collapse onto single line of sight from O's vantage — hierarchy invisible",
        falsification="Falsified if documented perception studies show O's population maintaining clear angular distinction between tiers.",
        target_events=["Police brutality perception studies by race"],
        data_sources=[
            {"name": "Pew Research — Police-community relations by race", "type": "public-dataset", "url": "https://www.pewresearch.org/"},
        ],
    ),
    "eq:decoy_transfer": dict(
        short_name="decoy_transfer_coefficient",
        type="quantitative", tier=2, difficulty="M",
        description="Decoy transfer: kinetic class-solidarity energy K(t) transferred to E through P_uppet with coefficient k_d",
        falsification="Falsified if documented cases show kinetic class energy passing to E at rate significantly below k_d.",
        target_events=["Labor union energy absorbed by Democratic Party establishment 1970–2020"],
        data_sources=[],
    ),
    "eq:ddos_bandwidth": dict(
        short_name="ddos_bandwidth_ceiling",
        type="quantitative", tier=2, difficulty="M",
        description="DDoS bandwidth ceiling: n > Γ simultaneous nodes exceeds F_enforce concentrated-force ceiling",
        falsification="Falsified if F_enforce simultaneously suppresses n > Γ nodes in any documented distributed mobilization event.",
        target_events=["George Floyd protests 2020 — simultaneous multi-city mobilization vs. National Guard capacity"],
        data_sources=[
            {"name": "Armed Conflict Location & Event Data (ACLED) — US protests 2020", "type": "public-dataset", "url": "https://acleddata.com/"},
        ],
    ),
    "eq:kinetic_parity": dict(
        short_name="armed_swarm_bandwidth",
        type="quantitative", tier=2, difficulty="M",
        description="Armed swarm bandwidth: Γ_armed < n nodes when γ(k) × n > total F_enforce force capacity",
        falsification="Falsified if F_enforce simultaneously neutralizes armed nodes with force-multiplier cost significantly below predicted minimum.",
        target_events=["Ruby Ridge 1992 and Waco 1993 — single-node siege costs vs. capacity"],
        data_sources=[],
    ),
    "eq:kinetic_asymmetry": dict(
        short_name="kinetic_capital_asymmetry",
        type="quantitative", tier=2, difficulty="M",
        description="Kinetic capital asymmetry: I_buffer armed > O_racialized armed — result of 350-year disarmament timeline",
        falsification="Falsified if gun-ownership data shows no racial asymmetry in kinetic capital distribution after controlling for income.",
        target_events=["Contemporary gun ownership by race demographics"],
        data_sources=[
            {"name": "Pew Research Center — Gun Ownership Survey 2017", "type": "public-dataset", "url": "https://www.pewresearch.org/social-trends/2017/06/22/americas-complex-relationship-with-guns/"},
        ],
    ),
    "eq:green_zone_exception": dict(
        short_name="sustained_siege_cost",
        type="quantitative", tier=2, difficulty="M",
        description="Sustained siege cost S(x_0) for neutralizing single armed node — demonstrates bandwidth constraint",
        falsification="Falsified if F_enforce besieges multiple simultaneous armed nodes with total cost significantly below sum of individual siege costs.",
        target_events=["Ruby Ridge siege 1992 (18 days, FBI HRT, surveillance aircraft)", "Waco siege 1993 (51 days, ATF + FBI)"],
        data_sources=[],
    ),
    "eq:escalation_ceiling": dict(
        short_name="escalation_ceiling_tiers",
        type="structural", tier=3, difficulty="S",
        description="Escalation ceiling: four-tier F_enforce response sequence with decreasing bandwidth ceiling per tier",
        falsification="Falsified if F_enforce escalation tiers do not follow the predicted bandwidth-ceiling sequence in any documented counter-insurgency case.",
        target_events=["George Floyd protests 2020 — National Guard deployment capacity limits"],
        data_sources=[],
    ),
    "eq:inclusion_predicate": dict(
        short_name="inclusion_predicate",
        type="quantitative", tier=2, difficulty="M",
        description="Inclusion predicate: tier membership maintained when V(x,t) > R(x,t) — value exceeds resource cost",
        falsification="Falsified if data shows V(x,t) ≤ R(x,t) for majority members of I_buffer in any documented extraction period.",
        target_events=["Gig economy reclassification of workers 2010–2024"],
        data_sources=[
            {"name": "Bureau of Labor Statistics contingent worker survey", "type": "public-dataset", "url": "https://www.bls.gov/cps/contingent-and-alternative-arrangements.htm"},
        ],
    ),
    "eq:terminal_swap": dict(
        short_name="terminal_interface_swap",
        type="structural", tier=3, difficulty="S",
        description="Terminal Interface Swap condition: I_buffer ejected from tier when V(x,t) ≤ R(x,t) at scale",
        falsification="Falsified if documented late-stage extraction shows I_buffer benefits maintained above minimum enforcement-compliance level.",
        target_events=["Middle-class erosion 2008–2024 — automation + offshoring"],
        data_sources=[],
    ),
    "eq:liability_phase": dict(
        short_name="liability_phase_optimization",
        type="structural", tier=3, difficulty="S",
        description="Liability phase: asymptotic optimization — minimize c(x,t) as biological variable x becomes liability",
        falsification="Falsified if documented terminal-phase extraction shows E maintaining I_buffer benefits above enforcement-compliance minimum.",
        target_events=["Post-industrial deindustrialization of white working class 1970–2020"],
        data_sources=[],
    ),
    "eq:noise_spectrum": dict(
        short_name="noise_spectrum_index",
        type="quantitative", tier=2, difficulty="M",
        description="Noise-spectrum index N(t) = ideological entropy of swarm — measures degree of agnostic diversification",
        falsification="Falsified if noise-spectrum index of a documented swarm fails to predict whether interference operator successfully redirects it.",
        target_events=["Occupy Wall Street 2011 — high noise spectrum, successful redirection", "BLM 2020 — moderate noise spectrum"],
        data_sources=[
            {"name": "ACLED — US social movements 2011–2020", "type": "public-dataset", "url": "https://acleddata.com/"},
        ],
    ),
    "eq:agnostic_swarm": dict(
        short_name="agnostic_swarm_payload",
        type="structural", tier=3, difficulty="S",
        description="Agnostic swarm: single executable payload at timestamp t* — no ideological frequency shared by nodes",
        falsification="Falsified if documented multi-node mobilizations with ideological diversity fail to execute coordinated simultaneous action.",
        target_events=["Anonymous DDoS actions 2010–2012 — ideologically diverse, single payload"],
        data_sources=[],
    ),
    "eq:botnet_load": dict(
        short_name="botnet_load_theorem",
        type="quantitative", tier=2, difficulty="M",
        description="Botnet Load Theorem: enforcement fails when n(t) > Γ_armed AND N(t) > N_threshold",
        falsification="Falsified if enforcement grid contains a swarm with n > Γ_armed nodes and high N(t) in any documented mobilization.",
        target_events=["George Floyd protests 2020 — 550+ cities simultaneously"],
        data_sources=[
            {"name": "ACLED — 2020 US protest dataset", "type": "public-dataset", "url": "https://acleddata.com/"},
        ],
    ),
    "eq:ideological_routing": dict(
        short_name="ideological_routing_operator",
        type="structural", tier=3, difficulty="S",
        description="Ideological routing: R_topo maps node i to its own community coordinate (x_i, y_i) — geographic self-routing",
        falsification="Falsified if nodes in documented distributed mobilizations fail to route to their own community coordinates.",
        target_events=[],
        data_sources=[],
    ),
    "eq:zugzwang_payoff": dict(
        short_name="zugzwang_payoff_function",
        type="quantitative", tier=2, difficulty="M",
        description="Zugzwang payoff: Π_E(stand-down) > Π_E(attack) when swarm is above Γ — Elite trapped into concession",
        falsification="Falsified if Elite actors systematically choose attack over stand-down when swarm exceeds Γ in documented cases.",
        target_events=["George Floyd protests 2020 — National Guard stand-down in some cities"],
        data_sources=[],
    ),
    "eq:defection_cascade": dict(
        short_name="defection_cascade",
        type="quantitative", tier=2, difficulty="M",
        description="Defection cascade: F_enforce defects when w_community(v) > w_state(v) — community attachment exceeds institutional loyalty",
        falsification="Falsified if documented enforcement nodes fail to defect when community overlap is maximal and state orders suppression of that community.",
        target_events=["Haitian Revolution 1791–1804 — Polish soldiers defecting to Haitian side"],
        data_sources=[
            {"name": "James (1938) — The Black Jacobins (Polish Legion defections)", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:empathy_permeability": dict(
        short_name="empathy_permeability",
        type="quantitative", tier=2, difficulty="M",
        description="Empathy permeability: trauma overlap δ_trauma(F, O) predicts enforcement node defection probability",
        falsification="Falsified if trauma overlap between enforcement and out-group nodes fails to predict defection rates in documented historical cases.",
        target_events=["Haitian Revolution — Polish soldiers shared serfdom history", "Vietnam War — US soldier fraggings"],
        data_sources=[
            {"name": "James (1938) — The Black Jacobins", "type": "peer-reviewed", "url": ""},
        ],
    ),
    "eq:semantic_overwrite": dict(
        short_name="semantic_overwrite",
        type="structural", tier=3, difficulty="S",
        description="Semantic overwrite: Dessalines redefines 'Black' as ideological constant decoupled from phenotype",
        falsification="Falsified if 1805 Haitian Constitution's ideological redefinition failed to include non-phenotypically Black allies within constitutional protections.",
        target_events=["Haitian Constitution 1805 — Dessalines's racial redefinition"],
        data_sources=[
            {"name": "Haitian Constitution of 1805 (primary source)", "type": "primary-source", "url": ""},
        ],
    ),

    # ── Chapter 17 ───────────────────────────────────────────────────────────
    "eq:92": dict(
        short_name="racism_as_institutional_vector",
        type="structural", tier=3, difficulty="S",
        description="Racism as institutional vector: requires state-power backing; marginalized-group prejudice lacks directional velocity for systemic harm",
        falsification="Falsified if documented cases of marginalized-group prejudice achieve systemic harm at rates comparable to Elite-backed prejudice without institutional support.",
        target_events=[],
        data_sources=[],
    ),
    "eq:93": dict(
        short_name="o_terminal_expansion",
        type="quantitative", tier=2, difficulty="M",
        description="O terminal expansion: Predatory Min-Max Function drives O toward terminal state O_final as Demographic Paradox operates",
        falsification="Falsified if documented demographic trends show O contracting rather than expanding under current algorithmic operation.",
        target_events=["Contemporary US demographic trends 2000–2040 projections"],
        data_sources=[
            {"name": "US Census Bureau 2020 demographic projections", "type": "public-dataset", "url": "https://www.census.gov/"},
            {"name": "Pew Research Center — US future demographics", "type": "public-dataset", "url": "https://www.pewresearch.org/"},
        ],
    ),

    # ── Chapter 19 (Equation Registry appendix) ───────────────────────────────
    "eq:94": dict(
        short_name="kernel_objective_registry_entry",
        type="structural", tier=3, difficulty="S",
        description="Registry restatement of kernel objective: max E(t) s.t. M_eff(t) < τ",
        falsification="Redundant with eq:5 and eq:56; falsified by the same conditions as those equations.",
        target_events=[],
        data_sources=[],
    ),
    "eq:95": dict(
        short_name="suppression_envelope_registry_entry",
        type="structural", tier=3, difficulty="S",
        description="Registry restatement of suppression envelope: Σ_sup = ψ_s + ψ_m + R(t) + Φ_load",
        falsification="Redundant with eq:8 and eq:58; falsified by the same conditions as those equations.",
        target_events=[],
        data_sources=[],
    ),
    "eq:96": dict(
        short_name="crash_condition_registry_entry",
        type="structural", tier=3, difficulty="S",
        description="Registry restatement of crash condition: M_eff(t) > τ",
        falsification="Redundant with eq:9 and eq:59; falsified by the same conditions as those equations.",
        target_events=[],
        data_sources=[],
    ),
    "eq:97": dict(
        short_name="tier_ordering_registry_entry",
        type="ordinal", tier=3, difficulty="S",
        description="Registry restatement of tier benefit ordering",
        falsification="Redundant with eq:60; falsified if any tier ordering is reversed in comprehensive data.",
        target_events=[],
        data_sources=[],
    ),
}

# ── Chapter heading pattern ────────────────────────────────────────────────────
CHAPTER_PAT    = re.compile(r'\\chapter(\*?)\{([^}]+)\}')
LABEL_PAT      = re.compile(r'\\label\{(eq:[^}]+)\}')
BEGIN_ENV_PAT  = re.compile(r'\\begin\{(equation|align|gather|multline|align\*|gather\*)\}')
END_ENV_PAT    = re.compile(r'\\end\{(equation|align|gather|multline|align\*|gather\*)\}')

# ── Equation content extraction ────────────────────────────────────────────────

def extract_equations(tex_path: Path) -> list[dict]:
    """Parse tex_path; return list of equation dicts in document order."""
    lines = tex_path.read_text(encoding="utf-8").splitlines()

    chapter_num   = 0
    chapter_title = "Front Matter"
    current_env   = None          # name of active math environment
    env_start     = 0             # 1-indexed line where current env started
    # Store (lineno, raw) pairs so multi-label environments know each line's
    # true source location (fixes Comment 1 — all labels shared env_start before).
    env_lines: list[tuple[int, str]] = []

    equations: list[dict] = []
    # chapter_seq tracks per-chapter sequential numbering
    chapter_seq: dict[int, int] = {}

    def _register(label: str, lineno: int, content: str):
        seq = chapter_seq.get(chapter_num, 0) + 1
        chapter_seq[chapter_num] = seq
        equations.append({
            "label":         label,
            "line":          lineno,
            "chapter":       chapter_num,
            "chapter_title": chapter_title,
            "seq":           seq,
            "statement":     content.strip(),
            "env":           current_env or "equation",
        })

    for i, raw in enumerate(lines, start=1):
        line = raw.strip()

        # ── chapter tracking ──────────────────────────────────────────────
        cm = CHAPTER_PAT.search(raw)
        if cm:
            starred = cm.group(1) == "*"
            title   = cm.group(2)
            if not starred:
                chapter_num   += 1
                chapter_title  = title
            else:
                chapter_title  = title  # starred chapters don't increment counter
            chapter_seq.setdefault(chapter_num, 0)

        # ── environment tracking ──────────────────────────────────────────
        bm = BEGIN_ENV_PAT.search(raw)
        if bm and current_env is None:
            current_env  = bm.group(1)
            env_start    = i
            env_lines    = [(i, raw)]
            continue

        if current_env is not None:
            em = END_ENV_PAT.search(raw)
            env_lines.append((i, raw))
            if em:
                full_content = "\n".join(r for _, r in env_lines)
                # Find ALL labels in this environment block
                all_labels_in_env = LABEL_PAT.findall(full_content)
                if len(all_labels_in_env) == 1:
                    # Single-labeled environment: content is the full block minus tags
                    label = all_labels_in_env[0]
                    content = re.sub(r'\\begin\{[^}]+\}', '', full_content)
                    content = re.sub(r'\\end\{[^}]+\}', '', content)
                    content = re.sub(r'\\label\{[^}]+\}', '', content)
                    content = content.strip()
                    _register(label, env_start, content)
                elif len(all_labels_in_env) > 1:
                    # Multi-labeled environment (align with per-row labels):
                    # register each labeled line with its actual source line number.
                    for line_no, env_line in env_lines:
                        lm = LABEL_PAT.search(env_line)
                        if lm:
                            label   = lm.group(1)
                            content = LABEL_PAT.sub('', env_line)
                            content = re.sub(r'\\\\(\[.*?\])?$', '', content)
                            content = re.sub(r'&\s*', '', content)
                            content = content.strip()
                            _register(label, line_no, content)
                current_env = None
                env_lines   = []
            continue

        # ── inline label (inside align on a single line with no begin/end) ─
        lm = LABEL_PAT.search(raw)
        if lm and current_env is None:
            label   = lm.group(1)
            content = LABEL_PAT.sub('', raw).strip()
            content = re.sub(r'\\\\(\[.*?\])?$', '', content).strip()
            _register(label, i, content)

    return equations


# ── Manuscript-based case-study detector ──────────────────────────────────────

_CASE_STUDY_PATS = [
    re.compile(r'\\paragraph\{Historical calibration', re.IGNORECASE),
    re.compile(r'\\paragraph\{Historical [Ii]nstantiation', re.IGNORECASE),
    re.compile(r'\\paragraph\{Empirical calibration', re.IGNORECASE),
    re.compile(r'\\paragraph\{Empirical anchor', re.IGNORECASE),
    re.compile(r'\\subsection\*?\{Case [Ss]tudy', re.IGNORECASE),
    re.compile(r'\\textbf\{Historical calibration', re.IGNORECASE),
]


def detect_existing_case_studies(tex_path: Path, equations: list[dict]) -> dict[str, int]:
    """Return label → case_study_line for equations that already have an
    empirical anchor in the manuscript.  Searches within 200 lines after
    each equation's label line, stopping at the next equation's line.

    Only patterns that explicitly mark an inline case study or historical
    calibration block are accepted; populated metadata alone is not sufficient.
    """
    raw_lines = tex_path.read_text(encoding="utf-8").splitlines()
    n = len(raw_lines)
    result: dict[str, int] = {}

    for idx, eq in enumerate(equations):
        eq_line = eq["line"]  # 1-indexed
        next_eq_line = equations[idx + 1]["line"] if idx + 1 < len(equations) else n + 1
        search_end = min(next_eq_line, eq_line + 200, n + 1)

        for lineno in range(eq_line, search_end):
            raw = raw_lines[lineno - 1]  # convert to 0-indexed
            for pat in _CASE_STUDY_PATS:
                if pat.search(raw):
                    result[eq["label"]] = lineno
                    break
            if eq["label"] in result:
                break

    return result


# ── Short-name derivation ──────────────────────────────────────────────────────

def _slug(label: str) -> str:
    """Derive a short file-system name from a label like 'eq:5' or 'eq:algo_prior'."""
    key = label.removeprefix("eq:")
    # for pure-numeric labels, use 'eq{N}'
    if key.isdigit():
        return f"eq{key}"
    # for descriptive labels, sanitize
    return re.sub(r'[^a-z0-9_]', '_', key.lower()).strip('_')


# ── New-label derivation (per-chapter format for T7) ──────────────────────────

def new_label(eq: dict, classification: dict) -> str:
    chapter = eq["chapter"]
    seq     = eq["seq"]
    slug    = classification.get("short_name", _slug(eq["label"]))
    slug    = slug.replace("_", "-")
    return f"eq:{chapter}.{seq}-{slug}"


# ── Notebook filename (Tier 1 only) ───────────────────────────────────────────

def notebook_name(eq: dict, classification: dict) -> str:
    if classification.get("tier", 3) == 1:
        ch  = eq["chapter"]
        seq = eq["seq"]
        sn  = classification.get("short_name", _slug(eq["label"]))
        return f"nb_ch{ch:02d}_eq{seq:02d}_{sn}.ipynb"
    return ""


# ── MD file generation ────────────────────────────────────────────────────────

_YAML_BOOL_TRUE  = {"true", "yes", "on"}

def _yaml_str(s) -> str:
    """Minimal YAML string quoting."""
    if not isinstance(s, str):
        return str(s)
    if not s:
        return '""'
    # quote if contains special chars
    if any(c in s for c in (':', '#', '[', ']', '{', '}', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'")):
        escaped = s.replace('"', '\\"')
        return f'"{escaped}"'
    return s


def generate_md(eq: dict, cl: dict, is_phase3: bool,
                case_study_line: "int | None" = None) -> str:
    label      = eq["label"]
    sn         = cl.get("short_name", _slug(label))
    nl         = new_label(eq, cl)
    nb         = notebook_name(eq, cl)
    typ        = cl.get("type", "structural")
    tier       = cl.get("tier", 3)
    diff       = cl.get("difficulty", "M")
    falsi      = cl.get("falsification", "")
    desc       = cl.get("description", "")
    t_events   = cl.get("target_events", [])
    d_sources  = cl.get("data_sources", [])

    # existing_case_study is true only when the manuscript scanner found an
    # explicit calibration/case-study block near this equation (Comment 2).
    existing = case_study_line is not None

    def yaml_list(items: list, indent: str = "  ") -> str:
        if not items:
            return "[]"
        lines = []
        for item in items:
            if isinstance(item, dict):
                parts = [f"{{name: {_yaml_str(item.get('name',''))}, type: {_yaml_str(item.get('type',''))}, url: {_yaml_str(item.get('url',''))}}}"]
                lines.append(f"{indent}- {parts[0]}")
            else:
                lines.append(f"{indent}- {_yaml_str(str(item))}")
        return "\n" + "\n".join(lines)

    # Build statement: truncate very long ones, ensure proper indentation for YAML block scalar
    stmt = eq.get("statement", "")
    if len(stmt) > 400:
        stmt = stmt[:400] + " …"
    # Indent every line of statement with 2 spaces for YAML literal block scalar
    stmt_indented = "\n".join("  " + ln for ln in stmt.splitlines()) if stmt else "  (empty)"

    te_yaml = yaml_list(t_events) if t_events else "[]"
    ds_yaml = yaml_list(d_sources) if d_sources else "[]"

    doc = f"""\
---
label: {label}
new_label: {nl}
chapter: {eq['chapter']}
chapter_title: "{eq['chapter_title']}"
line: {eq['line']}
statement: |
{stmt_indented}
type: {typ}
tier: {tier}
status: pending
existing_case_study: {"true" if existing else "false"}
phase3_headline: {"true" if is_phase3 else "false"}
target_events: {te_yaml}
data_sources: {ds_yaml}
difficulty: {diff}
notebook: "{nb}"
case_study_line: {case_study_line if case_study_line is not None else "null"}
falsification: {_yaml_str(falsi)}
---

# Notes

**Description**: {desc}

**Equation**: `{label}` — Chapter {eq['chapter']}, equation {eq['seq']} in chapter (line {eq['line']} in manuscript)

**Classification rationale**: {"Phase 3 headline — full quantitative case study target." if is_phase3 else f"Type={typ}, Tier={tier} assigned based on mathematical structure and data availability."}

**Next steps**:
- [ ] Verify LaTeX statement above matches manuscript
- [ ] Confirm target_events and data_sources
- [ ] Write falsification criterion (if placeholder)
- [ ] Set `status: in_progress` when case study work begins
- [ ] Set `status: complete` and populate `case_study_line` when done
"""
    return doc


# ── File-name convention ───────────────────────────────────────────────────────

def md_filename(eq: dict, cl: dict) -> str:
    ch   = eq["chapter"]
    seq  = eq["seq"]
    sn   = cl.get("short_name", _slug(eq["label"]))
    return f"eq_{ch}_{seq:02d}_{sn}.md"


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print(f"Scanning {TEX_FILE} …")
    equations = extract_equations(TEX_FILE)
    print(f"  Found {len(equations)} labeled equations.")

    # Write scan output JSON
    SCAN_JSON.write_text(json.dumps(equations, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Scan output → {SCAN_JSON}")

    # Detect existing case studies based on manuscript content (Comment 2).
    print("  Detecting existing case-study blocks in manuscript …")
    case_study_map = detect_existing_case_studies(TEX_FILE, equations)
    print(f"  Found {len(case_study_map)} equation(s) with existing case-study evidence.")

    # Remove stale eq_*.md files from prior runs before regenerating
    stale = list(OUT_DIR.glob("eq_*.md"))
    if stale:
        print(f"  Removing {len(stale)} stale .md files from prior runs …")
        for f in stale:
            f.unlink()

    # Remove stale .gitkeep if present
    gitkeep = OUT_DIR / ".gitkeep"
    if gitkeep.exists():
        gitkeep.unlink()

    generated = []
    for eq in equations:
        label     = eq["label"]
        cl        = KNOWN.get(label, {})
        # Fill defaults for unknowns
        if not cl.get("short_name"):
            cl["short_name"] = _slug(label)
        if not cl.get("type"):
            # Heuristic: if equation math contains \max, \min, \arg, \frac{d, classify as quantitative
            stmt = eq.get("statement", "")
            if any(kw in stmt for kw in (r'\max', r'\min', r'\arg', r'\frac{d', r'\sum_{', r'P_{')):
                cl["type"] = "quantitative"
                cl["tier"] = cl.get("tier", 2)
            elif any(kw in stmt for kw in (r'\rightarrow', r'\subset', r'\in ', r'\gg', r'\geq', r'\leq')):
                cl["type"] = "structural"
                cl["tier"] = cl.get("tier", 3)
            else:
                cl["type"] = "structural"
                cl["tier"] = cl.get("tier", 3)
        cl.setdefault("difficulty", "M")
        cl.setdefault("falsification", "")
        cl.setdefault("target_events", [])
        cl.setdefault("data_sources", [])
        cl.setdefault("description", f"Equation {label} from Chapter {eq['chapter']}: {eq['chapter_title']}")

        is_phase3      = label in PHASE3_LABELS
        cs_line        = case_study_map.get(label)  # None → existing_case_study: false
        fname          = md_filename(eq, cl)
        fpath          = OUT_DIR / fname

        fpath.write_text(generate_md(eq, cl, is_phase3, case_study_line=cs_line), encoding="utf-8")
        generated.append({
            "file":     fname,
            "label":    label,
            "chapter":  eq["chapter"],
            "seq":      eq["seq"],
            "type":     cl["type"],
            "tier":     cl["tier"],
            "phase3":   is_phase3,
        })

    print(f"  Generated {len(generated)} .md files in {OUT_DIR}/")

    # Summary stats
    by_type  = {}
    by_tier  = {}
    phase3_n = 0
    for g in generated:
        by_type[g["type"]] = by_type.get(g["type"], 0) + 1
        by_tier[g["tier"]] = by_tier.get(g["tier"], 0) + 1
        if g["phase3"]:
            phase3_n += 1

    print(f"\n  Summary:")
    print(f"    Total equations : {len(generated)}")
    print(f"    Phase 3 headline: {phase3_n}")
    for t, n in sorted(by_type.items()):
        print(f"    type={t:<15}: {n}")
    for t, n in sorted(by_tier.items()):
        print(f"    tier={t}          : {n}")

    return generated


if __name__ == "__main__":
    main()
