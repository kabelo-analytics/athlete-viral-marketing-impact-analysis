# Data Dictionary

## data/raw/campaign_events.csv (post-level)
- post_id: unique post identifier
- date: YYYY-MM-DD
- period: pre_campaign / campaign / post_campaign
- channel: TikTok, Instagram, YouTube, X, TV_Trailer, Website
- channel_type: social / video / offline_media / owned
- content_type: teaser, stunt_clip, doc_trailer, behind_scenes, partner_offer
- is_paid: 1 if paid distribution was used, else 0
- spend_usd: paid spend (0 if organic)
- impressions: reach / exposures
- video_views: views proxy
- likes / shares / comments: engagement
- clicks: clicks to landing pages
- landing_page: destination path

## data/raw/funnel_conversions.csv (daily by channel)
- signups, free_trials, memberships, rewards_joined

## data/processed/fact_channel_daily.csv
Daily by channel plus derived KPIs:
- ctr, cpc, signup_rate, trial_rate, membership_rate, cpa_membership

Interpretation notes:
- `Website` is included as a tracked destination touchpoint and should be interpreted separately from paid or earned media when comparing efficiency.
- Daily funnel counts are reporting aggregates, not user-level same-day journey records.

## data/processed/brand_interest_index.csv
- brand_search_index (0-100): proxy for brand lift / search interest

## data/processed/gym_activity.csv
- gym_visits: daily visits proxy
- new_memberships: daily gym memberships proxy
