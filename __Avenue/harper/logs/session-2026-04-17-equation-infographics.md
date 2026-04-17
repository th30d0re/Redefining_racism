# Session Log - 2026-04-17 Equation Infographic Prompts

## What Was Requested

Generate a detailed infographic prompt for every equation in the book *Redefining Racism*, explaining each equation and each variable in plain language accessible to people with no math background — so they understand what the equation is actually saying conceptually.

## How I Fixed It / What I Did

1. **Audited all ~100 equations** by reading the LaTeX source in large chunks across all 15 chapters, noting the surrounding prose context for each equation.

2. **Organized by chapter:** Equations 1.1–1.12 (Chapter 1), then Chapters 2–15, then Appendix. Each prompt includes:
   - The mathematical form (cleaned up for readability)
   - A plain-English one-paragraph explanation of what the equation says
   - A detailed infographic design brief specifying: title, visual elements, labeled components, historical examples, and a tagline

3. **Wrote output to:** `__Avenue/harper/equation_infographic_prompts.md`

4. **Key design principles applied to every prompt:**
   - Avoid math jargon in the brief
   - Anchor every abstract variable to a real historical event
   - Include a concrete "what this means in practice" translation
   - End with a punchy tagline for public-facing use

## Challenges Encountered

1. **Scale:** ~100 equations across 15 chapters required reading thousands of lines of context. Done in 10+ strategic read batches.
2. **Context-dependence:** Several equations use variables defined 200+ pages earlier (e.g., ψ, Φ_load, M(t), τ) — had to ensure each infographic brief was self-contained even when the equation references earlier definitions.
3. **Math-to-prose translation:** The equations range from simple inequalities to fractional-order differential equations. The challenge was finding the right visual metaphor for each — wave cancellation for Φ_load, compound interest for the multiplicative chain, solar systems for stationary leaders, etc.
4. **No-math audience tension:** Some equations (the navigation function, Lyapunov stability, fractional dynamics) require genuinely sophisticated concepts. Resolved by leading with the real-world implication and using the math as confirmation rather than explanation.

## Next Ideas (6 Ideas)

1. **Visual style guide:** Define a consistent color palette, typography system, and icon set for all infographics in the series so they look like a unified visual language across the book.
2. **Companion glossary card:** Create a single "variable key" card (like a legend) that shows what E, I_buffer, O_racialized, M(t), τ, ψ, Φ_load all mean — to accompany every infographic.
3. **Priority ranking:** Not all 100 equations need infographics immediately — identify the 12–15 "core" equations that appear most frequently in the book's argument and create those first.
4. **Interactive web version:** Convert the infographic prompts into an interactive timeline on a website where readers can scroll through equations in chapter order with embedded visualizations.
5. **Podcast episode pairing:** Each equation infographic could correspond to a specific podcast episode in the Open Source Republic series — Episode 2 (Eq 1.5 kernel objective), Episode 3 (Eq 3.1 revolution condition), etc.
6. **Accessibility audit:** After infographics are created, run alt-text and color-contrast accessibility checks to ensure they're usable for colorblind and low-vision readers.
