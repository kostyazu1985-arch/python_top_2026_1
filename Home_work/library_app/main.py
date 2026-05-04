from models import LibraryManager

def main():
    manager = LibraryManager("database.db")

    # Создаем данные
    manager.add_author("Николай Гоголь")
    manager.add_book("Шинель", author_id=1, year=1842, isbn="123-456")
    manager.add_reader("Костя", "Иванов", "kostya@example.com")

    # Выдаем книгу
    print("\n--- Процесс выдачи ---")
    manager.issue_book_to_reader(book_id=1, reader_id=1)

    # Смотрим активные выдачи
    active = manager.get_active_issues()
    print("Сейчас на руках:", active)

    # Возвращаем книгу
    if active:
        # Берем ID первой попавшейся активной выдачи
        manager.return_book_from_reader(issue_id=active[0].id)

    print("Активные после возврата:", manager.get_active_issues())

if __name__ == "__main__":
    main()
