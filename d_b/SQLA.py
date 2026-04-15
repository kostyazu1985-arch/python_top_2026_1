from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapper, Session, mapped_column, relationship

from datetime import date
from typing import List

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    books: Mapped[List["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"AUTHOR: {self.name}, ID: {self.id}"