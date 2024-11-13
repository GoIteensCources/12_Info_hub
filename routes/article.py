from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials, HTTPBearer
from fastapi_sso import GoogleSSO
from starlette import status


from werkzeug.security import check_password_hash
from settings import settings_app as s

route = APIRouter()


async def create():
    ...

async def get_by_id():
    ...


async def all_articles():
    ...


async def delete_by_id():
    ...


async def create_comment():
    ...


async def delete_comment():
    ...


async def search():
    ...

async def change_article():
    ...