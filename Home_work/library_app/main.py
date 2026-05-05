from models import LibraryManager

def main():
    manager = LibraryManager("database.db")

    while True:
        print("1. Добавить автора")
        print("2. Удалить автора")
        print("3. Добавить книгу")
        print("4. Удалить книгу")
        print("5. Показать все книги с авторами")
        print("6. Найти книги автора по имени")
        print("7. Добавить читателя")
        print("8. Удалить читателя")
        print("9. Выдать книгу")
        print("10. Вернуть книгу")
        print("11. Показать активные выдачи")
        print("12. Выйти")

        choice = input("\nВыберите действие: ")

        try:
            if choice == "1":
                name = input("Введите имя автора: ")
                manager.add_author(name)

            elif choice == "2":
                id_auth = int(input("Введите ID автора для удаления: "))
                manager.delete_author(id_auth)

            elif choice == "3":
                title = input("Название книги: ")
                auth_id = int(input("ID автора: "))
                year = int(input("Год издания: "))
                manager.add_book(title, auth_id, year)

            elif choice == "4":
                id_bk = int(input("Введите ID книги для удаления: "))
                manager.delete_book(id_bk)

            elif choice == "5":
                manager.display_all_books_with_authors()

            elif choice == "6":
                name = input("Введите имя автора для поиска: ")
                results = manager.find_books_by_author_name(name)
                print(f"Книги автора {name}: {results}")

            elif choice == "7":
                f_name = input("Имя читателя: ")
                l_name = input("Фамилия читателя: ")
                mail = input("Email: ")
                manager.add_reader(f_name, l_name, mail)

            elif choice == "8":
                id_rd = int(input("ID читателя для удаления: "))
                manager.delete_reader(id_rd)

            elif choice == "9":
                bk_id = int(input("ID книги: "))
                rd_id = int(input("ID читателя: "))
                manager.issue_book_to_reader(bk_id, rd_id)

            elif choice == "10":
                bk_id = int(input("ID книги, которую возвращают: "))
                manager.return_book_from_reader(bk_id)

            elif choice == "11":
                active = manager.get_active_issues()
                print("Активные выдачи:", active)

            elif choice == "12":
                print("До свидания!")
                break
            else:
                print("Неверный выбор, попробуйте снова")

        except ValueError as e:
            print(f"\n[ОШИБКА]: {e}")
        except Exception as e:
            print(f"\n[НЕПРЕДВИДЕННАЯ ОШИБКА]: {e}")


if __name__ == "__main__":
    main()
