import sqlite3 as sq

with sq.connect("cars_library.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS car(
            cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            color TEXT,
            price INTEGER
        );
    """)
    cur.execute("SELECT COUNT(*) as cnt FROM car")
    if cur.fetchone()["cnt"] == 0:
        cars_data = [
            ("Lada Granta", "Белый", 950000),
            ("Lada Vesta", "Серый", 1450000),
            ("Haval Jolion", "Красный", 2300000),
            ("Geely Coolray", "Синий", 2500000),
            ("Chery Tiggo 7", "Черный", 3500000),
            ("Toyota Camry", "Серебристый", 2600000),
            ("Hyundai Santa Fe", "Белый", 4200000),
            ("Kia Sportage", "Коричневый", 3700000),
            ("VW Tiguan", "Зеленый", 4300000),
            ("Skoda Yeti", "Пурпурный", 2800000),
            ("BMW X5", "Черный", 9500000),
            ("Audi A8", "Красный", 4800000),
            ("Mercedes S-Class", "Голубой", 5600000),
            ("Subaru Impreza", "Оранжевый", 3900000),
            ("Mazda CX-5", "Бордовый", 3400000),
        ]
        cur.executemany("INSERT INTO car (model, color, price) VALUES (?, ?, ?)", cars_data)
        cur.execute("SELECT model, color, price FROM car")
        print("Список автомобилей в БД:")
        for res in cur:
            print(f"Модель: {res['model']} | Цвет: {res['color']} | Цена: {res['price']} руб.")




# Ссылка github
# https://github.com/kostyazu1985-arch/python_top_2026_1/blob/main/Home_work/DZ.py