import sys
from os.path import isfile
from text_utils import *

while True:
    print("Введите имя файла для анализа: ")
    print("Введите 0 для выхода из программы")
    path = input(">>> ")
    if path == "0":
        sys.exit(0)

    if isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            break
    else:
        print("Такого файла нет")

while True:
    print("Выбрать необходимое действие: ")
    print("1. Посчитать количество строк в файле\n"
          "2. Посчитать количество слов в файле\n"
          "3. Посчитать количество символов в файле\n"
          "0. Выход из программы")
    action = input(">>> ")
    match action:
        case "1":
            print("Посчитать количество строк в файле")
            lines = get_count_lines(text)
            print(lines)
        case "2":
            print("Посчитать количество слов в файле")
            words = get_count_words(text)
            print(words)
        case "3":
            print("Посчитать количество символов в файле")
            characters = get_count_characters(text)
            print(characters)
        case "0":
            sys.exit(0)
        case _:
            print("Неверный выбор")



