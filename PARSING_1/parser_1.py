# from bs4 import BeautifulSoup
#
# f = open("index.html").read()
# soup = BeautifulSoup(f, "html.parser")
from re import search

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

from bs4 import BeautifulSoup
import requests

req = requests.get("https://wordpress.org/")
# req.encoding = "utf-8"
# print(req.headers["Content-Type"])
# print(req.content)
print(req.text)







































