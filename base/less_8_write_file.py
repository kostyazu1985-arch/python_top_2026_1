# with open("new_file", "w", encoding="utf-8") as f:
#     for i in range(3):
#         line = input("Введите текст:\n")
#         f.write(line+'\n')
# print("Файл закрыт!")
#
# with open("new_file", "a", encoding="utf-8") as f:
#     print("Файл открыт!")
#     for i in range(3):
#         line = input("Введите текст:\n")
#         f.write(line+'\n')
#
# with open("new_file", "r", encoding="utf-8") as f:
#     text = f.read()
#     text_lines = text.split("\n")
#     for i, v in enumerate(text_lines):
#         if i % 2 == 0:
#             text_lines.remove(v)
#
# with open("new_file", "w", encoding="utf-8") as f:
#     for line in text_lines:
#         f.write(line+'\n')




import json

person = {
    "name": "Саша",
    "age": 20,
    "phone": "2223192",
    "email": [
    "kostyazu1985@gmaill.com",
    "kostyazu2014@yandex.ru"
    ],
    "address": {
        "city": "Nizhny Novgorod",
        "country": "Российская Федерация",
        "street": "Spokeswoman",
        "house_number": 22,
    }
}
json_str = json.dumps(person, ensure_ascii=False, indent=4)

with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

with open("person.json", "r", encoding="utf-8") as f:
    person = json.load(f)
    print(person)