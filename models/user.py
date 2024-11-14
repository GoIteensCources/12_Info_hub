from sqlalchemy.orm import Mapped, mapped_column
from schemas.user import UserType


from settings import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password_hash: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[UserType] = mapped_column()

    def __str__(self):
        return f"User: {self.email}, {self.role}"

