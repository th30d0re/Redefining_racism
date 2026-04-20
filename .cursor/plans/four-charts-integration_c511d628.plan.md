---
name: four-charts-integration
overview: Add four TikZ/pgfplots figures to Paper/Redefining_Racism.tex — one in each of the four sections created during the Du Bois/AJR integration — then rebuild the PDF.
todos:
  - id: chart1_general_strike
    content: Insert General Strike causal-reversal flow diagram after the General Strike subsection (before line 2791 The System Kernel)
    status: pending
  - id: chart2_cannibalization
    content: Insert Cannibalization phase-transition dual-line pgfplots chart after the Venice/Rome paragraph (before line 6333 The Recursive Extraction Engine)
    status: pending
  - id: chart3_acemoglu_venn
    content: Insert Acemoglu Limit nested-ellipse Venn diagram at end of the Acemoglu Limit subsection (before line 7648 The Constitutional Shield)
    status: pending
  - id: chart4_abolition_map
    content: Insert Abolition Democracy two-column connector diagram after the enumerated list (before closing paragraph at line 8518)
    status: pending
  - id: build_charts
    content: Run two-pass pdflatex build and verify all new labels resolve
    status: pending
  - id: log_charts
    content: Create session log at __Avenue/harper/logs/session-YYYY-MM-DD-HHMMSS.md
    status: pending
isProject: false
---

# Four Remaining Charts Plan

## Context

All four insertion points are in [Paper/Redefining_Racism.tex](Paper/Redefining_Racism.tex). The book already uses TikZ + pgfplots extensively (50+ figures); all four charts follow existing style patterns. Each chart is inserted at the **end** of its host section/subsection, just before the next `\section` or `\subsection` heading.

---

## Chart 1 — General Strike Causal Timeline
**Type:** Horizontal TikZ flow diagram (same style as existing Fig. 1 causal-reversal diagram, lines 207–242)

**Where:** End of `\subsection{The General Strike of the Enslaved}` at line 2790, immediately before `\section{The System Kernel: The 13th Amendment Loophole}`.

**Visual argument:** Two rows.
- Top row (struck through, red): Conventional narrative arrow — *Lincoln issues Emancipation* → *Enslaved people freed* → *13th Amendment*
- Bottom row (green, correct): Actual causal sequence — *500k self-emancipate (1861–64)* → *Confederate labor/logistics collapse* → *Emancipation Proclamation (1863, institutional recognition)* → *13th Amendment (kernel recompile)*
- A "Causal Reversal" double arrow separating the two rows
- Caption makes the framework claim explicit: Out-group kinetic action forced the legal patch; the legal patch was not the cause.

**Label:** `fig:general_strike_causal`

---

## Chart 2 — Cannibalization Phase Transition
**Type:** pgfplots dual-line chart (same style as existing "Memory Gap" chart, lines 2806–2850)

**Where:** End of the Venice/Rome AJR paragraph at line 6322, immediately before `\section{The Recursive Extraction Engine}` (line 6333).

**Visual argument:** X-axis = time (indexed schematically: Pre-Civil War → Reconstruction → Jim Crow → Civil Rights → Present). Two lines:
- Solid dark red: Extraction from $O_{\text{racialized}}$ (rises, plateaus, then declines as capacity depletes)
- Dashed orange: Extraction from $I_{\text{buffer}}$ (flat, then rises sharply as first line saturates)
- A vertical dashed line labeled "Cannibalization Inflection" marking where the curves cross — this is the book's claim about the present moment
- Shaded region right of the inflection labeled "Current Phase: $I_{\text{buffer}}$ being consumed"
- Historical callout dots: Venice Serrata (1297), opioid crisis onset (~2000), Ruby Ridge/Waco (1992–94)

**Label:** `fig:cannibalization_phase`

---

## Chart 3 — Acemoglu Limit: Model Subset Diagram
**Type:** TikZ nested-ellipse (Venn-style) diagram

**Where:** End of the Acemoglu Limit subsection at line 7646, immediately before `\section{The Constitutional Shield}` (line 7648).

**Visual argument:** Three nested ellipses:
- Outermost: "This Book's Framework: Full Five-Tier Model" — contains all variables
- Middle: "AJR's Model: Elite Capture + Extractive Institutions" — correct at the descriptive level, missing three variables (labeled outside): $\psi$ (psychological wage), racial partition ($I_{\text{buffer}}$ vs. $O_{\text{racialized}}$), kinetic-guarantee asymmetry
- Innermost (small): "AJR's Special Case: Concession Theorem with $\psi=0$, no partition" — the condition under which AJR's prescription actually works
- A label at the outermost ring: "The patch requires the outer ring"
- A label at the middle ring: "AJR diagnoses here" with a note: "Reform prescription assumes here = outer ring"

**Label:** `fig:acemoglu_limit_venn`

---

## Chart 4 — Abolition Democracy ↔ Open-Source Republic Mapping
**Type:** TikZ two-column connector diagram

**Where:** After the enumerated list at line 8516, immediately before the closing paragraph of the Abolition Democracy subsection (before line 8518: "The Open-Source Republic is, in structural terms...").

**Visual argument:** Two columns connected by horizontal arrows:
- Left column (Du Bois 1935): four labeled boxes — Land Redistribution, Universal Public Education, Universal Suffrage, Federal Civil Rights Enforcement
- Right column (Open-Source Republic 2026): four matched boxes — Hard-Cap on $\max$ Variable, Algorithmic Transparency Laws, Dismantling the Tweedism Filter, 18 U.S.C. §242 + Abolition of Immunity
- Center column (thin, shaded): "Failed Because (1877)" with a short label for each row's failure mechanism — $\psi$ kept $I_{\text{buffer}}$ aligned with E / Redeemer govts defunded schools / White Primary + literacy tests / Federal troops withdrawn
- Caption: "The Open-Source Republic is the mathematical completion of Du Bois's 1935 specification. The center column records why Reconstruction's first attempt at each plank failed — and which variable the framework adds to prevent the same recompilation."

**Label:** `fig:abolition_democracy_map`

---

## Execution Order

1. Chart 1 (General Strike) — line 2790 insertion
2. Chart 2 (Cannibalization) — line 6322 insertion
3. Chart 3 (Acemoglu Limit Venn) — line 7646 insertion
4. Chart 4 (Abolition Democracy map) — line 8516 insertion
5. Two-pass `pdflatex` build to resolve all new `\label`/`\ref` entries
6. Session log at `__Avenue/harper/logs/session-YYYY-MM-DD-HHMMSS.md`

## Out of scope
- No changes to existing figures, chapter structure, or equation numbering
- No edits to podcast_prompts or equation_infographic_prompts