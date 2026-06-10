# Работа с данными и файлом
import os


# класс-шаблон для создания фильма
class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors


# класс для управления и хранения фильмов
class MovieModel:
    def __init__(self):
        self.filename = "movies_db.txt"  # сюда будем записывать фильмы
        self.movies = []
        self.load_movies_from_file()  # метод загрузки фильмов при старте программы

    # метод для перезаписи файла актуальными фильмами
    def save_movies_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for movie in self.movies:
                # объединяем свойства фильма в одну строчку
                line = f"{movie.title}||{movie.genre}||{movie.director}||{movie.year}||{movie.duration}||{movie.studio}||{movie.actors}\n"
                # записываем эту строчку в файл
                file.write(line)

    # метод для чтения и заполнения списка файла при запуске программы
    def load_movies_from_file(self):
        # проверяем создавался ли такой файл ранее
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()  # убираем \n в конце строки
                if clean_line:
                    parts = clean_line.split("||")  # делим строку обратно на части
                    # проверяем что в строке 7 элементов
                    if len(parts) == 7:
                        # создаем объект фильма из этих частей
                        movie = Movie(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
                        self.movies.append(movie)  # кладем фильм в наш список

    def add_movie(self, movie):
        self.movies.append(movie)  # добавляем фильм в список
        self.save_movies_to_file()  # сохраняем обновленный список в файл

    def get_all_movies(self):
        return self.movies

    def find_movie_by_title(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def delete_movie_by_title(self, title):
        movie = self.find_movie_by_title(title)
        if movie:
            self.movies.remove(movie)  # если фильм нашелся, удаляем его
            self.save_movies_to_file()  # перезаписываем обновленный список
            return True  # успешно удалено
        return False  # такого фильма не было
