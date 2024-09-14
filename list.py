phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
print(phones)
phones.append("iPhone 12")
count = len(phones)
print(count)
print(phones.count("iPhone 12"))
print(phones.count("iPhone 9"))
print(phones[1])
print(phones[3])
print(phones[1:3])
print(phones[:2])
print(phones[-1])
print(phones.index("Xiaomi Mi11"))
phones.sort()
print(phones)
print(phones.index("Xiaomi Mi11"))
print("iPhone 12" in phones)
print("iPhone 9" in phones)
del phones[1]
print(phones)
phones.remove("iPhone 12")
print(phones)
number = ["3", "5", "7", "9", "10.5"]
print(number)
number.append("Python")
count = len(number)
print(count)
print(number[0])
print(number[5])
del number[5]
print(number)
product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}
print(len(product))
product["memory"] = 64
print(product)
product["name"] = "iPhone 12 Pro"
print(product)
print(product["price"])
print(product["stock"])
print(product.get("name"))
print(product.get("discount"))
print(product.get("discount", 0))
print(product.get("country", "CN"))
print(product)
del product["stock"]
print(product)

from pprint import pprint

phones = ["Samsung Galaxy S21", "iPhone 12"]
product["recomended"] = phones
pprint(product)
print(product["recomended"])
product["recomended"].append("Xiaomi Mi11")
print(len(product["recomended"]))
print(product["recomended"][0])

stock = [
    {"name": "iPhone 12 plus", "stock": 24, "price": 65432.1,
     "recomeded": ["Samsung Galaxy S21", "iPhon12"]},
     {"name": "Samsung Galaxy S21", "stock": 8, "price": 50000.0, "discount": 5000},
     {"name": "Xiaomi Mi11", "stock": 42, "price": 38000.5}
]
print(stock)
print(stock[2])
stock[2]["price"] = stock[2]["price"] - 8000
print(stock[2]["price"])
print(stock[0]["recomeded"][1])
print(type(stock))
print(type(stock[0]))

mission ={
    "city": "Москва",
    "temperature": "20"
}
print(mission["city"])
mission["temperature"] = float(20)
mission["temperature"] = mission["temperature"] - 5
print(mission)
print(mission.get("country"))
print(mission.get("country", "Россия"))
mission["country"] = 'Россия'
count = len(mission)
print(count)
print(mission)
























