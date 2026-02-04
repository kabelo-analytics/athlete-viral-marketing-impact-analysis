"""Cleaning + transformation helpers.

These helpers are intentionally simple and Power BI-friendly.
"""
from __future__ import annotations
import pandas as pd

def safe_div(numer: pd.Series, denom: pd.Series) -> pd.Series:
    denom = denom.replace({0: pd.NA})
    return numer / denom
