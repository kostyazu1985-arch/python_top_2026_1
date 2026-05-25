import os
import pickle
from random import choice

file_name = "countries.pkl"

def load_data():
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    return {}

def save_data(data):
    with open(file_name, "wb") as f:
        pickle.dump(data, f)
    print("Файл сохранен")

def main():
    data = load_data()

    while True:
        print("\n" + "*" *30)
        print("Выбор действия:")
        print("1 - добавление данных")
        print("2 - удаление данных")
        print("3 - поиск данных")
        print("4 - редактирование данных")
        print("5 - просмотр данных")
        print("6 - завершение работы")

        choice = input("Ввод: ")

        if choice == "1":
            country = input("Введите название (страны с заглавной буквы): ")
            capital = input("Введите название (столицы с заглавной буквы): ")
            data[country] = (capital)
            save_data(data)

        elif choice == "2":
            country = input("Введите страну для удаления: ")
            if (country in data):
                del data[country]
                save_data(data)
                print(f"Данные о стране {country} удалены.")
            else:
                print("Такой страны нет в базе данных!")

        elif choice == "3":
            country = input("Введите название страны для поиска: ")
            if (country in data):
                print(f"Столица: {data[country]}")
            else:
                print("Страна не найдена!")

        elif choice == "4":
            country = input("Введите название страны для редактирования: ")
            if (country in data):
                new_capital = input("Введите новое название столицы: ")
                data[country] = (new_capital)
                save_data(data)
            else:
                print("Такой страны нет. Добавьте ее через пункт 1.")

        elif choice == "5":
            print(data)

        elif choice == "6":
            print("Работа завершена!")
            break

        else:
            print("Неверный ввод! Выберите число от 1 до 6.")


if (__name__ == "__main__"):
    main()

