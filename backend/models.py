from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    project: str
    message: str
    answer: str
    suggestions: list[str]
    next_steps: list[str]


class FeedbackRequest(BaseModel):
    name: str = Field(default="Anonymous", max_length=80)
    rating: int = Field(..., ge=1, le=5)
    comment: str = Field(default="", max_length=1000)
