def index():
    with open("templates/index.html", encoding="utf-8") as template:
        return template.read()


def news():
    with open("templates/news.html", encoding="utf-8") as template:
        return template.read()