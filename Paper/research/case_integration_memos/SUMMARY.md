# SCOTUS Case Integration Memos — Tier 1 Summary

**Generated:** 2026-04-23 | **Plan:** `scotus-case-integration-read_c0ca9b63`  
**Cases reviewed:** 12 | **Priority:** P0 (5), P1 (4), P2 (3)

---

## Escalation Gate Decision

**Tier-2 escalation: YES** — The Tier-1 pass identified ≥ 3 substantive body-paragraph gaps (new argument, not just footnote polish):

1. **Dobbs** — Zero `\cite{}` anchoring + missing body paragraph for Ch. 4 Active Patch chain + Thomas concurrence on Griswold/Lawrence/Obergefell (P0 — HIGH)
2. **Loving** — Warren "White Supremacy" majority language not integrated (P1 — HIGH)
3. **Dred Scott** — Missing cite at Ch. 10 "keep and carry arms" passage + false quotation marks (P0 — HIGH)
4. **Castle Rock** — Gendered enforcement-duty gap not developed in Ch. 4 (P2 — MEDIUM)
5. **Washington v. Davis** — Brennan dissent structural argument not anchored (P0 — MEDIUM)

Recommend drafting `scotus-tier2-integration-read.plan.md` for the gendered-kernel cases: **Bradwell v. Illinois, Muller v. Oregon, Reed v. Reed, Roe v. Wade, Relf v. Weinberger, Madrigal v. Quilligan, Obergefell v. Hodges**.

---

## Snippet Count by Chapter

| Chapter | Snippets Proposed | Priority | Cases |
|---------|------------------|----------|-------|
| Ch. 4 (Gendered Axis) | 4 | HIGH | Dobbs (§4b,4c,4d), Loving (§4a,4b), Castle Rock (§4b) |
| Ch. 10 (Enforcement/2A) | 5 | HIGH | Dred Scott (§4a,4b,4c,4d), Rahimi (§4b), Bruen (§4c) |
| Ch. 8–9 (Kinetic Guarantee) | 4 | MEDIUM | Bruen (§4a,4b), Rahimi (§4a), Dred Scott (§4d) |
| Ch. 12 (Proxy Variable/Intent) | 3 | MEDIUM | Washington v. Davis (§4a,4b,4c), Arlington Heights (§4a,4b) |
| Ch. 6 (Enforcement Architecture) | 3 | MEDIUM | DeShaney (§4a,4b), Castle Rock (§4a) |
| Ch. 3 (Boundary Enforcement) | 1 | HIGH | Loving (§4a) |
| Ch. 13 (Gold Clause) | 1 | LOW | Perry (§4a) |
| Ch. 11 (Marbury Abdication) | 1 | LOW | Marbury (§4a) |
| Methodology/Ch. 13 (Open Records) | 1 | LOW | Richmond Newspapers (§4a) |

**Total snippets proposed:** 23 (12 footnote-level, 11 body-paragraph-level)

---

## Cases Where Manuscript Characterization Is Materially Accurate

| Case | Assessment |
|------|-----------|
| Bruen | Accurate; "Proper Cause algorithm" framing correctly identifies what Thomas struck down |
| Washington v. Davis | Accurate characterization; gap is in cite density and verbatim anchoring, not doctrine |
| Rahimi | Accurate; "quarter step" / "kernel stabilization" framing verified against opinion text |
| Marbury | Quote verified verbatim accurate |
| DeShaney | Accurate; "no affirmative duty" paraphrase correct |
| Perry | Accurate; Cummings quote correctly attributed to oral argument (not opinion) |
| Richmond Newspapers | Accurate; "appellants' brief" attribution verified from markdown text |
| Castle Rock | Accurate; facts and holding correctly stated |
| Arlington Heights | Four-factor tabulation accurate; fifth factor (sequence of events) missing |

---

## Cases With Material Gaps Requiring Integration

| Case | Gap Type | Severity | Memo |
|------|----------|----------|------|
| Dred Scott | Missing `\cite{dredscott}` at Ch. 10 "keep and carry arms" passage + false quotation marks | **CORRECTION** | [dred_scott.md](dred_scott.md) |
| Dobbs | Zero `\cite{dobbs}` in manuscript; missing body paragraph; Thomas concurrence unused | **HIGH** | [dobbs.md](dobbs.md) |
| Loving | Warren "White Supremacy" majority language not integrated | **HIGH** | [loving_v_virginia.md](loving_v_virginia.md) |
| Washington v. Davis | No verbatim White majority quote; Davis/Arlington Heights over-merged | **MEDIUM** | [washington_v_davis.md](washington_v_davis.md) |
| DeShaney | Blackmun "Poor Joshua!" dissent not cited | **MEDIUM** | [deshaney.md](deshaney.md) |
| Castle Rock | Gendered enforcement-duty gap underdeveloped | **MEDIUM** | [castle_rock.md](castle_rock.md) |
| Bruen | Missing verbatim terminal test quote; Dobbs cross-connection absent | **LOW-MEDIUM** | [bruen.md](bruen.md) |
| Arlington Heights | Fifth Powell factor missing from table | **LOW** | [arlington_heights.md](arlington_heights.md) |
| Marbury | Missing pinpoint page number for quote | **LOW** | [marbury_v_madison.md](marbury_v_madison.md) |
| Perry | Missing Hughes verbatim "constitutional violation, no remedy" paradox quote | **LOW** | [perry.md](perry.md) |
| Richmond Newspapers | Cite is footnote-only; promotion to body paragraph optional | **LOW** | [richmond_newspapers.md](richmond_newspapers.md) |
| Rahimi | Missing verbatim Roberts reaffirmation; Thomas dissent "responsible citizens" unused | **LOW-MEDIUM** | [rahimi.md](rahimi.md) |

---

## New BibLaTeX Entries Required

| Key | Case | Status |
|-----|------|--------|
| `dobbs` | Dobbs v. Jackson Women's Health Organization (2022) | **ADD** — see [dobbs.md §4a](dobbs.md) for entry |
| `tel_wash_v_davis` | Washington v. Davis (1976) | Exists; rename to `wash_v_davis` (optional) |

**No other new bib entries needed** — all other Tier-1 cases are already in `references.bib`.

---

## Existing Bib Key Reference Table (Tier-1 Cases)

| Case | Bib Key | Notes |
|------|---------|-------|
| Dred Scott | `dredscott`, `fehrenbacher` | Both exist |
| Dobbs | **missing** | Add `dobbs` entry |
| Bruen | `bruen` | Exists |
| Washington v. Davis | `tel_wash_v_davis` | Exists; `tel_` prefix is non-standard |
| Rahimi | `rahimi2024` | Exists |
| Marbury | `marbury_1803` | Exists |
| Arlington Heights | `tel_arlington_heights` | Exists |
| DeShaney | `deshaney` | Exists |
| Loving | `loving_v_virginia_record_1967` | Exists |
| Castle Rock | `castlerock` | Exists |
| Perry | `perry_v_us_1935` | Exists (as `@case`) |
| Richmond Newspapers | `richmond_newspapers_1980` | Exists |

---

## Dred Scott Re-pull Status

- **Previous:** 68-line stub (50KB LOC page scan)
- **Current:** 11,058-line full text (645KB, Project Gutenberg EBook #31425 — Taney majority + all concurrences and dissents)
- **Key passages now accessible:**
  - "keep and carry arms wherever they went" (line 1098 of new MD)
  - "no rights which the white man was bound to respect" (line 658)
  - Missouri Compromise 2A holding: "Nor can Congress deny to the people the right to keep and bear arms" (line 2577)

---

## Priority Integration Order (Recommended)

If the user approves selective integration, this is the recommended order:

1. `dred_scott.md §4a` — Add `\cite{dredscott}` to Ch. 10 "keep and carry" passage (1-minute fix, correctness)
2. `dred_scott.md §4b` — Fix false quotation marks in Ch. 10 Bug #1 (correctness)
3. `dobbs.md §4a` — Add `@misc{dobbs,...}` to `references.bib`
4. `dobbs.md §4b` — Add `\cite{dobbs}` to Active Patch tcolorbox lines
5. `dobbs.md §4c` — Add Dobbs body paragraph for Ch. 4
6. `loving_v_virginia.md §4a` — Add Warren "White Supremacy" body text to Ch. 3/4
7. `deshaney.md §4b` — Add Blackmun "Poor Joshua!" footnote to Ch. 6
8. `washington_v_davis.md §4a` — Add White majority verbatim quote to Ch. 12
9. `rahimi.md §4b` — Add Thomas dissent "responsible citizens" passage to Ch. 8
10. `castle_rock.md §4b` — Add gendered enforcement-duty gap to Ch. 4
11. All remaining low-priority footnote additions (Bruen, Arlington, Marbury, Perry, Richmond Newspapers)

---

## Tier-2 Escalation Plan (if approved)

Recommended cases for `scotus-tier2-integration-read.plan.md`:

| Case | Rationale |
|------|-----------|
| Bradwell v. Illinois (1873) | Active Patch chain member — already cited; Myra Bradwell opinion content not verified |
| Muller v. Oregon (1908) | Gendered labor law — used in framework's gendered axis |
| Reed v. Reed (1971) | First successful sex-based EP challenge — connects Loving gendered-axis arc |
| Roe v. Wade (1973) | Pre-Dobbs Tier-1 precedent now overruled — verify Dobbs's characterization |
| Obergefell v. Hodges (2015) | Thomas concurrence targets it explicitly — verify current manuscript treatment |
| Relf v. Weinberger (1974) | Forced sterilization corpus stub — verify body integration |
| Madrigal v. Quilligan (1978) | Forced sterilization corpus stub — verify body integration |
