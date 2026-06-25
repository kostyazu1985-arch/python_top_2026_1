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
			EXISTS (существует)
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

FROM table_name_1 INNER JOIN table_name_2
ON связь_между_таблицами(первичным_и_внешним_ключами)

UNION - используется для объединения двух и более SELECT с исключением повторяющихся строк

INNER JOIN (внутреннее соединение). Возвращает только те строки, для которых есть совпадение по заданному
условию в обеих таблицах. Например, если есть две таблицы с данными о клиентах и заказах, INNER JOIN вернёт только тех
клиентов, у которых есть хотя бы один заказ. 1. INNER JOIN (внутреннее соединение). Возвращает только те строки,
для которых есть совпадение по заданному условию в обеих таблицах. Например, если есть две таблицы с данными о
клиентах и заказах, INNER JOIN вернёт только тех клиентов, у которых есть хотя бы один заказ.

LEFT JOIN (левое внешнее соединение). Возвращает все строки из левой таблицы и соответствующие строки из правой таблицы.
Если совпадений нет, для столбцов правой таблицы используются значения NULL.

RIGHT JOIN (правое внешнее соединение). Работает аналогично LEFT JOIN, но в приоритете — правая таблица.

FULL JOIN (полное внешнее соединение). Возвращает строки, когда есть совпадение в одной из таблиц. Если совпадения нет,
в столбцах таблицы, в которой нет совпадения, используются значения NULL.
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


# import sqlite3 as sq
#
# with sq.connect("db_4.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5
#     """)

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

    # for res in cur:
    #       print(res)

import sqlite3 as sq

cars = [
    ('BMW', 500000000),
    ('Honda', 8800000000),
    ('Citroen', 4500000000),
    ('Tank', 2800000000),
    ('Haval', 5600000000)
]

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS car (
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)

    # cur.execute("INSERT INTO car VALUES(1, 'Reno', 15000000)")
    # cur.execute("INSERT INTO car VALUES(2, 'Volvo', 18000000)")
    # cur.execute("INSERT INTO car VALUES(3, 'BMW', 16000000)")
    # cur.execute("INSERT INTO car VALUES(4, 'Lada', 25000000)")
    # cur.execute("INSERT INTO car VALUES(5, 'KIA', 39000000)")

    # for car in cars:
    #     cur.execute("INSERT INTO car VALUES (NULL, ?, ?)", car)

    # cur.executemany("INSERT INTO car VALUES(NULL, ?, ?)", cars)

    # cur.execute("UPDATE car SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executescript("""
    # DELETE FROM car WHERE model LIKE 'B%';
    # UPDATE car SET price = price + 55555
    # """)

# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS car (
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO car VALUES (NULL, 'Nissan', 3333333);
#     UPDATE car SET price = price + 111;
#     """)
#     con.commit()
# except sq.Error() as e:
#     if con :
#         con.rollback()
#     print("Ошибка выполнения запроса")
#
# finally:
#     if con:
#         con.close()