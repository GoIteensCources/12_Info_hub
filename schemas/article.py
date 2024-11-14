from typing import Optional


from pydantic import BaseModel, Field, ConfigDict



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

    ...


class SchListArticles(BaseModel):
    ...