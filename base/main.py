# import json

# with open("data.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
# print(hello world)
# print(type(data))

# data = {
#   "имя": "Иван",
#   "возраст": 33,
#   "город": "Самара",
#   "животное": "Слон"
# }

# with open("output.json", "w", encoding="utf-8") as f:
# str_data = json.dumps(data, ensure_ascii=False, indent=4 )

# print(str_data)
# print(type(str_data))

# str_data1 = '{"имя": "Иван", "возраст": 33, "город": "Самара", "животное": "Слон"}'
# data_json = json.loads(str_data1)

# print(str_data1)
# print(type(str_data1))

# try:
#     with open("unknown.json", "r", encoding="utf-8") as f:
#         data = json.load(f)
# except FileNotFoundError:
#     print("ОШИБКА")
# print("hello world")

import requests

response = requests.get("https://api.github.com")

# print(response)
# print(response.status_code)
# print(response.ok)
# print(response.reason)

# try:
#     response.raise_for_status()
#     print("Успешно")

# except requests.exceptions.HTTPError as e:
#     print(f"Ошибка {e}")

# print(response.text)
# data = response.json()
# print(data)

# print(response.content)
print(response.headers['cache-control'])
print(response.headers)
print(response.encoding)
