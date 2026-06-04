import csv
import time
from bs4 import BeautifulSoup
import requests


BASE_URL = "https://www.russianfood.com/recipes/bytype/?fid=926&page="

# Задаем "имя" для нашей программы (User-Agent), чтобы сайт думал, что зашел обычный человек через браузер
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def main():  # Главная функция нашей программы
    all_recipes = []  # Создаем пустой список, куда будем складывать все найденные рецепты

    print("Начинаем сбор рецептов...")

    for page in range(1, 11):
        print(f"Скачиваем страницу {page} из 10...")  # Показываем прогресс

        url = f"{BASE_URL}{page}"  # Склеиваем базовую ссылку и текущий номер страницы

        try:  # Защищаем программу от внезапных ошибок сети
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
        except Exception as e:  # Если случилась ошибка при скачивании:
            print(f"Ошибка при загрузке страницы {page}: {e}")
            continue  # Пропускаем эту страницу и идем к следующей

        soup = BeautifulSoup(response.text, "html.parser")

        recipe_cards = soup.find_all("div", class_="recipe_l")

        for card in recipe_cards:  # Перебираем каждую карточку рецепта отдельно
            # 1. ИЩЕМ НАЗВАНИЕ РЕЦЕПТА
            title_tag = card.find("div", class_="title")  # Ищем блок с классом 'title' внутри карточки
            if title_tag:  # Если такой блок нашелся:
                title = title_tag.text.strip()  # Берем из него текст и очищаем от лишних пробелов
            else:  # Если блока почему-то нет:
                title = "Название не указано"

            # 2. ИЩЕМ ОПИСАНЕ
            description_tag = card.find("div", class_="announce")
            if description_tag:
                description = description_tag.text.replace("Далее...", "").replace("\n", " ").strip()
            else:
                description = "Описание отсутствует"

            # 3. ИЩЕМ ВРЕМЯ ПРИГОТОВЛЕНИЯ
            time_tag = card.find("span", class_="prep_time")
            if not time_tag:  # Если специального класса нет, попробуем поискать в общем инфо-блоке
                time_tag = card.find("div", class_="info")

            if time_tag and "мин" in time_tag.text:  # Если нашли тег и в нем есть упоминание минут:
                cooking_time = time_tag.text.strip()  # Забираем время приготовления
            else:
                cooking_time = "Не указано"  # Если времени нет

            # Добавляем собранные данные об одном рецепте в наш общий список в виде словаря
            all_recipes.append(
                {
                    "Название": title,
                    "Описание": description,
                    "Время приготовления": cooking_time,
                }
            )

        time.sleep(1)  # Делаем паузу в 1 секунду между страницами

    # ЗАПИСЬ ВСЕХ СОБРАННЫХ ДАННЫХ В ФАЙЛ
    with open("recipes.csv", "w", encoding="utf-8-sig", newline="") as f:
        # Создаем названия колонок таблицы на основе ключей нашего словаря
        fieldnames = ["Название", "Описание", "Время приготовления"]

        # Создаем специальный объект-писатель для словарей
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")

        writer.writeheader()  # Записываем самую первую строчку — заголовки колонок
        writer.writerows(all_recipes)  # Записываем весь огромный список рецептов за один раз

    print(f"Готово! Собрано рецептов: {len(all_recipes)}")


if __name__ == "__main__":  # Проверяем, запущен ли этот файл напрямую (а не импортирован)
    main()  # Запускаем главную функцию

# Ссылка github
# https://github.com/kostyazu1985-arch/python_top_2026_1/blob/main/Home_work/DZ.py