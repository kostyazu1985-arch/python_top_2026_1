import sqlite3

# подключение к базе данных
conn = sqlite3.connect('school.db')

# cursor - объект для выполнения запросов
cursor = conn.cursor()

# создание таблицы (если не существует) ученики
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT NOT NULL,
grade INTEGER CHECK(grade BETWEEN 1 AND 11)
)
''')

# создание таблицы (если не существует) предметы
cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE
)
''')

# создание таблицы (если не существует) оценки
cursor.execute('''
CREATE TABLE IF NOT EXISTS grades(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER REFERENCES students(id),
subject_id INTEGER REFERENCES subjects(id),
score INTEGER CHECK(score BETWEEN 1 AND 5)
)
''')

# фиксируем изменения в БД
conn.commit()
print("Таблицы созданы")

# закрываем
conn.close()
