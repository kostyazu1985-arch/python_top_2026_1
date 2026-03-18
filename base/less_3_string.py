message = "Hello World"
name = 'Misha'
char = 'i'

print(type(message))
print(type(name))
print(type(char))

text = ("kugjgjhgj\n"
        "jhgjuyghjk\n"
        "kuhkuhkjhkuhbkh\n")
print(text)

long_text = """
jhkhkhjkjli
kjhkhkjhnkjjn
lijlijlm
"""
print(long_text)

alphabet = "abcdefgh"
print(alphabet[:4], alphabet[3:])
print(list(alphabet))

for char in alphabet:
    print(char)

print(len(alphabet))

name = "petrov michael sergeevich"
last_name = "Ivanov"
fullname = name + " " + last_name

print(" ".join([name, last_name]))
print(fullname)

print("a"*3)

print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.replace("e", "!!!",2))
print(name.count("e"))
email = "admin@yandex.ru"
print(email.endswith("yandex"))
print(email.startswith("min"))


if "admin" in email:
    print("admin in email")

input_value = "  hello!!!  "
print(input_value.strip("! "))
site = "auth.vk.spb.ru"
domens = site.split(".")
print(domens)
print(len(domens))
print(domens[0])
print(domens[-1])