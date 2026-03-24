# Задача 1
class Wolf:
    def howl(self):
        print("Уууу!")

class Dog:
    def bark(self):
        print("Гав!")

class Warewolf(Wolf, Dog):
    def transform(self):
        print("Превращение!")

monster = Warewolf()

monster.bark()
monster.transform()
monster.howl()

print(Warewolf.__mro__)
print("-" * 80)

# Задача 2
class EatMixin:
    def eat(self):
        print("Сотрудник ест.")

class SleepMixin:
    def sleep(self):
        print("Сотрудник спит.")

class Worker(EatMixin, SleepMixin):
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} работает.")

employee = Worker("Дмитрий")

employee.sleep()
employee.work()
employee.eat()

print("-" * 80)

# Задача 3
class A:
    def show(self):
        print("Класс A.")

class B:
    def show(self):
        print("Класс В.")

class C(A, B):
    def test(self):
        self.show()

obj = C()
obj.test()
# В Python поиск методов идет слева направо по списку родителей.
# Так как в class C(A, B) класс A стоит первым, его метод "перекрывает" метод класса B.

class C_new(B, A):
    def test(self):
        self.show()
obj_new = C_new()
obj_new.test()

print("-" * 80)

# Задача 4
class PrintMixin:
    def print_document(self, text):
        print(f"Печать документа: {text}")

class SaveMixin:
    def save_document(self, text):
        print(f"Сохранено: {text}")

class Document(SaveMixin, PrintMixin):
    def create(self, content):
        self.print_document(content)
        self.save_document(content)

my_doc = Document()
my_doc.create("Важный документ")


