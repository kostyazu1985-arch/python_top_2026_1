import requests


def get_url_image(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("message") and data.get("status") == "success":
            link = data.get("message")
            return link
        else:
            print(data.get("status"))
            return ""
    except Exception as e:
        print(f"Возникла ошибка: {e}")
        return ""

def get_image_by_url(image_url: str) -> bytes:
    try:
        response = requests.get(url=image_url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Возникла ошибка: {e}")
        return b""

def create_image(bytes_of_image: bytes) -> None:
    with open("dog.jpg", "wb") as file:
        file.write(bytes_of_image)


if __name__ == "__main__":
    URL = "https://dog.ceo/api/breeds/image/random"
    link = get_url_image(URL)
    print(link)
    if link:
        image = get_image_by_url(image_url=link)
        create_image(bytes_of_image=image)

#* изменить программу таким образом, чтобы она скачивала и сохранила 10 разных картинок
#** название картинки должно соответствовать наименованию породы
#*** сделать так, чтобы каждая порода сохранялась в свой отдельный каталог (прочитать os.mkdir)
