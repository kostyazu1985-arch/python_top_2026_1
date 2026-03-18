def check_age(age):
    if age >= 18:
        return True
    return False

def hello():
    print("Hello")
    age = 20
    return check_age(age)

def print_items(items):
    first = items[0]
    last = items[-1]
    return first, last, first+last

result = hello()
print(result)

# result = hello() # None
# result_age = check_age(10) # False
# print(result)
# print(result_age)