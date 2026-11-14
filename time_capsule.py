
from pydantic import BaseModel, Field
from typing import Optional


class CapsuleCreate(BaseModel):
    title: str = Field(min_length=5, max_length=100)

    category: str

    message: str = Field(min_length=30, max_length=2000)

    author: Optional[str] = "Anonymous"


class SituationRequest(BaseModel):
    situation: str = Field(min_length=10, max_length=1000)


class ModerationRequest(BaseModel):
    approved: bool
