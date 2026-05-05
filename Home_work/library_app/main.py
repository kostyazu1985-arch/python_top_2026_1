from models import LibraryManager

def print_menu():
    print("\n" + "=" * 30)
    print("МЕНЮ УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
    print("=" * 30)
    print("1. Добавить автора")
    print("2. Добавить книгу")
    print("3. Зарегистрировать читателя")
    print("-" * 30)
    print("4. Показать все книги (с авторами)")
    print("5. Найти книги по имени автора")
    print("-" * 30)
    print("6. Выдать книгу читателю")
    print("7. Вернуть книгу в библиотеку")
    print("8. Список книг 'на руках'")
    print("-" * 30)
    print("9. Удалить автора")
    print("10. Удалить книгу")
    print("11. Удалить читателя")
    print("0. Выйти")

def main():
    manager = LibraryManager("database.db")

    while True:
        print_menu()
        choice = input("\nВыберите пункт меню: ")

        try:
            if choice == "1":
                name = input("Введите имя автора: ")
                manager.add_author(name)

            elif choice == "2":
                title = input("Название книги: ")
                a_id = int(input("ID автора: "))
                year = int(input("Год издания: "))
                isbn = input("ISBN (необязательно): ")
                manager.add_book(title, a_id, year, isbn)

            elif choice == "3":
                f_name = input("Имя читателя: ")
                l_name = input("Фамилия читателя: ")
                email = input("Email: ")
                manager.add_reader(f_name, l_name, email)

            elif choice == "4":
                manager.display_all_books_with_authors()

            elif choice == "5":
                name = input("Введите имя автора для поиска: ")
                books = manager.find_books_by_author_name(name)
                print(f"Результаты: {books}")

            elif choice == "6":
                b_id = int(input("ID книги: "))
                r_id = int(input("ID читателя: "))
                manager.issue_book(b_id, r_id)

            elif choice == "7":
                b_id = int(input("ID возвращаемой книги: "))
                manager.return_book(b_id)

            elif choice == "8":
                active = manager.get_active_issues()
                print("\nСейчас на руках:")
                for item in active:
                    print(item)

            elif choice == "9":
                a_id = int(input("ID автора для удаления: "))
                manager.delete_author(a_id)

            elif choice == "10":
                b_id = int(input("ID книги для удаления: "))
                manager.delete_book(b_id)

            elif choice == "11":
                r_id = int(input("ID читателя для удаления: "))
                manager.delete_reader(r_id)

            elif choice == "0":
                print("Программа завершена!")
                break
            else:
                print("Неверный выбор, попробуйте снова")

        except ValueError as e:
            print(f"\n[ОШИБКА]: {e}")
        except Exception as e:
            print(f"\n[НЕПРЕДВИДЕННАЯ ОШИБКА]: {e}")


if __name__ == "__main__":
    main()
