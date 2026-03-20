class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

animal = Animal("Petr", 18)
print(animal.get_name())
print(animal.get_age())

