import json
from datetime import datetime, timezone
from pathlib import Path

from backend.models import FeedbackRequest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
FEEDBACK_PATH = DATA_DIR / "feedback.json"


def list_feedback() -> list[dict]:
    if not FEEDBACK_PATH.exists():
        return []
    return json.loads(FEEDBACK_PATH.read_text(encoding="utf-8"))


def append_feedback(req: FeedbackRequest) -> dict:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    items = list_feedback()
    item = {
        "name": req.name,
        "rating": req.rating,
        "comment": req.comment,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    items.append(item)
    FEEDBACK_PATH.write_text(json.dumps(items, indent=2), encoding="utf-8")
    return {"saved": True, "item": item}
