import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models import ChatRequest, ChatResponse, FeedbackRequest
from backend.services.assistant import generate_reply
from backend.storage import append_feedback, list_feedback

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_PATH = PROJECT_ROOT / "shared" / "project_blueprint.json"
BLUEPRINT = json.loads(BLUEPRINT_PATH.read_text(encoding="utf-8"))

app = FastAPI(
    title=BLUEPRINT["project_name"],
    description=BLUEPRINT["primary_goal"],
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "status": "running",
        "project": BLUEPRINT["project_name"],
        "app_type": BLUEPRINT["app_type"],
    }


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/blueprint")
def get_blueprint():
    return BLUEPRINT


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    return generate_reply(BLUEPRINT, req.message)


@app.post("/run", response_model=ChatResponse)
def run(req: ChatRequest):
    return generate_reply(BLUEPRINT, req.message)


@app.post("/feedback")
def feedback(req: FeedbackRequest):
    return append_feedback(req)


@app.get("/feedback")
def feedback_items():
    return {"items": list_feedback()}
