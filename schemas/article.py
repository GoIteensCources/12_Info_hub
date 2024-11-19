from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, HttpUrl, model_validator, ConfigDict

from schemas import UserBase


# class Author():
#     name: str
#     email: EmailStr
#     bio: Optional[str] = None
#
#
# class Article():
#     title: str
#     content: str
#     author: Author
#     tags: Optional[list[str]] = []
#     published_at: datetime = Field(default_factory=datetime.now)
#
#
# class CommentBase(BaseModel):
#     author_name: str
#     content: str
#     created_at: datetime = Field(default_factory=datetime.now)


class InputArticle(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = Field(min_length=3)
    content: str
    tags: Optional[list[str]] = Field(None)


class InputComment(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    content: str


class SchComment(InputComment):
    model_config = ConfigDict(from_attributes=True)
    ...


class SchArticle(InputArticle):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tags: list = Field(default=[])
    published_at: datetime


class SchListArticles(BaseModel):
    ...
