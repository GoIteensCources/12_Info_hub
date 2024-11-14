from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from settings import settings_app as s
from settings import get_session

route = APIRouter()


async def create_article():
    ...


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