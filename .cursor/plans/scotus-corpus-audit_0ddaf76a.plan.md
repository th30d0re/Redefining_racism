---
name: scotus-corpus-audit
overview: Audit the Supreme Court case research corpus (Paper/research/) against every case actually cited in Paper/Redefining_Racism.tex. Flag gaps, prioritize the next acquisition pass into three tiers, and stand up tooling so the corpus stays synchronized with the manuscript automatically on every build.
todos:
  - id: corpus_inventory
    content: Confirm the existing corpus — 57 markdown cases in Paper/research/markdown_cases/, 57 PDFs in Paper/research/ia_scotus_pdfs/, and the original 14-cluster pull list in Paper/research/internet_archive_scotus_pull_list.md. Fix the "58 total" arithmetic typo in the pull list's Full Case Count table (clusters actually sum to 57).
    status: completed
  - id: cite_key_extraction
    content: Extract every case cited in Paper/Redefining_Racism.tex — both `\cite{...}` keys and `\textit{... v. ...}` mentions. Normalize to a stable slug (e.g., dred_scott_v_sandford_1857).
    status: completed
  - id: tier1_pull
    content: Download & markitdown-convert Tier-1 gaps (cases with existing `\cite{}` keys in the manuscript). See Tier 1 table in plan body. Target 8 cases.
    status: completed
  - id: tier2_pull
    content: Download & markitdown-convert Tier-2 gaps (cases named and argued in the text but without `\cite{}` yet — mostly the gendered kernel / reproductive coercion cluster). Target 7 cases.
    status: completed
  - id: tier3_pull
    content: Download & markitdown-convert Tier-3 candidates (structurally relevant, high-value for next integration pass — intent-doctrine companions, juvenile-sentencing trilogy, VRA updates, religious-exemption arc, use-of-force doctrine). Target 20+ cases.
    status: completed
  - id: bruen_consolidation
    content: Consolidate Sources/NYSRA_v_BRUEN.md into the canonical markdown_cases/ library (or document the tier split). Do the same for Sources/Caetano_v_Massachusetts.md, District_of_Columbia_v_Heller.md, McDonald_v_City_of_Chicago.md, COMMONWEALTH_VS_DAVID_E_CANJURA.md.
    status: completed
  - id: case_index_yaml
    content: Create Paper/research/case_index.yaml as the single source of truth mapping cite_key → slug → pdf_path → md_path → cluster → chapters_cited_in → cited_count.
    status: completed
  - id: audit_script
    content: Write Paper/scripts/audit_scotus_corpus.py — parses the .tex source for case mentions, cross-references case_index.yaml, and prints (a) cited-but-missing, (b) present-but-uncited, (c) bib-key-but-no-PDF. Wire into `make pdf` as a lint step.
    status: completed
  - id: readme_refresh
    content: Update Paper/research/markdown_cases/README.md from "57 cases · 0 failures" to the post-Tier-1/Tier-2 count; add a status column (primary / companion / next-pass / audio-available).
    status: completed
  - id: session_log
    content: Write session log at __Avenue/harper/logs/session-2026-04-23-045450.md per the session-logging rule.
    status: completed
isProject: false
---

## SCOTUS Corpus Audit — Gap Analysis & Tiered Pull List

### Current State (baseline snapshot, 2026-04-23)

| Artifact | Count | Location |
|---|---|---|
| Markdown cases (markitdown-converted) | **57** | [Paper/research/markdown_cases/](Paper/research/markdown_cases/) |
| PDF records | **57** | [Paper/research/ia_scotus_pdfs/](Paper/research/ia_scotus_pdfs/) |
| Original pull list | 14 clusters | [Paper/research/internet_archive_scotus_pull_list.md](Paper/research/internet_archive_scotus_pull_list.md) |
| Ad-hoc analysis markdown (outside canonical library) | 5 | [Sources/](Sources/) — Heller, McDonald, Bruen, Caetano, Canjura |

**Arithmetic bug**: pull-list Full Case Count table shows 58 total but cluster sums are 57. Fix in first pass.

### Tier 1 — Hard Gap (explicit `\cite{}` keys in the manuscript, zero ambiguity)

These cases have working bibliography keys in [Paper/Redefining_Racism.tex](Paper/Redefining_Racism.tex) but **no primary source in the corpus yet**. Pull order follows manuscript load-bearing weight.

| # | Case | Year | Cite Key | Chapter / Argument | IA Search |
|---|---|---|---|---|---|
| 1 | **Dred Scott v. Sandford** | 1857 | `dredscott`, `fehrenbacher` | Ch. 1 (Tier-3 ordinal validation, 195-year arc), Ch. 10 (2A disarmament thesis — Taney's explicit articulation of why Black citizens cannot be armed) | [search](https://archive.org/search?query=dred+scott+sandford&and[]=collection%3A%22us-supreme-court%22) |
| 2 | **Loving v. Virginia** | 1967 | `loving_v_virginia_record_1967`, `bazile_opinion_1965` | Ch. 3 (1691 anti-miscegenation statute → 276-year arc); Bazile's Component-3 theological-overlay opinion already cited | [search](https://archive.org/search?query=loving+virginia&and[]=collection%3A%22us-supreme-court%22) |
| 3 | **DeShaney v. Winnebago County** | 1989 | `deshaney` | Ch. 6 ($F_\text{enforce}$ "no legal duty to protect" — cited 4x across Ch. 6, 10, 13) | [search](https://archive.org/search?query=deshaney+winnebago&and[]=collection%3A%22us-supreme-court%22) |
| 4 | **Town of Castle Rock v. Gonzales** | 2005 | `castlerock` | Ch. 6 companion to DeShaney (gendered dimension — restraining order, children murdered) | [search](https://archive.org/search?query=castle+rock+gonzales&and[]=collection%3A%22us-supreme-court%22) |
| 5 | **Washington v. Davis** | 1976 | `tel_wash_v_davis` | Ch. 11 ($\Sigma_\text{highway}$ intent-doctrine gating — paired with Arlington Heights) | [search](https://archive.org/search?query=washington+davis+1976&and[]=collection%3A%22us-supreme-court%22) |
| 6 | **Village of Arlington Heights v. Metropolitan Housing Development Corp.** | 1977 | `tel_arlington_heights` | Ch. 11 (the four-factor framework tabulated in the manuscript) | [search](https://archive.org/search?query=arlington+heights+metropolitan+housing&and[]=collection%3A%22us-supreme-court%22) |
| 7 | **New York State Rifle & Pistol Association v. Bruen** | 2022 | `bruen` | Ch. 10 (the "Proper Cause" algorithm & post-Bruen security-patch response — the Dobbs-era reactivation of the 2A vs. discretionary-licensing dialectic) | [search](https://archive.org/search?query=NYSRPA+bruen&and[]=collection%3A%22us-supreme-court%22) — *already have `Sources/NYSRA_v_BRUEN.md`, consolidate* |
| 8 | **Dobbs v. Jackson Women's Health Organization** | 2022 | *(no key yet — needs bib entry)* | Ch. 4 (Active Patch: Coverture → Comstock → Bradwell → Buck → **Dobbs**); Ch. 18 terminal node | [search](https://archive.org/search?query=dobbs+jackson+womens+health&and[]=collection%3A%22us-supreme-court%22) |

### Tier 2 — Named in Manuscript, No `\cite{}` Yet

Structurally central to the gendered-kernel argument (Ch. 4) but currently asserted without primary-source anchors.

| # | Case | Year | Chapter / Argument | IA Search |
|---|---|---|---|---|
| 9 | **Bradwell v. Illinois** | 1873 | Ch. 4 — separate-spheres codification; Bradley concurrence is quoted ("natural and proper timidity... law of the Creator") | [search](https://archive.org/search?query=bradwell+illinois&and[]=collection%3A%22us-supreme-court%22) |
| 10 | **Muller v. Oregon** | 1908 | Ch. 4 — protective-labor-law paradox | [search](https://archive.org/search?query=muller+oregon&and[]=collection%3A%22us-supreme-court%22) |
| 11 | **Reed v. Reed** | 1971 | Ch. 4 — Ginsburg brief, 14A turning point | [search](https://archive.org/search?query=reed+v+reed+1971&and[]=collection%3A%22us-supreme-court%22) |
| 12 | **Roe v. Wade** | 1973 | Ch. 4 — 2022 overturning is the Dobbs node above; Roe itself needs primary for the pre-patch baseline | [search](https://archive.org/search?query=roe+v+wade&and[]=collection%3A%22us-supreme-court%22) |
| 13 | **Relf v. Weinberger** | 1974 | Ch. 4 — reproductive coercion of Black sisters in Alabama | [search](https://archive.org/search?query=relf+weinberger&and[]=collection%3A%22us-supreme-court%22) |
| 14 | **Madrigal v. Quilligan** | 1978 | Ch. 4 — Mexican-American reproductive coercion, LA County | [search](https://archive.org/search?query=madrigal+quilligan&and[]=collection%3A%22us-supreme-court%22) |
| 15 | **Obergefell v. Hodges** | 2015 | Ch. 13 — brief mention; relevant to I_buffer expansion thesis | [search](https://archive.org/search?query=obergefell+hodges&and[]=collection%3A%22us-supreme-court%22) |

### Tier 3 — High-Value Next-Pass Candidates (not yet cited, but structurally demanded by the argument)

Grouped into **semantic bundles** so pulls happen in companion clusters (per session log "Next Idea 5").

**Bundle A — Intent-Doctrine Complex (companions to Washington v. Davis / Arlington Heights)**
- *Personnel Administrator of Massachusetts v. Feeney* (1979) — disparate-impact-is-not-intent, extended to sex
- *Mobile v. Bolden* (1980) — intent requirement imported into VRA (triggered 1982 amendment)
- *City of Richmond v. J.A. Croson Co.* (1989) — strict-scrutiny applied to state remedial programs
- *Adarand Constructors v. Peña* (1995) — same, federal

**Bundle B — Affirmative-Action Terminal Arc (completes the Ch. 11 concession-variable story already spanning Bakke → Grutter → Parents Involved → Fisher)**
- *Gratz v. Bollinger* (2003) — Grutter's undergraduate companion, struck UM points system
- *Schuette v. BAMN* (2014) — state AA bans upheld
- *Students for Fair Admissions v. Harvard / UNC* (2023) — overruled Grutter & Fisher; the Ch. 11 P_gaslight quote from Roberts ("way to stop discrimination...") reaches terminal velocity here

**Bundle C — Use-of-Force Doctrine (Ch. 6 $F_\text{enforce}$ architecture)**
- *Tennessee v. Garner* (1985) — deadly force limitation
- *Graham v. Connor* (1989) — objective-reasonableness standard
- *Scott v. Harris* (2007) — high-speed-pursuit immunity
- *Whren v. United States* (1996) — pretextual traffic stops (direct companion to Atwater 2001 already in corpus)
- *Rodriguez v. United States* (2015) — traffic-stop duration limits

**Bundle D — Juvenile-Sentencing Trilogy (8A architecture — companion to Harmelin 1991 already in corpus)**
- *Roper v. Simmons* (2005) — juvenile death penalty abolished
- *Graham v. Florida* (2010) — juvenile LWOP for non-homicide abolished
- *Miller v. Alabama* (2012) — mandatory juvenile LWOP abolished
- *Ramos v. Louisiana* (2020) — unanimous-jury requirement (6A incorporation)

**Bundle E — VRA Post-Shelby Arc (Ch. 7 Tweedism Filter, completes the Shelby County 2013 thread already in corpus)**
- *Brnovich v. DNC* (2021) — VRA Sec 2 substantially weakened
- *Allen v. Milligan* (2023) — Sec 2 upheld in Alabama (limit to the post-Shelby slide)
- *Rucho v. Common Cause* (2019) — partisan gerrymandering non-justiciable
- *Moore v. Harper* (2023) — ISL doctrine rejected

**Bundle F — Jury-Selection / Batson-Purkett Terminal Arc (completes Ch. 9 companion to Batson, Purkett, Foster already in corpus)**
- *Flowers v. Mississippi* (2019) — Batson applied 7-convictions deep

**Bundle G — Religious-Exemption / Dobbs-Era Counter-Reform (Ch. 18)**
- *Trump v. Hawaii* (2018) — travel ban; Korematsu-disavowal citation but validates same pattern
- *Kennedy v. Bremerton* (2022) — post-game prayer; strict-scrutiny flip
- *303 Creative v. Elenis* (2023) — public-accommodations carve-out on 1A grounds

**Bundle H — Excessive-Fines / Civil-Asset Architecture (Ch. 9 carceral-state funding)**
- *Timbs v. Indiana* (2019) — 8A excessive fines incorporated against states

### Execution Protocol (reuse from existing pull list)

All pulls follow the five-step protocol in [Paper/research/internet_archive_scotus_pull_list.md](Paper/research/internet_archive_scotus_pull_list.md) §"Agent Download Protocol":

1. `https://archive.org/search?query=CASE+NAME&and[]=collection%3A%22us-supreme-court%22`
2. Select item matching party caption + year
3. Direct PDF URL: `https://archive.org/download/{identifier}/{identifier}.pdf`
4. Drop PDF into `Paper/research/ia_scotus_pdfs/`
5. Run `markitdown` → `Paper/research/markdown_cases/{slug}.md`
6. Append row to `Paper/research/markdown_cases/README.md`

For cases without `us-supreme-court` collection hits (pre-1870 — e.g., Dred Scott 1857), fall back to Library of Congress `tile.loc.gov/storage-services/service/ll/usrep/...` per the existing manifest precedent for Yick Wo.

### Tooling — Build-Time Enforcement

After Tier 1 + Tier 2 are acquired, land `Paper/scripts/audit_scotus_corpus.py`:

```python
# Parse .tex → extract \cite{} keys + \textit{X v. Y} mentions
# Cross-reference against Paper/research/case_index.yaml
# Emit three-bucket diff:
#   (a) cited-but-missing  → fatal (fail the build)
#   (b) present-but-uncited → warning (orphan candidate)
#   (c) cite-key-but-no-PDF → fatal (broken bibliography)
```

Wire into `make pdf` immediately after BibTeX so every compilation enforces corpus-manuscript synchrony. This is the A→C→D traceability invariant from the user's Engineering Governance rules: every requirement (case referenced in text) traces to at least one MRV artifact (PDF + markdown in corpus).

### Summary — Target State After This Plan Completes

| Tier | Cases | Cumulative | Status |
|---|---|---|---|
| Baseline | 57 | 57 | complete |
| Tier 1 | 8 | 65 | pending |
| Tier 2 | 7 | 72 | pending |
| Tier 3 Bundle A–H | 20+ | 92+ | pending |

At Tier 3 completion: every case named in the manuscript has a primary source in the corpus, the intent-doctrine and use-of-force arguments have full primary-source coverage, and the AA / VRA / juvenile-sentencing / carceral-state chapters each have their companion clusters intact for the spectral / MRV analyses planned in the other active plans (algorithmic-epoch-podcast-sync, empirical_hardening_and_spectral_rewrite, four-charts-integration).
