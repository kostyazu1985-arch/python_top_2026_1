"""
СУБД - Система управления базами данных
SQL(Structured Query Language) - язык структурированных запросов

столбцы - называются полями(атрибутами), содержат информацию про свойства объектов
строки - называются записями (кортежи), содержат значения конкретного свойства

SQLite

SQLiteStudio
DB Browser for SQLite

*.db, *.db3, *.sqlite, *.sqlite3

SELECT [ALL | DISTINCT] (* | столбец1 [,столбец-n])
FROM таблица1 [, таблица-n]
WHERE условие
			AND OR
			выражение [NOT] BETWEEN начальное_значение AND конечное_значение
			выражение [NOT] LIKE шаблон_строки
				% - любое количество символов
				_ - один любой символ
			выражение [NOT] GLOB регулярное_выражение
				* - любое количество знаков
				? - соответствует одному символу
				. - соответствует любому одиночному символу
				[символы] - соответствует любому символу из списка [abc]
				[начальный-символ-конечный_символ] - соответствует любому одиночному символу из заданного диапазона [0-9]
				^ - этот символ используется в начале списка и соответствует любому символу, который НЕ входит в список [^0-9]
			IS [NOT] NULL - позволяет выбирать все строки, столбцы которых имеют значение NULL
			выражение [NOT] IN (набор значений | выражение)
GROUP BY (группировать по)
HAVING условие - нужен для использования условий агрегирования
ORDER BY col_name | col_number [ASC | DESC]

INSERT INTO ИМЯ_ТАБЛИЦЫ [столбец1 [, столбец-n]
VALUE [значение_1, [,значение_2]]

INSERT INTO ИМЯ_ТАБЛИЦЫ [список_столбцов]
SELECT СПИСОК_СТОЛБЦОВ
FROM СПИСОК_ТАБЛИЦ
WHERE УСЛОВИЕ

UPDATE имя_таблицы
SET столбец1 = значение
[WHERE условие]

DELETE FROM имя_таблицы
WHERE условие

LIMIT количество_строк OFFSET смещение
LIMIT [смещение,] количество_строк
Декартово произведение(все возможные комбинации строки одной таблицы с каждой строкой другой таблицы)

функции агрегирования
SUM
AVG
COUNT
MIN
MAX
Однострочные подзапросы: =, >, <, >=, <= (возвращает только одну строку)
Многострочные подзапросы: IN (NOT IN) (возвращает более одной строки, список значений)
Операторы BETWEEN, LIKE, IS NULL - нельзя применять к подзапросам
В подзапросах нельзя использовать ORDER BY, GROUP BY
"""

# import sqlite3 as sq
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()

    # СОЗДАНИЕ ТАБЛИЦЫ
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS persons (
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79000000000',
    # age INTEGER NOT NULL CHECK (age > 0 AND age < 120),
    # email TEXT UNIQUE
    # )
    # """)

    # ПЕРЕИМЕНОВАНИЕ ТАБЛИЦЫ
    # cur.execute("""
    # ALTER TABLE persons
    # RENAME TO person_table
    # """)

    # ДОБАВЛЕНИЕ СТОЛБЦА В ТАБЛИЦУ
    # cur.execute("""
    #     ALTER TABLE person_table
    #     ADD COLUMN address TEXT
    #     """)

    # УДАЛЕНИЕ СТОЛБЦА ИЗ ТАБЛИЦЫ
    # cur.execute("""
    #        ALTER TABLE person_table
    #        DROP COLUMN address
    #        """)

    # ПЕРЕИМЕНОВАНИЕ СТОЛБЦА В ТАБЛИЦЕ
    # cur.execute("""
    #     ALTER TABLE person_table
    #     RENAME COLUMN address TO home_address
    #     """)

    # УДАЛЕНИЕ ТАБЛИЦЫ
    # cur.execute ("""
    # DROP TABLE person_table
    # """)


# import sqlite3 as sq
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS persons (
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79000000000',
    # age INTEGER NOT NULL CHECK (age > 0 AND age < 120),
    # email TEXT UNIQUE
    # )
    # """)

    # заполнение таблицы
#     cur.execute("""
# INSERT INTO persons
# VALUES (1, "DMITRY", '+79040648571', 29, 'dimitry88@gmail.com')
# """)

#     cur.execute("""
# INSERT INTO persons (email, name, age)
# VALUES ('anton@gmail.com', 'Антон', 44)
# """)


import sqlite3 as sq

with sq.connect("db_4.db") as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware 
    ORDER BY Price DESC
    LIMIT 2, 5
    """)

    # res = cur.fetchall()
    # print(res)

    # res1 = cur.fetchone()
    # print(res1)

    # res2 = cur.fetchmany(2)
    # print(res2)

    # res3 = cur.fetchmany(10)
    # print(res3)

    # res4 = cur.fetchall()
    # print(res4)
    #
    # for res in res4:
    #     print(res)

    for res in cur:
          print(res)








