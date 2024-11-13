import asyncio

from werkzeug.security import generate_password_hash

from settings import Base, async_session, engine
from models.user import User
from schemas import UserTypeEnum


async def create_bd():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_data():
    async with async_session() as sess:
        u1 = User(name="admin",
                  email="admin@ex.com",
                  password=generate_password_hash("admin"),
                  user_role=UserTypeEnum.ADMIN)
        u2 = User(name="user", email="user@ex.com", password=generate_password_hash("user"), user_role=UserTypeEnum.USER)



        sess.add_all([u1, u2])
        await sess.commit()


async def main():
    await create_bd()
    print("database created")
    await insert_data()
    print("data added")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())