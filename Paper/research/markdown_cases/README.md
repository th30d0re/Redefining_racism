# SCOTUS Case Corpus — Markdown Library

**102 cases · 0 failures · last updated 2026-04-23**

Primary-text tier: full markitdown-converted PDFs from the Internet Archive `us-supreme-court` collection, the Library of Congress U.S. Reports, SCOTUS.gov slip opinions, and CourtListener. Each file is the raw primary-source text of the case record or slip opinion.

Companion analysis notes (curated framework annotations) live in [`Sources/`](../../Sources/).
Canonical case index (cite_key → slug → pdf_path → md_path → cluster): [`case_index.yaml`](../case_index.yaml).
Corpus-manuscript sync audit: `python3 Paper/scripts/audit_scotus_corpus.py`.

---

## Status Legend

| Status | Meaning |
|---|---|
| `primary` | Core opinion PDF from IA microfilm, SCOTUS.gov, or LOC — full text |
| `companion` | Related record, brief, or partial transcript used as primary source |
| `research-stub` | Lower-court case; markdown is a research summary, not a primary-source conversion |
| `next-pass` | Tier 3 — downloaded and converted; awaiting full manuscript integration |

---

## Baseline (57 cases — original corpus)

| Case | Year | Cluster | Cite Key(s) | Status |
|---|---|---|---|---|
| Abbott v. Perez | 2018 | voting_rights | — | primary |
| Atwater v. City of Lago Vista | 2001 | carceral_enforcement | `atwater` | primary |
| Bailey v. Alabama | 1911 | peonage_13th | — | primary |
| Batson v. Kentucky | 1986 | jury_selection | — | primary |
| Brown v. Board of Education | 1954 | naacp_brown | `brown_v_board_record_1951` | primary |
| Buck v. Bell | 1927 | eugenics | — | primary |
| Buckley v. Valeo | 1976 | campaign_finance | — | primary |
| Caetano v. Massachusetts | 2016 | second_amendment | `caetano` | primary |
| Citizens United v. FEC | 2010 | campaign_finance | — | primary |
| Civil Rights Cases | 1883 | reconstruction_amendments | — | primary |
| Cooper v. Aaron | 1958 | naacp_brown | — | primary |
| Crawford v. Marion County Election Board | 2008 | voting_rights | — | primary |
| District of Columbia v. Heller | 2008 | second_amendment | `heller` | primary |
| Fisher v. University of Texas | 2016 | affirmative_action | — | primary |
| Foster v. Chatman | 2016 | jury_selection | — | primary |
| Green v. County School Board | 1968 | naacp_brown | — | primary |
| Grovey v. Townsend | 1935 | white_primaries | — | primary |
| Grutter v. Bollinger | 2003 | affirmative_action | — | primary |
| Harmelin v. Michigan | 1991 | carceral_enforcement | — | primary |
| Harper v. Virginia State Board of Elections | 1966 | voting_rights | — | primary |
| Hudson v. Michigan | 2006 | carceral_enforcement | — | primary |
| Jones v. Alfred H. Mayer Co. | 1968 | spatial_containment | — | primary |
| Korematsu v. United States | 1944 | racial_classification | — | primary |
| McCleskey v. Kemp | 1987 | carceral_enforcement | — | primary |
| McCutcheon v. FEC | 2014 | campaign_finance | — | primary |
| McDonald v. City of Chicago | 2010 | second_amendment | `mcdonald` | primary |
| McLaurin v. Oklahoma State Regents | 1950 | naacp_brown | — | primary |
| Milliken v. Bradley | 1974 | spatial_containment | — | primary |
| Moore v. Dempsey | 1923 | peonage_13th | — | primary |
| NFIB v. Sebelius | 2012 | commerce_clause | — | primary |
| Nixon v. Condon | 1932 | white_primaries | — | primary |
| Nixon v. Herndon | 1927 | white_primaries | — | primary |
| NLRB v. Jones & Laughlin Steel | 1937 | commerce_clause | — | primary |
| Ozawa v. United States | 1922 | racial_classification | — | primary |
| Parents Involved v. Seattle | 2007 | affirmative_action | — | primary |
| Plessy v. Ferguson | 1896 | reconstruction_amendments | — | primary |
| Purkett v. Elem | 1995 | jury_selection | — | primary |
| Regents of UC v. Bakke | 1978 | affirmative_action | — | primary |
| San Antonio ISD v. Rodriguez | 1973 | spatial_containment | `san_antonio_v_rodriguez` | primary |
| Shelby County v. Holder | 2013 | voting_rights | — | primary |
| Shelley v. Kraemer | 1948 | spatial_containment | — | primary |
| Skinner v. Oklahoma | 1942 | eugenics | — | primary |
| Slaughterhouse Cases | 1873 | reconstruction_amendments | — | primary |
| Smith v. Allwright | 1944 | white_primaries | `smith_v_allwright` | primary |
| South Carolina v. Katzenbach | 1966 | voting_rights | — | primary |
| Strauder v. West Virginia | 1880 | jury_selection | — | primary |
| Swann v. Charlotte-Mecklenburg | 1971 | spatial_containment | — | primary |
| Sweatt v. Painter | 1950 | naacp_brown | — | primary |
| Terry v. Ohio | 1968 | carceral_enforcement | — | primary |
| United States v. Armstrong | 1996 | carceral_enforcement | — | primary |
| United States v. Bhagat Singh Thind | 1923 | racial_classification | — | primary |
| United States v. Cruikshank | 1876 | reconstruction_amendments | — | primary |
| United States v. Reese | 1876 | reconstruction_amendments | — | primary |
| United States v. Reynolds | 1914 | peonage_13th | — | primary |
| Utah v. Strieff | 2016 | carceral_enforcement | — | primary |
| Williams v. Mississippi | 1898 | reconstruction_amendments | `williams_v_miss` | primary |
| Yick Wo v. Hopkins | 1886 | reconstruction_amendments | — | primary |

---

## Tier 1 — Explicit Cite-Key Gaps (12 cases added)

| Case | Year | Cluster | Cite Key(s) | Status |
|---|---|---|---|---|
| Marbury v. Madison | 1803 | constitutional_foundation | `marbury_1803` | primary |
| Dred Scott v. Sandford | 1857 | racial_classification | `dredscott` | primary |
| Loving v. Virginia | 1967 | reconstruction_amendments | `loving_v_virginia_record_1967` | primary |
| Washington v. Davis | 1976 | intent_doctrine | `tel_wash_v_davis` | primary |
| Village of Arlington Heights v. Metropolitan Housing Dev. Corp. | 1977 | intent_doctrine | `tel_arlington_heights` | primary |
| DeShaney v. Winnebago County | 1989 | carceral_enforcement | `deshaney` | primary |
| Richmond Newspapers v. Virginia | 1980 | first_amendment | `richmond_newspapers_1980` | primary |
| Perry v. United States | 1935 | macroeconomics_finance | `perry_v_us_1935` | primary |
| Town of Castle Rock v. Gonzales | 2005 | carceral_enforcement | `castlerock` | primary |
| New York State Rifle & Pistol Assoc. v. Bruen | 2022 | second_amendment | `bruen` | primary |
| Dobbs v. Jackson Women's Health Organization | 2022 | gendered_kernel | `dobbs` | primary |
| United States v. Rahimi | 2024 | second_amendment | `rahimi2024` | primary |

---

## Tier 2 — Named in Manuscript, No Cite Key (7 cases added)

| Case | Year | Cluster | Chapters | Status |
|---|---|---|---|---|
| Bradwell v. Illinois | 1873 | gendered_kernel | ch4 | primary |
| Muller v. Oregon | 1908 | gendered_kernel | ch4 | primary |
| Reed v. Reed | 1971 | gendered_kernel | ch4 | primary |
| Roe v. Wade | 1973 | gendered_kernel | ch4 | primary |
| Relf v. Weinberger | 1974 | gendered_kernel | ch4 | research-stub |
| Madrigal v. Quilligan | 1978 | gendered_kernel | ch4 | research-stub |
| Obergefell v. Hodges | 2015 | buffer_class_expansion | ch13 | primary |

> `research-stub` = lower federal court (D.D.C. / C.D. Cal.); no SCOTUS PDF available; markdown is a detailed research summary.

---

## Tier 3 — Next-Pass Candidates (26 cases added)

### Bundle A — Intent-Doctrine Complex
| Case | Year | Cluster | Status |
|---|---|---|---|
| Personnel Administrator of Massachusetts v. Feeney | 1979 | intent_doctrine | next-pass |
| Mobile v. Bolden | 1980 | voting_rights | next-pass |
| City of Richmond v. J.A. Croson Co. | 1989 | affirmative_action | next-pass |
| Adarand Constructors v. Pena | 1995 | affirmative_action | next-pass |

### Bundle B — Affirmative-Action Terminal Arc
| Case | Year | Cluster | Status |
|---|---|---|---|
| Gratz v. Bollinger | 2003 | affirmative_action | next-pass |
| Schuette v. Coalition to Defend Affirmative Action | 2014 | affirmative_action | next-pass |
| Students for Fair Admissions v. Harvard | 2023 | affirmative_action | next-pass |

### Bundle C — Use-of-Force Doctrine
| Case | Year | Cluster | Status |
|---|---|---|---|
| Tennessee v. Garner | 1985 | carceral_enforcement | next-pass |
| Graham v. Connor | 1989 | carceral_enforcement | next-pass |
| Whren v. United States | 1996 | carceral_enforcement | next-pass |
| Scott v. Harris | 2007 | carceral_enforcement | next-pass |
| Rodriguez v. United States | 2015 | carceral_enforcement | next-pass |

### Bundle D — Juvenile-Sentencing Trilogy
| Case | Year | Cluster | Status |
|---|---|---|---|
| Roper v. Simmons | 2005 | carceral_enforcement | next-pass |
| Graham v. Florida | 2010 | carceral_enforcement | next-pass |
| Miller v. Alabama | 2012 | carceral_enforcement | next-pass |
| Ramos v. Louisiana | 2020 | carceral_enforcement | next-pass |

### Bundle E — VRA Post-Shelby Arc
| Case | Year | Cluster | Status |
|---|---|---|---|
| Rucho v. Common Cause | 2019 | voting_rights | next-pass |
| Brnovich v. Democratic National Committee | 2021 | voting_rights | next-pass |
| Allen v. Milligan | 2023 | voting_rights | next-pass |
| Moore v. Harper | 2023 | voting_rights | next-pass |

### Bundle F — Jury Selection Terminal Arc
| Case | Year | Cluster | Status |
|---|---|---|---|
| Flowers v. Mississippi | 2019 | jury_selection | next-pass |

### Bundle G — Religious-Exemption / Dobbs-Era Counter-Reform
| Case | Year | Cluster | Status |
|---|---|---|---|
| Trump v. Hawaii | 2018 | racial_classification | next-pass |
| Kennedy v. Bremerton School District | 2022 | first_amendment | next-pass |
| 303 Creative LLC v. Elenis | 2023 | first_amendment | next-pass |

### Bundle H — Excessive-Fines / Civil-Asset Architecture
| Case | Year | Cluster | Status |
|---|---|---|---|
| Timbs v. Indiana | 2019 | carceral_enforcement | next-pass |

---

## Summary

| Tier | Cases | Cumulative | PDFs | MDs |
|---|---|---|---|---|
| Baseline | 57 | 57 | 57 | 57 |
| Tier 1 | 12 | 69 | 12 | 12 |
| Tier 2 | 7 | 76 | 5 | 7 |
| Tier 3 | 26 | 102 | 25 | 26 |
| **Total** | **102** | **102** | **99** | **102** |

> Tier 2 PDFs = 5 because Relf (1974) and Madrigal (1978) are lower-court cases with no SCOTUS PDF; their markdowns are research summaries.  
> Two extra MDs are Relf and Madrigal stubs (no corresponding PDF).

---

## Tooling

```bash
# Run corpus-manuscript sync audit (checks cited-but-missing, bib-key-but-no-PDF)
python3 Paper/scripts/audit_scotus_corpus.py

# Regenerate case_index.yaml after adding new cases
# (edit Paper/scripts/download_new_scotus_cases.py CASES list, then re-run)

# Download + convert new cases
python3 Paper/scripts/download_new_scotus_cases.py --tiers 1 2 3

# Audit is also wired into make pdf:
make scotus-audit
```

## File Naming Convention

`{slug}_{year}.md` where slug = case name lowercased, spaces/punctuation → `_`, e.g.:
- `district_of_columbia_v_heller_2008.md`
- `new_york_state_rifle_pistol_association_v_bruen_2022.md`
- `village_of_arlington_heights_v_metropolitan_housing_development_corp_1977.md`
