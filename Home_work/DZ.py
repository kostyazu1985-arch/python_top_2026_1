import csv # для записи данных в csv
import time # пауза от бана
from bs4 import BeautifulSoup # для поиска по тегам
import requests # для скачивания веб страниц


class RecipeParser:

    def __init__(self):
        self.base_url = "https://www.russianfood.com/recipes/bytype/?fid=926&page="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        self.all_recipes = [] # для хранения всех рецептов

    # метод для скачивания страницы по ее номеру
    def fetch_page(self, page_number):
        url = f"{self.base_url}{page_number}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Ошибка при загрузке страницы {page_number}: {e}")
            return None

    # метод для извлечения рецептов из html
    def parse_page(self, html_text):
        if not html_text:
            return

        soup = BeautifulSoup(html_text, "html.parser")

        recipe_cards = soup.find_all("div", class_="recipe_l")

        for card in recipe_cards:
            # ищем название
            title_tag = card.find("div", class_="title")
            title = title_tag.text.strip() if title_tag else "Название не указано"

            # ищем описание
            description_tag = card.find("div", class_="announce")
            if description_tag:
                description = description_tag.text.replace("Далее...", "").replace("\n", " ").strip()
            else:
                description = "Описание отсутствует"

            # ищем время приготовления
            time_tag = card.find("span", class_="prep_time")
            if not time_tag:
                time_tag = card.find("div", class_="info")

            if time_tag and "мин" in time_tag.text:
                cooking_time = time_tag.text.strip()
            else:
                cooking_time = "Не указано"

            self.all_recipes.append(
                {
                    "Название": title,
                    "Описание": description,
                    "Время приготовления": cooking_time,
                }
            )

    # метод для сохранения данных в csv
    def save_to_csv(self, filename):
        if not self.all_recipes:
            print("Нет данных для сохранения")
            return

        with open(filename, "w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "Название",
                "Описание",
                "Время приготовления",
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            writer.writerows(self.all_recipes)
        print(f"Данные ({len(self.all_recipes)} шт.) сохранены в файл '{filename}'")

    # главный метод для запуска процесса
    def run(self, start_page=1, end_page=10):
        print("Запуск ООП-парсера...")

        for page in range(start_page, end_page + 1):
            print(f"Обработка страницы {page} из {end_page}...")

            page_html = self.fetch_page(page)
            self.parse_page(page_html)
            time.sleep(1)

if __name__ == "__main__":
    parser = RecipeParser()
    parser.run(start_page=1, end_page=10)
    parser.save_to_csv("oop_recipes.csv")




# Ссылка github
# https://github.com/kostyazu1985-arch/python_top_2026_1/blob/main/Home_work/DZ.py