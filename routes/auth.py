from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status


from werkzeug.security import check_password_hash
from settings import settings_app as s

route = APIRouter()