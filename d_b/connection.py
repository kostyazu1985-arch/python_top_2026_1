from sqlalchemy import ForeignKey, Column, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine("sqlite:///lib.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class  Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author{self.name}>"

    def get_book_count(self) -> int:
        return len(self.books)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    years = Column(Integer)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Bookk{self.title}>"

session = Session()
author = Author(name="Толстой")

book1 = Book(title="Война и мир", years=1869, author=author)
book2 = Book(title="Петр Первый", years=1900, author=author)

session.add_all([author, book1, book2])
session.commit()
