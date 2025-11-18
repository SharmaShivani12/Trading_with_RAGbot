

from typing import List
try:
    # If market.py is on the same path, import its mapping
    from market import COIN_MAP
except ImportError:
    COIN_MAP = {}


def get_universe() -> List[str]:
    """
    Return a list of coin symbols we can consider for buckets.

    Prefer COIN_MAP keys (used in the rest of your app). If that's
    not available for some reason, fall back to a static list.
    """
    if COIN_MAP:
        return list(COIN_MAP.keys())

    # Reasonable default universe if COIN_MAP isn't found
    return ["btc", "eth", "sol", "ada", "dot", "xrp", "ltc", "link", "matic"]
