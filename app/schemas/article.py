from datetime import datetime

from pydantic import BaseModel, Field


class ArticleCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1)
    tags: list[str] = []


class ArticleOut(BaseModel):
    id: str
    title: str
    content: str
    tags: list[str]
    created_at: datetime | None = None
