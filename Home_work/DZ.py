from sqlalchemy import Column, String, Integer, Float, Boolean, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base() # базовый класс для моделей

class Movie(Base): # определение модели Movie
    __tablename__ = "movies" # название таблицы
    id = Column(Integer, primary_key=True) # поля таблицы
    title = Column(String, nullable=False)
    genre = Column(String)
    year = Column(Integer)
    duration = Column(Integer)
    rating = Column(Float)
    is_available = Column(Boolean, default=True)

    def __repr__(self): # метод красивого отображения в консоли
        return f"<Movie(title='{self.title}', genre='{self.genre}', rating={self.rating})>"

engine = create_engine('sqlite:///cinema.db', echo=False) # настройка БД
Session = sessionmaker(bind=engine)
session = Session()

# ---Функции для работы с БД---
# Создает фильм, добавляет в БД
def create_movie(title, genre, year, duration, rating):
    new_movie = Movie(title=title, genre=genre, year=year, duration=duration, rating=rating)
    session.add(new_movie)
    session.commit()
    return new_movie

# Возвращает все фильмы (используем новый синтаксис select, который заменил старый метод query())
def get_all_movies():
    return session.scalars(select(Movie)).all()

# Возвращает фильмы жанра
def get_movies_by_genre(genre_name):
    return session.scalars(select(Movie).where(Movie.genre == genre_name)).all()

# Фильмы с рейтингом ≥ указанного
def get_high_rated_movies(min_rating):
    return session.scalars(select(Movie).where(Movie.rating >= min_rating)).all()

# Фильмы после указанного года
def get_movies_after_year(year):
    return session.scalars(select(Movie).where(Movie.year > year)).all()

# Один фильм по названию
def get_movie_by_title(title):
    return session.scalars(select(Movie).where(Movie.title == title)).first()

# ---блок запуска---
# Создать таблицы через Base.metadata.create_all(engine)
if __name__ == '__main__':
    Base.metadata.drop_all(engine) # чтобы данные не дублировались при перезапуске
    Base.metadata.create_all(engine)
    print("Таблицы созданы!")

# Добавить минимум 5 фильмов (разные жанры, годы, рейтинги)
create_movie("Бриллиантовая рука", "комедия", 1969, 94, 8.6)
create_movie("Горничная", "ужасы", 2025, 131, 7.6)
create_movie("Прыгуны", "мультфильм", 2026, 104, 7.8)
create_movie("Острые козырьки: Бессмертный человек", "история", 2026, 112, 6.5)
create_movie("Убежище", "боевик", 2026, 107, 7.0)

# Вызвать все функции чтения и вывести результаты в консоль
# Оформить вывод с разделителями и заголовками
print("1. Все фильмы в базе:")
print(get_all_movies())
print("-" * 30)

print("2. Фильмы в жанре 'ужасы':")
print(get_movies_by_genre("ужасы"))
print("-" * 30)

print("3. Фильмы с рейтингом 7.6 и выше:")
print(get_high_rated_movies(7.6))
print("-" * 30)

print("4. Фильмы вышеедшие после 2025 года:")
print(get_movies_after_year(2025))
print("-" * 30)

print("5. Поиск фильма 'Бриллиантовая рука':")
print(get_movie_by_title("Бриллиантовая рука"))
print("-" * 30)