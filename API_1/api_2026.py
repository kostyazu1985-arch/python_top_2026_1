"""
API — это посредник или «переводчик» между программами: он принимает запрос от одной системы, передаёт его другой,
а затем возвращает ответ. Пользователь или программа не вникают во внутренние механизмы работы сервиса — они просто
получают нужный результат.
"""
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# print(todos[:10])
# print(type(todos))

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1
# print(todos_by_user)

top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_user)

max_completed = top_user[0][1]
# print(max_completed)

users = []
for user, num_completed in top_user:
    if num_completed < max_completed:
        break
    users.append(str(user))

# print(users)

max_user = " and ".join(users)
s = "s" if len(users) > 1 else ""
print(f"user{s} {max_user} completed {max_completed} todos")

def keep(todo):
    is_completed = todo["completed"]
    has_max_count = str(todo["userId"] in users)
    return is_completed and has_max_count

with open("filtered_file.json", 'w') as data_file:
    filtered_todos = list(filter(keep, todos))
    # print(filtered_todos)
    json.dump(filtered_todos, data_file, indent=4)

with open("filtered_file.json", 'r') as f:
    data = json.load(f)
    print(data)

