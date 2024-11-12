from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials, HTTPBearer
from fastapi_sso import GoogleSSO
from starlette import status

from werkzeug.security import check_password_hash
from settings import settings_app as s

route = APIRouter()


async def registration_user():
    ...


async def get_by_id_user():
    ...


async def get_all_users():
    ...


async def delete_user():
    ...


