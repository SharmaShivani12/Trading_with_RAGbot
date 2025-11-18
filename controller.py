
from typing import Tuple, Any
from bucket_pipeline import run_bucket_pipeline


def route_query(user_input: str) -> Tuple[str, Any]:
    """
    Route the user query to the appropriate high-level agent.

    Returns:
        (route, result)

        route:
            - "bucket"  -> portfolio / bucket result from run_bucket_pipeline
            - "none"    -> controller did not handle, caller should fall back
    """
    text = user_input.lower()

    if "bucket" in text or "portfolio" in text:
        return "bucket", run_bucket_pipeline(user_input)

    # Future: you could add routes for "backtest", "risk", etc.
    return "none", None
