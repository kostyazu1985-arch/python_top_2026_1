import sqlite3

# подключение к базе данных
conn = sqlite3.connect('school.db')

# cursor - объект для выполнения запросов
cursor = conn.cursor()

query_all_students = """
    SELECT *
    FROM students
"""

query_students_high = """
    SELECT name, grade
    FROM students
    WHERE grade >= 9
"""

# выполняем запрос
cursor.execute(query_all_students)
# получаем результат
rows = cursor.fetchall()
print(rows)

for student in rows:
    print(f'{student[1]} - {student[3]} класс')
conn.close()