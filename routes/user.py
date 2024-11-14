from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import InputUserData, ListBaseUsers, OutUser, UpdateUser

from models.user import User
from settings import get_session
from werkzeug.security import generate_password_hash
from routes.auth import get_current_admin, get_current_user

route = APIRouter()


@route.post("/")
async def registration(data_user: InputUserData,
                       session: AsyncSession = Depends(get_session)) -> OutUser:
    stmt = select(User).filter_by(email=data_user.email)
    user = await session.scalar(stmt)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is exists")

    user_dict = data_user.model_dump()
    user_dict["password_hash"] = generate_password_hash(user_dict["password"])
    del user_dict["password_repeat"]
    del user_dict["password"]

    new_user = User(**user_dict)

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return OutUser.model_validate(new_user)


@route.get("/account/all/")
async def get_all_users(session: AsyncSession = Depends(get_session),
                        _=Depends(get_current_admin)) -> ListBaseUsers:
    users = await session.scalars(select(User))
    count = await session.scalar(select(func.count()).select_from(User))
    return ListBaseUsers(users=users, count_users=count)


@route.get("/account/")
async def account_current_user(current_user=Depends(get_current_user)) -> OutUser:
    return OutUser.model_validate(current_user)


@route.put("/")
async def change_by_id(data: UpdateUser,
                       current_user=Depends(get_current_user),
                       session: AsyncSession = Depends(get_session)) -> OutUser:
    if data.username:
        current_user.username = data.username
    if data.bio:
        current_user.bio = data.bio

    await session.commit()
    await session.refresh(current_user)
    return OutUser.model_validate(current_user)


async def drop_user():
    pass
