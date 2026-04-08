# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# # подключение к базе данных
# engine = create_engine('sqlite:///mydb.db')
#
# # базовый класс
# Base = declarative_base()
#
# # рабочее пространство
# Session = sessionmaker(bind=engine)
# session = Session()


from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, create_engine, Float

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

    def is_adult(self):
        return self.age >= 18 if self.age else False

engine = create_engine('sqlite:///mydb.db', echo=True)

Base.metadata.create_all(engine)
print("OK")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Product(name='{self.name}', price='{self.price}')>"

    def in_stock(self):
        return self.stock > 0 and self.is_available

    def add_stock(self, quantity):
        if quantity > 0:
            self.stock += quantity
        else:
            raise ValueError("Количество не должно быть отрицательным")

Session = sessionmaker(bind=engine)
session = Session()

# user1 = User(name="Иван", email="ivan@mail.ru", age=25)
# user2 = User(name="Мария", email="maria@gmail.com", age=26)
#
# session.add(user1)
# session.add(user2)
#
# session.commit()
# print(f"User added {user1.id}, {user2.id}")
#
# session.close()

# all_users = session.query(User).all()
# for user in all_users:
#     print(user)

# first_user = session.query(User).first()
# print(first_user)

# user = session.query(User).get(2)
# print(user)
# user = session.get(User, 2)
# print(user)

# adult_user = session.query(User).filter(User.age >= 18).all()
# print(f"{len(adult_user)}")

# ivan = session.query(User).filter(User.name == "Иван").first()
# print(ivan)

# user = session.query(User).filter(User.email == "ivan@mail.ru").first()
#
# session.delete(user)
# session.commit()
#
# print(f"user delete")
#
# session.close()

