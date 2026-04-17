# Session Log - 2026-04-16 (full root = all episode text)

## What Was Wrong / What Was Requested

The user clarified they wanted `00_ROOT_The_Open_Source_Republic.md` to contain the **full text** of all 17 episode prompts in one file, not only links and a `cat` recipe.

## How I Fixed It / What I Did

1. Rebuilt `podcast_prompts/00_ROOT_The_Open_Source_Republic.md` as:
   - A compact **series master** block (manuscript title, persona, four-part table, full anti-suppression protocol).
   - A **verbatim** section concatenating `Episode_01` through `Episode_17` in order, each preceded by a visible `### FILE: ...` delimiter.

2. Added `podcast_prompts/00_ROOT_SERIES_MASTER_FRAGMENT.md` — the first 63 lines of the bundle (everything above the verbatim episodes). This is the editable source for the master block so it is not hand-edited inside the 2000+ line generated file.

3. Added `podcast_prompts/build_full_series_prompt.sh` — regenerates `00_ROOT_The_Open_Source_Republic.md` from the fragment + all `Episode_NN_*.md` files. Uses `compgen -G` to resolve each episode glob.

## Challenges Encountered

1. **File size / duplication:** The combined file repeats anti-suppression inside every episode (verbatim requirement). Acceptable tradeoff for single-paste workflows.

2. **Maintenance:** Without a build script, the monolith would drift from episode files. The fragment + script pattern keeps a single regeneration command.

## Next Ideas (6 Ideas)

1. Add `build_full_series_prompt.sh` to a Makefile at repo root with target `podcast-full-prompt`.
2. CI job that fails if `00_ROOT` is stale compared to `sha256sum` of inputs.
3. Optional second output `_FULL_SERIES_PROMPT.md` without the master fragment (episodes only) for shorter context windows.
4. Strip duplicate anti-suppression from episode bodies in the bundle only (non-verbatim "smart merge") — smaller file but no longer strictly verbatim.
5. Git LFS for `00_ROOT` if the repo grows uncomfortable with large text blobs.
6. Pre-commit hook to run `build_full_series_prompt.sh` when any `Episode_*.md` or the fragment changes.
