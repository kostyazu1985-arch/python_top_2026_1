# Определение класса Animal
class Animal:
    # атрибут класса
    counter = 0 # Общая переменная для всего класса (счетчик созданных животных)
    # Конструктор класса (вызывается в момент инициализации объекта класса)
    # self - ссылка на сам объект
    def __init__(self, breed, name, age, color='Gray'): # Метод, который задает свойства при создании объекта
        # определение атрибутов объекта
        self.breed = breed # Записываем породу в личное свойство объекта
        self.name = name # Записываем имя в личное свойство объекта
        self.color = color # Записываем цвет объекта
        self.vozrast = age # Записываем возраст в свойство с именем vozrast
        # добавится в объект без указания в параметрах конструктора
        self.country = "Russia" # Автоматически присваиваем каждому объекту страну "Russia"
        Animal.counter += 1 # Увеличиваем общий счетчик класса при каждом создании нового животного

    # функция, написанная внутри класса = МЕТОД ОБЪЕКТА
    # и вызывается для конкретного объекта через точку
    def hello(self):
        print(f"Hi, I am {self.name}, {self.breed}, i am {self.vozrast}") # Печатаем данные конкретного объекта

    # self - объект из которого вызывается метод
    # self.name - это name того объекта, который вызвал метод
    def bye(self, friend): # Метод bye, принимает дополнительный аргумент friend
        print(f"Bye, {friend}. {self.name} go to sleep!") # Печатаем прощание к другу от имени объекта

print(Animal.counter) # Выводим значение счетчика (сейчас там 0)
dog_chappy = Animal(breed="Spaniel", name="Chappy", age=3) # Создаем объект класса Animal с заданными параметрами
print(Animal.counter)
cat_barsik = Animal(breed="Sfinks", name="Barsik", color="Black", age=2)
print(Animal.counter)

dog_chappy.host = "Valera" # Создаем НОВЫЙ атрибут host (хозяин) только для конкретной собаки Чаппи

# print(dog_chappy.country)
# print(cat_barsik.country)
# print(cat_barsik.color)
# print(dog_chappy) # Выводим весь объект на экран
# print(dog_chappy.name) # Выводим значение атрибута name объекта
# print(dog_chappy.breed) # Выводим значение атрибута breed объекта
# print(Animal.host) # Ошибка: у всего класса Animal нет атрибута host
# print(dog_chappy.host) # Выведет "Valera"
# print(cat_barsik.host) # Ошибка: у кота Барсика нет атрибута host

dog_chappy.hello() # Чаппи печатает информацию о себе
cat_barsik.hello() # Барсик печатает информацию о себе
cat_barsik.bye(friend="Misha") # Барсик прощается с Мишей
dog_chappy.bye(friend="Marina") # Чаппи прощается с Мариной