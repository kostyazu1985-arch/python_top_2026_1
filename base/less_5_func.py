# def print_hello(name): # сигнатура функции
#     print(name.title()) # тело функции
#
# def print_fio(name, last_name, age):
#     name = name.title()
#     last_name = last_name.upper()
#     new_age = age * 2
#     print(name, last_name, new_age)
#
# def hello():
#     print("Hello")
#
# hello()
# hello()
# name = "Dima"
# print_hello(name=name)
#
# my_age = 18
# my_name = "Vlad"
# my_last_name = "Petrov"
# print_fio(name=my_name, last_name=my_last_name, age=my_age)
#
# # numbers =[2,7,9,11,15]
# def get_min_value(numbers):
#     min_value = numbers[0]
#     for i in numbers:
#         if i < min_value:
#             min_value = i
#     print(min_value)
#
# numbers_1 = [1,2,6,7,8,9]
# numbers_54 = [1,8,6,-2,9]
#
# # get_min_value(numbers_1)
# # get_min_value(numbers=numbers_54)
# # get_min_value([1000,7,9,0])
# # get_min_value(numbers=[-6,7,9])
#
# # text_1 = "hello11 privet 25"
# def get_count_numbers(text):
#     count = 0
#     sum_numbers = 0
#     symbols = "0123456789"
#     for i in text:
#         if i in symbols:
#             count += 1
#         if i.isdigit():
#             sum_numbers += int(i) # int("1124") = 1124 int("1124a") = error
#     print(f"Количество цифр - {count}")
#     print(f"Сумма цифр - {sum_numbers}")
#
# # text_1 = "hello11 privet 25"
# # get_count_numbers(text=text_1)

# найти максимальное четное число
array = [1, 5, 8, 10, 7]
def get_max_even_number(numbers):
    max_value = None  # Лучше начать с None, так как мы еще не нашли ни одного четного

    for i in numbers:
        if i % 2 == 0:  # Сначала проверяем на четность
            # Если это первое четное число или оно больше текущего максимума
            if max_value is None or i > max_value:
                max_value = i

    return max_value

# Вызываем и печатаем результат
print(get_max_even_number(array))
# мы объединяем фильтрацию четных чисел и поиск максимального значения с помощью функции max()
print(max(i for i in [1, 5, 8, 10, 7] if i % 2 == 0))









