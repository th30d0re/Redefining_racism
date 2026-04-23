# Village of Arlington Heights v. Metropolitan Housing Development Corp., 429 U.S. 252 (1977)

**Slug:** `village_of_arlington_heights_v_metropolitan_housing_development_corp_1977` | **Priority:** P1  
**Cite key(s):** `\cite{tel_arlington_heights}` — exists in `references.bib` ✓  
**Chapters cited in:** Ch. 12 (co-cited with Washington v. Davis for the intent doctrine), with Table 12.x displaying the four-factor framework applied to highway routing  
**Primary text:** [Paper/research/markdown_cases/village_of_arlington_heights_v_metropolitan_housing_development_corp_1977.md](../markdown_cases/village_of_arlington_heights_v_metropolitan_housing_development_corp_1977.md)

> **OCR note:** The IA PDF is a full microfilm appellate bundle (67,521 lines). Too noisy for direct quote extraction. Opinion language below is from the published 429 U.S. 252 text.

---

## 1. What the book says now

The manuscript's Arlington Heights analysis is in Ch. 12 Table (lines ~9341–9360). The tabulation presents four factors:

| Factor | Application |
|--------|-------------|
| Disproportionate Impact | highways disproportionately displaced Black residents |
| Historical Background | Redlining preceded highway placement |
| Procedural Departures | Planners cancelled hearings in Black neighborhoods |
| Contemporary Statements | Miami planners citing "continued whiteness of central Miami" |

The table is used to demonstrate that the Arlington Heights framework is "hermetically sealed" against structural racism claims — each factor is either legally insufficient alone or unobtainable.

---

## 2. What the opinion actually holds

**Powell majority (7-1-1; Powell, joined by Burger, Stewart, White, Blackmun, Rehnquist; Marshall concurring in part; Brennan and Stevens recused):**

The Powell majority established the multi-factor evidentiary framework for proving discriminatory purpose circumstantially:

> "Determining whether invidious discriminatory purpose was a motivating factor demands a sensitive inquiry into such circumstantial and direct evidence of intent as may be available. The impact of the official action whether it 'bears more heavily on one race than another' may provide an important starting point. Sometimes a clear pattern, unexplainable on grounds other than race, emerges from the effect of the state action even when the governing legislation appears neutral on its face." — 429 U.S. 252, 266 (1977).

The five Powell factors (the manuscript's table omits the fifth):
1. **Disproportionate impact** — "may provide an important starting point"
2. **Historical background** — "the historical background of the decision is one evidentiary source, particularly if it reveals a series of official actions taken for invidious purposes"
3. **Sequence of events** — "the specific sequence of events leading up to the challenged decision also may shed some light"
4. **Departures from normal procedures** — "departures from the normal procedural sequence also might afford evidence"
5. **Legislative or administrative history** — "the legislative or administrative history may be highly relevant, especially where there are contemporary statements by members of the decisionmaking body"

Powell also emphasized: "A plaintiff does not make out a violation of the Equal Protection Clause simply by showing that an official action has a discriminatory effect."

---

## 3. Gap diagnosis

- [x] **Manuscript's four-factor tabulation is accurate but incomplete**: The manuscript's Table correctly lists four factors (impact, historical background, departures, contemporary statements). However, Powell's framework has **five** factors — the "specific sequence of events leading up to the challenged decision" is omitted. This is a minor gap but affects the claim that the table is a comprehensive presentation of the framework.
- [ ] **Merge "departures" and "legislative history"**: The manuscript's third factor ("Procedural Departures") correctly captures Powell's fourth factor, but the manuscript omits Powell's fifth factor (legislative/administrative history — "particularly… where there are contemporary statements by members of the decisionmaking body"). The table should include both.
- [x] **Quote verified**: The manuscript accurately characterizes the holding — plaintiffs must prove discriminatory purpose, and disproportionate impact alone is insufficient. No mischaracterization.
- [ ] **Cross-link to Washington v. Davis memo**: Davis established the discriminatory-purpose requirement; Arlington Heights specified how to prove it. The two cases are correctly co-cited in the manuscript but never analyzed in tandem. A brief note on the Davis → Arlington Heights doctrinal sequence would clarify the constitutional architecture.

---

## 4. Ready-to-paste LaTeX snippets

### 4a. Add the missing fifth factor to Table 12.x

```latex
% In the Arlington Heights table, add row after "Contemporary Statements":
\textbf{Sequence of Events} & The specific sequence leading to the challenged
decision, which may reveal a pattern of exclusion the decisionmaker was aware of.
(Very difficult to document without extensive discovery; rarely available to plaintiffs
challenging infrastructure decisions taken decades earlier.)\\
```

### 4b. Verbatim Powell quote footnote — Ch. 12 (near the intent-doctrine section)

```latex
\footnote{Powell, J., for the Court: ``Determining whether invidious discriminatory
purpose was a motivating factor demands a sensitive inquiry into such circumstantial
and direct evidence of intent as may be available. The impact of the official action
whether it `bears more heavily on one race than another' may provide an important
starting point.'' \textit{Village of Arlington Heights v.\ Metropolitan Housing
Development Corp.}, 429 U.S.\ 252, 266 (1977) \cite{tel_arlington_heights}.
Powell's phrase ``important starting point'' is the tell: disproportionate impact is
not a sufficient terminal condition; it merely opens the inquiry. Every subsequent
factor requires evidence that is either too remote, too recent to apply to historical
infrastructure decisions, or routinely laundered through race-neutral bureaucratic
language.}
```

---

## Integration priority

**LOW-MEDIUM** — The manuscript's Arlington Heights treatment is accurate and structurally sound. The missing fifth factor (§4a) is a precision gap, not a mischaracterization. The Powell verbatim quote (§4b) would strengthen the footnote architecture.
