"""
bucket/backtest.py

Backtest Agent for buckets.

Very simple backtest:
- For each coin, fetch historical prices via load_crypto_history(symbol)
- Compute return over the user horizon (or as much data as available)
- Aggregate to bucket-level return using weights.
"""

from typing import Dict, List
from datetime import timedelta

import pandas as pd

from market import load_crypto_history


def _compute_coin_return(df: pd.DataFrame, horizon_days: int) -> float:
    """
    Compute simple % return over the last `horizon_days`.

    If there isn't enough data, fall back to the full history.
    """
    if df.empty or "Close" not in df.columns:
        return 0.0

    df = df.sort_values("Date")

    if horizon_days is not None and "Date" in df.columns:
        # Filter to horizon window if dates are datetime-like
        try:
            df["Date"] = pd.to_datetime(df["Date"])
            end_date = df["Date"].iloc[-1]
            start_cut = end_date - timedelta(days=horizon_days)
            df = df[df["Date"] >= start_cut]
        except Exception:
            # If date parsing fails, just use all data
            pass

    if len(df) < 2:
        return 0.0

    start = float(df["Close"].iloc[0])
    end = float(df["Close"].iloc[-1])
    if start <= 0:
        return 0.0
    return (end - start) / start  # e.g. 0.25 = +25%


def backtest_buckets(buckets: List[Dict], prefs: Dict) -> List[Dict]:
    """
    Backtest each bucket and compute total return + per-coin contribution.

    Returns:
        [
          {
            "name": "Conservative",
            "risk": "conservative",
            "total_return_pct": 12.3,
            "coins": [
              {"symbol": "btc", "weight": 0.5, "return_pct": 10.0},
              ...
            ]
          },
          ...
        ]
    """
    horizon_days = prefs.get("horizon_days", 30)
    results: List[Dict] = []

    for bucket in buckets:
        bname = bucket.get("name", "Bucket")
        brisk = bucket.get("risk", "unknown")
        coins = bucket.get("coins", [])

        bucket_return = 0.0
        coin_results: List[Dict] = []

        for c in coins:
            sym = c["symbol"]
            weight = float(c.get("weight", 0.0))

            try:
                df = load_crypto_history(sym)
            except Exception:
                r = 0.0
            else:
                r = _compute_coin_return(df, horizon_days)

            bucket_return += weight * r
            coin_results.append(
                {
                    "symbol": sym,
                    "weight": round(weight, 4),
                    "return_pct": round(r * 100.0, 2),
                }
            )

        results.append(
            {
                "name": bname,
                "risk": brisk,
                "total_return_pct": round(bucket_return * 100.0, 2),
                "coins": coin_results,
            }
        )

    return results
