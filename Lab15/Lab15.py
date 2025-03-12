## В интерактивном режиме произвести простые вычисления и
# преобразования строки.

a = int(input())
b = int(input())
print("Common operations")
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
print("====== 2 =======")
print(round(4.131))
print(round(4.131,1))
print("======= 3 ======")

n = 123
print(str(n))
c = '123'
print(int(c))
print("====== Strings =======")

# преобразования строки

str = ("Это "
       "строка")

str2 = "Это тоже\n\tстрока"

str3 = f"a:{a} b:{b} c:{c}"

print(str2 + str3)
print(f"len str:{len(str)}")
print("By index:",str[1])

print("=============")

print("A" > "a")
print("A" > "A")
print("A" == "A")

print("====== up/low =======")
name = 'vlad'
print(name.upper())
print((name + 'VLAD').lower())
print("====== Unicode =======")
print(ord("V"))
print(len(name))
print("====== Search =======")
txt = "hello world"
print("world" in txt)
print("===== Methods =====")
t1 = " hel lo "
t2 = "world"
t3 = ["V","l","a","d"]
print("".join(t3))
print(txt.find("he"))
print(t1.strip())
print(t1.split())
print(t2.replace("wo","lo"))

print("=== форматирование строки ===")

t4 = "It's a {l1}".format(l1="string")
t5 = "{0} {1}".format("Hello" , 23)
print(t4)
print(t5)

