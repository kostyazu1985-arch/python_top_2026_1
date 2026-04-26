from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name})>"

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False) # Внешний ключ книги с автором
    author = relationship("Author", back_populates="books") # Ссылка на объект автора

class Reader(Base):
    __tablename__ = "readers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False, unique=True)

class LibraryManager:
    def __init__(self, db_path):
      self.engine = create_engine(f"sqlite:///{db_path}")
      self.Session = sessionmaker(bind=self.engine)
      self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

# CRUD

    def add_author(self, name: str):
        new_author = Author(name=name)
        self.session.add(new_author)
        self.session.commit()
        return new_author

    def get_all_authors(self):
        return self.session.scalars(select(Author)).all() # для получения списка всех объектов

    def find_author_by_id(self, author_id):
        return self.session.get(Author, author_id) # поиск записи по первичному ключу

    def update_author(self, author_id, new_name: str):
        author = self.find_author_by_id(author_id) # находим автора, меняем атрибут и сохраняем
        if author:
            author.name = new_name
            self.session.commit()
        return author

    def delete_author(self, author_id):
        author = self.find_author_by_id(author_id) # находим автора, удаляем и сохраняем
        if author:
            self.session.delete(author)
            self.session.commit()
            return True
        return False

























