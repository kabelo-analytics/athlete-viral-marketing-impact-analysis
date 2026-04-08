# Athlete Viral Marketing Impact Analysis

This project analyses an athlete-led viral marketing campaign to determine how reach, conversion, brand lift, and offline behaviour move together in a synthetic marketing scenario.

## Problem

Campaigns can produce high impressions but weak commercial conversion. The analysis examines whether awareness translated into signups, trials, and memberships, and identifies where scale, conversion efficiency, and offline demand diverged.

## What This Project Analyses

- Which channels delivered the most reach and which converted that reach more efficiently
- Whether awareness converted to action across the funnel: clicks, signups, trials, memberships
- Cost per membership for spend-bearing channels, with Website treated separately as a conversion destination
- Brand lift signals and offline wellness behaviour change relative to the campaign window

## Data

- Type: synthetic campaign dataset (portfolio-safe, shipped as prebuilt raw and processed tables)
- Raw and processed tables are in `data/raw` and `data/processed`
- Core model table: `data/processed/fact_channel_daily.csv`
- Supporting dimensions and proxies:
  - `data/processed/dim_channel.csv`
  - `data/processed/dim_period.csv`
  - `data/processed/brand_interest_index.csv`
  - `data/processed/gym_activity.csv`

## Data Model

The dataset is organised as a Power BI-friendly table set centred on `fact_channel_daily`, with lightweight dimension and proxy tables for channel, period, brand interest, and gym activity.

| Table | Role |
|---|---|
| `fact_channel_daily` | Daily metrics by channel - impressions, clicks, spend, signups, trials, memberships |
| `dim_channel` | Channel dimension: name, type, primary KPI |
| `dim_period` | Campaign-phase lookup table used for period grouping |
| `brand_interest_index` | Brand lift proxy: search interest trend |
| `gym_activity` | Offline behaviour proxy: gym visits and new memberships |

## Approach

1. Review the shipped raw and processed campaign tables
2. Inspect the notebook and helper scripts for table structure and KPI definitions
3. Use the processed outputs for reporting and Power BI consumption

## Key Findings

- TikTok delivered the highest impressions by a significant margin and the largest absolute membership volume, but its downstream conversion per click trailed Website, Instagram, and YouTube.
- Among spend-bearing channels in this synthetic dataset, TikTok posted the lowest reported CPA, while Website acted as the strongest conversion destination rather than a comparable media channel.
- Brand search index showed a measurable uplift during the campaign window relative to the pre-campaign baseline.
- Offline membership activity spiked early in the campaign period, indicating demand concentrated around launch rather than appearing on a fixed two-week lag.

## Deliverables

- Packaged dataset plus helper files: `src/generate_data.py`, `src/clean_transform.py`
- Jupyter inspection notebook: `notebooks/01_generate_and_clean.ipynb`
- Report pack:
  - `reports/00_executive_summary.md`
  - `reports/01_insights_and_recommendations.md`
  - `reports/02_data_dictionary.md`
  - `reports/athlete_viral_marketing_dashboard.html` - self-contained HTML dashboard
- Power BI-friendly processed inputs in `data/processed`
- PBIX: `dashboard/athlete-viral-marketing-impact-analysisv1.pbix`

## How to Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/generate_data.py
python src/clean_transform.py
```

The repository currently ships prebuilt tables for analysis. The helper scripts are lightweight placeholders rather than a full public regeneration pipeline.

## Live Dashboard

[View interactive HTML dashboard](https://kabelo-analytics.github.io/athlete-viral-marketing-impact-analysis/)

---

Built by Kabelo Makua - kabelo-analytics - https://km-webdvlpr.github.io/III.IV/
