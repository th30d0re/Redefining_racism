---
name: dubois-acemoglu-integration
overview: Integrate W.E.B. Du Bois's Black Reconstruction (five core concepts beyond the psychological wage) and Acemoglu & Robinson's Why Nations Fail (both as corroboration and as engaged critique) into Redefining_Racism.tex across seven chapters, with one new bibliography entry and five new subsections.
todos:
  - id: bib
    content: Add \bibitem{acemoglu_robinson} after \bibitem{dubois} in the bibliography
    status: completed
  - id: portugal_ajr
    content: "Ch. Portugal: add extractive-institutions corroboration paragraph + \\cite{acemoglu_robinson}"
    status: completed
  - id: propaganda_history
    content: "Ch. Redefining Racism + Gaslighting: add 'Propaganda of History' framing paragraphs citing Du Bois"
    status: completed
  - id: general_strike
    content: "Ch. Enforcement Engine: insert new \\subsection 'The General Strike of the Enslaved' before the 13th Amendment section"
    status: completed
  - id: counter_revolution_containment
    content: "Ch. Containment: expand intro with Counter-Revolution of Property paragraph; enrich Pullman section with Du Bois prior-art footnote"
    status: completed
  - id: tweedism_ajr
    content: "Ch. Tweedism: add AJR 'economic-elite capture' citation to chapter intro"
    status: completed
  - id: acemoglu_limit
    content: "Ch. Contradiction: insert Counter-Revolution anchor in Concession Theorem list + new \\subsection 'The Acemoglu Limit' before The Constitutional Shield"
    status: completed
  - id: cannibalization_venice
    content: "Ch. Cannibalization: add Venice/Rome extractive-collapse precedent paragraph citing AJR"
    status: completed
  - id: global_containment_ajr
    content: "Ch. Global Containment: add AJR citations to Imperial Core Theorem and Imperial Extraction Archive sections"
    status: completed
  - id: abolition_democracy
    content: "Ch. Post-Kinetic Horizon: insert new \\subsection 'Abolition Democracy: Du Bois's Unfinished Kernel' under Architecture of the Open-Source Republic"
    status: completed
  - id: critical_junctures
    content: "Ch. Redefining Racism Diagnostic Model: add critical-junctures footnote mapping Runtime Logs to AJR's framework"
    status: completed
  - id: build_pdf
    content: Rebuild Paper/Redefining_Racism.pdf after all edits
    status: completed
  - id: log
    content: Create session log at __Avenue/harper/logs/session-YYYY-MM-DD-HHMMSS.md per user rule
    status: completed
isProject: false
---

## Context

Current state in [Paper/Redefining_Racism.tex](Paper/Redefining_Racism.tex):
- `\bibitem{dubois}` exists (line 8876); Du Bois is cited 8x but only for the "public and psychological wage"
- Acemoglu & Robinson: zero citations, no `\bibitem`, no term "extractive institutions" anywhere in the `.tex`

Target: add five Du Bois concepts and both supportive + critical engagement with Why Nations Fail.

---

## Part A — Du Bois (five new concepts)

### A1. General Strike of the Enslaved → Ch. Enforcement Engine
**Where:** Insert new subsection in [Paper/Redefining_Racism.tex](Paper/Redefining_Racism.tex) immediately before line 2670 (`\section{The System Kernel: The 13th Amendment Loophole (1865)}`).

**New subsection title:** `\subsection{The General Strike of the Enslaved: Du Bois's Proof of Out-Group Kinetic Agency}`

**Content (~3 paragraphs):** Du Bois's core claim in Black Reconstruction ch. 4 — that the self-emancipation of ~500,000 enslaved people during the Civil War constituted a *general strike* that decisively tipped Union victory — is the framework's missing kinetic-agency proof for 1863–1865. Connect to:
- The Concession Theorem section [Paper/Redefining_Racism.tex:7461](Paper/Redefining_Racism.tex) (Emancipation-as-military-necessity) — add `\cite{dubois}` there with a forward reference.
- Reinforces the Haitian Theorem (line 7682) by showing the general-strike mechanism operated domestically too.

### A2. Counter-Revolution of Property → Ch. Containment + Concession Theorem
**Where 1:** Expand introductory paragraphs of Ch. Containment at [Paper/Redefining_Racism.tex:3124-3127](Paper/Redefining_Racism.tex) with a paragraph invoking Du Bois's thesis that Reconstruction was overthrown not by racism-first but by Northern capital recognizing that Black-led multiracial democracy threatened industrial extraction.

**Where 2:** Add new subsection in Ch. The Contradiction at line 7454 `\section{The Concession Theorem: Historical Proof}`, between items 4 (Civil Rights Act) and 5 (Fair Sentencing Act), or as an anchor paragraph preceding the enumerated list: show Reconstruction (1865–1877) as the clearest historical instance of $\Delta\max = 0$ — reforms enacted, then property reasserted.

**Content:** Du Bois's core reframe: Reconstruction was not a failure of Black governance but a successful counter-revolution by Northern capital + Southern Redeemer elite. Direct ancestor of the book's "Elite uses racial division to dissolve interracial democracy" thesis.

### A3. Abolition Democracy → Ch. Post-Kinetic Horizon
**Where:** New subsection in [Paper/Redefining_Racism.tex:8342](Paper/Redefining_Racism.tex) `\section{The Architecture of the Open-Source Republic}`, inserted after `\subsection{The Systematic Reset and the Amendment Paradox}` (line 8346) and before `\subsection{The Interface War}` (line 8352).

**New subsection title:** `\subsection{Abolition Democracy: Du Bois's Unfinished Kernel}`

**Content:** Du Bois defined Abolition Democracy as requiring four planks — (1) land redistribution (40-acres-and-a-mule), (2) universal public education, (3) universal suffrage, (4) federal enforcement of civil rights. Map each plank to the existing Open-Source Republic patches (§8388 `Hard-Capping the $\max$ Variable`, §8387 transparency laws, §8379 dismantling Tweedism Filter, §8374 enforcement of 18 U.S.C. § 242). Frames the Open-Source Republic as the mathematical completion of Du Bois's 1935 specification.

### A4. "Propaganda of History" → Ch. Redefining Racism + Ch. Gaslighting
**Where 1:** Add a paragraph to Ch. Redefining Racism near [Paper/Redefining_Racism.tex:169-172](Paper/Redefining_Racism.tex) introducing Du Bois's "Propaganda of History" (final chapter of Black Reconstruction) as the prior-art diagnosis of $P_{\text{gaslight}}$.

**Where 2:** Anchor paragraph inside `\section{Racial Gaslighting}` at [Paper/Redefining_Racism.tex:7908](Paper/Redefining_Racism.tex), citing Du Bois's account of how Dunning-school historiography erased Black agency — explicit prior art for the gaslighting variable.

### A5. Black Worker Agency / Solidarity Failures → Pullman + Class-Solidarity Antidote
**Where 1:** Enrich Pullman section at [Paper/Redefining_Racism.tex:3136-3138](Paper/Redefining_Racism.tex) with a short footnote or inline citation: Du Bois's Black Reconstruction ch. 17 ("The Propaganda of History") and ch. 7 ("Looking Backward") already diagnosed the ARU pattern — white labor's refusal of cross-racial solidarity — in the 1880s Knights of Labor collapse.

**Where 2:** Add `\cite{dubois}` to `\section{Class Solidarity as the Algorithmic Antidote}` at [Paper/Redefining_Racism.tex:4461](Paper/Redefining_Racism.tex).

---

## Part B — Acemoglu & Robinson (both supportive + critique)

### B0. New bibliography entry
Insert after `\bibitem{dubois}` at [Paper/Redefining_Racism.tex:8876](Paper/Redefining_Racism.tex):

```latex
\bibitem{acemoglu_robinson}
Acemoglu, D., and Robinson, J.A. \textit{Why Nations Fail: The Origins of Power, Prosperity, and Poverty}. New York: Crown Business, 2012.
```

### B1. Supportive: Ch. Portugal — extractive institutions corroboration
**Where:** [Paper/Redefining_Racism.tex:833](Paper/Redefining_Racism.tex) (end of the "industrialized global architecture" paragraph, before `\section{Portuguese Class Dynamics}`).

**Content:** One-paragraph note that Acemoglu & Robinson independently identify the Portuguese Atlantic system as the textbook case of *extractive institutions* — corroboration from mainstream economics. Cite `\cite{acemoglu_robinson}`. Then foreshadow the critique (deferred to Ch. Contradiction): AJR's model lacks the racial-partition and psychological-wage variables required to explain why extractive institutions become structurally self-perpetuating rather than merely inefficient.

### B2. Supportive: Ch. Global Containment — Imperial Core Theorem
**Where:** [Paper/Redefining_Racism.tex:8304](Paper/Redefining_Racism.tex) `\section{The Imperial Core Theorem}` and [Paper/Redefining_Racism.tex:8065](Paper/Redefining_Racism.tex) `\section{The Imperial Extraction Archive}`.

**Content:** Map AJR's extractive/inclusive dichotomy onto the 5-tier international hierarchy. Use their Nogales/Mexico-US border example as a miniature proof. Cite `\cite{acemoglu_robinson}` twice.

### B3. Supportive: Critical Junctures → runtime-log framing
**Where:** Footnote or short paragraph in Ch. Redefining Racism `\section{The Diagnostic Model: Racism as a Fractal Computer Virus}` at [Paper/Redefining_Racism.tex:359](Paper/Redefining_Racism.tex), OR inside the Equation Registry era calibration at [Paper/Redefining_Racism.tex:8698](Paper/Redefining_Racism.tex).

**Content:** The book's Runtime Logs (1486, 1676, 1705, 1787, 1803, 1865, 1934, 1964, 1968, 1994) correspond one-to-one with AJR's "critical junctures." The framework's version-update model operationalizes what AJR left conceptual.

### B4. CRITIQUE: Ch. The Contradiction — "The Acemoglu Limit"
**Where:** New subsection inserted in [Paper/Redefining_Racism.tex](Paper/Redefining_Racism.tex) between line 7500 and line 7502, i.e., between the Concession Theorem's closing paragraph and `\section{The Constitutional Shield}`.

**New subsection title:** `\subsection{The Acemoglu Limit: Why ``Inclusive Institutions'' Cannot Recompile Without Dismantling the Racial Partition}`

**Content (~4–5 paragraphs):**
- Acknowledge AJR's correct identification of extractive institutions and elite capture.
- State the critique: AJR's prescription (build "inclusive institutions" via pluralism + centralized state) is structurally insufficient in any system where a racial partition has already been installed, because the psychological wage ($\psi$) and the kinetic-guarantee asymmetry (Second Amendment/Haitian proof) cause every "inclusive" reform to recompile back into extraction via the Concession Theorem.
- Show that AJR's "iron law of oligarchy" is a *special case* of the Concession Theorem with $\psi = 0$ and no racial partition.
- Identify the three variables AJR's model is missing: $\psi$ (psychological wage), the racial partition ($I_{\text{buffer}}$ vs $O_{\text{racialized}}$), and the kinetic guarantee asymmetry.
- Conclude: Why Nations Fail diagnoses the disease; it cannot write the patch, because the patch requires the full five-tier framework developed in this book.

### B5. Supportive: Ch. Cannibalization — extractive systems self-consume
**Where:** [Paper/Redefining_Racism.tex:6193](Paper/Redefining_Racism.tex) `\section{The Collapse: Cannibalizing the In-Group}` — add one paragraph citing AJR's historical cases (Venice's *Serrata* and Book of Gold; Rome's latifundia collapse) as empirical precedents for the extraction-kernel eventually turning on its own In-group.

### B6. Supportive: Ch. Tweedism — economic-elite capture of political institutions
**Where:** [Paper/Redefining_Racism.tex:3408](Paper/Redefining_Racism.tex) `\chapter{Tweedism and the Puppet Class}` introduction (first paragraphs).

**Content:** Brief `\cite{acemoglu_robinson}` tying their concept of "economic elites capturing political institutions" to the Green Primary ($P_{\text{uppet}}$ filter) — but noting that AJR never formalize the filter math.

---

## Summary of edits

- New `\bibitem`: 1 (`acemoglu_robinson`)
- New `\subsection`: 3 (General Strike, Abolition Democracy, The Acemoglu Limit)
- Expanded section intros: 3 (Ch. Containment, Ch. Tweedism, Ch. Post-Kinetic Horizon)
- Added paragraphs/footnotes: 4 (Redefining Racism intro, Portugal, Global Containment, Cannibalization)
- Inline citation adds: ~8 additional `\cite{dubois}` and ~6 additional `\cite{acemoglu_robinson}` hooks

## Out of scope / explicit non-goals

- No restructuring of existing chapter order.
- No re-compilation of the `.lof` / `.pdf` in the plan (will regenerate only after edits are approved and applied).
- No changes to equation numbering (new material will reference existing equations; any new equations will be placed at the end of the sequence).
- No edits to podcast_prompts, equation_infographic_prompts, or the `__Avenue/harper/logs/` — those are separate workstreams.

## Execution order (when plan is approved)

1. Add `\bibitem{acemoglu_robinson}`.
2. Ch. Portugal: add one paragraph + cite (B1).
3. Ch. Redefining Racism + Gaslighting: Propaganda of History paragraphs (A4).
4. Ch. Enforcement Engine: General Strike subsection (A1).
5. Ch. Containment: Counter-Revolution paragraph + Pullman cite (A2 part 1, A5).
6. Ch. Tweedism: AJR intro cite (B6).
7. Ch. Contradiction: Counter-Revolution anchor + "The Acemoglu Limit" subsection (A2 part 2, B4).
8. Ch. Cannibalization: Venice/Rome precedent (B5).
9. Ch. Global Containment: Imperial Core + Extraction Archive cites (B2).
10. Ch. Post-Kinetic Horizon: Abolition Democracy subsection (A3).
11. Critical Junctures framing (B3) — last, because it touches the early diagnostic model and should be written after the later chapters are finalized for cross-references.
12. After edits: run the user's existing LaTeX build to regenerate `Paper/Redefining_Racism.pdf`.
13. Create session log at `__Avenue/harper/logs/session-YYYY-MM-DD-HHMMSS.md` per the user's logging rule.