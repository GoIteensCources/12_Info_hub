from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, HttpUrl, model_validator, ConfigDict


class Author():
    name: str
    email: EmailStr
    bio: Optional[str] = None


class Article():
    title: str
    content: str
    author: Author
    tags: Optional[list[str]] = []
    published_at: datetime = Field(default_factory=datetime.now)


class CommentBase(BaseModel):
    author_name: str
    content: str
    created_at: datetime = Field(default_factory=datetime.now)

