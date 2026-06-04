import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="caption")
        for item in news:
            title = item.find("h3", class_="topic-title").text.strip()

            print(title)

        # print(news)

    def run(self):
        self.get_html()
        self.parsing()















