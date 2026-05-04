from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from datetime import date


# Базовый класс для всех таблиц
class Base(DeclarativeBase):
    pass


# --- ТАБЛИЦЫ (МОДЕЛИ) ---

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}')"


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    isbn = Column(String, unique=True)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="books")
    issues = relationship("BookIssue", back_populates="book")

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}')"


class Reader(Base):
    __tablename__ = "readers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    issues = relationship("BookIssue", back_populates="reader")

    def __repr__(self):
        return f"Reader(id={self.id}, name='{self.first_name} {self.last_name}')"


class BookIssue(Base):
    __tablename__ = "book_issues"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    issue_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book = relationship("Book", back_populates="issues")
    reader = relationship("Reader", back_populates="issues")

    def __repr__(self):
        return f"Issue(id={self.id}, book_id={self.book_id}, return={self.return_date})"


# --- МЕНЕДЖЕР БИБЛИОТЕКИ ---

class LibraryManager:
    def __init__(self, db_path):
        self.engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # --- МЕТОДЫ ДЛЯ АВТОРОВ (CRUD) ---
    def add_author(self, name):
        author = Author(name=name)
        self.session.add(author)
        self.session.commit()
        print(f"Добавлен автор: {name}")

    def get_all_authors(self):
        return self.session.query(Author).all()

    def find_author_by_id(self, author_id):
        return self.session.get(Author, author_id)

    def update_author(self, author_id, new_name):
        author = self.find_author_by_id(author_id)
        if author:
            author.name = new_name
            self.session.commit()

    def delete_author(self, author_id):
        author = self.find_author_by_id(author_id)
        if author:
            self.session.delete(author)
            self.session.commit()

    # --- МЕТОДЫ ДЛЯ КНИГ (CRUD) ---
    def add_book(self, title, author_id, year, isbn=None):
        author = self.find_author_by_id(author_id)
        if author:
            book = Book(title=title, author_id=author_id, year=year, isbn=isbn)
            self.session.add(book)
            self.session.commit()
            print(f"Добавлена книга: {title}")
        else:
            print(f"Ошибка: Автор с ID {author_id} не найден!")

    def get_all_books(self):
        return self.session.query(Book).all()

    def find_book_by_id(self, book_id):
        return self.session.get(Book, book_id)

    def update_book(self, book_id, new_title=None, new_year=None, new_isbn=None):
        book = self.find_book_by_id(book_id)
        if book:
            if new_title: book.title = new_title
            if new_year: book.year = new_year
            if new_isbn: book.isbn = new_isbn
            self.session.commit()

    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()

    # --- МЕТОДЫ ДЛЯ ЧИТАТЕЛЕЙ (CRUD) ---
    def add_reader(self, first_name, last_name, email):
        try:
            reader = Reader(first_name=first_name, last_name=last_name, email=email)
            self.session.add(reader)
            self.session.commit()
            print(f"Добавлен читатель: {first_name} {last_name}")
        except Exception:
            self.session.rollback()
            print(f"Ошибка: Email {email} уже занят!")

    def get_all_readers(self):
        return self.session.query(Reader).all()

    def find_reader_by_id(self, reader_id):
        return self.session.get(Reader, reader_id)

    def update_reader(self, reader_id, first_name=None, last_name=None, email=None):
        reader = self.find_reader_by_id(reader_id)
        if reader:
            if first_name: reader.first_name = first_name
            if last_name: reader.last_name = last_name
            if email: reader.email = email
            self.session.commit()

    def delete_reader(self, reader_id):
        reader = self.find_reader_by_id(reader_id)
        if reader:
            self.session.delete(reader)
            self.session.commit()

    # --- ЛОГИКА ВЫДАЧИ И ВОЗВРАТА ---
    def issue_book_to_reader(self, book_id, reader_id):
        # Проверяем, не занята ли книга (есть ли выдача без даты возврата)
        active_issue = self.session.query(BookIssue).filter_by(book_id=book_id, return_date=None).first()

        if active_issue:
            print(f"Книга ID {book_id} уже выдана!")
            return

        new_issue = BookIssue(book_id=book_id, reader_id=reader_id, issue_date=date.today())
        self.session.add(new_issue)
        self.session.commit()
        print(f"Книга ID {book_id} выдана читателю ID {reader_id}.")

    def return_book_from_reader(self, issue_id):
        issue = self.session.get(BookIssue, issue_id)
        if issue and issue.return_date is None:
            issue.return_date = date.today()
            self.session.commit()
            print(f"Книга по выдаче №{issue_id} возвращена.")
        else:
            print("Ошибка возврата.")

    def get_active_issues(self):
        return self.session.query(BookIssue).filter(BookIssue.return_date == None).all()
