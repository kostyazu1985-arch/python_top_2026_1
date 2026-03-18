# Списки
numbers = []
cars = ["bmw", "audi"]

# получение длины списка
print(len(cars))

# добавление элемента в конец списка
cars.append("lada")
print(cars)

# добавление элемента по индексу
cars.insert(0,"kia")
print(cars)

# расширение списка
cars.extend(["honda", "mazda"])
print(cars)

#удаление элемента из списка (только первое вхождение)
cars.remove("honda")
print(cars)

#получение индекса элемента
ind_mazda = cars.index("mazda")
print(ind_mazda)

#подсчет количества элементов
count_mazda = cars.count("mazda")
print(count_mazda)

#удаление и получение элемента по индексу
deleted_element = cars.pop()
print(deleted_element)
print(cars)

#проверка вхождения элементов в список
bmw = "bmw" in cars
print(bmw)
if "mers" not in cars:
    print("ok")

#срез
#  -4     -3     -2      -1
#   0      1      2       3
#['kia', 'bmw', 'audi', 'lada']
print(cars)
print(cars[-3:])
#[start:end:step]
print(cars[::-1])

#for car in cars:
#    if len(car) > 3:
#        for i in car:
#            print(i.upper())

#name = input("Введите свое имя: ")
#print("Вы ввели имя -", name)

N = 3 #количество итераций
i = 0 # нач значение счетчика цикла
my_list = []

print()

while i < N:
    item = input("Введите строку: ")
    if len(item) > 3:
        my_list.append(item)
    else:
        print(f"Строка {item} менее 3 символов!")
    i += 1

print(my_list)

"""
пользователь вводит с клавиатуры строки
ввод закончить при вводе строки end (в любом регистре)
добавлять в список строки с ! на конце
"""
words = []
while True:
    text = input("Введите строку:\n")
    if text.lower() == "end":
        break
    else:
        if text:
            if text[-1] == "!":
                words.append(text)
                print(words)

