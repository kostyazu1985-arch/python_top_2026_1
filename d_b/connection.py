from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, Table
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
        return f"<Author {self.name}>"

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
        return f"<Book {self.title}>"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(75), nullable=False)

    profile = relationship("UserProfile", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<Book {self.username}>"

class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(Integer, primary_key=True)
    bio = Column(String(250))

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"<Book {self.bio[:30]}>"

book_association_table = Table(
    'book_tags',
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    books = relationship("Book", secondary=book_association_table, back_populates="tags")

    def __repr__(self):
        return f"<TAG {self.name[:30]}>"

Book.tags = relationship("Tag", secondary=book_association_table, back_populates="books")

Base.metadata.create_all(engine)
session = Session()

author = Author(name="Ремарк222")

book1 = Book(title="222Три товарища", years=1855, author=author)
book2 = Book(title="222Триумфальная арка", years=1968, author=author)
book3 = Book(title="222Жизнь взаймы", years=1949, author=author)


tags1 = Tag(name="Фантастика")
tags2 = Tag(name="Классика")
tags3 = Tag(name="Комедия")

book1.tags.append(tags1)
book2.tags.append(tags2)

session.add_all([tags1, tags2, tags3])

# user1 = User(username="User1")
# profile1 = UserProfile(bio = "читатель книг", user = user1)
# session.add_all([user1, profile1])



#

# session.commit()

# author = session.query(Author).filter_by(name="Айзек Азимов").first()
# print(author)
# print(author.get_book_count())
# print(author.books)
# book = session.query(Book).filter_by(title="Я, робот").first()
# print(book)
# print(book.author)
# author = session.query(Author).first()
# session.delete(author)
#
session.commit()
session.close()
