from datetime import datetime, timezone

def get_current_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
