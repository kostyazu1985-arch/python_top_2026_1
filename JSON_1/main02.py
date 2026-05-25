# 19.05.2026
# marshal
# pickle
# json

# dump() сохраняет данные в файл
# load() считывает данные из файла

# dumps() сохраняет в память
# loads() считывает из памяти

import pickle

# filename = "basket.txt"
#
# shop_list = {
#     "фрукты": ["Яблоки", "Груши"],
#     "овощи": ["Лук", "Томаты"],
#     "Бюджет": 1000
# }
#
# with open(filename, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(filename, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)

# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     dict = {"first": 'a', 'second': 3, 'third': [1, 2, 3]}
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f"число {Test.num}\nСтрока {Test.st}\nСписок{Test.lst}\nСловарь {Test.dict}\nКортеж {Test.tpl}"
#
# obj = Test()
# print(obj)
#
# d_save = pickle.dumps(obj)
# print(f'Сериализация в строку\n{d_save}')
#
# d_read = pickle.loads(d_save)
# print(f'Десериализация в строку\n{d_read}')


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a}, {self.b}, {self.c}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr["c"]
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
# item1 = Test2()
# item2 = pickle.dumps(item1) # __getstate__
# item3 = pickle.loads(item2) # __setstate__
#
# print(item3.__dict__)
# print(item3)


# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding="utf-8")
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith("\n"):
#             line = line[:-1]
#             return f"{self.count} {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state["file"]
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding="utf-8")
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("hello.txt")
# # print(reader.read_line())
# # print(reader.read_line())
# # print(reader.read_line())
# # print("*" * 50)
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())
# print(new_reader.read_line())
# print(new_reader.read_line())


# data = {
#     "first_name": "Иван",
#     "last_name": "Петров"
# }
#
# print(data)

# import json
#
# data = {
#     "first_name": "Ivan",
#     "last_name": "Smith",
#     "hobbies": ("python", "coding", "programming"),
#     "ages": 999,
#     "children": [
#         {
#             "name": "Petr",
#             "age": 9
#         },
#     ],
# }

# print(data)

# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)

# with open("data_file.json", "r") as f:
#     data = json.load(f)
#     print(data)

# json_string = json.dumps(data, sort_keys=True)
# print(json_string)
# print("*" * 150)
#
# data = json.loads(json_string)
# print(data)

# x = {
#     "name": "Виктор"
# }
#
# y = {
#     "name": "Иван"
# }
# print(json.dumps(x))
# print(json.loads(json.dumps(x)))

# print(json.dumps(y, ensure_ascii=False))


# import json
# from random import choice
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         # data = []
#         data = {}
#
#     # data.append(person_dict)
#
#     data[num] = person_dict
#
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# 21.05.2026

import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ''
        for i in self.marks:
            a += str(i) + ", "

        return f"Студент: {self.name} {a[:-2]}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @classmethod
    def dump_to_json(cls, stud, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []

        data.append({"name": stud.name, "marks": stud.marks})
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r") as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = ""
        for i in self.students:
            a += str(i) + "\n"
        return f"Группа: {self.group}\n{a}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @classmethod
    def change_group(cls, group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    @classmethod
    def dump_group(cls, file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, "w") as f:
            stud_list = []
            for i in group.students:
                stud_list.append([i.name, i.marks])
            data.append(stud_list)
            json.dump(data, f, indent=4)

    @classmethod
    def upload_group(cls, file):
        with open(file, "r") as f:
            print(json.load(f))



st1 = Student("John", [5, 1, 4, 3, 4, 5, 2])
st2 = Student("Ivan", [3, 2, 4, 3, 2, 5, 3])
st3 = Student("Petr", [5, 3, 5, 3, 5, 3, 2])
st4 = Student("Olga", [4, 3, 4, 3, 5, 3, 2])
sts = [st1, st2, st3]

# Student.dump_to_json(st1, "student.json")
# Student.dump_to_json(st2, "student.json")
# Student.load_from_file("student.json")

my_group = Group(sts, "Python-54")
# print(my_group)
#
# my_group.add_student(st4)
# print(my_group)
#
# my_group.remove_student(1)
# print(my_group)
#
# sts2 = [st4]
# my_group2 = Group(sts2, "Python-66")
# print(my_group2)
#
# Group.change_group(my_group, my_group2, 1)
# print(my_group)
# print(my_group2)

# Group.dump_group('group.json', my_group)
Group.upload_group('group.json')


# print(st1)
# st1.add_mark(5)
# print(st1)
# st1.delete_mark(1)
# print(st1)
# st1.edit_mark(5, 4)
# print(st1)
# print(st1.average_mark())
