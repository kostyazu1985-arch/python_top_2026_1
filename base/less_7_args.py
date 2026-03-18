import argparse

# создать парсер аргументов
parser = argparse.ArgumentParser(description='Обработка файла')

# добавляем аргументы
parser.add_argument('file', help='Имя файла для обработки')
parser.add_argument("output_file", help="Имя выходного файла")
args = parser.parse_args()
print(args.file)
print(args.output_file)
