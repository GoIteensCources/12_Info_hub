from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from settings import settings_app as s
from settings import get_session
from models.article import Article
from schemas.article import InputArticle, SchArticle

route = APIRouter()


async def create_article():
    ...


async def get_article_by_id():
    ...


async def all_articles():
    ...


@route.put('/change/{article_id}')
async def change_article(article_id: int, article_data: InputArticle, session: AsyncSession = Depends(get_session)):
    article = await session.get(Article, article_id)

    article.title = article_data.title
    article.content = article_data.content
    article.tags = article_data.tags

    await session.commit()
    await session.refresh(article)
    return {"message": f"{article_id} changed successfully"}


@route.delete('/{article_id}')
async def delete_article_by_id(article_id: int, session: AsyncSession = Depends(get_session)):
    article = await session.get(Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    await session.delete(article)
    await session.commit()
    return SchArticle.model_validate(article)


async def create_comment():
    ...


async def delete_comment():
    ...


async def search():
    ...
