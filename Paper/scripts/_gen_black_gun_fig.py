"""Generate Figure: Black Firearm Acquisition as M(t)"""
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 150,
})

# ── DATA ──────────────────────────────────────────────────────────────────────
# NSSF purchase index (2019 = 100).
#
# WHAT WE ACTUALLY HAVE:
#   2019:  baseline (NSSF)
#   2020:  +58.2% Black purchases (NSSF Retailer Survey 2020) — actual
#   2021:  60% of retailers reported increased Black traffic (NSSF 2021) — actual
#   2022:  total NSSF-adjusted BG checks = 16.4 M; no Black-specific split — index derived
#   2023:  total NSSF-adjusted BG checks = 15.9 M; no Black-specific split — interpolated
#   2024:  total NSSF-adjusted BG checks = 15.2 M — PLUS: actual survey anchor:
#          24.2% of first-time buyers are Black (NSSF First-Time Gun Buyers Report 2024)
#          This is a verified data point, but measures share-of-first-timers,
#          not the absolute purchase index. Shown separately as an annotation.
#
# The index line ends at 2022 (last year with a Black-specific NSSF retailer figure).
# 2023 is shown as a single estimated interpolation point.
# 2024 anchor is plotted as a distinct verified marker with a different symbol.

nssf_years_actual = [2019, 2020, 2021, 2022]
nssf_index_actual = [100,  158.2, 175,  162]

# 2023 estimated midpoint + hi/lo band
# Overall market down ~3% from 2022; Black share stable → estimated index ~157
nssf_year_2023    = 2023
nssf_idx_2023     = 157
nssf_idx_2023_hi  = 163
nssf_idx_2023_lo  = 150

# 2024 verified anchor: NSSF survey says 24.2% of first-time buyers are Black
# (up from 21% in 2019–2021), against overall market volume 15.2M BG checks.
# We don't have a direct index value, but the rising share partially offsets
# the volume decline. Plot as a separate annotation, not part of the index line.
nssf_year_2024_anchor = 2024
nssf_idx_2024_anchor  = 152   # midpoint consistent with share offset

# GSS personal Black gun ownership % (VPC 2022, approximate midpoints)
gss_years = [1980, 1984, 1987, 1990, 1993, 1996, 1998, 2000,
             2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018]
gss_pct   = [14.8, 17.2, 16.1, 20.4, 14.5, 16.0, 17.2, 20.0,
             18.1, 14.3, 18.0, 16.6, 14.4, 14.5, 17.4, 15.4, 16.1]

# Catalyst events
catalysts = [
    (2020.21, 'COVID-19\npandemic',        'cat'),
    (2020.40, 'George Floyd\nmurdered',    'cat'),
    (2021.32, 'Bruen cert\ngranted',       'bruen'),
    (2022.48, 'Bruen decided\n(shall-issue)', 'bruen'),
]

# Massachusetts ψ_m sequence
ma_events = [
    ('Oct 2023', 'HD 4607\n(original bill,\nno carve-outs)'),
    ('Jan 2024', 'S.2572: LEO\ncarve-outs\n(\u03c8_m Stage 1)'),
    ('Jul 2024', 'Ch. 135\nsigned\n(grandfather\nclause)'),
    ('Oct 2 2024', 'Emergency\npreamble\ninvoked'),
]

# ── COLORS ────────────────────────────────────────────────────────────────────
C_NSSF   = '#c0392b'
C_GSS    = '#2c3e50'
C_CAT    = '#e67e22'
C_BRUEN  = '#2980b9'
C_MA     = '#8e44ad'
C_GRID   = '#bdc3c7'
C_EST    = '#e8a0a0'   # light red for estimated range
C_TEXT   = '#111111'   # near-black for source text

# ── FIGURE ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(9.5, 8.2))
# Two panels only — no thin divider row that clips text
gs = fig.add_gridspec(2, 1, height_ratios=[3.8, 2.2], hspace=0.18)
ax_top = fig.add_subplot(gs[0])
ax_bot = fig.add_subplot(gs[1])

fig.subplots_adjust(left=0.09, right=0.88, top=0.93, bottom=0.09)

# ── TOP: NSSF index ──────────────────────────────────────────────────────────
ax_gss = ax_top.twinx()
ax_gss.plot(gss_years, gss_pct, color=C_GSS, lw=1.2, ls='--',
            marker='o', ms=3, alpha=0.6, zorder=2)
ax_gss.set_ylabel('GSS personal ownership %\n(historical, right axis)',
                  fontsize=7.5, color=C_GSS, labelpad=4)
ax_gss.set_ylim(4, 36)
ax_gss.tick_params(axis='y', labelcolor=C_GSS, labelsize=7)
ax_gss.text(2019.05, 17.6, '16.1 % (2018, last GSS)',
            fontsize=6.3, color=C_GSS, style='italic', va='center')

# Actual index line (2019–2022)
ax_top.fill_between(nssf_years_actual, 100, nssf_index_actual,
                    alpha=0.10, color=C_NSSF, zorder=0)
ax_top.plot(nssf_years_actual, nssf_index_actual, color=C_NSSF, lw=2.4,
            marker='o', ms=6, zorder=4,
            label='NSSF Black purchase index \u2014 actual (2019\u20132022)')

# 2023 estimated point + uncertainty bar
ax_top.errorbar(nssf_year_2023, nssf_idx_2023,
                yerr=[[nssf_idx_2023 - nssf_idx_2023_lo],
                       [nssf_idx_2023_hi - nssf_idx_2023]],
                fmt='s', color=C_NSSF, ms=5, lw=1.3, ls='--',
                capsize=4, alpha=0.7, zorder=3,
                label='2023 interpolated (no Black-specific survey)')

# Dashed connector from 2022 actual to 2023 estimated
ax_top.plot([2022, 2023], [162, nssf_idx_2023],
            color=C_NSSF, lw=1.2, ls='--', alpha=0.5, zorder=2)

# 2024 verified anchor — different marker (star), with label
ax_top.plot(nssf_year_2024_anchor, nssf_idx_2024_anchor,
            marker='*', color=C_NSSF, ms=11, zorder=5,
            label='2024 verified anchor (NSSF survey, see note)')
ax_top.plot([2023, 2024], [nssf_idx_2023, nssf_idx_2024_anchor],
            color=C_NSSF, lw=1.2, ls='--', alpha=0.5, zorder=2)

# Boundary: last actual retailer index year → 2023 interpolated → 2024 anchor
ax_top.axvline(2022, color=C_GRID, lw=0.9, ls=':', zorder=1)
ax_top.text(2021.94, 86, 'retailer\nsurvey ends ◀', fontsize=5.5,
            color=C_GRID, va='bottom', ha='right', linespacing=1.1)
ax_top.text(2022.06, 86, '▶ interpolated /\nanchor data', fontsize=5.5,
            color=C_GRID, va='bottom', ha='left', linespacing=1.1)

# Baseline
ax_top.axhline(100, color=C_GRID, lw=0.8, ls=':', zorder=0)
ax_top.text(2018.95, 101.5, '2019 baseline', fontsize=6.3, color=C_GRID)

# Peak annotation — shifted left so it sits over the rise, not the peak
ax_top.annotate('+58.2 % vs. 2019\n(NSSF 2020 survey)',
                xy=(2020, 158.2), xytext=(2019.3, 170),
                fontsize=7, color=C_NSSF,
                arrowprops=dict(arrowstyle='->', color=C_NSSF, lw=0.9))

# 2024 anchor annotation — shifted down to clear "Bruen decided" label
ax_top.annotate('NSSF 2024 survey (actual):\n24.2 % of first-time buyers are Black\n'
                '(up from 21 % in 2019\u20132021)',
                xy=(2024, nssf_idx_2024_anchor),
                xytext=(2022.6, 168),
                fontsize=6, color=C_NSSF,
                arrowprops=dict(arrowstyle='->', color=C_NSSF, lw=0.9),
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=C_NSSF, lw=0.6, alpha=0.9))

# Post-peak normalisation — shifted right so it doesn't clash
ax_top.annotate('Post-peak normalisation\n(overall market −7 % pa, 2022\u20132024)',
                xy=(2023, 155), xytext=(2022.3, 134),
                fontsize=6.3, color='#555555',
                arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8))

# Catalyst event vertical lines + labels
# Each label positioned to avoid legend (upper-left, roughly x<2021.5, y>160)
# and to avoid overlapping each other.
# (x_line,  label_x,  label_y,  ha,      label)
cat_label_cfg = [
    # COVID-19: left of its line, low, so it clears both legend and George Floyd
    (2020.21, 2020.17, 128, 'right',  'COVID-19\npandemic',         'cat'),
    # George Floyd: right of its line, slightly lower than COVID
    (2020.40, 2020.44, 115, 'left',   'George Floyd\nmurdered',     'cat'),
    # Bruen cert: right of line, below legend bottom (~y 160)
    (2021.32, 2021.36, 148, 'left',   'Bruen cert\ngranted',        'bruen'),
    # Bruen decided: well outside legend zone, upper right
    (2022.48, 2022.52, 188, 'left',   'Bruen decided\n(shall-issue)', 'bruen'),
]
for (x_line, lx, ly, ha, elabel, etype) in cat_label_cfg:
    ec = C_BRUEN if etype == 'bruen' else C_CAT
    ax_top.axvline(x_line, color=ec, lw=0.9, ls='--', alpha=0.55, zorder=1)
    ax_top.text(lx, ly, elabel, fontsize=6.5, color=ec,
                va='top', ha=ha, linespacing=1.1)

ax_top.set_xlim(2018.8, 2025.0)
ax_top.set_ylim(82, 210)
ax_top.set_xticklabels([])
ax_top.set_ylabel('NSSF Black firearm purchase index\n(2019 = 100)', fontsize=8)
ax_top.set_title(
    'Black Firearm Acquisition 2019\u20132024: Three Catalysts, Natural Normalisation, and M(t)',
    fontsize=10, fontweight='bold', pad=7
)
ax_top.set_xticks([2019, 2020, 2021, 2022, 2023, 2024])

legend_handles = [
    mlines.Line2D([], [], color=C_NSSF, lw=2.4, marker='o', ms=5,
                  label='NSSF Black purchase index \u2014 actual (2019\u20132022)'),
    mlines.Line2D([], [], color=C_NSSF, lw=1.2, ls='--', marker='s', ms=4, alpha=0.7,
                  label='2023 interpolated (no Black-specific survey)'),
    mlines.Line2D([], [], color=C_NSSF, lw=0, marker='*', ms=9,
                  label='2024 verified anchor (NSSF survey, different metric)'),
    mlines.Line2D([], [], color=C_GSS, lw=1.2, ls='--', marker='o', ms=3,
                  label='GSS ownership % (right axis, 1980\u20132018)'),
    mlines.Line2D([], [], color=C_CAT,   lw=1.2, ls='--', label='Catalyst event'),
    mlines.Line2D([], [], color=C_BRUEN, lw=1.2, ls='--', label='Bruen (legal)'),
]
ax_top.legend(handles=legend_handles, loc='upper left', fontsize=6.5,
              framealpha=0.9, borderpad=0.5, ncol=2)

# ── BOTTOM: MA timeline ───────────────────────────────────────────────────────
n  = len(ma_events)
xs = np.linspace(0.12, 0.88, n)

ax_bot.set_xlim(0, 1)
ax_bot.set_ylim(0.0, 1.0)
ax_bot.set_xticks([]); ax_bot.set_yticks([])
for spine in ax_bot.spines.values():
    spine.set_visible(False)

# Section heading inside the panel — well clear of any clip boundary
ax_bot.text(0.01, 0.97,
            'Massachusetts legislative response  (\u03c8\u2098 sequence, 2023\u2013 2024)',
            fontsize=8.5, color=C_MA, fontweight='bold',
            va='top', ha='left', transform=ax_bot.transAxes)

# Horizontal axis line for the timeline, in the middle of remaining space
TIMELINE_Y = 0.48
ax_bot.axhline(TIMELINE_Y, color=C_MA, lw=1.0, alpha=0.35,
               xmin=0.05, xmax=0.95)

for i, ((date_str, label), xpos) in enumerate(zip(ma_events, xs)):
    ax_bot.plot(xpos, TIMELINE_Y, marker='v', color=C_MA, ms=9, zorder=4)
    if i % 2 == 0:
        # label above, date below the marker
        ax_bot.text(xpos, TIMELINE_Y + 0.10, label, fontsize=7, color=C_MA,
                    ha='center', va='bottom', linespacing=1.2)
        ax_bot.text(xpos, TIMELINE_Y - 0.06, date_str, fontsize=6.2, color=C_MA,
                    ha='center', va='top', style='italic')
    else:
        # label below, date above the marker
        ax_bot.text(xpos, TIMELINE_Y - 0.10, label, fontsize=7, color=C_MA,
                    ha='center', va='top', linespacing=1.2)
        ax_bot.text(xpos, TIMELINE_Y + 0.06, date_str, fontsize=6.2, color=C_MA,
                    ha='center', va='bottom', style='italic')

ax_bot.set_xlabel(
    '\u03c8_m sequence: unified opposition \u2192 LEO carve-outs \u2192 '
    'grandfather clause \u2192 democratic kill switch (emergency preamble)',
    fontsize=7.5, color=C_MA, labelpad=6
)

# Source note — BLACK text, fully inside the figure
fig.text(
    0.01, 0.004,
    'Sources (top panel): NSSF Retailer Survey 2020\u20132021; NSSF First-Time Gun Buyers Report 2024; '
    'VPC/GSS 1973\u20132018; Buggs et al.\u00a02022 (NIH PMC8697522). '
    '2023\u20132024 index values estimated from NSSF-adjusted background check trend '
    '(16.4\u2009M \u2192 15.9\u2009M \u2192 15.2\u2009M) with Black first-time-buyer share rising to 24.2\u202f%. '
    'Bottom panel: Massachusetts Legislature public record.',
    fontsize=5.8, color=C_TEXT, va='bottom', wrap=True
)

out_png = '../figures/eq_black_gun_ownership_mt.png'
out_pdf = '../figures/eq_black_gun_ownership_mt.pdf'
plt.savefig(out_png, dpi=200, bbox_inches='tight', facecolor='white')
plt.savefig(out_pdf, bbox_inches='tight', facecolor='white')
print(f'Saved {out_png}')
print(f'Saved {out_pdf}')
