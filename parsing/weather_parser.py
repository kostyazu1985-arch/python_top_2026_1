import requests
import json

from bs4 import BeautifulSoup as bs


BASE_URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/"

def get_html(url: str) -> str | None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 YaBrowser/25.12.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html = response.text
        return html
    except Exception as e:
        print(f"При выполнении запроса возникла ошибка: {e}")
        return None

def parse_html(html: str) -> dict:
    # парсим html текст в объект soup
    soup = bs(html, "html.parser")
    weather_data = {}

    # находим таблицу с погодой по дням
    table = soup.find_all('table')[2]

    # находим все строки данной таблицы
    rows = table.find_all('tr')
    day = soup.find_all('div', class_="dates short-d")[0].text
    weather_data = {day: {}}

    for row in rows:
        cells = row.find_all('td')

        weather_day = cells[0].text # Ночь
        weather_data[day][weather_day] = {}

        weather_fact = cells[1].find('div')["title"] # пасмурно
        weather_temp = cells[1].text # температура °C
        weather_feeling = cells[2].text # Ощущается как °C
        weather_probability = cells[3].text # Вероятность осадков %
        weather_pressure = cells[4].text # Давление мм. рт. ст.
        weather_wind_direction = cells[5].find_all('span')[0]['title'] # направление ветра
        weather_wind_speed_kmh = cells[5].find_all('span')[1]['title'].strip() # скорость ветра км/ч
        weather_wind_speed_ms = cells[5].find_all('span')[1].text # скорость ветра м/с
        weather_humidity = cells[6].text # Влажность воздуха

        weather_data[day][weather_day]["Температура"] = weather_temp
        weather_data[day][weather_day]["Облачность"] = weather_fact
        weather_data[day][weather_day]["Ощущается"] = weather_feeling
        weather_data[day][weather_day]["Вероятность осадков"] = weather_probability
        weather_data[day][weather_day]["Давление"] = weather_pressure
        weather_data[day][weather_day]["Ветер"] = {
            "Направление": weather_wind_direction,
            "Скорость (км/ч)": weather_wind_speed_kmh,
            "Скорость (м/с)": weather_wind_speed_ms,
        }
        weather_data[day][weather_day]["Влажность"] = weather_humidity
    return weather_data


def write_weather_data_to_json(data: dict):
    with open("weather.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    html = get_html(url=BASE_URL)
    weather_data = parse_html(html=html)
    write_weather_data_to_json(data=weather_data)



