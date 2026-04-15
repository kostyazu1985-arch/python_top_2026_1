from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, create_engine, select, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# --- МОДЕЛИ ---
class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    # Связь: один жанр ко многим фильмам
    movies = relationship("Movie", back_populates="genre", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Genre(id={self.id}, name='{self.name}')>"


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    duration = Column(Integer)
    rating = Column(Float)
    is_available = Column(Boolean, default=True)

    # Внешний ключ на таблицу жанров
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)

    # Обратная связь к жанру
    genre= relationship("Genre", back_populates="movies")

    def __repr__(self):
        return f"Movie(id={self.id}, title='{self.title}', genre='{self.genre.name if self.genre else 'None'}')"



# --- МЕНЕДЖЕРЫ ---
class GenreManager:
    def __init__(self, session):
        self.session = session

    # Создает жанр
    def create(self, name, description):
        genre = Genre(name=name, description=description)
        self.session.add(genre)
        self.session.commit()
        return genre

    # Все жанры
    def get_all(self):
        return self.session.scalars(select(Genre)).all()

    # Жанр по ID
    def get_by_id(self, genre_id):
        return self.session.get(Genre, genre_id)

    # Жанр по названию
    def get_by_name(self, name):
        return self.session.scalars(select(Genre).where(Genre.name == name)).first()

    # Обновляет название
    def update_name(self, genre_id, new_name):
        genre = self.get_by_id(genre_id)
        if genre:
            genre.name = new_name
            self.session.commit()

    # Обновляет описание
    def update_description(self, genre_id, new_description):
        genre = self.get_by_id(genre_id)
        if genre:
            genre.description = new_description
            self.session.commit()

    # Удаляет жанр
    def delete_by_id(self, genre_id):
        genre = self.get_by_id(genre_id)
        if genre:
            self.session.delete(genre)
            self.session.commit()

    # Жанры с количеством фильмов
    def get_genres_with_movies_count(self):
        query = (
            select(Genre.name, func.count(Movie.id))
            .outerjoin(Movie)
            .group_by(Genre.id)
        )
        return self.session.execute(query).all()



class MovieManager:
    def __init__(self, session):
        self.session = session

    # Создает фильм по названию жанра
    def create_with_genre_name(self, title, year, duration, rating, genre_name):
        genre = self.session.scalars(select(Genre).where(Genre.name == genre_name)).first()
        if not genre:
            raise ValueError(f"Жанр {genre_name} не найден")

        movie = Movie(title=title, year=year, duration=duration, rating=rating, genre_id=genre.id)
        self.session.add(movie)
        self.session.commit()
        return movie

    # Все фильмы
    def get_all_movies(self):
        return self.session.scalars(select(Movie)).all()

    # Фильм по ID
    def get_by_id(self, movie_id):
        return self.session.get(Movie, movie_id)

    # Фильмы жанрам
    def get_by_genre(self, genre_id):
        return self.session.scalars(select(Movie).where(Movie.genre_id == genre_id)).all()

    # Меняет жанр фильма
    def update_genre(self, movie_id, new_genre_id):
        movie = self.get_by_id(movie_id)
        if movie:
            movie.genre_id = new_genre_id
            self.session.commit()

    # Удаляет фильм
    def delete_by_id(self, movie_id):
        movie = self.get_by_id(movie_id)
        if movie:
            self.session.delete(movie)
            self.session.commit()



# --- ВЬЮВЕР для красивого вывода---
class CinemaViewer:
    @staticmethod
    def print_header(text):
        print(f"\n{'='*15} {text.upper()} {'='*15}")

    @staticmethod
    def print_movies(movies):
        for m in movies:
            print(f"[{m.id}] {m.title} ({m.year}) | Жанр: {m.genre.name} | Рейтинг: {m.rating}")

    @staticmethod
    def print_genres(genres):
        for g in genres:
            print(f"[{g.id}] {g.name}: {g.description}")

    @staticmethod
    def print_stats(stats):
        print("Статистика по жанрам:")
        for name, count in stats:
            print(f" - {name}: {count} фильмов")



# --- Запуск ---
if __name__ == "__main__":
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    g_manager = GenreManager(session)
    m_manager = MovieManager(session)
    viewer = CinemaViewer()

    # Работа с жанрами
    viewer.print_header("Создание жанров")
    g_manager.create("Приключения", "Захватывающие фильмы")
    g_manager.create("Военный", "Серьезное кино")
    g_manager.create("Фэнтези", "Красивые фильмы")
    viewer.print_genres(g_manager.get_all())

    # Работа с фильмами (связи)
    viewer.print_header("Добавление фильмов")
    m_manager.create_with_genre_name("Зов предков", 2020, 100, 7.7, "Приключения")
    m_manager.create_with_genre_name("Малыш", 2026, 114, 7.8, "Военный")
    m_manager.create_with_genre_name("Буратино", 2026, 102, 7.0, "Фэнтези")
    viewer.print_movies(m_manager.get_all_movies())

    # Демонстрация обновления и статистики
    viewer.print_header("Обновление и статистика")
    m_manager.update_genre(1,2) # переносим Зов предков из Приключений в Военный

    stats = g_manager.get_genres_with_movies_count()
    viewer.print_stats(stats)

    # Удаление
    viewer.print_header("Удаление жанра")
    print("Удаляем жанр 'Фэнтези' (вместе с ним удалятся и фильмы из-за cascade)...")
    fantasy = g_manager.get_by_name("Фэнтези")
    g_manager.delete_by_id(fantasy.id)

    print("\nОставшиеся фильмы:")
    viewer.print_movies(m_manager.get_all_movies())






























