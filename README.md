# Athlete Viral Marketing Impact Analysis

This project analyses an athlete-led viral marketing campaign to determine whether reach translates into acquisition — across channels, conversion stages, and offline behaviour signals.

## Problem

Campaigns can produce high impressions but weak commercial conversion. The analysis examines whether awareness translated into signups, trials, and memberships, and identifies which channels drove efficient growth versus which contributed primarily to reach volume.

## What This Project Analyses

- Which channels delivered the most reach — and which delivered the best acquisition efficiency
- Whether awareness converted to action across the funnel: clicks, signups, trials, memberships
- Cost per membership by channel, with spend efficiency mapped against conversion outcomes
- Brand lift signals and offline wellness behaviour change relative to the campaign window

## Data

- Type: synthetic campaign dataset (portfolio-safe, seeded for reproducibility)
- Raw and processed tables are in `data/raw` and `data/processed`
- Core model table: `data/processed/fact_channel_daily.csv`
- Supporting dimensions and proxies:
  - `data/processed/dim_channel.csv`
  - `data/processed/dim_period.csv`
  - `data/processed/brand_interest_index.csv`
  - `data/processed/gym_activity.csv`

## Data Model

The dataset follows a star schema designed for direct Power BI consumption.

| Table | Role |
|---|---|
| `fact_channel_daily` | Daily metrics by channel — impressions, clicks, spend, signups, trials, memberships |
| `dim_channel` | Channel dimension: name, type, spend category |
| `dim_period` | Date dimension: week, campaign phase, is_campaign_active flag |
| `brand_interest_index` | Brand lift proxy: weekly search index trend |
| `gym_activity` | Offline behaviour proxy: gym visits and new memberships |

## Approach

1. Generate campaign and funnel data (`src/generate_data.py`)
2. Clean and transform to analysis-ready tables (`src/clean_transform.py`)
3. Produce channel-level decision outputs for reporting and Power BI consumption

## Key Findings

- TikTok delivered the highest impressions by a significant margin but the lowest direct conversion efficiency — consistent with its structural role as an upper-funnel awareness channel rather than a direct-response acquisition tool.
- Paid search and email produced the lowest cost-per-membership despite significantly lower reach volumes.
- Brand search index showed a measurable uplift during the campaign window, confirming awareness was building even where immediate conversion was not occurring.
- Offline gym activity spiked approximately two weeks post-campaign, consistent with a consideration-to-action lag typical of wellness product adoption.

## Deliverables

- Python data pipeline: `src/generate_data.py`, `src/clean_transform.py`
- Jupyter analysis notebook: `notebooks/01_generate_and_clean.ipynb`
- Report pack:
  - `reports/00_executive_summary.md`
  - `reports/01_insights_and_recommendations.md`
  - `reports/02_data_dictionary.md`
  - `reports/athlete_viral_marketing_dashboard.html` — self-contained HTML dashboard
- Power BI-ready star-schema inputs in `data/processed`
- PBIX: `dashboard/athlete-viral-marketing-impact-analysisv1.pbix`

## How to Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/generate_data.py
python src/clean_transform.py
```

## Live Dashboard

[View interactive HTML dashboard](https://kabelo-analytics.github.io/athlete-viral-marketing-impact-analysis/)

---

Built by Kabelo Makua · kabelo-analytics · https://km-webdvlpr.github.io/III.IV/
