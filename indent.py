import random

x = random.randint(1, 10)

if x > 5:
    print("Больше 5")
else:
    print("Меньше 5")

print(f"X = {x}")

def is_more_than_five(number):
    if number > 5:
        print("Больше 5")
    else:
        print("Меньше 5")

rand_num = random.randint(1, 10)
is_more_than_five(rand_num)

def do_something():
    print("Я внутри функции")
    print("Я внутри функции")

x = 0
while x < 10:
    print(x)
x = x + 1
