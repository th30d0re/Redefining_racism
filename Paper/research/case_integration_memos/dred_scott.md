# Dred Scott v. Sandford, 60 U.S. (19 How.) 393 (1857)

**Slug:** `dred_scott_v_sandford_1857` | **Priority:** P0  
**Cite key(s):** `\cite{dredscott}`, `\cite{fehrenbacher}` — both exist in `references.bib` ✓  
**Chapters cited in:** Ch. 10 (1 `\cite{dredscott, fehrenbacher}` hit at line ~1702), Ch. 2 (footnote text mention, no cite), Ch. 10 §Weaponizing Disarmament (text quote, **no cite**)  
**Primary text:** [Paper/research/markdown_cases/dred_scott_v_sandford_1857.md](../markdown_cases/dred_scott_v_sandford_1857.md)  
**Source quality:** Re-pulled from Project Gutenberg EBook #31425 (full 675KB text, 11,058 lines — Taney majority + all six concurrences/dissents including McLean and Curtis dissents)

---

## 1. What the book says now

**Ch. 10 — Bug #1 section (line ~1702):**
```latex
In \textit{Dred Scott v.\ Sandford} (1857), Chief Justice Taney demonstrated how
Bug \#1 (undefined ``the people'') could be exploited \cite{dredscott, fehrenbacher}.
He excluded Black people from ``the people,'' declaring they ``had no rights which the
white man was bound to respect,'' explicitly noting that inclusion would grant them the
right to bear arms---``an outcome he found unacceptable.''
```

**Ch. 10 — Weaponizing Disarmament subsection (line ~3110):**
```latex
To justify this, he revealed the core algorithmic fear of the Elite: if Black people
were granted citizenship, it would entitle them to the full privileges of the In-group,
which would give them the right "to keep and carry arms wherever they went."
```
→ **NO `\cite{dredscott}` in this passage.** The direct Taney quote appears here without citation.

**Ch. 2 footnote (line ~1208):**
```latex
the permanent and heritable phenotypic lock is documented by the 1662 Virginia
\textit{partus sequitur ventrem} statute … and confirmed across 195 years through
\textit{Dred Scott} (1857).
```
→ Text mention, no cite.

---

## 2. What the opinion actually holds

**Taney majority (7-2; Wayne, Nelson, Grier, Daniel, Campbell, Catron concurring; McLean and Curtis dissenting):**

The "parade of horribles" — Taney's enumeration of what would happen if Black people were citizens (the structural 2A passage):

> "It would give to persons of the negro race, who were recognised as citizens in any one State of the Union, the right to enter every other State whenever they pleased, singly or in companies, without pass or passport, and without obstruction, to sojourn there as long as they pleased, to go where they pleased at every hour of the day or night without molestation, unless they committed some violation of law for which a white man would be punished; and it would give them the full liberty of speech in public and in private upon all subjects upon which its own citizens might speak; to hold public meetings upon political affairs, and to **keep and carry arms wherever they went**. And all of this would be done in the face of the subject race of the same color, both free and slaves, and inevitably producing discontent and insubordination among them, and endangering the peace and safety of the State." — 60 U.S. at 416–417.

The "no rights" passage (used extensively in manuscript):

> "They had for more than a century before been regarded as beings of an inferior order, and altogether unfit to associate with the white race, either in social or political relations; and so far inferior, that **they had no rights which the white man was bound to respect**; and that the negro might justly and lawfully be reduced to slavery for his benefit." — 60 U.S. at 407.

The independent 2A holding in the Missouri Compromise analysis (a separate passage):

> "Nor can Congress deny to the people the right to keep and bear arms, nor the right to trial by jury, nor compel any one to be a witness against himself in a criminal proceeding." — 60 U.S. at 451.

---

## 3. Gap diagnosis

- [x] **Missing cite at Ch. 10 Weaponizing Disarmament (line ~3110)**: The direct Taney quote "to keep and carry arms wherever they went" appears with NO `\cite{dredscott}`. This is the manuscript's single most important structural Dred Scott argument, and it is uncited.
- [x] **False quotation marks in Ch. 10 Bug #1 section**: The manuscript (line ~1702) puts "an outcome he found unacceptable" in quotation marks. This is NOT a Taney quote — Taney never uses this phrase. His stated concern is that armed Black citizens would produce "discontent and insubordination among them, and endangering the peace and safety of the State." The false-quote framing should be corrected to paraphrase or the actual Taney language should be substituted.
- [ ] **Ch. 2 footnote cite missing**: The footnote at line ~1208 names *Dred Scott* but has no `\cite{dredscott}`. Every case citation should be anchored.
- [ ] **Missouri Compromise 2A passage unused**: The second 2A passage (line ~2577 in our MD) — "Nor can Congress deny to the people the right to keep and bear arms" — is Taney's holding on Congressional power in the territories. This passage is actually the stronger statement of the case's 2A doctrine (it is a direct constitutional holding, not merely a parade-of-horribles hypothetical) but the manuscript only cites the parade-of-horribles passage. The Missouri Compromise passage would strengthen the Ch. 10 2A historical-architecture argument.
- [ ] **Curtis dissent (pro-citizenship) not cited**: Justice Curtis's dissent establishes the counter-reading — that Black people were citizens at the founding, with a documented historical record. This is the structural counter-reading the framework would want to cite as evidence that the racial exclusion was contested and constructed, not natural. Curtis's dissent was sufficiently powerful that Taney changed his majority opinion after seeing it — a fact documented by Fehrenbacher that the manuscript could use.

---

## 4. Ready-to-paste LaTeX snippets

### 4a. Fix missing cite at Ch. 10 Weaponizing Disarmament (line ~3110)

```latex
% At line ~3110, add \cite after the Taney quote:
To justify this, he revealed the core algorithmic fear of the Elite: if Black people
were granted citizenship, it would entitle them to the full privileges of the In-group,
which would give them the right ``to keep and carry arms wherever they went''
\cite{dredscott}---``inevitably producing discontent and insubordination among them,
and endangering the peace and safety of the State.'' 60 U.S.\ 393, 416--417 (1857).
```

### 4b. Fix false quotation in Ch. 10 Bug #1 (line ~1702)

```latex
% Replace: explicitly noting that inclusion would grant them the right to bear arms---
%           ``an outcome he found unacceptable.''
% With:
explicitly noting that inclusion would mean they could ``keep and carry arms wherever
they went''---an outcome Taney characterizes as inevitably ``endangering the peace and
safety of the State.'' \textit{Dred Scott}, 60 U.S.\ at 416--417 \cite{dredscott}.
```

### 4c. Add cite to Ch. 2 footnote (line ~1208)

```latex
% In the Ch. 2 footnote, add cite after "Dred Scott (1857)":
confirmed across 195 years through \textit{Dred Scott} (1857) \cite{dredscott}.
```

### 4d. Missouri Compromise 2A passage — Ch. 10 (after the "keep and carry" passage)

```latex
% Add to Ch. 10 §Weaponizing Disarmament, after the existing Taney quote:
Taney's parade of horribles was not merely dicta. The same opinion contained a
\textit{holding} on Congressional power equally explicit about the Second Amendment's
scope: ``Nor can Congress deny to the people the right to keep and bear arms.''
60 U.S.\ at 451. In the same ruling that excluded Black people from ``the people,''
Taney simultaneously reaffirmed that ``the people'' retain an absolute right to arms
that Congress cannot abridge. The exclusion and the guarantee are two clauses of the
same operational formula: define ``the people'' narrowly, and the kinetic guarantee
distributes narrowly. Expand ``the people,'' and the kinetic guarantee expands with it.
The \textit{Dred Scott} opinion is therefore not merely a precedent about citizenship;
it is the kernel's operating manual for managing the relationship between the
definitional scope of constitutional personhood and the distribution of lethal capacity.
```

---

## Integration priority

**HIGH** — The missing `\cite{dredscott}` at the "keep and carry arms" passage (§4a) is the single highest-priority fix in the entire Tier-1 set. The false quotation marks (§4b) is a correctness issue. The Missouri Compromise passage (§4d) is an expansion opportunity that would significantly strengthen the Ch. 10 2A historical argument.
