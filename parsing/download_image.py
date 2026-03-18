import  requests

def download_image_by_url(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open("image.svg", "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(e)


url = "https://www.logotypes.dev/apple?version=color"
download_image_by_url(url=url)
