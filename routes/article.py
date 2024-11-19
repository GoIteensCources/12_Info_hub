from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import session
from starlette import status
from sqlalchemy import select
from fastapi.responses import JSONResponse

from models import Comment, User, Article
from routes.auth import get_current_user
from schemas import InputComment
from settings import settings_app as s
from settings import get_session

route = APIRouter()


async def create_article():
    ...


async def get_article_by_id(session: AsyncSession, article_id: int):
    stmt = select(Article).filter(Article.id == article_id)
    result = await session.execute(stmt)  # Execute the query async
    article = result.scalars().first()
    return article


async def all_articles():
    ...


async def change_article():
    ...


async def delete_article_by_id():
    ...


@route.post("/create_comment/")
async def create_comment(content: str, article_id: int, current_user: User = Depends(get_current_user),
                         session: AsyncSession = Depends(get_session)
                         ):
    stmt = select(Article).filter(Article.id == article_id)
    article = await session.scalar(stmt)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    new_comment = Comment(content=content, user_id=current_user.id, article_id=article_id)
    session.add(new_comment)
    await session.commit()
    await session.refresh(new_comment)
    return InputComment.model_validate(new_comment)


@route.post("/delete_comment/")
async def delete_comment(comment_id: int, session: AsyncSession = Depends(get_session)
                         ):
    result = await session.execute(select(Comment).filter(Comment.id == comment_id))

    comment = result.scalars().first()

    if comment:
        await session.delete(comment)
        await session.commit()
        return JSONResponse(content={"message": f"Comment {comment_id} успішно видалений."}, status_code=200)
    else:
        JSONResponse(content={"message": f"Comment {comment_id} незнайдено."}, status_code=400)


async def search():
    ...
