# Экран и интерфейс
# класс для взаимодействия пользователя и консоли
class MovieView:
    def show_menu(self):
        print("\n===== Редактирование данных каталога фильмов =====")
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")
        return input("Выберите вариант действия: ")

    def get_movie_input(self):
        print("\n--- Добавление нового фильма ---")
        title = input("Введите название фильма: ")
        genre = input("Введите жанр: ")
        director = input("Введите режиссера: ")
        year = input("Введите год выпуска: ")
        duration = input("Введите длительность (мин): ")
        studio = input("Введите студию: ")
        actors = input("Введите актеров (через запятую): ")
        # возвращаем все строки одним кортежем
        return title, genre, director, year, duration, studio, actors

    def display_movie_list(self, movies):
        print("\n--- Каталог фильмов ---")
        if not movies:
            print("Каталог пока пуст")
            return
            # перебираем фильмы и выводим их индекс и название
        for index, movie in enumerate(movies, 1):
            print(f"{index}. {movie.title} ({movie.genre})")

    def display_movie_details(self, movie):
        # выводим инфу о фильме
        if movie:
            print(f"\n--- Информация о фильме: {movie.title} ---")
            print(f"Жанр: {movie.genre}")
            print(f"Режиссер: {movie.director}")
            print(f"Год выпуска: {movie.year}")
            print(f"Длительность: {movie.duration} мин")
            print(f"Студия: {movie.studio}")
            print(f"Актеры: {movie.actors}")
        else:
            print("\nФильм не найден")

    # метод чтобы спросить у пользователя название фильма
    def get_title_input(self, message):
        return input(message)

    # метод вывода сообщений (успех, ошибка)
    def show_message(self, message):
        print(message)
