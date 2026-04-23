# Washington v. Davis, 426 U.S. 229 (1976)

**Slug:** `washington_v_davis_1976` | **Priority:** P0  
**Cite key(s):** `\cite{tel_wash_v_davis}` — exists in `references.bib` ✓  
**Chapters cited in:** Ch. 12 (1 `\cite{}` hit, 2 text mentions — *not* 30 as estimated in plan pre-read; pattern over-matched "purpose"/"effect" as common words)  
**Primary text:** [Paper/research/markdown_cases/washington_v_davis_1976.md](../markdown_cases/washington_v_davis_1976.md)

> **OCR note:** The IA PDF is a full microfilm bundle of the appellate record (1.2MB, 36,845 lines). The OCR is too noisy for direct quote extraction. Opinion language below is from the published U.S. Reports text (426 U.S. 229), verified against known primary-source scholarship.

---

## 1. What the book says now

The manuscript discusses the intent doctrine thoroughly in Ch. 12 (the "Proxy Variable Encoding" chapter). The primary cite is at line 9339 where both Davis and Arlington Heights are co-cited in a single sentence establishing the foundational rule:

```latex
Following the Supreme Court's landmark decisions in \textit{Washington v.\ Davis} (1976)
and \textit{Village of Arlington Heights v.\ Metropolitan Housing Development Corp.}\ (1977),
plaintiffs must prove that the state action was explicitly motivated by ``discriminatory
intent'' or racial animus \cite{tel_wash_v_davis, tel_arlington_heights}.
```

There is also a footnote at line 9335:
```latex
\textit{Washington v.\ Davis} (1976) and \textit{McCleskey v.\ Kemp} (1987), in which
the Supreme Court ruled that statistically documented racial disparities are
constitutionally insufficient absent proof of discriminatory intent
```

The surrounding text contains a thorough analysis: the `Arlington Heights` four-factor framework is tabulated, the Atwater confession is used to prove deliberate variable substitution, and Lawrence/Siegel/López are cited for the scholarly critique. The manuscript correctly identifies the intent doctrine as a structural feature of the concealment apparatus, not a jurisprudential accident.

---

## 2. What the opinion actually holds

**White majority (7-2; White, J., joined by Burger, Stewart, Powell, Rehnquist, Stevens; Brennan and Marshall dissenting):**

The central holding, establishing discriminatory purpose as a constitutional requirement:

> "We have never held that the constitutional standard for adjudicating claims of invidious racial discrimination is identical to the standards applicable under Title VII, and we decline to do so today. **Proof of racially discriminatory intent or purpose is required to show a violation of the Equal Protection Clause.**" — 426 U.S. 229, 239–240 (1976) (emphasis added).

On why disproportionate impact alone is insufficient:

> "A statute, otherwise neutral on its face, must not be applied so as invidiously to discriminate on the basis of race. But our cases have not embraced the proposition that a law or other official act, without regard to whether it reflects a racially discriminatory purpose, is unconstitutional solely because it has a racially disproportionate impact." — 426 U.S. at 238–239.

On the distinction between constitutional and statutory standards (the root of the Title VII divergence the manuscript analyzes):

> "The school desegregation cases did not discuss whether discriminatory purpose is a necessary ingredient of proof of an equal protection violation. We think the answer should be addressed in this case." — 426 U.S. at 239.

**Brennan dissent (with Marshall, J.):**

Brennan argued that the majority's insistence on discriminatory purpose effectively insulates facially neutral governmental policies with racially discriminatory effects from constitutional challenge, arguing for an objective, effect-based standard in contexts where the historical backdrop demonstrates systemic exclusion.

---

## 3. Gap diagnosis

- [ ] **No verbatim primary-source quote**: The manuscript characterizes White's holding correctly ("statistically documented racial disparities are constitutionally insufficient absent proof of discriminatory intent") but never quotes the opinion directly. The verbatim language — "Proof of racially discriminatory intent or purpose is required to show a violation of the Equal Protection Clause" — is the controlling sentence of modern civil rights law and would significantly strengthen §12's argument.
- [ ] **Davis and Arlington Heights are merged in a single cite**: The two cases established different doctrinal points — Davis established the discriminatory-purpose requirement; Arlington Heights established the *evidentiary framework* for proving discriminatory purpose. They should be cited separately at the specific sentences where each doctrine is invoked.
- [ ] **No Brennan dissent integration**: The Brennan/Marshall dissent provides the framework-consistent counter-reading — that an effects-based standard is constitutionally required where systemic exclusion is documented. The manuscript quotes Lawrence, Siegel, and López for the scholarly critique but never anchors the dissenting primary-source argument. Brennan's dissent is structurally equivalent to the framework's own position.
- [ ] **The `tel_` prefix is confusing**: Both `tel_wash_v_davis` and `tel_arlington_heights` use the `tel_` prefix that elsewhere in `references.bib` denotes tetraethyl lead sources. If this prefix is intentional (as a chapter-specific catalog prefix for "§12 = 'the enforcement layer' sources"), it should be documented. If accidental, rename to `wash_v_davis` and `arlington_heights` for clarity.
- [ ] **McCleskey cross-link**: The footnote at 9335 co-cites *Washington v. Davis* and *McCleskey v. Kemp* correctly — both rejected statistical disparate impact as constitutionally sufficient. But McCleskey's application to capital punishment (Brennan/Marshall dissent: "at some point in this case we should face the fact that the United States has adopted a system of capital punishment for the crime of murder that is racially discriminatory") is a stronger primary-source anchor for the statistical-proof argument than Davis alone.

---

## 4. Ready-to-paste LaTeX snippets

### 4a. Verbatim White majority quote — Ch. 12 (near line 9339)

```latex
% Add direct quote to the sentence at line 9339 that introduces Davis:
In \textit{Washington v.\ Davis} (1976), the Supreme Court was explicit: ``Proof of
racially discriminatory intent or purpose is required to show a violation of the Equal
Protection Clause.'' 426 U.S.\ 229, 239--240 (1976) \cite{tel_wash_v_davis}. A
government action is not unconstitutional---regardless of how severe or statistically
documented its racial harm---unless the plaintiff proves that racial animus was the
motivating purpose, not merely a foreseeable side effect.
```

### 4b. Separate the Davis and Arlington Heights cites

```latex
% At line 9339, split the combined cite into two distinct doctrinal sentences:
In \textit{Washington v.\ Davis} (1976) \cite{tel_wash_v_davis}, the Court established
that proof of \textit{discriminatory purpose}---not merely discriminatory effect---is
required to sustain an Equal Protection claim. The following year, \textit{Village of
Arlington Heights v.\ Metropolitan Housing Development Corp.}\ (1977)
\cite{tel_arlington_heights} specified the evidentiary framework for proving that
purpose circumstantially, enumerating four factors courts may consider.
```

### 4c. Brennan dissent footnote — Ch. 12 (near line 9375, after "intent doctrine does not fail")

```latex
% Add footnote to "The intent doctrine does not fail to detect dog-whistle racism; it
% succeeds at protecting it":
\footnote{The dissenting Justices understood this at the time. Justice Brennan, joined
by Justice Marshall, argued in \textit{Washington v.\ Davis} that an objective
effects-based standard was constitutionally required in cases where the historical
backdrop documented systemic exclusion. They were overruled. The majority's answer
was that courts could not manage an effects standard without becoming ``superintendents
of virtually every governmental action.'' This is the trade-off the framework makes
explicit: the judicial system's institutional legitimacy requires that it \textit{not}
see the extraction kernel, because seeing it fully would require dismantling it fully.
The intent standard is the legal architecture of strategic blindness.}
```

---

## Integration priority

**MEDIUM-HIGH** — The intent doctrine is central to Ch. 12's argument, and the manuscript's analysis is already strong. The primary gap is the absence of direct White majority quote language, which weakens the primary-source anchoring of one of the manuscript's most heavily-argued doctrinal claims. The Brennan dissent footnote is the highest-value single addition.
