# создание класса Car
class Car:
    # конструктор класса
    def __init__(self, brand, model, year, is_available_sale=True):
        # сохраняем параметры конструктора в объект
        self.brand = brand
        self.model = model
        self.year = year
        self.is_available_sale = is_available_sale
        # определим атрибут объекта (без передачи в конструктор)
        self.car_type = "passenger car"
        self.is_power = False # флаг устанавливающий заведен авто или нет
        self.is_drive = False # флаг устанавливающий в движении авто или нет

    def get_info(self):
        print(f"Марка: {self.brand} модель {self.model} год выпуска {self.year}")

    def power_on(self):
        if not self.is_power==True:
            print(f"Автомобиль {self.brand} {self.model} {self.year} года УЖЕ ЗАВЕДЕН!")
            return
        print(f"Автомобиль {self.brand} {self.model} {self.year} года ЗАВЕДЕН!")
        self.is_power = True

    def power_off(self):
        if self.is_power==False:
            print(f"Автомобиль {self.brand} {self.model} {self.year} года УЖЕ ЗАГЛУШЕН!")
            return
        if self.is_drive==True:
            print(f"Автомобиль {self.brand} {self.model} {self.year} года не могу заглушить авто в движении!")
            self.is_power = False

    def car_go(self):
        if self.is_drive:
            print(f"Автомобиль {self.brand} {self.model} {self.year} года ПОЕХАЛ!")
            return
        print(f"Автомобиль {self.brand} {self.model} {self.year} года УЖЕ ЗАГЛУШЕН!")
        self.is_drive = True

    def car_stop(self):
        print(f"Автомобиль {self.brand} {self.model} {self.year} года ОСТАНОВИЛСЯ!")

    def car_turn(self, direction):
        if direction.upper() in ["НАЛЕВО", "НАПРАВО"]:
            print(f"Автомобиль {self.brand} {self.model} {self.year} повернул {direction}")
        else:
            print(f"Ошибка: Направление {direction} неверное !")

car_1 = Car(brand="Lada", model="Vesta", year=2025)
car_2 = Car(brand="BMW", model="M3", year=2025, is_available_sale=False)





# car_2.power_off()
# car_2.power_on()
# car_2.power_off()
# car_2.power_on()
#
#
# car_1.get_info()
# car_2.get_info()
#
# car_1.power_on()
# car_2.power_on()
#
# car_1.power_off()
# car_2.power_off()
#
# car_1.car_go()
# car_2.car_go()
#
# car_1.car_turn(direction="НАЛЕВО")
# car_2.car_turn(direction="НАПРАВО")
#
# car_1.car_stop()
# car_2.car_stop()


car_2.power_off()
car_2.power_on()
car_2.car_go()
car_2.power_off()
