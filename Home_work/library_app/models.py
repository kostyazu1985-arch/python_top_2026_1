from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from datetime import date


# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass


# --- ТАБЛИЦЫ (МОДЕЛИ) ---

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author") # связь с книгами

    def __repr__(self):
        return f"Автор(id={self.id}, имя='{self.name}')"


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
        return f"Книга(id={self.id}, название='{self.title}')"


class Reader(Base):
    __tablename__ = "readers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    issues = relationship("BookIssue", back_populates="reader")

    def __repr__(self):
        return f"Читатель(id={self.id}, имя='{self.first_name} {self.last_name}')"


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
        status = f"вернул {self.return_date}" if self.return_date else "на руках"
        return f"выдача {self.id}: книга {self.book_id} у читателя {self.reader_id} ({status})"


# --- МЕНЕДЖЕР ЛОГИКИ ---

class LibraryManager:
    def __init__(self, db_path):
        self.engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # --- МЕТОДЫ ПОИСКА ---

    def find_books_by_author_name(self, author_name):
        return self.session.query(Book).join(Author).filter(Author.name == author_name).all()

    def display_all_books_with_authors(self):
        books = self.session.query(Book).join(Author).all()
        print("\n--- СПИСОК ВСЕХ КНИГ ---")
        for book in books:
            print(f"Книга: '{book.title}' | Автор: {book.author.name} | Год: {book.year}")

    # ---CRUD---

    def add_author(self, name):
        author = Author(name=name)
        self.session.add(author)
        self.session.commit()
        print(f"Добавлен автор: {name}")

    def delete_author(self, author_id):
        author = self.session.get(Author.id, author_id)
        if author:
            if len(author.books) > 0:
                raise ValueError(f"Нельзя удалить автора '{author.name}', у него есть книги в базе!")
            self.session.delete(author)
            self.session.commit()
            print(f"Автор удален")
        else:
            print(f"Автор не найден")

    def add_book(self, title, author_id, year, isbn=None):
        author = self.session.get(Author.id, author_id)
        if not author:
            raise ValueError(f"Автора с ID {author_id} не существует")
        book = Book(title=title, author_id=author_id, year=year, isbn=isbn)
        self.session.add(book)
        self.session.commit()
        print(f"Добавлена книга: {title}")

    def delete_book(self, book_id):
        book = self.session.get(Book, book_id)
        if book:
            active_issue = self.session.query(BookIssue).filter_by(book_id=book.id, return_date=None).first()
            if active_issue:
                raise ValueError(f"Нельзя удалить книгу '{book.title}', она выдана читателю!")
            self.session.delete(book)
            self.session.commit()
            print("Книга удалена")

    def add_reader(self, first_name, last_name, email):
        try:
            reader = Reader(first_name=first_name, last_name=last_name, email=email)
            self.session.add(reader)
            self.session.commit()
            print(f"Добавлен читатель: {first_name} {last_name}")
        except:
            self.session.rollback()
            raise ValueError(f"Читатель с email '{email}' уже существует")

    def delete_reader(self, reader_id):
        reader = self.session.get(Reader, reader_id)
        if reader:
            active_issue = self.session.query(BookIssue).filter_by(reader_id=reader.id, return_date=None).first()
            if active_issue:
                raise ValueError(f"Нельзя удалить читателя, он еще не вернул книгу!")
            self.session.delete(reader)
            self.session.commit()
            print("Читатель удален")

    # --- ЛОГИКА ВЫДАЧИ И ВОЗВРАТА ---
    def issue_book_to_reader(self, book_id, reader_id):
        active_issue = self.session.query(BookIssue).filter_by(book_id=book_id, return_date=None).first()
        if active_issue:
            raise ValueError("Книга уже выдана")

        if not self.session.get(Book, book_id) or not self.session.get(Reader, reader_id):
            raise ValueError("Неверный ID книги или читателя")

        issue = BookIssue(book_id=book_id, reader_id=reader_id, issue_date=date.today())
        self.session.add(issue)
        self.session.commit()
        print("Книга успешно выдана")

    def return_book_from_reader(self, book_id):
        issue = self.session.query(BookIssue).filter_by(book_id=book_id, return_date=None).first()
        if issue:
            issue.return_date = date.today()
            self.session.commit()
            print(f"Книга возвращена.")
        else:
            print("Для этой книги нет активных задач.")

    def get_active_issues(self):
        return self.session.query(BookIssue).filter(BookIssue.return_date == None).all()
