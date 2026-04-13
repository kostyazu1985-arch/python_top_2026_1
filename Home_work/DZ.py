from sqlalchemy import Column, String, Integer, Float, Boolean, create_engine, select, delete
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
        return f"ID: {self.id} | '{self.title}'({self.year}) Жанр: {self.genre} | Рейтинг: {self.rating} | В прокате: {self.is_available}"

class MovieManager:
    def __init__(self, session):
        self.session = session

# ---Функции для работы с БД---
# Создает фильм, добавляет в БД
    def create_movie(self, title, genre, year, duration, rating):
        new_movie = Movie(title=title, genre=genre, year=year, duration=duration, rating=rating)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

# Возвращает все фильмы (используем новый синтаксис select, который заменил старый метод query())
    def get_all_movies(self):
        return self.session.scalars(select(Movie)).all()

# Возвращает фильм по ID
    def get_by_id(self, movie_id):
        return self.session.get(Movie, movie_id)

# Возвращает фильм по названию
    def get_movie_by_title(self, title):
        return self.session.scalars(select(Movie).where(Movie.title == title)).first()

# Возвращает фильмы жанра
    def get_movies_by_genre(self, genre_name):
        return self.session.scalars(select(Movie).where(Movie.genre == genre_name)).all()

# Фильмы с рейтингом ≥ указанного
    def get_high_rated_movies(self, min_rating):
        return self.session.scalars(select(Movie).where(Movie.rating >= min_rating)).all()

# Фильмы после указанного года
    def get_movies_after_year(self, year):
        return self.session.scalars(select(Movie).where(Movie.year > year)).all()

# Методы обновления
# Обновляет рейтинг
    def update_rating(self, movie_id, new_rating):
        movie = self.get_by_id(movie_id)
        if movie:
            movie.rating = new_rating
            self.session.commit()

# Обновляет жанр
    def update_genre(self, movie_id, new_genre):
        movie = self.get_by_id(movie_id)
        if movie:
            movie.genre = new_genre
            self.session.commit()

# Меняет статус
    def update_availability(self, movie_id, is_available):
        movie = self.get_by_id(movie_id)
        if movie:
            movie.is_available = is_available
            self.session.commit()

# Полное обновление
    def update_full(self, movie_id, **kwargs):
        movie = self.get_by_id(movie_id)
        if movie:
            for key, value in kwargs.items():
                setattr(movie, key, value)
            self.session.commit()

# Методы удаления
# Удаляет по ID
    def delete_by_id(self, movie_id):
        movie = self.get_by_id(movie_id)
        if movie:
            self.session.delete(movie)
            self.session.commit()

# Удаляет по названию
    def delete_by_title(self, title):
        movie = self.get_movie_by_title(title)
        if movie:
            self.session.delete(movie)
            self.session.commit()

# Меняет is_available на False
    def soft_delete(self, movie_id):
        self.update_availability(movie_id, False)

# Логика отображения
# Выводит заголовок с разделителем
class MovieViewer:
    def print_header(self, text):
        print(f"\n{'='*10} {text.upper()} {'='*10}")

# Выводит список фильмов
    def print_all(self, movies):
        if not movies:
            print("Список пуст!")
        for movie in movies:
            print(movie)

# Выводит один фильм
    def print_one(self, movie):
        if movie:
            print(movie)
        else:
            print("Фильм не найден!")

# Выводит статистику по фильмам
    def print_statistics(self, movies):
        if not movies: return
        avg_rating = sum(m.rating for m in movies) / len(movies)
        print(f"Всего фильмов: {len(movies)} | Средний рейтинг: {avg_rating:.2f}")

# ---блок запуска---
if __name__ == '__main__':
    engine = create_engine('sqlite:///cinema.db')
    Base.metadata.drop_all(engine) # чтобы данные не дублировались при перезапуске
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    db_session = Session()

    manager = MovieManager(db_session)
    viewer = MovieViewer()

# CREATE
    viewer.print_header("Добавление фильмов")
    manager.create_movie("Хищник: планета смерти", "фантастика", 2025, 108, 7.4)
    manager.create_movie("Домовенок Кузя 2", "семейный", 2026, 92, 5.9)
    manager.create_movie("Брюс Всемогущий", "комедия", 2003, 97, 7.8)
    manager.create_movie("Наследник", "триллер", 2026, 105, 6.9)
    manager.create_movie("Вот это ДРАМА!", "драма", 2026, 107, 7.3)

# READ/STATISTICS
    all_movies = manager.get_all_movies()
    viewer.print_all(all_movies)
    viewer.print_statistics(all_movies)

# UPDATE
    viewer.print_header("Обновление данных")
    manager.update_rating(1, 9.0) # обновляем рейтинг у ID 1(хищник)
    try:
        manager.update_full(5, title="Вот это ДРАМА!", genre="мелодрама", rating=8.0) # полное обновление (Вот это ДРАМА!)
        print("Успешно обновлено!")
    except Exception as e:
        print("Ошибка обновления")
    viewer.print_one(manager.get_by_id(1))
    viewer.print_one(manager.get_by_id(5))

# DELETE/SOFT DELETE
    viewer.print_header("Удаление")
    manager.soft_delete(2) # мягкое удаление(скрываем из проката)
    manager.delete_by_title("Брюс Всемогущий") # полное удаление по названию

    print("Итоговый список:")
    viewer.print_all(manager.get_all_movies())

