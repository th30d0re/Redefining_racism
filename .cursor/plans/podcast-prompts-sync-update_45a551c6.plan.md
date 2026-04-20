---
name: podcast-prompts-sync-update
overview: Bring podcast_prompts/ back in sync with Paper/Redefining_Racism.tex by adding the Du Bois / Acemoglu-Robinson vocabulary and the Chapter 1 & Chapter 2 targeted revisions into the root series file and seven affected episode files. No new episodes; surgical inserts only.
todos:
  - id: root-batches
    content: Add Batch C (Du Bois), Batch D (AJR), Batch E (Ch1/Ch2 sharpening) to podcast_prompts/00_ROOT_SERIES_FRAGMENT.md shared block
    status: completed
  - id: ep01
    content: "Episode 1: add formalism-as-precision-forcing note, revise Zero-Day to industrialization-of-phenotype, compress LSD to Mode 2, add model-minority buffer-tier bullet, add Propaganda-of-History + Critical-Junctures mentions"
    status: completed
  - id: ep02
    content: "Episode 2: add Casa-dos-Escravos domestic-ψ-transmission bullet, African-kingdom-modularity bullet, reorder Firmin to illustration-of-general-claim, add AJR extractive-institutions supportive note"
    status: completed
  - id: ep07
    content: "Episode 7: insert General Strike of the Enslaved bullet before 13th Amendment content"
    status: completed
  - id: ep09
    content: "Episode 9: add Counter-Revolution of Property framing for 1877 overthrow + Du Bois Pullman/Knights-of-Labor prior art"
    status: completed
  - id: ep10
    content: "Episode 10: add AJR economic-elite-capture citation for the Tweedism / Green Primary mechanism"
    status: completed
  - id: ep12
    content: "Episode 12: add AJR Venice Serrata + Rome latifundia as extractive-collapse precedents for cannibalization"
    status: completed
  - id: ep14
    content: "Episode 14: add Du Bois Propaganda of History as prior-art diagnosis of P_gaslight (Dunning school)"
    status: completed
  - id: ep15
    content: "Episode 15: add Counter-Revolution/Reconstruction anchor to Concession Theorem list + new major bullet on The Acemoglu Limit"
    status: completed
  - id: ep16
    content: "Episode 16: add AJR Imperial Core / extractive-vs-inclusive corroboration bullet"
    status: completed
  - id: ep17
    content: "Episode 17: add Abolition Democracy → Open-Source Republic 4-plank / 4-patch mapping bullet"
    status: completed
  - id: rebuild-root
    content: Run ./podcast_prompts/build_full_series_prompt.sh to regenerate the bundled 00_ROOT_The_Open_Source_Republic.md
    status: completed
  - id: session-log
    content: Create __Avenue/harper/logs/session-YYYY-MM-DD-HHMMSS.md per user logging rule
    status: completed
isProject: false
---

# Podcast Prompts Sync Update

## What changed in the paper that the prompts do not yet know about

The podcast prompts were last synced at commit `fa3b77f`. Since then, four tranches of material were integrated into [Paper/Redefining_Racism.tex](Paper/Redefining_Racism.tex):

1. **Du Bois — 5 new concepts** (General Strike of the Enslaved, Counter-Revolution of Property, Abolition Democracy, Propaganda of History, Black-worker solidarity prior art) — per [.cursor/plans/dubois-acemoglu-integration_1e039287.plan.md](.cursor/plans/dubois-acemoglu-integration_1e039287.plan.md).
2. **Acemoglu & Robinson** (extractive institutions corroboration, critical-junctures framing, **the Acemoglu Limit** critical engagement, Imperial Core / Venice-Rome cannibalization precedents) — same plan.
3. **Chapter 1 targeted revisions** — per [.cursor/plans/chapter_1_targeted_revisions_a9445844.plan.md](.cursor/plans/chapter_1_targeted_revisions_a9445844.plan.md): (a) formalism-as-precision-forcing genre declaration, (b) Zero-Day reframed to *industrialization of phenotype*, (c) LSD/IFAS section compressed and explicitly Mode 2, (d) model-minority → differential buffer-tier insertion paragraph.
4. **Chapter 2 targeted revisions** — per [.cursor/plans/chapter_2_targeted_revisions_9cb0aeff.plan.md](.cursor/plans/chapter_2_targeted_revisions_9cb0aeff.plan.md): (a) Casa dos Escravos as domestic ψ-transmission mechanism (legal/narrative, not physical co-presence), (b) African-kingdom participation as evidence of algorithm **modularity**, (c) Firmin framing reordered (general mechanism first, Firmin as illustration).

Already correctly reflected (no action needed): Woodard / `libidinal_extraction.exe` batch and Ruby Ridge / Waco / `R(x_i)` batch. Also skipped: the four new TikZ/pgfplots figures (visual only) and the Fig 1.2 Elite Wealth Accumulation chart (visual only).

## Strategy

- **Root file** gets two new Batch C + Batch D blocks in the "Cross-series vocabulary additions" section (same structure as the existing Batch A / Batch B blocks) plus four Ch.1/Ch.2 update bullets.
- **Seven episode files** get surgical inserts. No new episodes.
- **No edits** to Episodes 3, 5, 6, 11, 13 (their chapter scopes were untouched by this round).

## Edits per file

### [podcast_prompts/00_ROOT_The_Open_Source_Republic.md](podcast_prompts/00_ROOT_The_Open_Source_Republic.md)
Add two new vocabulary batches to the "Cross-series vocabulary additions" section (alongside existing Batch A and Batch B):

- **Batch C — Du Bois / Black Reconstruction prior art**: `General Strike of the Enslaved` [Ep 7], `Counter-Revolution of Property` [Ep 9, reprised Ep 15], `Abolition Democracy` [Ep 17], `Propaganda of History` [Ep 1 intro + Ep 14], `Knights-of-Labor / ARU prior art` [Ep 9 Pullman, Ep 10].
- **Batch D — Acemoglu & Robinson engagement**: `extractive institutions` [Ep 2], `critical junctures → Runtime Logs` [Ep 1], `economic-elite capture → Tweedism` [Ep 10], `Venice Serrata / Rome latifundia extractive collapse` [Ep 12], `Imperial Core / inclusive-institutions corroboration` [Ep 16], `The Acemoglu Limit` [Ep 15] — AJR prescription fails on partitioned systems because it omits ψ, the racial partition, and the kinetic-guarantee asymmetry.
- **Batch E — Ch. 1/Ch. 2 methodological sharpening**: `formalism as precision-forcing device (not measurement instrument)` [Ep 1], `Zero-Day = industrialization of phenotype (not phenotypic awareness)` [Ep 1], `LSD/IFAS 1966 read explicitly as Mode 2 (functional output, not intent)` [Ep 1], `differential buffer-tier insertion (model-minority response)` [Ep 1], `domestic ψ transmission via Casa dos Escravos legal/narrative infrastructure (no physical co-presence required)` [Ep 2], `African-kingdom participation = algorithmic modularity, not counter-evidence` [Ep 2], `Firmin-as-illustration (general epistemological-infrastructure penetration is the claim, Firmin is the sharpest instance)` [Ep 2].

Then regenerate the bundled root file by running `./podcast_prompts/build_full_series_prompt.sh` at the end.

### [podcast_prompts/Episode_01_Redefining_Racism.md](podcast_prompts/Episode_01_Redefining_Racism.md)
- Add a new opening bullet in "Episode Content Guide": **A methodological note on formalism** — equations function as precision-forcing devices, not measurement instruments (mirrors the new §before the Tri-Modal Enclosure Model in the tex).
- Revise the "Zero-Day Exploit" bullet: phenotypic awareness predates Portugal; the zero-day is the **industrialization of phenotype** as a legally codified, heritable, transatlantic capital asset.
- Compress the "IFAS 1966 / LSD" reference into a Mode 2 framing (functional output of epistemic enclosure, not a claim about intent) — and strip any "system's response was decisive" language that may be in the prompt.
- Add a new bullet on **differential buffer-tier insertion** as the framework's answer to the model-minority objection (predicts different outcomes by differential insertion point in the hierarchy, not uniform extraction).
- Add one bullet naming Du Bois's **"Propaganda of History"** as the prior-art diagnosis of $P_{\text{gaslight}}$ and AJR's **critical junctures** as a conceptual ancestor of the Runtime Logs (both are allowed namings; actual mechanics stay in Eps 14 and 15).

### [podcast_prompts/Episode_02_Initializing_the_Vector.md](podcast_prompts/Episode_02_Initializing_the_Vector.md)
- Add bullet: **domestic ψ transmission** — Portuguese peasants received the psychological wage through the Casa dos Escravos legal infrastructure, royal proclamations, and Zurara's chronicle, *not* through physical co-presence with the enslaved (who were offshore in Madeira/Brazil). The wage requires legal legibility, not visible proximity.
- Add bullet: **African-kingdom participation as modularity evidence** — Kongo, Benin, and later Dahomey/Asante elite participation does *not* undermine the moral-hack thesis; it is evidence the algorithm can interface with pre-existing extraction hierarchies via exchange of firearms/goods. Modularity is *why* the algorithm was globally exportable.
- Rewrite the Firmin mention so the *general claim* (variable-based sorting had penetrated even rigorous critics' epistemological infrastructure) precedes Firmin as its sharpest historical instance — not the other way around.
- Add one-sentence AJR supportive note: Acemoglu & Robinson independently identify the Portuguese Atlantic system as the textbook case of **extractive institutions**; the book's engaged critique of their prescription is deferred to Ep 15.

### [podcast_prompts/Episode_07_Enforcement_Engine.md](podcast_prompts/Episode_07_Enforcement_Engine.md)
Insert a new bullet immediately before the 13th Amendment loophole content: **The General Strike of the Enslaved (Du Bois, *Black Reconstruction* ch. 4)** — ~500,000 self-emancipations in 1861–64 forced Confederate collapse and made Emancipation a military necessity. This is the missing kinetic-agency proof for the 1863–65 window; it reinforces the Haitian Theorem domestically and sets up the Concession Theorem's first historical instantiation (covered in Ep 15).

### [podcast_prompts/Episode_09_Containment_Field.md](podcast_prompts/Episode_09_Containment_Field.md)
- Add a bullet framing Reconstruction's 1877 overthrow as Du Bois's **Counter-Revolution of Property** — not a failure of Black governance but a successful counter-revolution by Northern capital aligned with Southern Redeemer elite. Direct ancestor of the book's "Elite uses the racial partition to dissolve interracial democracy" thesis. (Deeper Concession-Theorem formalization is Ep 15.)
- In the existing Pullman segment, add a sentence citing Du Bois's prior-art diagnosis of the Knights-of-Labor / ARU racial-exclusion pattern in the 1880s as the historical precursor to the 1894 ARU exclusion.

### [podcast_prompts/Episode_10_Puppet_Show.md](podcast_prompts/Episode_10_Puppet_Show.md)
Add one bullet: AJR independently describe the phenomenon of "economic elites capturing political institutions" — the Green Primary ($P_{\text{uppet}}$ filter) is the book's formalization of that observation; AJR never write the filter math.

### [podcast_prompts/Episode_12_Manufactured_Crisis.md](podcast_prompts/Episode_12_Manufactured_Crisis.md)
Add one bullet citing AJR's **Venice Serrata / Book of Gold** and **Rome latifundia collapse** as empirical precedents for the extraction kernel eventually turning on its own In-group — the same cannibalization dynamic the chapter diagnoses at US 2026 scale.

### [podcast_prompts/Episode_14_Gaslighting.md](podcast_prompts/Episode_14_Gaslighting.md)
Add one bullet: **Du Bois's "Propaganda of History"** (final chapter of *Black Reconstruction*) is the prior-art diagnosis of $P_{\text{gaslight}}$ — specifically the Dunning-school historiographic erasure of Black agency. Frame as explicit operational proof the variable existed and was documented in 1935.

### [podcast_prompts/Episode_15_The_Contradiction.md](podcast_prompts/Episode_15_The_Contradiction.md)
Two additions:
- Add **Reconstruction (1865–1877) / Counter-Revolution of Property** as an anchor entry in the Concession Theorem's historical-proof list (before Emancipation Proclamation if it's listed chronologically, or before the New Deal entry).
- Add a new major bullet: **The Acemoglu Limit** — AJR correctly identify extractive institutions and elite capture, but their prescription ("inclusive institutions via pluralism + centralized state") fails on any racially partitioned system because ψ and the kinetic-guarantee asymmetry force every "inclusive" reform to recompile back into extraction via the Concession Theorem. AJR's "iron law of oligarchy" is a *special case* of the Concession Theorem with ψ = 0 and no racial partition. The three variables AJR omit: ψ, the racial partition ($I_{\text{buffer}}$ vs $O_{\text{racialized}}$), and the kinetic guarantee. AJR diagnose the disease; they cannot write the patch.

### [podcast_prompts/Episode_16_Global_Machine.md](podcast_prompts/Episode_16_Global_Machine.md)
Add one bullet: AJR's extractive-vs-inclusive dichotomy and their Nogales/Mexico–US border example map cleanly onto the 5-tier international hierarchy and the **Imperial Core Theorem** — supportive citation, not a critique (the critique already lives in Ep 15's Acemoglu Limit).

### [podcast_prompts/Episode_17_Conclusion.md](podcast_prompts/Episode_17_Conclusion.md)
Add a new major bullet in the Open-Source-Republic architecture section: **Abolition Democracy — Du Bois's unfinished kernel**. Du Bois's four planks (land redistribution, universal public education, universal suffrage, federal civil-rights enforcement) map one-to-one onto the four Open-Source-Republic patches (hard-cap on the $\max$ variable, algorithmic transparency laws, dismantling the Tweedism filter, 18 U.S.C. § 242 + abolition of qualified immunity). The Open-Source Republic is the mathematical completion of Du Bois's 1935 specification.

## Final step

Run `./podcast_prompts/build_full_series_prompt.sh` to regenerate the bundled [podcast_prompts/00_ROOT_The_Open_Source_Republic.md](podcast_prompts/00_ROOT_The_Open_Source_Republic.md) with all the per-episode changes baked in.

Then create a session log at `__Avenue/harper/logs/session-YYYY-MM-DD-HHMMSS.md` per the user's logging rule.

## Out of scope

- No changes to Episodes 3, 5, 6, 8, 11, 13 (their chapter scopes were not touched by this round).
- No changes to [podcast_prompts/00_ROOT_SERIES_FRAGMENT.md](podcast_prompts/00_ROOT_SERIES_FRAGMENT.md) beyond the vocabulary-batch additions that also appear in the bundled root (fragment and root share the shared block).
- No new episodes, no new variables beyond those already registered in the tex's Symbol Registry.
- No edits to [__Avenue/harper/equation_infographic_prompts.md](__Avenue/harper/equation_infographic_prompts.md) — separate workstream.
- The four new TikZ charts and the Elite-Wealth chart are visual additions and do not require prompt changes (the content they illustrate is already covered by the vocabulary updates above).
