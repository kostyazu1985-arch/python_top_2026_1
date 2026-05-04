from models import LibraryManager  # импорт менеджера из файла моделей

def main():
    manager = LibraryManager("database.db")  # инициализация менеджера

    # добавим автора и сохраним его ID
    manager.add_author("Н.В.Гоголь")

    # добавим книги с корректным author_id
    manager.add_book("Шинель", author_id=5, year=1841, isbn="555-777")
    manager.add_book("Ревизор", author_id=5, year=1835)

    # список всех книг
    print("=" * 50)
    books = manager.get_all_books()
    for b in books:
        print(f"Книга: {b.title}, Год: {b.year}")

    # проверяем читателей
    print("=" * 50)
    manager.add_reader("Дмитрий", "Долгорукий", "dimon@mail.ru")
    manager.add_reader("Павлик", "Морозов", "pasha@mail.ru")

    # проверка email с обработкой ошибок
    try:
        manager.add_reader("Копия", "Морозова", "pasha@mail.ru")
    except Exception as e:
        print(f"Не удалось добавить читателя: {e}")

    # обновление читателя с проверкой
    try:
        manager.update_reader(1, first_name="Димон")
        print("Читатель успешно обновлён")
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")

    # удаление с проверкой
    try:
        manager.delete_reader(2)
        print("Читатель успешно удалён")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")

    # итоговый список читателей
    print("Список читателей:")
    for r in manager.get_all_readers():
        print(f"{r.id}: {r.first_name} {r.last_name} ({r.email})")

if __name__ == "__main__":
    main()