from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer)
    isbn = Column(String, unique=True)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False) # Внешний ключ книги с автором

    author = relationship("Author", back_populates="books") # Ссылка на объект автора

class Reader(Base):
    __tablename__ = "readers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False, unique=True)

class LibraryManager:
    def __init__(self, db_url):

        self.engine = create_engine(db_url) # движок подключения к бд

        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):

        Base.metadata.create_all(self.engine)
        print("Таблицы authors, books, readers спешно созданы!")


























