a = "Прив3т т3б3".replace('3', "е")
print(a)
a = "Приветы".replace("ы", "")
print(a)
a = "ПриветЫ".replace("ы", "")
print(a)
a = "ПриветЫ".lower().replace("ы", "").capitalize()
print(a)
a = "Привет мир!".replace('мир', "python")
print(a)
a = "Предложение из нескольких слов"
print(len(a.split()))
a = 2
b = 0.5
print(a + b)
name = "Вячеслав"
b = f"Привет {name}!"
print(b)
a = None
b = 0
print(a is None)
print(b is None)
print(a == b)
a = 2
print(type(a))
b = "2.0"
print(type(b))
c = 2.0
print(type(c))
name = input("Введите ваше имя: ")
print(f"Привет, {name}")
age = int(input("Сколько вам лет? "))
birth_year = 2024 - age
print(f"Вы родились в {birth_year} году.")
a = "2.0"
b = float(a)
print(type(b))
v = int(input("Введите число от 1 до 10: "))
a = v + 10
print(a)
name = input("Введите ваше имя: ").upper()
print(f"Привет, {name}! Как дела?")
print(float("1"))
print(int(2.0))
print(bool(1))
print(bool(" "))
print(bool(0))
