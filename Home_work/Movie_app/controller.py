# Управляет всем. Связывает модель и представление и запускает программу
# импортируем классы из соседних файлов
from model import MovieModel, Movie
from view import MovieView


# класс который связывает модель и представление
class MovieController:
    def __init__(self, model, view):
        self.model = model # связь контроллера с моделью данных
        self.view = view # связь контроллера с интерфейсом

    def run(self):
        while True:
            choice = self.view.show_menu() # показываем меню и ждем выбор пользователя

            if choice == "1":
                title, genre, director, eyar, duration, studio, actors = self.view.get_movie_input()
                new_movie = Movie(title, genre, director, eyar, duration, studio, actors)
                self.model.add_movie(new_movie)
                self.view.show_message("Фильм успешно добавлен!")

            elif choice == "2":
                movies = self.model.get_all_movies()
                self.view.display_movie_list(movies)

            elif choice == "3":
                title = self.view.get_title_input("Введите название фильма для просмотра: ")
                movie = self.model.find_movie_by_title(title)
                self.view.display_movie_details(movie)

            elif choice == "4":
                title = self.view.get_title_input("Введите название фильма для удаления: ")
                success = self.model.delete_movie_by_title(title)
                if success:
                    self.view.show_message("Фильм успешно удален из каталога!")
                else:
                    self.view.show_message("Ошибка: фильм с таким названием не найден!")

            elif choice.lower() == "q":
                self.view.show_message("Программа завершена!")
                break

            else:
                self.view.show_message("Неверный вариант! Выберите от 1 до 4 или q")


if __name__ == "__main__":
    my_model = MovieModel()
    my_view = MovieView()
    my_controller = MovieController(my_model, my_view)
    my_controller.run()

