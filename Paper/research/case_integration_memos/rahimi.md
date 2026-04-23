# United States v. Rahimi, 602 U.S. ___ (2024)

**Slug:** `united_states_v_rahimi_2024` | **Priority:** P0  
**Cite key(s):** `\cite{rahimi2024}` — exists in `references.bib` ✓  
**Chapters cited in:** Ch. 8 (data table footnote), Ch. 9 (multiple analytical references)  
**Primary text:** [Paper/research/markdown_cases/united_states_v_rahimi_2024.md](../markdown_cases/united_states_v_rahimi_2024.md)

---

## 1. What the book says now

The manuscript's Rahimi analysis is in Ch. 9 (lines ~9008–9043). Key characterizations:

**Line 9010 (precise analytical note):**
> "A critical precision on *Rahimi*: this was an 8–1 decision in which Chief Justice Roberts's majority *explicitly reaffirmed* the *Bruen* historical-tradition test. Justice Thomas — the author of *Bruen* — was the sole dissenter, arguing that even this narrow restriction lacks historical support. Multiple law review analyses characterize *Rahimi* as reinforcing, not limiting, *Bruen*…. The holding is narrow: only individuals adjudicated by a court to pose a 'credible threat to physical safety' may be temporarily disarmed. *Rahimi* is a quarter step, not an overturning."

**Line 9038:**
> "*Rahimi* (2024) is a quarter step in the same direction but requires precision: *Rahimi* does not overturn or modify *Bruen*. The majority (8–1) explicitly reaffirmed the historical-tradition test; Thomas (the *Bruen* author) was the sole dissenter. The holding is narrow — adjudicated-dangerous-person with a civil DV restraining order only."

The manuscript uses "kernel stabilization" as its interpretive frame for Rahimi (the system preserving Bruen by carving out a narrow DV exception that doesn't threaten the core disarmament architecture).

---

## 2. What the opinion actually holds

**Roberts majority (8-1; Roberts, joined by all except Thomas):**

Reaffirmation of Bruen (slip op. at 6–8):
> "As we explained in *Bruen*, the appropriate analysis involves considering whether the challenged regulation is consistent with the principles that underpin our regulatory tradition…. A court must ascertain whether the new law is 'relevantly similar' to laws that our tradition is understood to permit, 'apply[ing] faithfully the balance struck by the founding generation to modern circumstances.'" — *Rahimi*, slip op. at 6.

The terminal holding:
> "When an individual poses a clear threat of physical violence to another, the threatening individual may be disarmed." — *Rahimi*, slip op. at 13 (syllabus ¶(3)).

On the historical tradition:
> "Together, the surety and going armed laws confirm what common sense suggests: When an individual poses a clear threat of physical violence to another, the threatening individual may be disarmed. Section 922(g)(8) is not identical to these founding-era regimes, but it does not need to be. Like the surety and going armed laws, Section 922(g)(8)(C)(i) applies to individuals found by a court to threaten the physical safety of another." — *Rahimi*, slip op. at 13.

**Thomas dissent (sole dissenter — on historical-tradition grounds, not pro-DV-violence):**

Thomas's dissent is structural, not ideological — he argues the government failed to meet Bruen's historical-tradition burden:

On the government's "responsible citizens" theory (Thomas, dissenting, slip op. at 28):
> "The Government's position is a bald attempt to refashion this Court's doctrine. At the outset of this case, the Government contended that the Court has already held the Second Amendment protects only 'responsible, law-abiding' citizens…. The Government's claim that the Court already held the Second Amendment protects only 'law-abiding, responsible citizens' is specious at best."

Thomas's constitutional argument:
> "When the Constitution refers to 'the people,' the term 'unambiguously refers to all members of the political community.'" — *Rahimi*, Thomas, J., dissenting, slip op. at 28 (quoting *Heller*).

---

## 3. Gap diagnosis

- [ ] **No verbatim Roberts reaffirmation quote**: The manuscript correctly characterizes Roberts as reaffirming Bruen, but never quotes the reaffirmation directly. The verbatim language — "A court must ascertain whether the new law is 'relevantly similar' to laws that our tradition is understood to permit, 'apply[ing] faithfully the balance struck by the founding generation to modern circumstances'" — is the Roberts majority's clearest statement that Bruen is alive and controlling.
- [ ] **Thomas dissent on "responsible citizens" is unused**: This is a significant integration opportunity. Thomas's dissent explicitly rejects the government's "responsible citizens" / "law-abiding" exclusion theory as having "no doctrinal or constitutional mooring." Yet the manuscript (line ~8224 and Ch. 8 generally) argues that the "law-abiding, responsible citizens" framing is a structural exclusion mechanism. Thomas himself — the Bruen author — argues the same structural point: the Second Amendment protects *all the people*, not just the government-approved subset. The Dred Scott-to-Bruen-to-Rahimi chain (exclusion from "the people" in 1857 → exclusion from "responsible citizens" in 2022 → structural rejection of both exclusions by Thomas in dissent in 2024) is a primary-source trifecta that the manuscript partially assembles but doesn't complete.
- [ ] **"Kernel stabilization" frame not explained**: The manuscript uses "kernel stabilization" as its analytical term for Rahimi, but doesn't connect this to any specific language in the opinion. The frame is the manuscript's own — which is fine — but a footnote explaining the interpretive claim and its grounding would strengthen the argument.
- [x] **Manuscript's characterization is accurate**: The "quarter step" framing, the 8-1 vote, the narrow "credible threat" holding, the Thomas dissent characterization — all verified against the opinion. No mischaracterizations found.

---

## 4. Ready-to-paste LaTeX snippets

### 4a. Roberts reaffirmation verbatim footnote — Ch. 9 (near line 9038)

```latex
% Add to the "quarter step" characterization at line ~9038:
\footnote{Roberts's majority verbatim: ``A court must ascertain whether the new law
is `relevantly similar' to laws that our tradition is understood to permit, `apply[ing]
faithfully the balance struck by the founding generation to modern circumstances.'\,''
\textit{United States v.\ Rahimi}, 602 U.S.\ \_\_\_ (2024) \cite{rahimi2024}, slip
op.\ at 6 (quoting \textit{Bruen}). The majority's decision to uphold the DV
restraining order ban is thus \textit{within} the Bruen framework, not an exception
to it. The kernel stabilization reading is supported: the historical tradition of
disarming individuals found by a court to pose a credible threat has a clear founding-era
analogue (surety laws and going-armed laws), meaning the DV application does not require
any modification of the core test that the extraction architecture depends on.}
```

### 4b. Thomas dissent primary-source anchor — Ch. 8 (near the "law-abiding responsible citizens" passage)

```latex
% Add to or near the "responsible citizens" discussion in Ch. 8:
The most structurally significant primary-source confirmation of this argument comes
from Justice Thomas himself. In \textit{United States v.\ Rahimi} (2024)
\cite{rahimi2024}, Thomas dissented on the grounds that even the narrow DV restraining
order ban lacked sufficient historical-tradition support. But in doing so, he provided
the framework's own analysis in primary-source form: the Government's argument that the
Second Amendment protects only ``responsible, law-abiding'' citizens is, Thomas wrote,
``a bald attempt to refashion this Court's doctrine'' that is ``specious at best.''
\textit{Rahimi}, Thomas, J., dissenting, slip op.\ at 28. The constitutional text is
unambiguous: the Second Amendment protects ``the right of \textit{the people}''---and
``the people,'' as \textit{Heller} itself stated, ``unambiguously refers to all members
of the political community.'' The exclusion apparatus that \textit{Dred Scott} built on
``the people'' and that the modern disarmament architecture rebuilds on ``responsible
citizens'' is, in the view of the \textit{Bruen} author, constitutionally unauthorized.
The kernel's structural response: it excluded Thomas's reading from the majority in
\textit{Rahimi} just as it had excluded the 39th Congress's reading from \textit{Dred
Scott}.
```

---

## Integration priority

**MEDIUM** — The manuscript's Rahimi analysis is largely accurate. The Thomas dissent integration (§4b) is the highest-value addition, completing a Dred Scott → Bruen → Rahimi primary-source chain that is currently assembled only partially.
