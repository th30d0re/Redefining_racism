# US Code Phase 2: Untapped Statutes for *Redefining Racism*

> Add 7 new statutory excerpts from the `nickvido/us-code` repo to `Redefining_Racism.tex` — targeting the book's biggest "opportunity gaps" where arguments reference specific federal laws by name but never quote the actual code.

---

## Diagnosis

Phase 1 added 9 excerpts (18 USC 922(g), 922(o), 926B, 521, 241, 242; 42 USC 2000d; 52 USC 10301; 50 USC 1801). But the book makes substantive claims about several other federal statutes — sometimes by name, sometimes by policy effect — without ever quoting the code. The `us-code` repo contains the verbatim text for all of them. This plan adds the highest-impact excerpts, priority-ordered by argumentative payoff.

---

## Priority 1 — The 13th Amendment Kernel: Peonage & Forced Labor

**Statute:** 18 USC §§1581 (Peonage) and 1589 (Forced Labor)
**Source file:** `reference/us-code/uscode/title-18-crimes-and-criminal-procedure/chapter-077-peonage-slavery-and-trafficking-in-persons.md`
**Book references:** ~20 mentions of the 13th Amendment loophole, convict leasing, involuntary servitude (Chapter 5, concentrated around lines 2176–2525)

**Why it matters:** The book's entire architecture hinges on the "except as punishment for crime" loophole. The federal code *nominally* criminalizes involuntary servitude (§1581, §1589) while simultaneously permitting it for prisoners. Quoting the actual statutory text makes this contradiction undeniable as primary-source evidence.

**Inline placement:** After the "System Kernel: The 13th Amendment Loophole" section header (~line 2176).
**Appendix placement:** New `\subsection*` in "Primary Statutory Sources."

---

## Priority 2 — The Controlled Substances Act (War on Drugs Engine)

**Statute:** 21 USC §812 (Schedules of controlled substances) and §841 (Prohibited acts A — manufacture/distribution)
**Source file:** `reference/us-code/uscode/title-21-food-and-drugs/chapter-013-drug-abuse-prevention-and-control.md`
**Book references:** Ehrlichman confession (~1276), cannabis scheduling (~3482), crack/powder disparity (~3435), Tameka Drummer (~3494), entire Chapter 8 War on Drugs arc

**Why it matters:** The CSA is the single most destructive statute in the book's argument — the "Variable Swap" from race to criminal status. The book discusses it extensively but never quotes the operative scheduling language or the prohibited-acts section that makes possession/distribution a federal crime. The statutory text is "race-neutral" — which is the *entire point* of the Variable Swap proof.

**Inline placement:** In the War on Drugs section (~line 3482), after the discussion of Schedule I classification.
**Appendix placement:** New `\subsection*` in "Primary Statutory Sources."

---

## Priority 3 — Federal Sentencing: Three-Strikes Mandatory Life

**Statute:** 18 USC §3559 (Sentencing classification of offenses) — subsection (c) covers "three strikes" mandatory life
**Source file:** `reference/us-code/uscode/title-18-crimes-and-criminal-procedure/chapter-227-sentences.md`
**Book references:** 1994 Crime Bill "three-strikes" (~4491), mandatory minimums (~4495), Tameka Drummer's life sentence (~3496)

**Why it matters:** The book discusses the 1994 Crime Bill's three-strikes provision and its devastating impact. Quoting §3559(c) shows readers the actual statutory machinery — the cold, bureaucratic text that converts a third felony into an automatic life sentence — juxtaposed with the human reality of Tameka Drummer.

**Inline placement:** Near the Crime Bill discussion (~line 4491) or the Drummer case (~line 3494).
**Appendix placement:** New `\subsection*` in "Primary Statutory Sources."

---

## Priority 4 — Civil Asset Forfeiture

**Statute:** 18 USC §981 (Civil forfeiture)
**Source file:** `reference/us-code/uscode/title-18-crimes-and-criminal-procedure/chapter-046-forfeiture.md`
**Book references:** "Bug #4 (due process exception) → civil asset forfeiture" (~line 1219, 1254)

**Why it matters:** The book identifies civil asset forfeiture as one of the four Constitutional "bugs" being exploited. Quoting the actual forfeiture statute shows how federal law enables property seizure without a criminal conviction — turning the due process clause into an extraction tool.

**Inline placement:** Near the Bug #4 diagram (~line 1254).
**Appendix placement:** New `\subsection*` in "Primary Statutory Sources."

---

## Priority 5 — Prison-Made Goods (Convict Labor Infrastructure)

**Statute:** 18 USC chapter 85 (Prison-Made Goods) — §§1761–1762
**Source file:** `reference/us-code/uscode/title-18-crimes-and-criminal-procedure/chapter-085-prison-made-goods.md`
**Book references:** Convict leasing analysis (~2187–2221), carceral bonds (~2458–2517)

**Why it matters:** The book's convict leasing analysis shows how prison labor persists as an extraction mechanism. The federal code regulates interstate commerce in prison-made goods — implicitly acknowledging that prison labor is a commodity. Quoting this text makes the "interface swap" from chattel slavery to carceral labor concrete at the statutory level.

**Inline placement:** In the carceral bonds section (~line 2458).
**Appendix placement:** New `\subsection*` in "Primary Statutory Sources."

---

## Priority 6 — Chinese Exclusion (Immigration as Racial Filter)

**Statute:** 8 USC chapter 7 (Exclusion of Chinese)
**Source file:** `reference/us-code/uscode/title-08-aliens-and-nationality/chapter-007-exclusion-of-chinese.md`
**Book references:** Page Act of 1875 (~line 1835), naturalization cycle diagram (~942, 962)

**Why it matters:** The book references the Page Act as the first racially gendered immigration restriction. The US Code still retains the historical codification of the Chinese Exclusion era provisions (many repealed/omitted, but the statutory scaffolding remains visible). Showing the actual text — even with "[Repealed]" annotations — powerfully illustrates how racial exclusion was *encoded* in federal law and later papered over.

**Inline placement:** Near the Page Act discussion (~line 1835).
**Appendix placement:** New `\subsection*` in "Primary Statutory Sources."

---

## Priority 7 — Wiretap Act (Domestic Surveillance Framework)

**Statute:** 18 USC §2511 (Interception and disclosure of wire, oral, or electronic communications prohibited)
**Source file:** `reference/us-code/uscode/title-18-crimes-and-criminal-procedure/chapter-119-wire-and-electronic-communications-interception-and-interception-of-oral-communications.md`
**Book references:** COINTELPRO wiretapping (~3297), RFK wiretap authorization of King (~3297), FISA already excerpted (~3394)

**Why it matters:** The book already includes the FISA *foreign intelligence* surveillance statute. Adding the *domestic* wiretap statute (Title III of the Omnibus Crime Control Act of 1968) completes the surveillance framework — showing both the legal tools the state used against COINTELPRO targets and the nominal "protections" that were routinely bypassed.

**Inline placement:** Near the COINTELPRO wiretap discussion (~line 3297).
**Appendix placement:** New `\subsection*` in "Primary Statutory Sources."

---

## Implementation Approach

Same pipeline as Phase 1:

1. Add 7 new entries to the `SNIPPETS` table in `tools/usc_extract.py`
2. Run `make usc-snippets` to generate `.tex` files under `Paper/usc_snippets/`
3. Add `\uscinline{}` calls at each inline placement point in `Paper/Redefining_Racism.tex`
4. Add corresponding `\subsection*` + `\label` + `\input` entries in the existing "Primary Statutory Sources" appendix
5. Build with `latexmk -pdf` and verify compilation
6. Update session log

---

## What This Plan Does NOT Add (and why)

| Statute | Reason for exclusion |
|---------|---------------------|
| Fair Housing Act (42 USC ch. 45) | Only one passing reference in the book (~line 1615); argumentative payoff too low |
| NVRA / Motor Voter (52 USC ch. 205) | VRA enforcement excerpt already covers voting theme sufficiently |
| RICO (18 USC ch. 96) | Book doesn't make a RICO argument; adding it would be a non sequitur |
| Community Reinvestment Act (12 USC ch. 30) | Redlining discussion is historical/spatial, not currently anchored to CRA text |
| HMDA (12 USC ch. 29) | Same — more of a data-reporting statute than a primary argument anchor |
| ADA (42 USC ch. 126) | Not part of the book's thesis |
| Eugenics compensation (42 USC ch. 160) | Fascinating but the book's eugenics discussion is historical/pre-statutory |

---

## Estimated Changes

- **`tools/usc_extract.py`**: 7 new SNIPPETS entries
- **`Paper/usc_snippets/`**: 7 new `.tex` files generated
- **`Paper/Redefining_Racism.tex`**: ~7 inline insertions + ~7 appendix entries
- **Build artifacts**: Updated `.pdf`, `.lof`, `.aux`, etc.
