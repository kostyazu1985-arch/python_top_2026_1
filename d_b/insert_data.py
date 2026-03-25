import sqlite3

# подключение к базе данных
conn = sqlite3.connect('school.db')

# cursor - объект для выполнения запросов
cursor = conn.cursor()

students = [
    ("Алексей Федоров", "alex@mail.ru", 10),
    ("Мария Смирнова", "mariya@mail.ru", 10),
    ("Владимир Кравцов", "vladimir@mail.ru", 9),
    ("Елена Иванова", "elena@mail.ru", 9),
    ("Алексей Петров", "aleksey@mail.ru", 2),
    ("Сергей Черный", "sergey@mail.ru", 3),
]

cursor.executemany("INSERT INTO students (name, email, grade) VALUES (?, ?, ?)", students)
conn.commit()
print("Данные о студентах успешно добавлены!")
conn.close()