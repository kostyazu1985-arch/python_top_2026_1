from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
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
    year = Column(Integer)
    isbn = Column(String, unique=True)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False) # Внешний ключ книги с автором
    author = relationship("Author", back_populates="books") # Ссылка на объект автора

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', year={self.year})>"


class Reader(Base):
    __tablename__ = "readers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False, unique=True)

    def __repr__(self):
        return f"<Reader(id={self.id}, name='{self.first_name} {self.last_name}')>"

class LibraryManager:
    def __init__(self, db_path):
      self.engine = create_engine(f"sqlite:///{db_path}")
      Base.metadata.create_all(self.engine)
      Session = sessionmaker(bind=self.engine)
      self.session = Session()




# CRUD для Book
    def add_author(self, name):
        author = Author(name=name)
        self.session.add(author)
        self.session.commit()

    def get_all_authors(self):
        return self.session.query(Author).all()  # для получения списка всех объектов

    def find_author_by_id(self, author_id):
        return self.session.get(Author, author_id)  # поиск записи по первичному ключу

    def update_author(self, author_id, new_name: str):
        author = self.find_author_by_id(author_id)  # находим автора, меняем атрибут и сохраняем
        if author:
            author.name = new_name
            self.session.commit()

    def delete_author(self, author_id):
        author = self.find_author_by_id(author_id)  # находим автора, удаляем и сохраняем
        if author:
            self.session.delete(author)
            self.session.commit()

    def add_book(self, title, author_id, year, isbn=None): # добавляет новую книгу
        author = self.find_author_by_id(author_id)
        if author:
            new_book  = Book(title=title, author_id=author_id, year=year, isbn=isbn)
            self.session.add(new_book)
            self.session.commit()
            print(f"Книга с названием {title} добавлена к автору {author.name}.")
        else:
            print(f"Ошибка! Автора с таким ID {author_id} не существует")

    def get_all_books(self): #  возвращает список всех книг
        return self.session.query(Book).all() # возврат списка объектов из т books

    def find_book_by_id(self, book_id): # находит и возвращает книгу по её ID
        return self.session.get(Book, book_id) # поиск записи по первичному ключу

    def update_book(self, book_id, new_title=None, new_year=None, new_isbn=None): # обновляет поля книги
        book = self.find_book_by_id(book_id)
        if book: # обновляет новое значение (если не None)
            if new_title: book.title = new_title
            if new_year: book.year = new_year
            if new_isbn: book.isbn = new_isbn
            self.session.commit()
            print(f"Данные книги {book_id} успешно обновлены!")

    def delete_book(self, book_id): # удаляет книгу по ID
        book = self.find_book_by_id(book_id) # находим автора, удаляем и сохраняем
        if book:
            self.session.delete(book)
            self.session.commit()
            print(f"Книга {book_id} успешно удалена!")


# Методы для READER

    def add_reader(self, first_name, last_name, email): #  добавляет нового читателя
        try:
            new_reader = Reader(first_name=first_name, last_name=last_name, email=email)
            self.session.add(new_reader)
            self.session.commit()
            print(f"Читатель {first_name} {last_name} успешно зарегистрирован")
        except Exception:
            self.session.rollback() # отмена неудачной операции
            print(f"Ошибка! {email} уже существует!")

    def get_all_readers(self): # возвращает список всех читателей
        return self.session.query(Reader).all()

    def find_reader__by_id(self, reader_id): # находит и возвращает читателя по его ID
        return self.session.get(Reader, reader_id)

    # обновляет поля читателя
    def update_reader(self, reader_id, first_name=None, last_name=None, email=None):
        reader = self.find_reader_by_id(reader_id)
        if reader:
            if first_name: reader.first_name = first_name
            if last_name: reader.last_name = last_name
            if email: reader.email = email
            self.session.commit()
            print(f"Данные {reader_id} обновлены!")

    #  удаляет читателя по ID
    def delete_redaer(self, reader_id):
        reader = self.find_reader_by_id(reader_id)
        if reader:
            self.session.delete(reader)
            self.session.commit()
            print(f"Читатель {reader_id} успешно удален!")
























