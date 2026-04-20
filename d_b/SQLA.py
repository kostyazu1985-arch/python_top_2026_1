from sqlalchemy import ForeignKey, String, create_engine, select, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapper, Session, mapped_column, relationship

from datetime import date
from typing import List

from d_b.connection import author


class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    books: Mapped[List["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"AUTHOR: {self.name}, ID: {self.id}"

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self):
        return f"BOOK: {self.title}, ID: {self.id}"


engine = create_engine("sqlite:///books.db")
Base.metadata.create_all(engine)

# with Session(engine) as session:
#     author1 = Author(name="Айзек Азимов")
#     book1 = Book(title="Основание", year=1950, author=author1)
#     book2 = Book(title="Я, робот", year=1958, author=author1)
#
#     session.add(author1)
#     session.commit()

# with Session(engine) as session:
#     stm = select(Author).where(Author.name == "Айзек Азимов")
#
#     author_result = session.execute(stm).scalar_one_or_none()
#
#     if author_result:
#         print(f"{author_result}")
#         print(f"{author_result.books}")
#
#
#     stm_book = select(Book).where(Book.title == "Основание")
#     book_result = session.execute(stm_book).scalar_one_or_none()
#
#     if book_result:
#         print(f"{book_result}")


# with Session(engine) as session:
#     stm = select(Author).where(Author.name == "Айзек Азимов")
#     author_upd = session.execute(stm).scalar_one_or_none()
#
#     if author_upd:
#         print(f"{author_upd}")
#         author_upd.name = "Azimov"
#         session.commit()
#         print(f"{author_upd}")


with Session(engine) as session:
    stmd = select(Book).where(Book.title == "Основание")
    book_del = session.execute(stmd).scalar_one_or_none()

    if book_del:
        print(f"{book_del}")
        session.delete(book_del)
        session.commit()
        print(f"{book_del}")
