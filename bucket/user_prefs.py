

from typing import Dict


def parse_user_preferences(text: str) -> Dict:
    """
    Extract a small set of preferences from user text.

    We keep this intentionally simple and rule-based for now.
    """
    t = text.lower()

    # --- Risk level ---
    if "conservative" in t or "low risk" in t:
        risk = "conservative"
    elif "aggressive" in t or "high risk" in t:
        risk = "aggressive"
    else:
        risk = "balanced"

    # --- Number of coins ---
    num_coins = 5  # default
    for n in range(3, 11):
        if f"{n} coin" in t or f"{n} coins" in t:
            num_coins = n
            break
        if f"top {n}" in t:
            num_coins = n
            break

    # --- Time horizon (days) ---
    horizon_days = 30  # default
    if "90 day" in t or "3 month" in t or "quarter" in t:
        horizon_days = 90
    elif "7 day" in t or "1 week" in t:
        horizon_days = 7
    elif "year" in t or "12 month" in t:
        horizon_days = 365

    prefs = {
        "risk": risk,
        "num_coins": num_coins,
        "horizon_days": horizon_days,
        # For future extension:
        "themes": [],       # e.g. ["defi", "l2"]
        "exclude": [],      # e.g. ["meme"]
    }
    return prefs
