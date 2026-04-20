from models import LibraryManager # импорт менеджера из файла моделей

def main():
    database_url = "sqlite:///database.db" # путь к файлу бд

    manager = LibraryManager(database_url) # активация менеджера библиотеки

    manager.create_tables() # метод создания таблиц

if __name__ == "__main__":
    main()