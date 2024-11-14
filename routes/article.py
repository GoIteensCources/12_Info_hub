from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status

from models import Article
from schemas import InputArticle, SchArticle
from settings import settings_app as s
from settings import get_session
from routes.user import  get_current_user

route = APIRouter()


@route.post("/")
async def create_article(article: InputArticle,
                         user=Depends(get_current_user),
                         session=Depends(get_session)) -> SchArticle:
    new_article = Article(**article.model_dump(), author=user)
    session.add(new_article)
    try:
        await session.commit()
        await session.refresh(new_article)
        return SchArticle.model_validate(new_article)

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Помилка при створенні статті")


async def get_article_by_id():
    ...


async def all_articles():
    ...


async def change_article():
    ...


async def delete_article_by_id():
    ...


async def create_comment():
    ...


async def delete_comment():
    ...


async def search():
    ...
