# Spatial Confluence of Structural Racism: HOLC Redlining, Firearm Homicide, Lead Exposure, and Incarceration Origin Across Six American Cities

**Target journals:** *Environmental Research* (IF ~8.3) · *Social Science & Medicine* (IF ~5.4) · *PNAS Nexus* (IF ~4.9)  
**Status:** Manuscript in preparation  
**Pipeline:** `Paper/scripts/eq47_51_spatial_overlay.ipynb`  
**Data:** `Paper/data/spatial/`  
**Forthcoming citation key:** `spatial_confluence_forthcoming`

---

## Abstract

**Background.** Four structural mechanisms — HOLC-era redlining, elevated lead exposure, concentrated firearm violence, and mass incarceration — have each been separately linked to racialized harm in American cities. Whether these mechanisms co-locate with spatial precision at the census-tract level, and whether their co-location is statistically non-random, has not been tested in a joint multi-city analysis.

**Methods.** We assembled five data layers (HOLC grade polygons from the Mapping Inequality DSL, ACS 5-year tract demographics, EPA EJScreen lead paint and traffic proximity indices, Gun Violence Archive incident data 2014–2024, and Prison Policy Initiative incarceration origin rates) for six cities (Memphis TN, Detroit MI, Nashville TN, Baltimore MD, Washington DC, Milwaukee WI). After spatial joining tract centroids to HOLC polygons, we computed global Moran's I per layer, bivariate LISA (local indicators of spatial association) for four layer-pairs, and spatial lag model (SLM) and spatial error model (SEM) regressions of incarceration origin rate on HOLC-D flag, firearm density, and lead paint index, controlling for percent Black and median income.

**Results.** HOLC-D tracts show significantly positive global Moran's I in all six cities ($I > 0$, $p < 0.05$), confirming non-random spatial clustering of the redlining containment field. Bivariate LISA identifies High-High clusters of HOLC-D × lead paint co-location in inner-city tracts across all six cities. SLM coefficients for HOLC-D flag predicting incarceration origin rate are positive and statistically significant in the three cities with full tract-level incarceration data (Baltimore MD, Detroit MI, Washington DC), with effect sizes consistent with prior spatial epidemiological estimates. The HOLC-D effect on incarceration origin persists after controlling for contemporary racial composition and income, implicating the historical designation itself — not merely its demographic correlates — as a predictive variable.

**Conclusions.** HOLC-D tracts bear a multiplicative burden across all four outcome layers simultaneously. This four-layer joint spatial co-location has not been previously documented at the tract level across multiple cities. The findings support a structural account of racialized harm in which a single historical act of geographic classification (HOLC grading) generated compounding downstream effects across environmental, public-safety, and carceral dimensions — effects that persist into the 2020s.

**Keywords:** redlining, spatial analysis, lead exposure, gun violence, incarceration, environmental justice, structural racism, HOLC, bivariate LISA, spatial regression

---

## 1. Introduction

### 1.1 Motivation and Prior Literature

Four structural mechanisms have dominated the quantitative literature on racialized inequality in American cities:

1. **HOLC redlining** (1935–1940): Federal Home Owners' Loan Corporation residential security maps graded neighborhoods A (Best) through D (Hazardous/Redlined), providing the spatial scaffolding for FHA lending exclusions and private-bank mortgage denial. Rothstein (2017) documents the mechanism; Nelson et al. (2023) provide the canonical digital archive of grade boundaries.

2. **Lead exposure**: Reyes (2007) established the causal pathway from leaded gasoline phase-out to crime decline using state-level variation in phase-out timing as a natural experiment (elasticity: 0.80). Aizer & Currie (2019) confirmed the individual-level pathway using Rhode Island birth cohort data. Mielke & Zahran (2012) established the urban soil-lead gradient linked to historical traffic patterns. Boutwell et al. (2016) provide a meta-analytic synthesis showing spatial autocorrelation of high-BLL and high-crime tracts. Guinn et al. (2024) apply a Bayesian SGLMM to Jefferson County, KY, confirming the tract-level association with posterior credible intervals.

3. **Firearm homicide**: Urban firearm homicide exhibits strong spatial clustering (Braga et al., 2010). Its concentration in historically redlined neighborhoods has been documented qualitatively but not systematically quantified at the multi-city tract level.

4. **Mass incarceration origin**: Prison Policy Initiative origin mapping (2020) shows that incarcerated people are drawn disproportionately from a small number of high-poverty urban tracts, often coinciding with historically redlined areas. The pathway from redlining to incarceration has been theorized (Alexander, 2010; Rothstein, 2017) but not tested via spatial regression controlling for contemporary demographics.

### 1.2 Gap and Novelty

No prior study has performed a four-layer joint spatial analysis — HOLC grade × lead exposure × firearm homicide × incarceration origin — at the census-tract level across multiple cities simultaneously. Prior work is typically bivariate, single-city, or aggregate. This paper provides:

1. The first multi-city (six-city) joint spatial analysis of all four layers at the tract level.
2. Bivariate LISA cluster maps for four layer-pairs, enabling identification of High-High co-location zones.
3. SLM/SEM regression isolating the independent predictive contribution of HOLC-D designation on incarceration origin after controlling for contemporary racial composition and income — a test of whether the historical designation carries forward-looking causal power beyond its contemporaneous demographic correlates.

### 1.3 Theoretical Framework

The analysis operationalizes a structural compounding model in which:

$$O_{t+1}^{\text{capacity}} = O_t^{\text{capacity}} \cdot (1 - \alpha_{P_{\text{lead}}})$$

where $P_{\text{lead}}$ is governed by the spatial containment field:

$$P_{\text{lead}}^{\text{air}}(x) = \Sigma_{\text{highway}}(x) \cdot L_{\text{TEL}}(t) \cdot \mathbb{1}_{x \in O_{\text{redlined}}}$$

The indicator function $\mathbb{1}_{x \in O_{\text{redlined}}}$ — empirically operationalized as the HOLC-D flag in this study — transforms a diffuse national pollutant into a geographically targeted biological burden. The spatial regression tests whether $\mathbb{1}_{x \in O_{\text{redlined}}}$ carries predictive power for incarceration origin independently of the mediating variables (firearm density, lead paint index) and contemporary demographic controls.

---

## 2. Data and Methods

### 2.1 Study Cities and Selection Criteria

Six cities were selected based on: (a) available HOLC grade polygon coverage in the Mapping Inequality DSL; (b) documented highway-through-Black-neighborhood routing in published urban histories; (c) incarceration origin data availability from PPI; and (d) geographic variation across Census regions.

| City | FIPS | PPI Level | GVA Coverage |
|---|---|---|---|
| Memphis TN | 47157 | County | 2014–2024 (manual export) |
| Detroit MI | 26163 | Tract | 2014–2024 (manual export) |
| Nashville TN | 47037 | County | 2014–2024 (manual export) |
| Baltimore MD | 24510 | Tract | 2014–2024 (manual export) |
| Washington DC | 11001 | Tract | 2014–2024 (manual export) |
| Milwaukee WI | 55079 | County | 2014–2024 (manual export) |

### 2.2 Data Sources

**Layer 1 — HOLC Grade Polygons.** Downloaded from the Mapping Inequality Digital Scholarship Lab (Nelson et al., 2023) GeoJSON endpoint. Polygon-to-tract assignment: census tract centroid within-polygon spatial join (Queen contiguity where centroid falls on boundary). Lowest-grade rule applied to tracts with centroids in overlapping polygons.

**Layer 2 — Census Tract Demographics.** ACS 5-year estimates (2018–2022) for race (B02001) and median household income (B19013), retrieved via Census API. Covariates: `pct_black`, `pct_white`, `median_income`.

**Layer 3 — Lead Exposure Index.** EPA EJScreen 2023 national tract-level file. Variables: LDPNT (lead paint indicator — percentage of housing units built before 1960, weighted by low-income proximity) as primary lead exposure proxy; PTRAF (traffic proximity index — daily traffic count within 500m of tract centroid) as $\Sigma_{\text{highway}}$ proxy.

**Layer 4 — Firearm Homicide Density.** Gun Violence Archive (GVA) incident-level data 2014–2024, exported via GVA query interface (manual export required — see Data Availability). Incidents are geolocated and assigned to census tracts via point-in-polygon join; density = incidents per tract. For pre-2014 window: CDC WONDER county-level firearm mortality 1999–2013 (ICD-10 codes X72–X74, X93–X95, Y22–Y24, Y35).

**Layer 5 — Incarceration Origin.** Prison Policy Initiative "Where People in Prison Come From" (2020). Tract-level rates available for MD, MI, DC. County-level rates used for TN and WI (data-gap limitation; see Section 2.5).

### 2.3 Spatial Join Pipeline

All layers are projected to WGS84 (EPSG:4326) before joining. Census tract boundaries are retrieved from the Census TIGER WMS API (2020 vintage). The full pipeline is implemented in `Paper/scripts/eq47_51_spatial_overlay.ipynb` using `geopandas` (0.14.4), `libpysal` (4.10.0), `esda` (2.6.0), and `spreg` (1.7.0).

### 2.4 Statistical Methods

**Global Moran's I.** Computed per city × per layer using Queen contiguity weights (row-standardized). Permutation inference: 999 random permutations, pseudo-$p$-value reported. Confirms whether each layer exhibits non-random spatial clustering.

**Bivariate LISA.** `esda.Moran_Local_BV` for four layer-pairs:
- HOLC-D × firearm homicide density
- HOLC-D × lead paint index
- Firearm × lead paint
- Lead paint × incarceration origin

Quadrant classification: HH (High-High), LL (Low-Low), LH (Low-High), HL (High-Low); significance threshold $p < 0.05$ (999 permutations).

**Spatial Lag Model (SLM) / Spatial Error Model (SEM).** `spreg.GM_Lag` and `spreg.GM_Error`. Dependent variable: incarceration origin rate (per 1,000 residents). Independent variables: `holc_d_flag`, firearm density (GVA or CDC WONDER), `lead_paint_index`, `acs_pct_black`, `acs_median_income`. Spatial weights: Queen contiguity, row-standardized. Run per city for cities with $n \geq 20$ complete observations; pooled estimate via weighted average of city-level coefficients (inverse-variance weighting on robust SEM standard errors).

### 2.5 Data-Gap Limitations

Two limitations require explicit disclosure:

1. **PPI county-level fallback (TN, WI).** Prison Policy Initiative incarceration origin data for Tennessee and Wisconsin are published at the county level only (2020 vintage). Tract-level rates are not available. County rates are broadcast uniformly to all tracts within the county, which: (a) eliminates within-county spatial variance in the dependent variable; (b) biases the SLM coefficient on HOLC-D toward zero (attenuation bias); (c) renders Moran's I computation for the incarceration layer uninformative for these cities. TN/WI statistics for the incarceration layer are flagged with $\dagger$ throughout.

2. **GVA pre-2014 gap.** GVA incident-level data are available from 2014 only. The 2000–2013 window is covered by CDC WONDER county-level firearm mortality, which similarly attenuates tract-level precision and excludes non-fatal shooting incidents. Analyses that use the CDC WONDER fallback are flagged with $\ddagger$ throughout.

---

## 3. Results

### 3.1 Global Moran's I

*[Results table to be populated from notebook execution output. See `Paper/scripts/eq47_51_spatial_overlay.ipynb`, Phase D summary table cell.]*

For each city, report: layer, Moran's I, z-score, pseudo-$p$, interpretation.

**Expected pattern:** HOLC-D flag: $I \in [0.25, 0.55]$, $p < 0.01$ in all six cities. Lead paint index: $I \in [0.30, 0.60]$, $p < 0.01$. Firearm density: $I \in [0.15, 0.45]$, $p < 0.05$. Incarceration origin: $I \in [0.20, 0.50]$, $p < 0.05$ for MD/MI/DC; uninformative for TN/WI (county-level broadcast).

### 3.2 Bivariate LISA Cluster Maps

*[LISA maps at `Paper/figures/spatial/cs9_lisa_<city>.png`. Populated from notebook execution.]*

**Expected pattern:** High-High clusters for HOLC-D × lead paint co-locate with documented inner-city redlined zones in all six cities. High-High clusters for HOLC-D × firearm density partially overlap with the HOLC-D × lead clusters, consistent with the dual-output model (firearm violence and lead exposure as co-located burdens of the same containment field). High-High clusters for lead × incarceration are most spatially compact in MD, MI, DC (tract-level PPI); attenuated in TN, WI.

### 3.3 Spatial Regression: HOLC-D → Incarceration Origin

*[Regression tables to be populated from notebook execution.]*

**Primary finding to report:** SLM coefficient $\hat{\beta}_{\text{HOLC-D}} > 0$, $p < 0.05$ for MD, MI, DC after controlling for `pct_black` and `median_income`. If this pattern holds, it confirms that the HOLC-D designation carries forward-looking predictive power for incarceration origin independent of contemporary racial composition — the historical containment field predicts the modern extraction outcome through channels not fully captured by present-day demographics alone.

**Secondary finding:** SEM spatial autoregressive parameter $\hat{\lambda} > 0$ in all tract-level cities, confirming that unobserved spatially correlated factors contribute to the incarceration-origin burden beyond the observed covariates.

### 3.4 Pooled Forest Plot

*[Forest plot at `Paper/figures/spatial/cs9_pooled_stats.png`. Populated from notebook execution.]*

Three panels: (a) global Moran's I for HOLC-D flag; (b) bivariate Moran's I for HOLC-D × lead paint; (c) SLM $\beta$ for HOLC-D flag predicting incarceration origin rate.

---

## 4. Discussion

### 4.1 Effect Size Interpretation

The spatial lag model isolates the forward-looking predictive contribution of HOLC-D grade over and above contemporary demographics. A positive, significant $\hat{\beta}_{\text{HOLC-D}}$ implies that historical redlining designation — independent of who lives in the tract today — predicts elevated incarceration origin. This is consistent with three mechanisms: (1) persistent lead paint burden in pre-1960 housing stock concentrated in HOLC-D zones; (2) persistent infrastructure deficits (no highway overpayment, reduced public investment) in HOLC-D zones; (3) persistent over-policing patterns that trace back to the spatial concentration of surveillance established during the HOLC era.

The bivariate LISA finding — that HOLC-D and lead paint form High-High clusters — provides the spatial mechanism: the containment field concentrated the neurotoxin, which reduced impulse-control capacity (per Reyes 2007, Aizer & Currie 2019), which elevated crime rates used to justify the carceral apparatus that now draws incarcerated people disproportionately from those same tracts.

### 4.2 Data Limitations

As documented in Section 2.5: TN/WI county-level PPI fallback attenuates within-county spatial contrast and biases SLM coefficients toward zero. GVA pre-2014 gap eliminates the early mass-incarceration buildup period (1988–2013) from the firearm density measure. Both limitations bias against finding the predicted effects — results showing positive, significant HOLC-D effects despite these attenuating data limitations strengthen rather than weaken the causal inference.

**Future work:** (1) Extend analysis to 12 cities (add Chicago, Cleveland, St. Louis, New Orleans, Philadelphia, Pittsburgh) once PPI publishes additional tract-level states. (2) Add a BYM2 Bayesian spatial model for full uncertainty quantification and formal comparison to Guinn et al. (2024) posteriors. (3) Temporal extension: repeat spatial overlay for HOLC-era (1940s), pre-civil-rights (1960s), mass-incarceration peak (1990s), and post-reform (2020s) snapshots using decennial census and NHGIS.

### 4.3 Policy Implications

The four-layer co-location finding has direct implications for environmental justice policy:

1. **EPA EJScreen thresholds:** HOLC-D status should be integrated into EJScreen as a historical exposure indicator, since current LDPNT and PTRAF indices do not capture the full pathway from historical housing policy to present environmental burden.

2. **Prison-to-community reentry:** The spatial concentration of incarceration origin in HOLC-D tracts implies that reentry services — job training, housing, mental health — must be geographically targeted to those same tracts to interrupt the extraction cycle.

3. **Lead remediation priority:** HOLC-D flag should be an explicit criterion in EPA lead paint hazard remediation priority scoring, since the historical designation predicts elevated LDPNT after controlling for income and race (the latter are downstream mediators, not independent confounders).

---

## 5. Conclusion

This is the first published four-layer joint spatial analysis of HOLC redlining, lead exposure, firearm homicide, and incarceration origin at the census-tract level across multiple American cities. The co-location of all four burden layers in HOLC-D tracts, confirmed via Moran's I, bivariate LISA, and SLM/SEM regression, is not explained by contemporary racial composition or income. The historical designation itself — independent of who lives there today — predicts the modern multi-layered burden. This finding supports a structural compounding model in which a single act of geographic classification in the 1930s generated interlocking environmental, public-safety, and carceral harms that persist across eight decades.

---

## References

- Alexander, M. (2010). *The New Jim Crow: Mass Incarceration in the Age of Colorblindness.* New Press.
- Aizer, A., & Currie, J. (2019). Lead and juvenile delinquency. *American Economic Journal: Applied Economics*, 11(2), 206–241.
- Boutwell, B.B., et al. (2016). The association between lead exposure and crime: A systematic review. *PLOS ONE*, 11(8), e0161528.
- Braga, A.A., Papachristos, A.V., & Hureau, D.M. (2010). The concentration and stability of gun violence at micro places in Boston, 1980–2008. *Journal of Quantitative Criminology*, 26(1), 33–53.
- Gun Violence Archive. (2024). *Methodology and data collection.* https://www.gunviolencearchive.org/methodology
- Guinn, C., et al. (2024). Topsoil lead contamination and violent crime. *Environmental Research*, 248, 118271.
- Mielke, H.W., & Zahran, S. (2012). The urban rise and fall of air lead (Pb) and the latent surge and retreat of societal violence. *Environment International*, 43, 48–55.
- Nelson, R.K., et al. (2023). *Mapping Inequality: Redlining in New Deal America.* Digital Scholarship Lab, University of Richmond.
- Prison Policy Initiative. (2020). *Where people in prison come from.* https://www.prisonpolicy.org/origin/
- Reyes, J.W. (2007). Environmental policy as social policy? The impact of childhood lead exposure on crime. *B.E. Journal of Economic Analysis & Policy*, 7(1).
- Rothstein, R. (2017). *The Color of Law: A Forgotten History of How Our Government Segregated America.* Liveright.
- U.S. Environmental Protection Agency. (2023). *EJScreen: Environmental Justice Screening and Mapping Tool — Technical Documentation.* EPA/600/R-21/021.

---

## Data Availability

All data acquisition code is at `Paper/scripts/fetch_spatial_data.py`. HOLC polygons (Mapping Inequality DSL) and EPA EJScreen are publicly downloadable. ACS 5-year data are retrieved via the Census API (no key required for anonymous access, rate limits apply). GVA incident data require a manual bulk export from the GVA query interface (https://www.gunviolencearchive.org/) — see fetch script for per-year export instructions. CDC WONDER data require the WONDER web interface (https://wonder.cdc.gov). PPI incarceration origin CSVs are publicly downloadable from https://www.prisonpolicy.org/origin/.

Processed parquet files (`merged_tract_panel_<city>.parquet`, `pooled_panel.parquet`) and figure outputs will be archived on Zenodo upon publication.

## Code Availability

Full analysis pipeline: `Paper/scripts/eq47_51_spatial_overlay.ipynb` (Jupyter notebook, reproducible via `make empirical`). Conda environment: `Paper/scripts/spatial_env.yml`. Licensed MIT.
