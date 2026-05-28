"""
CSV (от англ. Comma‑Separated Values — «значения, разделённые запятыми») — это текстовый формат для хранения
табличных данных.

Проще говоря, CSV‑файл — это таблица, сохранённая в простом текстовом файле. Каждая строка файла соответствует строке
таблицы, а значения внутри строки разделены специальными символами — чаще всего запятыми, но бывают и другие разделители.
"""
import csv

# csv.reader
# csv.writer
# csv.DictReader
# csv.DictWriter

# with open("data_1.csv") as r_file:
#     filed_name = ["Имя", "Должность", "Возраст"]
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=filed_name)
#     count = 0
#
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f'{row["Имя"]}-{row["Должность"]}. Возраст:{row["Возраст"]} лет')
#         count += 1
#     print(f"В файле {count} строки")

# with open("student.csv", "w") as f:
#     # writer = csv.writer(f, delimiter=";")
#     writer = csv.writer(f, delimiter=";", lineterminator="\n")
#
#     writer.writerow(["Имя", "Группа", "Возраст"])
#     writer.writerow(["Паша", "9", "16"])
#     writer.writerow(["Даша", "7", "14"])
#     writer.writerow(["Игнат", "11", "12"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3570', 'London, Best str' ],
#         ['sw2', 'Cisco', '3580', 'London, Vest str' ],
#         ['sw3', 'Cisco', '3590', 'London, Better str' ],
#         ['sw4', 'Cisco', '3575', 'London, Beset str' ]]
#
# with open("data_new.csv", 'w') as f:
#     # writer = csv.writer(f, delimiter=";", lineterminator="\n")
#     writer = csv.writer(f, delimiter=";", lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
#
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open("data_new.csv", 'r') as f:
#     print(f.read())

# with open("student1.csv", 'w') as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\n', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 10})
#     file_writer.writerow({"Имя": "Паша", "Возраст": 16})
#     file_writer.writerow({"Возраст": 12, "Имя": "Игорь"})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("hosts.csv", "w") as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter=";", lineterminator="\n")
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)