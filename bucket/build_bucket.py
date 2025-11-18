

from typing import Dict, List
import random


def _select_coins(universe: List[str], num_coins: int) -> List[str]:
    """
    Helper: pick num_coins from universe (deterministic shuffle seed for reproducibility).
    """
    # Use a fixed seed so results are reproducible for the same universe / prefs
    rnd = random.Random(42)
    coins = universe.copy()
    rnd.shuffle(coins)
    return coins[: max(1, min(num_coins, len(coins)))]


def build_buckets(universe: List[str], prefs: Dict) -> List[Dict]:
    """
    Build 1–3 buckets depending on user risk preference.

    Returns:
        List of dicts like:
        {
          "name": "Conservative",
          "risk": "conservative",
          "coins": [{"symbol": "btc", "weight": 0.5}, ...]
        }
    """
    num_coins = prefs.get("num_coins", 5)
    user_risk = prefs.get("risk", "balanced")

    buckets: List[Dict] = []

    # --- Conservative bucket (tilt to top of universe) ---
    conservative_universe = universe[: max(3, num_coins)]
    csel = _select_coins(conservative_universe, num_coins)
    c_weight = 1.0 / len(csel)
    buckets.append(
        {
            "name": "Conservative",
            "risk": "conservative",
            "coins": [{"symbol": sym, "weight": c_weight} for sym in csel],
        }
    )

    # --- Balanced bucket (mix of top & mid caps) ---
    mid_start = 1
    mid_end = min(len(universe), num_coins * 2)
    balanced_universe = universe[mid_start:mid_end] or universe
    bsel = _select_coins(balanced_universe, num_coins)
    b_weight = 1.0 / len(bsel)
    buckets.append(
        {
            "name": "Balanced",
            "risk": "balanced",
            "coins": [{"symbol": sym, "weight": b_weight} for sym in bsel],
        }
    )

    # --- Aggressive bucket (tilt to tail / smaller caps) ---
    if len(universe) > num_coins:
        tail_universe = universe[-max(num_coins * 2, 3) :]
    else:
        tail_universe = universe
    asel = _select_coins(tail_universe, num_coins)
    a_weight = 1.0 / len(asel)
    buckets.append(
        {
            "name": "Aggressive",
            "risk": "aggressive",
            "coins": [{"symbol": sym, "weight": a_weight} for sym in asel],
        }
    )

    # Optionally return only the bucket matching user risk.
    # For the competition it's nicer to show all 3, so the user
    # can compare risk/return.
    return buckets
