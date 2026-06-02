import csv

FILENAME = "devices.csv"

# Создание csv файла и запись данных в него

data_to_write = [
    ["hostname", "vendor", "model", "location"],
    ["sw1", "Cisco", "3750", "London"],
    ["sw2", "Cisco", "3850", "Liverpool"],
    ["sw3", "Cisco", "3650", "Liverpool"],
    ["sw4", "Cisco", "3550", "London"],
]

with open(FILENAME, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(data_to_write)
print("Файл успешно создан!")

# Чтение данных из файла и вывод на экран

with open(FILENAME, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)