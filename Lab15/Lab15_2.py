
## демонстрацией работы со
# структурами данных Python (списки, кортежи, словари).

print("=== Списки ===")

# Список (list) представляет тип данных,
# который хранит набор или последовательность элементов.

numbers = [1, 2, 4, 5, 341 ,23]
users = ['user 1','user 2','user 3']
numbers2 = list(numbers)

print("1:",numbers)
print("2:",users[0] , users[-1])
print("3:",numbers2 * 2)

# Разложение

u1,u2,u3 = users
print("4:",u1,u2,u3)

# Перебор
print("4:")
for user in users:
    print(user)

# Сравнение

if numbers2 == numbers:
    print("5:", "true")
else:
    print("5:", "false")

# Получение части списка

print("6:",numbers2[1:4:2])


# Основные методы списка

print("7:\nlength:", len(numbers2))

numbers.append("Vlad") # [1, 2, 4, 5, 341 ,23,"Vlad"]
numbers.insert(1, "Hello")   # [1,"Hello", 2, 4, 5, 341 ,23,"Vlad"]
numbers.extend([666,1337]) # [1,"Hello", 2, 4, 5, 341 ,23,"Vlad",666,1337]
indexOfVlad = numbers.index("Vlad") # 7
removedItem = numbers.pop(indexOfVlad) # [1,"Hello", 2, 4, 5, 341 ,23,666,1337]
numbers.pop() # [1,"Hello", 2, 4, 5, 341 ,23,666]
numbers.remove("Hello") # [1, 2, 4, 5, 341 ,23,666]
del numbers[0] # [2, 4, 5, 341 ,23,666]
numbers[3:5] = [6,7]  # [2, 4, 5, 6 ,7,666]
print(numbers)
numbers.reverse() #  [666, 7 , 6 , 5 , 4 , 2]
print(numbers)
numbers.sort() # [2, 4, 5, 6 ,7,666]
print(numbers)
print("8:",numbers.count(4)) # кол-во вхождений 1
print("9:",max(numbers)) # 666
print("10:",min(numbers))  # 2
numbers.clear() # []
print(numbers)

users2 = users.copy()  # [ user 1, user 2, user 3 ]
print("11:",users2)
users2.append("New user")
print("12:",users2 + users)

print("=== Кортежи ===")

# Кортеж (tuple) представляет последовательность элементов, которая во
# многом похожа на список за тем исключением, что кортеж является
# неизменяемым (immutable) типом.
# Поэтому мы не можем добавлять или удалять элементы в кортеже, изменять его.


t1 = (1,2,3,4,5)
print(t1)
t2 = tuple([43,23,6,"wfw","VLad","wf",1])
print(t2)
t3 = 1,'Hello'
print(t3)

print("len t2:" , len(t2))
print(t3[0], " - " , t3[1])

n1,n2 = t3
print("n1,n2:",n1,n2)

print("t1:")
i = 0
while i < len(t1):
    print(t1[i])
    i+=1

if "VLad" in t2:
    print("true")
else:
    print("false")


print("=== Словари ===")

# Словарь (dictionary) в языке Python хранит коллекцию элементов,
# где каждый элемент имеет уникальный ключ и
# ассоциированое с ним некоторое значение.

dict1 = {1:"Hello",2:"World"}
print(dict1)
dict2 = {"@gmail.com":"Google","@mail.ru":"MailRu","@yandex.com":"Yandex"}
emails = dict(dict2)
print(emails)

## Преобр.

phonesList = [
    ["+375(29)","A1"],
    ["+375(44)","MTC"],
    ["+375(25)","Life"],
]
phones = dict(phonesList)
print(phones)
phonesCort = (
    ("+375(29)","A1"),
    ("+375(44)","MTC"),
    ("+375(25)","Life"),
)
phones2 = dict(phonesCort)
print(phones2)

# Получение и изменение

print("-->")
print("Old:",dict1[1])
dict1[1] = "Apple"
print("New:",dict1[1])

email1 = emails.get("@gmail.com","Unknown email")
print("GetEmail:",email1)

if 1 in dict1:
    num = dict1[1]
    print("num:",num)
else:
    print("num: null")

# Del.
print("<--")
del dict2["@mail.ru"]
print(dict2)

d1 = dict1.pop(2,"Unknown")
print(d1, " - " , dict1)

# Копирование и объединение словарей
print("<------->")
fruits = dict1.copy()
print(fruits)

dict2.update(fruits)
print(dict2)

# Перебор
print("====<>=====")
print("1:")
for key in phones:
    print(f"{key}: {phones[key]}")
print("2:")
for key,value in dict2.items(): # возвращает набор кортежей
    print(f"{key}: {value}")
print("3:")
for key in phones.keys():
    print(f"{key}")
print("4:")
for values in phones.values():
    print(values)

