
from typing import Dict, Any, List
from bucket.user_prefs import parse_user_preferences
from bucket.universe import get_universe
from bucket.build_bucket import build_buckets
from bucket.backtest import backtest_buckets


def run_bucket_pipeline(user_text: str) -> Dict[str, Any]:
    """
    Main entry point for the bucket / portfolio multi-agent pipeline.

    Args:
        user_text: natural language query from the user

    Returns:
        A dictionary with:
            - "preferences": parsed user preferences
            - "buckets": list of bucket definitions
            - "evaluation": backtest results per bucket
    """
    # 1) Parse user preferences
    prefs = parse_user_preferences(user_text)

    # 2) Get the tradable universe
    universe = get_universe()

    # 3) Build bucket(s) based on preferences & universe
    buckets = build_buckets(universe, prefs)

    # 4) Backtest / evaluate each bucket
    eval_results = backtest_buckets(buckets, prefs)

    return {
        "preferences": prefs,
        "buckets": buckets,
        "evaluation": eval_results,
    }
