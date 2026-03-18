from functools import reduce
def sum_numbers(a, b):
    return a + b
print(sum_numbers(2,3)) # 5

add = lambda x, y: x + y
print(add(1, 2)) # 3

square = lambda x : x * x
print(square(3)) # 9

students = [
    {"name": "Alisa", "grade": 85},
    {"name": "Bob", "grade": 70},
    {"name": "Mark", "grade": 60},
    {"name": "Vlad", "grade": 100},
    {"name": "Lena", "grade": 90},
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
print(sorted_students) # [{'name': 'Vlad', 'grade': 100}, {'name': 'Lena', 'grade': 90}, {'name': 'Alisa', 'grade': 85}, {'name': 'Bob', 'grade': 70}, {'name': 'Mark', 'grade': 60}]

# filter
# map
# reduce
numbers = [1,5,8,0,20,3,7,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [8, 0, 20, 10]

words = ["apple", "banana", "cherry", "grape", "123"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words) # ['banana', 'cherry']

def chek_len(x):
    return len(x) < 4

short_words = list(filter(chek_len, words))
print(short_words) # ['123']

# map
numbers = [1,5,8,0,20,3,7,10]
double_list = list(map(lambda x: x * 2, numbers))
print(double_list) # [2, 10, 16, 0, 40, 6, 14, 20]

lst_1 = [1,2,3]
lst_2 = [4,5,6]
sums = list(map(lambda x,y: x + y, lst_1, lst_2))
print(sums) # [5, 7, 9]

# reduce
numbers = [1,5,8,0,20,3,7,10]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers) # 54

max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number) # 20