# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.is_hungry = True
#
#     def bark(self):
#         print(f"{self.name} сказала гав-гав")
#
#     def eat(self):
#         if self.is_hungry:
#             print(f"{self.name} поела и рада!")
#             self.is_hungry = False
#         else:
#             print(f"{self.name} не голодна!")
#
#     def get_info(self):
#         print(f"Собака {self.name} . Возраст {self.age}. Голодна {self.is_hungry}.")
#
# dog_1 = Dog("Бобик", 3)
#
# dog_2 = Dog("Шарик", 12)
#
#
# print(dog_1.name) # Бобик
# print(dog_2.name) # Шарик
#
# dog_1.bark() # Бобик сказала гав-гав
# dog_2.bark() # Шарик сказала гав-гав
# dog_1.eat() # Бобик поела и рада!
# dog_2.eat() # Шарик поела и рада!
# dog_1.get_info() # Собака Бобик . Возраст 3. Голодна False.
# dog_2.get_info() # Собака Шарик . Возраст 12. Голодна False.
from datetime import datetime


# class User:
#     def __init__(self, name, password):
#         self.name = name # Public
#         self._login = "login1" # Protected
#         self.__password = password # Private
#
#     def get_pass(self):
#         return self.__password
#
#     def set_pass(self, new_password):
#         self.__password = new_password
#
#     def show_info(self):
#         print(f"Name {self.name}. Password: {self.__password}")
#
# user = User('Petr', "12345")
#
# print(user.name) # Petr
# print(user._login) # login1
# print(user.get_pass()) # 12345
# user.set_pass('qwerty')
# print(user.get_pass()) # qwerty
#
#
# class Safe():
#     def __init__(self):
#         self.__name = "Ivan"
#         self.__money = 10000
#
#     def get_name(self):
#         return self.__name
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, new_money):
#         if new_money > 0:
#             self.__money += new_money
#             print(f"User added {new_money}")
#
#         else:
#             print("Сумма должна быть положительной")
#
#     def take_money(self, new_money):
#         if new_money > 0:
#             self.__money -= new_money
#             print(f"User added {new_money}")
#
#         else:
#             print("Сумма должна быть положительной")
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
# my_safe = Safe()
#
# print(f"{my_safe.get_name()}, {my_safe.get_money()}")
# my_safe.add_money(100)
# my_safe.set_name("Petr")
# print(f"{my_safe.get_name()}, {my_safe.get_money()}")
# my_safe.take_money(1000)
# print(f"{my_safe.get_name()}, {my_safe.get_money()}")


# class Account:
#     def __init__(self):
#         self.__name = ''
#         self.__password = ''
#
#     def set_name(self,new_name):
#         self.__name = new_name
#
#     def set_password(self,new_password):
#         if len(new_password) > 5:
#             self.__password = new_password
#             print("пароль установлен")
#         else:
#             print("ошибка при установке пароля")
#
#     def get_name(self):
#         return self.__name
#
#     def get_password(self):
#         return self.__password
#
#     def chek_name(self, name):
#         if name == self.__name:
#             return True
#         else:
#             return False
#
#     def chek_password(self, password):
#         return self.__password == password
#         # if password == self.__password:
#         #     return True
#         # else:
#         #     return False
#
# acc = Account()
# acc.set_name("Иван")
# acc.set_password("password212313")
# print(acc.get_name())
# print(acc.get_password())
# print(acc.chek_name("Иван"))
# print(acc.chek_password("password212313"))

# @property декоратор

# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#
#     @age.setter
#     def age(self, new_age):
#         if 0 < new_age <= 100:
#             self.__age = new_age
#         else:
#             print("Ошибка!")
#
#
# p = Person(29)
# print(p.age)
# p.age = 39
# print(p.age)


# class Water:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def get_temperature(self):
#         return self.__temperature
#
#     def set_temperature(self, new_temperature):
#         if 0 <= new_temperature <= 100:
#             self.__temperature = new_temperature
#             print("ok")
#         else:
#             print("error")
#
#     def get_state(self):
#         if self.__temperature <= 0:
#             return "ice"
#         elif self.__temperature >= 100:
#             return "steam"
#         else:
#             return "water"
#
# w = Water(105)
# print(w.get_temperature())
# print(w.get_state())


# НАСЛЕДОВАНИЕ

# class Teacher:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.age = age
#         self.surname = surname
#
# class Student:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.age = age
#         self.surname = surname
#
# class Worker:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.age = age
#         self.surname = surname


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("Животное издало звук")
#
#     def get_info(self):
#         print(f"Имя {self.name}. Возраст {self.age}")
#
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
#
#     def speak(self):
#         print("гав-гав")
#
#     def fetch(self):
#         print(f"{self.name} принес палку")
#
#
# a1 = Animal("Васька", 5)
# a1.speak()
# a1.get_info()
#
# dog = Dog("Бобик", 5, "Корги")
# dog.fetch()
# dog.speak()
# dog.get_info()


# class Parent:
#     def __init__(self, name):
#         self.name = name
#         print("Parent created")
#
#     def greet(self):
#         print(f"привет я {self.name}")
#
# class Child(Parent):
#     def __init__(self, name,  age):
#         super().__init__(name)
#         self.age = age
#         print("Child created")
#
#     def greet(self):
#         super().greet()
#         print(f"мне {self.age} лет")
#
#
# c = Child("Женя", 6)
# c.greet()


# class Transport:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         print(f"Транспорт {self.brand} {self.model}, год выпуска {self.year}")
#
# class Car(Transport):
#     def __init__(self, brand, model, year, doors):
#         super().__init__(brand, model, year)
#         self.doors = doors
#
#     def get_info(self):
#         print(f"Автомобиль {self.brand} {self.model} {self.year}, количество дверей: {self.doors}")
#
# t = Transport('BMW', 'X5', 2015)
# t.get_info()
#
# c = Car('BMW', 'X5', 2015, 5)
# c.get_info()


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def get_bonus(self):
#         return 0
#
# class Manager(Employee):
#     def __init__(self,name,salary, command):
#         super().__init__(name,salary)
#         self.command=command
#
#     def get_bonus(self):
#         return self.salary*1.10
#
# em = Employee("Иван", 50000)
# print(em.get_bonus())
# print(f"{em.name} {em.salary}")
# man = Manager("Петр", 100000, 7)
# print(man.get_bonus())
# print(f"{man.name} {man.salary}")


# class A:
#     def speak(self):
#         print("Я класс А")
#
# class B:
#     def speak(self):
#         print("Я класс B")
#
# class C(A,B):
#     pass
#
# obj = C()
# obj.speak()
#
# print(C.__mro__) # порядок поиска методов

# class LogMixin:
#      def log(self,message):
#          print(f"[LOG] {message}")
#
# class SaveMixin:
#      def save(self):
#          print(f"Сохранено в базу данных")
#
# class User(LogMixin, SaveMixin):
#     def __init__(self, name):
#         self.name = name
#
#     def register(self):
#         self.log(f"Регистрация пользователя {self.name}")
#         self.save()
#
# u = User("Petr")
# u.register()

# class Car:
#     def drive(self):
#         print("Машина едет")
#
# class Plane:
#     def fly(self):
#         print("Самолет летит")
#
# class FlyingCar(Car, Plane):
#     pass
#
# fc = FlyingCar()
# fc.fly()
# fc.drive()

# from datetime import datetime
#
# class TimeMixin:
#     def get_time(self):
#         return datetime.now().strftime("%H:%M:%S")
#
# class Task(TimeMixin):
#     def __init__(self, name):
#         self.name = name
#
#     def create(self):
#         current_time = self.get_time()
#         print(f"Задача {self.name} создана в: {current_time}")
#
# my_task = Task("Сделать ДЗ")
# my_task.create()

# class A:
#     def __init__(self):
#         print("A init")
#
# class B(A):
#     def __init__(self):
#         print("B init")
#         A.__init__(self)
#
# class C(A):
#     def __init__(self):
#         print("C init")
#         A.__init__(self)
#
# class D(B, C):
#     def __init__(self):
#         print("D init")
#         B.__init__(self)
#         C.__init__(self)
#
# d = D()
# print(D.__mro__)

# class A:
#     def __init__(self):
#         print("A init")
#
# class B(A):
#     def __init__(self):
#         print("B init")
#         super().__init__()
#
# class C(A):
#     def __init__(self):
#         print("C init")
#         super().__init__()
#
# class D(B, C):
#     def __init__(self):
#         print("D init")
#         super().__init__()
#
# d = D()


class LogMixin:
     def log(self,message):
         print(f"[LOG] {message}")

class SaveMixin:
     def save(self, message, level="INFO"):
         print(f"[{level}] {self.__class__.__name__}: {message}]")

     def log_error(self, message):
         self.log(message, level="ERROR")

class UserService(LogMixin):
    def create_user(self, name):
        self.log(f"Создание пользователя: {name}")
        self.log(f"Пользователь {name} создан")

class OrderService(LogMixin):
    def create_order(self, order_id):
        self.log(f"Создание заказа: {order_id}")
        self.log(f"Заказ {order_id} создан")


u = UserService()
u.create_user("Petr")

o = OrderService()
o.create_order(123)

