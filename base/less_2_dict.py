#словари
# person = {}
# car = {
#     "brand": "bmw",
#     "model": "x5",
#     "year": 1997
# }
# #добавление элемента в словарь
# person["name"] = "Alex"
# person["age"] = 19
# person["name"] = "Dima"
# person["skills"] = ["python", "sql", "go"]
# print(person)
#
# #получение значения по ключу
# age = person.get("age1", "err")
# print(age)
# #person["age"]
# print(len(person))
#
# #удаление и получение элемента по ключу
# age = person.pop("age")
# print(age)
# print(person)
#
# print(person.keys())
# print(person.values())
# print(person.items())
#
# mylist1 = [1,2,3,4,5]
# print(id(mylist1))
#
# mylist2 = mylist1.copy()
# print(id(mylist2))
#
# mylist1.pop()
#
# print(mylist1)
# print(mylist2)
#
# #задача
# person = []
# N = 3
# for i in range(N): #range(start, stop, step) range(N) = [0,1,2,3,4...,N-1]
#     #i+1, так как i начинается с 0
#     print(f"Введите информацию о {i+1} человеке из {N}")
#     name = input("Введите имя: ")
#     age = input("Введите возраст: ")
#     person_info = {"name": name, "age": age}
#     person.append(person_info)
#
# print(person)

# users = {
#     "Dima": {
#         "phone": "234536456",
#         "street": "Lenina"
#     },
#     "Igor": {
#         "phone": "234536456123",
#         "street": "Titova"
#     },
#     "Elena": {
#         "phone": "234536456123789",
#         "street": "Titova"
#     },
# }
# print(users["Dima"]["phone"])
# print(users.get("Igor2", {}).get("street", "not found"))
# # item - ключ
# # users - словарь
# # users[item], users.get(item) - значения элемента словаря по ключу item
# for item in users: # ("Dima", "Igor", "Elena") !!! KEYS
#     print(f"{item} - {users.get(item)}")
#
# for value in users.values():
#     print(value)
#
# for key, value in users.items():
#     print(key, value)
#
# user_1 = {"name": "Dima", "age": 22}
# user_1_other = {"street": "Lenina", "city": "SPB"}
#
# user_1.update(user_1_other)
# print(user_1)

users_count = 3
users_info = {}

for i in range(users_count):
    print(f"Введите информацию о {i}-м пользователе")
    name = input("Username: ")
    users_info[name] = {}

    street = input("Street: ")
    phone = input("Phone: ")

    users_info[name]["street"] = street
    users_info[name]["phone"] = phone

for user in users_info:
    print(f"Имя пользователя: {user}")
    print(f"Улица: {users_info[user] ['street']}")
    print(f"Телефон: {users_info[user] ['phone']}")
    print("#############################")

