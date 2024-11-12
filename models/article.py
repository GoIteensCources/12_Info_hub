from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Article():
    __tablename__ = 'Article'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    tags: Mapped[list[str]] = mapped_column(JSON)

    published_at: Mapped[float] = mapped_column(default=datetime.now())

    author = relationship("Author", backref="Article")


class Author():
    __tablename__ = 'Author'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    bio: Mapped[str] = mapped_column(nullable=True)


class Comments():
    __tablename__ = "Comments"

    id: Mapped[int] = mapped_column(primary_key=True)

    author_name: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    article = relationship("Article", backref="Comments")
