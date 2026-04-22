# `Paper/data/` — Curated datasets for empirical notebooks

This directory holds the CSV/JSON inputs consumed by the equation-level
Jupyter notebooks under `Paper/scripts/`. Each file is committed to the
repository so that `make empirical` can run end-to-end without network
access.

## Spectral-formulation datasets (Chapter 8, Interference Engine)

The files below feed `Paper/scripts/spectral_fourier.ipynb`,
`Paper/scripts/spectral_laplace.ipynb`, `Paper/scripts/scotus_corpus_analysis.ipynb`,
and `Paper/scripts/eq40_45_interference_engine.ipynb`.

> **Data availability status (2026-04-22)**
> - ✅ SCOTUS keyword counts — generated from 57 PDF opinions
> - ✅ All original spectral inputs (GT, CR, ANES, backlash proxies)
> - ⏳ GDELT per-axis — placeholder only; requires BigQuery (see below)
> - ⏳ NYT per-axis — not yet retrieved; requires free API key (see below)

### Two-stage pipeline: `raw/` → processed

The spectral inputs follow a transparent two-stage pipeline:

1. **`Paper/data/raw/`** — archived source-attributed exports. Each file
   is committed once and treated as immutable. Header comments record
   the upstream provider, retrieval method, retrieval date, variable
   codes, and any basket composition. Editing these files is a manual
   curatorial act, not a build-time side effect.
2. **`Paper/data/*.csv` / `.json`** — analysis-ready outputs produced by
   `Paper/scripts/preprocess_spectral_data.py`. This script performs
   only deterministic preprocessing transformations (interpolation on a
   uniform grid, smoothing, share computation, per-segment min-max
   rescaling) — it never generates, fits, or calibrates signal values.

> `make empirical` **does not** run the preprocessor. The empirical
> target is a pure consumer of the committed processed files, which
> keeps the spectral analysis inputs bit-stable across runs and avoids
> hidden write-side-effects on datasets referenced by the manuscript
> and registry. Use the separate `make data-refresh` target when you
> intentionally re-run preprocessing after editing a raw file.

### File map

| Processed file | Raw source | Consumer | Shape | Period | Upstream provider |
| --- | --- | --- | --- | --- | --- |
| `google_trends_class_identity.csv` | `raw/google_trends_raw.csv` | `spectral_fourier.ipynb` | ~1096 rows × 3 cols | Weekly, 2004–2024 | Google Trends (Pytrends CLI snapshot, 2024-12-31). |
| `congressional_record_word_freq.csv` | `raw/congressional_record_raw.csv` | `spectral_fourier.ipynb` | 60 rows × 5 cols | Annual, 1965–2024 | GovInfo bulk Congressional Record + ProQuest Congressional keyword search (2024-11-15). |
| `anes_issue_salience.csv` | `raw/anes_momp_raw.csv` | `spectral_fourier.ipynb` | 73 rows × 4 cols | Annualized (originally biennial), 1948–2020 | ANES Time Series Cumulative Data File, 2022 release (2024-10-20). |
| `historical_shocks.json` | `raw/historical_shocks_raw.json` | `spectral_laplace.ipynb` | 4 records | 1865 / 1964 / 2008 / 2020 | Author-constructed timeline of political shocks and backlash-onset labels. |
| `backlash_proxies.csv` | `raw/backlash_proxies_raw.csv` | `spectral_laplace.ipynb` | ~95 rows × 4 cols | Annual, 1865–2024 | Published academic estimates (Trelease 1971, Foner 1988, Carter 1996, Pew 2010–2020, Skocpol & Williamson 2012, SPLC / ADL extremism reports). |
| `gdelt_per_axis.csv` | `raw/gdelt_per_axis_raw.csv` | `eq40_45_interference_engine.ipynb` | ~138 rows × 6 cols | Monthly, 2013–2024 | GDELT GKG v2, BigQuery public dataset. **Requires BigQuery** — see "Retrieving GDELT data" section below. Placeholder CSV committed. |
| `nyt_per_axis.csv` | `raw/nyt_per_axis_raw.csv` | `eq40_45_interference_engine.ipynb` | ~180 rows × 7 cols | Quarterly, 1979–2024 | NYT Article Search API (free key, register at developer.nytimes.com). **Preferred alternative to GDELT** — see "Retrieving NYT data" section below. |
| `scotus_keyword_counts.csv` | `raw/scotus_keyword_counts_raw.csv` | `scotus_corpus_analysis.ipynb` | ~110 rows × 14 cols | 1873–2018 | Internet Archive SCOTUS opinion PDFs (57 cases). **Requires** `python3 Paper/scripts/scotus_text_extract.py`. |

### Column dictionaries

**`google_trends_class_identity.csv`** (preprocessed)

- `date` — week-ending date (Sunday), ISO-8601.
- `class_signal_index` — Google Trends index (0–100) averaged across
  the keyword basket `{'union', 'strike', 'class war', 'minimum wage',
  'labor rights'}`, gap-filled and lightly smoothed.
- `identity_signal_index` — Google Trends index averaged across
  `{'racism', 'gender war', 'trans rights', 'intersectionality',
  'privilege'}`, gap-filled and lightly smoothed.

**`congressional_record_word_freq.csv`** (preprocessed)

- `year` — calendar year.
- `class_word_freq` — Congressional Record occurrences (sum across
  chambers) of `{'union', 'strike', 'minimum wage', 'labor', 'working
  class'}`.
- `identity_word_freq` — occurrences of `{'racism', 'racial', 'sexism',
  'gender identity', 'LGBT*'}`.
- `class_share` — `class_word_freq / (class_word_freq + identity_word_freq)`.
- `identity_share` — `identity_word_freq / (class_word_freq + identity_word_freq)`.

**`anes_issue_salience.csv`** (preprocessed)

- `year` — survey / interpolation year.
- `econ_salience_pct` — share naming economy / jobs / cost-of-living
  as "most important problem" (ANES VCF0875 roll-up).
- `race_salience_pct` — share naming race / civil rights (ANES VCF0875
  racial-problems category).
- `cross_group_solidarity_pct` — share agreeing with the ANES
  cross-race economic-solidarity item (nearest analogue to VCF9015).

Biennial ANES rows are linearly interpolated onto a uniform 1-year
grid for FFT use; the unsmoothed biennial values live in
`raw/anes_momp_raw.csv`.

**`historical_shocks.json`** — list of shock records with fields

- `shock_year`, `backlash_onset_year`, `label`, `description`
- `damping_ratio_guess`, `natural_period_years` — initial values
  supplied to `scipy.optimize` when fitting `H(s)`.

**`backlash_proxies.csv`** (preprocessed)

- `shock_year` — matches a record in `historical_shocks.json`.
- `year` — calendar year.
- `backlash_index` — raw magnitude in native units (Klan membership in
  thousands; favourability percent; militia membership in thousands).
- `backlash_index_norm` — per-shock min-max rescale of `backlash_index`
  onto a common 0–100 axis. The Laplace notebook fits
  `backlash_index_norm` so heterogeneous unit scales are comparable on
  one response axis.

**`gdelt_per_axis.csv`** (preprocessed)

- `year_month` — ISO-8601 year-month (e.g. `1979-01`).
- `race_share` — fraction of total articles matching race-axis theme codes.
- `gender_share` — fraction matching gender-axis theme codes.
- `religion_share` — fraction matching religion-axis theme codes.
- `sexuality_share` — fraction matching sexuality-axis theme codes.
- `total_count` — total article count for the month (denominator).

> **Note**: This file is a placeholder until the GDELT BigQuery query is run.
> All share columns will be `NaN` in the committed placeholder. Run
> `python3 Paper/scripts/gdelt_per_axis_query.py` and then `make data-refresh`.

**`scotus_keyword_counts.csv`** (preprocessed)

- `case_name` — case title (matches download manifest).
- `year` — decision year.
- `total_words` — word count of the text section.
- `class_count`, `race_count`, `gender_count`, `religion_count`, `sexuality_count` — raw keyword counts per basket.
- `class_per_1k`, `race_per_1k`, `gender_per_1k`, `religion_per_1k`, `sexuality_per_1k` — counts per 1,000 words.
- `class_share` — `class_per_1k / (class_per_1k + identity_per_1k)`.
- `identity_share` — `1 - class_share`.
- `is_dissent` — `True` for dissenting opinion sections, `False` for majority.

> **Note**: This file requires `python3 Paper/scripts/scotus_text_extract.py` to be run first.

### Additional dataset: suppression substitution proxies

| Processed file | Raw source | Consumer | Shape | Period | Upstream provider |
| --- | --- | --- | --- | --- | --- |
| `eq40_45_suppression_proxies.csv` | Author-constructed ordinal calibration | `eq40_45_interference_engine.ipynb` | 30 rows × 5 cols | Annual, 1956–1985 | Church Committee (1976), Carter (1996), ANES Cumulative (2022), manuscript calibration |

**`eq40_45_suppression_proxies.csv`** — ordinal suppression-component proxies for the suppression substitution analysis (Section D of the interference-engine case study).

- `year` — calendar year.
- `R_proxy` — kinetic repression component. Coded 1.0 during full COINTELPRO activity (1956–1971), declining to 0.30 post-Church Committee. Based on Church Committee Final Report (1976).
- `phi_load_proxy` — phase-load component. Rising from 0.20 (1956, race-only axis) to 0.65 (1979, Moral Majority full activation). Based on manuscript calibration at lines 4815–4833 and ANES solidarity data.
- `psi_s_proxy` — status wage / Southern Strategy component. Low in 1956, rising through Nixon Southern Strategy (1968), peaking with Reagan coalition (1980). Based on Carter (1996) and Black & Black (2002).
- `sigma_sup_composite` — sum of the three components (unnormalized). The notebook normalizes by the window mean for stability analysis.

> **Note**: All values are ordinal calibration estimates, not cardinal measurements. Per manuscript line 4964.

### Preprocessing steps applied by `preprocess_spectral_data.py`

| Processed file | Transformations |
| --- | --- |
| `google_trends_class_identity.csv` | (1) reindex to uniform W-SUN grid; (2) linear interpolation of missing weeks; (3) 3-week centered rolling mean. |
| `congressional_record_word_freq.csv` | (1) sort ascending; (2) compute `class_share`, `identity_share` as fractions of the combined basket total. |
| `anes_issue_salience.csv` | (1) sort ascending; (2) linear interpolation of biennial rows onto a 1-year grid. |
| `historical_shocks.json` | verbatim pass-through (validated as JSON). |
| `backlash_proxies.csv` | (1) sort ascending by `(shock_year, year)`; (2) per-shock min-max rescale to `backlash_index_norm ∈ [0, 100]`. |
| `gdelt_per_axis.csv` | (1) sort ascending by `year_month`; (2) compute per-axis shares as `axis_count / total_count`; (3) replace zero denominators with NaN. |
| `nyt_per_axis.csv` | (1) drop rows with failed retrieval (count == -1); (2) sort ascending by `year_quarter`; (3) compute per-axis shares as `axis_count / total_count`; (4) replace zero denominators with NaN. |
| `scotus_keyword_counts.csv` | (1) sort ascending by `(year, case_name)`; (2) compute `class_share = class_per_1k / (class_per_1k + identity_per_1k)`. |

### Refreshing the processed files

If you edit a file in `Paper/data/raw/`, regenerate the processed
outputs with:

```
make data-refresh
```

This is the only target that writes to the processed CSV/JSON files.
`make empirical` never overwrites them.

---

## Retrieving NYT per-axis data (preferred — no BigQuery needed)

The NYT Article Search API is free and requires only a registration at
[developer.nytimes.com](https://developer.nytimes.com/).

**Steps:**

1. Register at https://developer.nytimes.com/ and create an app.
2. Copy your API key (it is a 32-character string).
3. Run the retrieval script:

```bash
python3 Paper/scripts/nyt_per_axis_query.py --api-key YOUR_KEY_HERE
```

The script queries 5 axes × 45 years × 4 quarters = 900 requests.
At the 10 req/min rate limit this takes ~90 minutes.  It writes results
incrementally to `Paper/data/raw/nyt_per_axis_raw.csv` and can be
resumed after interruption (existing rows are skipped).

4. After retrieval completes, run:

```bash
make data-refresh
```

This generates `Paper/data/nyt_per_axis.csv`.

**Keyword queries per axis:**

| Axis | Query string |
|---|---|
| Race | "civil rights" OR "racial discrimination" OR "race relations" OR "systemic racism" OR "police brutality" OR "racial justice" |
| Gender | "gender discrimination" OR "women's rights" OR feminism OR "sexual harassment" OR "gender pay gap" OR "Title IX" |
| Religion | "religious freedom" OR "religious rights" OR evangelical OR "separation of church" OR "prayer in school" OR "religious liberty" |
| Sexuality | "gay rights" OR "LGBTQ" OR "same-sex" OR transgender OR "homosexual" OR "sexual orientation" |
| Class | "income inequality" OR "wealth gap" OR "working class" OR "labor rights" OR "economic inequality" OR "poverty" |

---

## Retrieving GDELT per-axis data (alternative — requires Google Cloud)

GDELT GKG v2 provides monthly per-axis theme shares from April 2013–2024.
This requires a free Google Cloud account with a project.

**Option A — BigQuery Console (no Python client needed):**

1. Go to https://console.cloud.google.com/bigquery
2. Log in with your Google account.
3. Create a free project if prompted (no billing required for the 1 TB free tier).
4. Click "+ Compose New Query" and paste the SQL from running:
   ```bash
   python3 Paper/scripts/gdelt_per_axis_query.py
   ```
5. Run the query (estimated scan: 100–300 GB, within the free 1 TB/month quota).
6. Click "Save Results → CSV (Google Drive or local)".
7. Save to `Paper/data/raw/gdelt_per_axis_raw.csv`.
8. Run `make data-refresh`.

**Option B — Python client:**

```bash
pip install google-cloud-bigquery
gcloud auth application-default login   # requires gcloud CLI
python3 Paper/scripts/gdelt_per_axis_query.py --method bigquery
make data-refresh
```

**Note on coverage:** GKG v2 coverage begins April 2013. The GDELT query
will return ~138 months (April 2013–December 2024), not 1979–2024.
For the full 1979–2024 period, use the NYT API approach instead.
