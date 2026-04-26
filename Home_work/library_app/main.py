from mypy.server.update import find_unloaded_deps

from models import LibraryManager # импорт менеджера из файла моделей

def main():
  manager = LibraryManager("database.db") # инициализация менеджера
  manager.create_tables()

  print("ДОБАВЛЕНИЕ АВТОРОВ") # добавление авторов (create)
  manager.add_author("Федор Достоевский")
  manager.add_author("Иван Бунин")
  manager.add_author("Николай Гоголь")
  manager.add_author("Иван Тургенев")

  print("СПИСОК ВСЕХ  АВТОРОВ") # получение всех авторов (read)
  authors = manager.get_all_authors()
  for author in authors:
      print(author)

  print("ПОИСК АВТОРА С ID 2") # поиск по id (read)
  found = manager.find_author_by_id(2)
  print(f"Найден: {found}")

  print("ОБНОВЛЕНИЕ АВТОРА С ID 1") # Обновление имени (update)
  manager.update_author(1, "Ф.М.Достоевский")

  print("ИТОГОВЫЙ СПИСОК ПОСЛЕ ОБНОВЛЕНИЯ") # проверка изменений и удаление (delete)
  for author in manager.get_all_authors():
      print(author)

  print("УДАЛЕНИЕ АВТОРА С ID 3") # удаление одного автора
  manager.delete_author(3)
  print("АВТОРЫ ПОСЛЕ УДАЛЕНИЯЯ:", manager.get_all_authors())



if __name__ == "__main__":
    main()