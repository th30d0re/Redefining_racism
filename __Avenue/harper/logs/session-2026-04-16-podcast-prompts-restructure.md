# Session Log — 2026-04-16 — Podcast Prompts Restructure to Match 17-Chapter / 4-Part Book

## What Was Wrong / What Was Requested

The user asked: "`@podcast_prompts` now can you edit the prompts."

The `podcast_prompts/` folder held 16 episode files that had drifted badly from the current state of `Paper/Redefining_Racism.tex`. Since the prompts were last authored, the manuscript had been restructured into a **four-part, 14-chapter architecture** with several major changes:

- A new **Chapter 4: The Architecture of Kinship** was inserted between Bacon's Rebellion (Ch 3) and the Gendered Axis (Ch 5). The episode series had no counterpart.
- Former Chapter 7 was retitled and split into two chapters: **Ch 9 "The Recompile"** and **Ch 10 "The Full Algorithm"**.
- **Ch 11 "The Kinetic Guarantee"** became a single-variable deep-dive on firearms asymmetry and the disarmament timeline.
- **Ch 12 "The Contradiction"** absorbed both the gaslighting section and the theorem cluster (Concession Theorem, Constitutional Shield, *Bruen* Load-Balancing, Grandfather Clause, Haitian Theorem).
- **Ch 13 "The Global Containment Field"** was expanded with the Môle Saint-Nicolas Gambit, the Legitimation Inversion Lemma / Firmin Protocol, Global Firminism, and the $P_{\text{debt}}$ Inversion.
- The book adopts explicit **Part I–IV framing**: Specification and Origins, Installation, Scaling and Runtime, Diagnostics and Output.

Before starting, I asked three targeted questions and got explicit answers:

1. **chapter_refs → `full`**: fix chapter numbers/titles, update cross-episode ALREADY-COVERED / DO-NOT-discuss lists, retune each sign-off/teaser, and align every chapter/section reference inside the Episode Content Guide.
2. **kinship_episode → `new_ep`**: create a brand-new **Episode 4 on Kinship**, and renumber Eps 4–16 → 5–17 (growing the series from 16 to 17 episodes).
3. **part_structure → `yes_add`**: add a "Series Arc" paragraph to each episode naming which Part it belongs to (e.g., "Ep 8 sits inside Part II: The Installation").

## How I Fixed It / What I Did

Worked through the restructure as a single ordered pipeline. Every step was captured in the live todo list.

### 1. File renames

Executed a batch `git mv` that shifted Eps 4–16 to 5–17 while preserving history:

```bash
git mv Episode_04_Gendered_Axis_Part1.md Episode_05_Gendered_Axis_Part1.md
git mv Episode_05_Gendered_Axis_Part2.md Episode_06_Gendered_Axis_Part2.md
# ... 11 more renames through ...
git mv Episode_16_Conclusion.md Episode_17_Conclusion.md
```

### 2. New Episode 4 (Kinship)

Wrote a fresh `Episode_04_Kinship.md` covering Chapter 4:
- Pre-colonial West African kinship baselines (Igbo patrilineality + Women's War; Yoruba dual-sex governance; Akan matrilineality and the *Ohemaa*).
- Distributed intimacy as structural immunity against the Min-Max Function.
- The demographic cataclysm of the slave trade.
- The colonial patriarchal overwrite and the "Outside Wife" modern echo.
- Positioned as the **Part II opener** — the first installation chapter, proving the African relational operating system the colonial virus had to overwrite.

### 3. Episode-by-episode updates (17 files total)

For every episode I applied the same checklist:

| Block | Action |
|---|---|
| Title banner | Update episode number |
| Series Context & Persona | Re-state episode index, re-count preceding episodes |
| **Series Arc** (NEW) | Add paragraph naming its Part (I/II/III/IV) and its beat within that Part |
| Serialization Rules | Update current episode number, update target chapter, rewrite `ALREADY COVERED` list to match new 17-ep structure (every prior episode's topics), rewrite `DO NOT discuss/preview` list to match new forward episodes |
| Anti-Suppression Language Protocol | Preserved (already uniform across files) |
| Episode Content Guide | Point to correct chapter number and section titles; re-number internal cross-references (e.g., "see Episode 9" becomes "see Episode 10") |
| Sign-Off / Teaser | Retune to tease the correct *next* episode and its new chapter title |

Notable content migrations baked into the new prompts:

- **Ep 8 (Compounding)** absorbs Judicial Entrenchment / Economic Reality Test content that used to float.
- **Ep 9 (Containment)** picks up the Capture Variable discussion formerly adjacent.
- **Ep 11 (Recompile)** was rescoped to cover *all* of Chapter 9 — including the Manufactured Crisis, crack markets, Broken Windows, and the 1994 Crime Bill — because re-reading the tex confirmed those sections live inside Ch 9, not Ch 10.
- **Ep 12 (Full Algorithm)** was completely rewritten to cover Chapter 10: Demographic Paradox, Modern Security Patch ($P_{\text{spatial}}$, *Bruen* disruption, felony trap, complexity tax), Universal Latent Criminality, the full 5-Tier Set-Theoretic Reveal with Predatory Min-Max equation, the Epstein stress test, the §922(g)(3) Crisis, and the Geopolitical Override.
- **Ep 13 (Kinetic Guarantee)** was rewritten to cover Chapter 11 end-to-end — but with an explicit note that the Grandfather Clause theorem now lives in Ch 12 and so is Ep 15 material.
- **Ep 14 (Gaslighting)** was rewritten to focus only on the *gaslighting half* of Chapter 12 (Kernel Denial, Victimhood Inversion, Nonviolence Mandate, formal definition of $P_{\text{gaslight}}$).
- **Ep 15 (The Contradiction)** was retuned to cover only the *theorem half* of Chapter 12 (Reform Paradox, Concession Theorem, Constitutional Shield / Intent Standard, *Bruen* Load-Balancing Proof, Grandfather Clause as formal theorem, Haitian Theorem, Framers' Confessions, Gendered Bug).
- **Ep 16 (Global Machine)** was extended with the new Chapter 13 material: Môle Saint-Nicolas Gambit (1891), Legitimation Inversion Lemma / three-phase Firmin Protocol, Admiral Killick's divide-by-zero event, Global Firminism as counter-public, UN Reparations Vote (2026), and the $P_{\text{debt}}$ Inversion.
- **Ep 17 (Conclusion)** was rewritten against Chapter 14: opens with the manuscript's own Runtime Log: Final Output tcolorbox, walks the Revised Definition, the Vector equation, the three Terminal Findings, the explicit Four-Part Arc summary, $O_{\text{final}} = \text{Everyone} \setminus E$, the Unresolved Variable, and closes with `return $\vec{R}_{\text{acism}}$`.

### 4. Cross-episode references

Every internal reference of the form "see Episode N" inside the 17 prompts was shifted by +1 where that reference pointed past the Kinship insertion point (old Ep 4+ → new Ep 5+). Forward teasers now always name the correct successor episode *and* its new chapter label.

## Challenges Encountered

1. **Moving target on which chapter owned which section.** The biggest rework was realizing mid-pass that the Manufactured Crisis / 1994 Crime Bill lived in Chapter 9 ("The Recompile"), not Chapter 10. That forced a reallocation of content across Eps 11 and 12, and a full rewrite of Ep 12 rather than a surface edit.

2. **Similar chapter movement for the Grandfather Clause.** Initially scoped it to Ep 13 (Kinetic Guarantee / Ch 11). Re-reading Ch 12 showed it is now a formal theorem inside The Contradiction — so it moved to Ep 15. Ep 13 was rewritten to explicitly *forward-reference* that migration so the listener isn't confused.

3. **File not found on Ep 15.** First read attempt failed because the filename was `Episode_15_The_Contradiction.md`, not `Episode_15_Contradiction.md`. Fixed by `ls`-ing the directory and using the correct filename. Minor, but would have been faster to enumerate the directory before assuming naming.

4. **Keeping the Anti-Suppression Language Protocol intact across 17 files** while rewriting large blocks around it. Handled by doing targeted `StrReplace`s rather than full file writes wherever possible, and only falling back to `Write` when the content changes exceeded ~60% of the file.

5. **Preventing reference drift in the ALREADY-COVERED lists.** Each prompt's ALREADY-COVERED block had to be regenerated from the new 17-episode sequence, not mechanically bumped — because the Kinship insertion changed *which topic each preceding episode actually covers*, not just the numbers. Worked through each block by hand.

6. **Ep 16's Firmin material.** Chapter 13 had new subsections (Môle Saint-Nicolas, Legitimation Inversion Lemma, Global Firminism) that did not exist when the prompt was first written. Had to grep/read the tex to extract the three-phase Firmin Protocol and the Du~Bois prefiguration passage so the content guide carried actual manuscript-accurate detail rather than paraphrase.

## Next Ideas (6 Ideas)

1. **Auto-verifier script.** Add a tool (`tools/verify_podcast_refs.py` or a shell script) that parses every `Episode_*.md` and asserts: (a) the filename episode number matches the banner; (b) every "Episode N" reference inside a file points to a file that exists; (c) the `ALREADY COVERED` list's indices are a contiguous `1..N-1`. Run it in pre-commit so drift is caught immediately the next time the manuscript moves.

2. **Chapter-to-episode map as a canonical file.** Drop a `podcast_prompts/_manifest.yaml` that holds `episode → {part, chapter_number, chapter_title, sections}` as the single source of truth. Have each prompt import its header from that manifest at render-time (or have the verifier check the prompt matches it).

3. **Autogenerate the Series Arc block.** Given the manifest, the Series Arc paragraph ("Ep X is the Nth beat of Part Y…") is deterministic. Generate it so it never needs hand-editing when an episode moves.

4. **Shared Anti-Suppression Protocol file.** Extract the identical Anti-Suppression Language Protocol into `podcast_prompts/_shared/anti_suppression.md` and include-by-reference (or have a build script inline it). Currently it is duplicated 17 times, which is exactly the kind of thing the MVVM-S / DRY rules in the user rules would flag.

5. **Cross-link back to the tex.** Each Episode Content Guide section could carry a `\label{…}` pointer (as a comment) to the manuscript section it draws from. Makes it trivial to re-sync the prompt next time a section is renamed, split, or moved.

6. **Render a single-PDF "Show Bible"** from all 17 prompts plus a cover page that diagrams the Part → Chapter → Episode map. Useful as a handoff artifact to the voice-generation tool and as a diff target: if that PDF's bookmarks and the book's TOC stop matching, something has drifted.
