# from bs4 import BeautifulSoup
#
# f = open("index.html").read()
# soup = BeautifulSoup(f, "html.parser")

# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find_all("div", class_="row")[1].find("div", class_="links").text

# row = soup.find("div", {"class": "name"})
# row = soup.find("div", {"data-set": "salary"})

# row = soup.find("div", string="Alena").parent.parent
# row = soup.find("div", string="Alena").find_parent(class_="row")

# row = soup.find("div", id="whois1")
# row = soup.find("div", id="whois2").find_next_sibling()
# row = soup.find("div", id="whois2").find_previous_sibling()
#
# print(row)

# from bs4 import BeautifulSoup
#
# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", class_="row")
#
# # print(row)
#
# copywriter = []
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# from bs4 import BeautifulSoup
# import re
#
# def get_salary(s):
#     # pattern = r"\d+"
#     pattern = r"[0-9]+"
#
#     # res = re.findall(pattern, s)[0]
#     res = search(pattern, s).group()
#     print(res)
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
#
# # print(salary)
#
# for i in salary:
#     get_salary(i.text)
#     # print(i.text)

# from bs4 import BeautifulSoup
# import requests
#
# req = requests.get("https://wordpress.org/")
# # req.encoding = "utf-8"
# # print(req.headers["Content-Type"])
# # print(req.content)
# print(req.text)


from bs4 import BeautifulSoup
import requests
import re
import csv

# req = requests.get("https://wordpress.org/")
# req.encoding = "utf-8"

# print(req)
# print(req.headers)
# print(req.headers['Content-Type'])
# print(req.content)
# print(req.text)

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow([data["name"], data["url"], data["rating"], data["snippet"]])
#
# def get_data(html):
#     # soup = BeautifulSoup(html, "html.parser")
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[2]
#     plugins = p1.find_all("li")
#     for plugin in plugins:
#         try:
#             name = plugin.find("h3", class_="entry-title").text
#         except AttributeError:
#             name = ""
#         url = plugin.find("h3", class_="entry-title").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").text
#         replace_rating = refined(rating)
#         snippet = plugin.find("div", class_="entry-excerpt").text.strip()
#
#         data = {"name": name, "url": url, "rating": replace_rating, "snippet": snippet}
#         write_csv(data)
#         # return data
#
# def main():
#     url = "https://wordpress.org/plugins/"
#     # print(get_data(get_html(url)))
#     get_data(get_html(url))
#
# if __name__ == "__main__":
#     main()


# from bs4 import BeautifulSoup
# import requests
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins_list.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow([data["name"], data["url"], data["active"], data["tested"]])
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("li", class_="wp-block-post")
#     for element in p1:
#         name = element.find("h3", class_="entry-title").text
#         url = element.find("h3", class_="entry-title").find("a")["href"]
#         active = element.find("span", class_="active-installs").text.strip()
#
#         try:
#             tested = element.find("span", class_="tested-with").text.strip()
#             test = refined(tested)
#         except AttributeError:
#             test = ""
#
#         data = {
#             "name": name,
#             "url": url,
#             "active": active,
#             "tested": test
#         }
#         write_csv(data)
#
#         # return test
#
#
# def main():
#     for i in range(1, 15):
#         url = f"https://wordpress.org/plugins/browse/popular/page/{i}/"
#         # print(get_data(get_html(url)))
#         get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()


# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news", 'news.txt')
#     pars.run()
#
#
# if __name__ == "__main__":
#     main()
