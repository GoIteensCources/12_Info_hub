from typing import Any

from pydantic import BaseModel, Field, EmailStr, model_validator, ConfigDict
import enum


class UserType(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class InputUserData(BaseModel):
    username: str = Field(min_length=4)
    email: EmailStr
    password: str = Field(min_length=6)
    password_repeat: str = Field(min_length=6)
    role: UserType = UserType.USER

    @model_validator(mode="after")
    @classmethod
    def valid_pass(cls, data: Any):
        if data.password != data.password_repeat:
            raise ValueError("passwords not match")
        return data


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str = Field(min_length=4)
    email: EmailStr

    role_user: UserType = UserType.USER


class ListBaseUsers(BaseModel):
    users: list[UserBase | None]
    count_users: int


class UserBaseDetails(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class FullUserBase(UserBase):
    model_config = ConfigDict(from_attributes=True)

    user_details: UserBaseDetails | None = None