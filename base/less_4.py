#s = "https://google.com"
#j = ['Hello', 'Python!', 'Hello', 'JS!']
#print(s.upper())
#print(s.lower())
#print(s.capitalize())
#print(s.replace(' ', ''))
#print(s.find('o'))
#print(s.count("o"))
#print(s.split(" "))
#x = ', '.join(j)
#print(x)

# s = [1, 2, 3, 4, 5]
# x = 7
# s.append(x)
# print(s)

# s = [1, 2, 3, 4, 5, 6]
# x = [0, 9, 8, 7]
# s.extend(x)
# print(s)

# s = [1, 2, 3, 4, 5, 6]
# s.insert(0, 0)
# print(s)

# s = [1, 2, 3, 4, 5, 6]
# if 3 in s:
#  s.remove(3)
# print(s)
from itertools import count

# s = "Привет мир!"
# c = "аеёиоуыэюя"
# count = 0
# for char in s.lower():
#     if char in c:
#         count += 1
# print(count)


# s = "Привет мир!"
# reversed_s = ""
# for i in s:
#     reversed_s = i+reversed_s
# print(reversed_s)

# s = "алла"
# reversed_s = ""
# for i in s:
#     reversed_s = i+reversed_s
# if s == reversed_s:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# s = "алла"
# cleaned = ''
# for char in s:
#     if ('а' <= char <= 'я') or ('ё'== char) or ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('А' <= char <= 'Я'):
#         if 'A' <= char <= 'Z':
#             cleaned += char(ord(char) + 32)
#         elif 'А' <= char <= 'Я':
#             if char == "Ё":
#                 cleaned  += 'ё'
#             else:
#                 cleaned += char(ord(char) + 32)
#         elif char == 'Ё':
#             cleaned += 'ё'
#         else:
#             cleaned += char
# reversed_cleaned = ''
# for i in range(len(cleaned) -1, -1, -1):
#     reversed_cleaned += cleaned[i]
# if cleaned == reversed_cleaned:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = 0
# for i in s:
#     if i % 2 == 0:
#         x += i
# print(x)

# s = {'a':3, 'b':4}
# x = {'a':7, 'c':9}
# for key in x:
#     if key in s:
#         s[key] += x[key]
#         continue
#     s[key] = x[key]
# print(s)

# a = {'a':3, 'b':4}
# b = {'a':7, 'c':9}
# x = {k: a.get(k, 0) + b.get(k, 0) for k in a | b}
# print(x)
"""
Создать строку, разбить на список слов, посчитать сколько слов длинее 5-6 символов, 
в результате создать словарь, где результатом будет ключ=длина слова значение=сколько таких слов

s = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium"
st = s.split(" ")
counter =0
rez = {}
for i in st:
    if len(i) > 5:
        counter += 1
    rez[len(i)] = st.count(i)
print(counter)
print(rez)
"""
