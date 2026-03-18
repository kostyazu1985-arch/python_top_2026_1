# множества - set
from less_3_tuple import person

users = {"Anna","Sasha", "Lena", "Anna"}
users_list = {"Anna","Sasha", "Lena", "Anna"}
users_set = set(users_list)
print(users_set)
print(users)

set_of_cars = set()
print(type(set_of_cars))
set_of_cars.add("audi")
set_of_cars.add("bmw")
set_of_cars.add("lada")
#set_of_cars.remove("lada")

#set_of_cars.discard("lada222")
print(len(set_of_cars))
for car in set_of_cars:
    print(car)

set_of_cars_2 = {"audi", "UAZ", "mazda"}

# объединение множеств - union |
result_set_of_cars = set_of_cars.union(set_of_cars_2)
print(result_set_of_cars)
print(set_of_cars | set_of_cars_2)

# пересечение множеств - intersection &
print("Intersection")
result_set_of_cars = set_of_cars.intersection(set_of_cars_2)
print(result_set_of_cars)
print(set_of_cars & set_of_cars_2)

# разность множеств - difference -
print("Difference")
result_set_of_cars = set_of_cars.difference(set_of_cars_2)
print(result_set_of_cars)
print(set_of_cars - set_of_cars_2)

# симметричная разность множеств - symmetric_difference ^
print("Symmetric_difference")
result_set_of_cars = set_of_cars.symmetric_difference(set_of_cars_2)
print(result_set_of_cars)
print(set_of_cars ^ set_of_cars_2)

# issubset
users = {"Masha", "Dasha", "Sasha", "Lena"}
superusers = {"Sasha", "Lena"}

print("issubset")
print(users.issubset(superusers))
print(superusers.issubset(users))

persons = frozenset({"Masha", "Sasha"})
print(type(persons))

numbers = ["234534", "23542345", "23546346"]
set_numbers = frozenset(numbers)
print(set_numbers)