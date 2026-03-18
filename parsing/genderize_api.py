import requests


def get_gender_by_name(name: str):
    url = "https://api.genderize.io/"
    params = {"name": name}
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    gender = data["gender"]
    probability = data["probability"]
    result = f"Имя {name} имеет пол - {gender} с вероятностью {probability * 100:.2f}%"
    return result

result = get_gender_by_name(name="Женя")
print(result)