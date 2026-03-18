import random
import string

from base.less_3_string import alphabet

# генерация случайного целого числа в диапазоне [min, max]
print(random.randint(1,10))

# генерация случайного числа с плавающей точкой
rand_float = random.uniform(1.5, 5.5)

# округление
print(round(rand_float,3))

# готовые последовательности
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

print(letters)
print(digits)
print(punctuation)

# генерация нескольких случайных символов из заданного набора(в список)
text = random.choices(letters, k=3)
print(text)

# генерация одного случайного символа из заданного набора
char = random.choice(punctuation)
print(char)

def generate_random_string(length: int):
    alphabet = letters + digits + punctuation
    # выбираем length случайных элементов и объединяем в строку
    password = ""
    for i in range (length):
        char = random.choice(alphabet)
        password += char
    print(password)

def generate_random_string_list_compr(length: int):
    alphabet = letters + digits + punctuation
    # выбираем length случайных элементов и объединяем в строку
    password = "".join(random.choice(alphabet) for i in range (length))
    print(password)


generate_random_string(8)
generate_random_string_list_compr(8)

uniq_chars = "".join(random.sample(string.ascii_letters + string.digits, 8))
print(uniq_chars)