# Athlete-led Viral Marketing Impact Analysis (Synthetic Data)

**Goal (plain English):**  
I wanted a portfolio project that feels like real work — not a random Kaggle dataset. So I built a synthetic (but realistic) dataset around an **extreme athlete-led viral campaign** and analysed whether it moved the needle for a wellness brand (and by extension: gyms, health insurers, and rewards programmes).

TikTok is the main character here — it’s the awareness engine — but the analysis is honest about what it does well (reach) and where it needs help (conversion).

---

## What’s inside this repo

- ✅ **Synthetic dataset (raw + processed)** — ready for **Power BI**
- ✅ **Jupyter Notebook** — shows how the data is generated + cleaned
- ✅ **Power BI-friendly tables** (`fact_channel_daily` + dims)
- ✅ Recruiter-readable write-up in `reports/`
- ⏳ Placeholder folder for your PBIX dashboard (`dashboard/`)

---

## The business questions

1. Which channels drove the most **reach** vs the best **efficiency**?
2. Does awareness translate into action? (Clicks → Signups → Trials → Memberships)
3. What’s the **cost per membership** by channel?
4. Do we see signs of **brand lift** and **offline wellness behaviour**?

---

## Data model (Power BI)

Start with:

- `data/processed/fact_channel_daily.csv` (daily by channel)
- Join to:
  - `data/processed/dim_channel.csv` on `channel`
  - Use `date` for your Date table
- Add:
  - `data/processed/brand_interest_index.csv` (brand lift proxy)
  - `data/processed/gym_activity.csv` (offline proxy)

---

## Quick measures to build

- Total Spend, Impressions, Clicks
- CTR = Clicks / Impressions
- Signups, Trials, Memberships
- CPA (Membership) = Spend / Memberships
- Brand Search Index trend (pre vs campaign vs post)
- Gym Visits / New Memberships trend

---

## Folder structure

- `data/raw/` → “messy reality” (post-level + daily conversions)
- `data/processed/` → Power BI-ready tables
- `notebooks/` → how the data is generated + cleaned
- `reports/` → executive summary + insights + data dictionary
- `src/` → helper modules
- `dashboard/` → drop your PBIX here

---

## Disclaimer

This is a **synthetic dataset** created for portfolio demonstration.  
It’s inspired by real-world campaign patterns, but it is **not** Netflix data and not an actual athlete contract dataset.

---

## Author

Kabelo (kabelo-analytics)
