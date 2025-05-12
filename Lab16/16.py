from operator import index
import sympy as sp
import numpy as np
import mglearn
import random
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split





# 2.	Используя возможности SymPy - библиотека для символьных вычислений,
# работа с производными, интегралами, пределами и алгебраическими выражениям:
# 2.1.	Найдите производную функции f(x) = x2 + 1;

x = sp.Symbol('x')
f = x**2 + 1
r1 = sp.diff(f,x)
print("1# Производная = ",r1)


# 2.2.	Найдите интеграл функции f(x) = x2 + 1 на отрезке [0, 1];

r2 = sp.integrate(f,(x,0,1))
print("Интеграл = ",r2)

# 2.3.	Найдите предел функции f(x) = 1/x2 + 1 при x→∞.
inf = sp.oo
f2 = (1/x**2)+1
r3 = sp.limit(f2,x,inf)
print("Предел =",r3)

#3.	Используя возможности NumPy - библиотека для работы с массивами и линейной алгеброй:
#3.1.	создайте одномерный массив из 20 целых случайных чисел;

arr = np.random.randint(1,10,20)
print("одномерный массив = ",arr)

#3.2.	преобразуйте созданный массив в двумерный массив размером [4,5];

arr2d = np.reshape(arr,(4,5))
print("двумерный массив\n",arr2d)


#3.3.	разделите полученный массив на 2 массива;

arr1 ,arr2 = np.array_split(arr2d,2)
print("Arr1 = ",arr1)
print("Arr2 = ",arr2)

#3.4.	найдите все заданные значения в первом массиве (например, равные 6);

n = np.where(arr1 == 6)
if n != None:
    print("Value:",
    arr1[n]," Index:" , n)
else:
    print("No 6")

#3.5.	подсчитайте количество найденных элементов;

c = np.sum(arr1 == 6)
print(c)

#3.6.	во втором массиве найдите мин, макс и среднее;

max = np.max(arr2)
min = np.min(arr2)
avg = np.mean(arr2)
print("Max:",max)
print("Min:",min)
print("Avg:",avg)

#4.	Используя возможности Pandas - библиотека для анализа данных, работа с таблицами (DataFrame) и сериями (Series).:
#4.1.	Изучите структуры данных Series и Dataframe;
#4.2.	создайте объекты Series из массива NumPy, из словаря;

arr3 = np.arange(1,4)

s1 = pd.Series(arr3,index=["x","y","z"])
print("Series (array):\n",s1)

users = {1:['user 1', 20], 2:['user 2', 21], 3:['user 3', 22]}

s2 = pd.Series(users)
print("Series (Dictionary):\n",s2)

print("Indexes:",s2[2] ," x:", s1['x'])
#4.3.	произведите с ним различные математические операции;

print("s1 max:",s1.max())
print("s1 min:",s1.min())
print("s1 avg:",s1.mean())
print("s1 sum:",s1.sum())

#4.4.	создайте объекты Dataframe из массива NumPy, словаря и объекта Series;

mat = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(mat)
print("DataFrame:\n",df)

users = {'hostname':['user 1', 'user 2','user 3'], 'age':[20, 21,31]}

df2 = pd.DataFrame(users,index=['u1','u2','u3'])
print("DF2:\n",df2)

df3 = pd.DataFrame(s1)
print("DF3:\n",df3)

#5.	Продемонстрируйте работу с пакетом Matplotlib - библиотека для построения графиков:
#5.1.	Постройте график функции f(x) = x2 + 1;
print("Matplotlib")
xpoints=[]
ypoints=[]

for x in range(-3,4,1):
    y = x**2 +1
    xpoints.append(x)
    ypoints.append(y)
plt.plot(xpoints,ypoints)
plt.title("График f(x) = x^2 + 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()


#5.2.	Постройте график поверхности функции f(x, y) = x2 + 2y2 + 1;

xplots = np.linspace(-5,5,100) # Создаем 100 точек для X
yplots = np.linspace(-5,5,100) # Создаем 100 точек для Y
X,Y = np.meshgrid(xplots,yplots) # Создаем сетку значений
Z = X**2 + 2*(Y**2) + 1

fig = plt.figure() # Создаем фигуру
ax_3d = fig.add_subplot(111, projection='3d') # Добавляем 3D-график
ax_3d.plot_surface(X,Y,Z)  # Строим 3D-поверхность
plt.title("График поверхности f(x, y) = x^2 + 2y^2 + 1")
plt.show()


#5.3.	Постройте несколько видов диаграмм;

#1
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y, color='r' , width=0.25)
plt.show()

#2

x = np.random.normal(170, 10, 250)
plt.hist(x,bins=10)
plt.show()

#3

y = np.array([25,25,45,5])
l = ['Cargo 1','Cargo2','Cargo3','Cargo4']
plt.pie(y,labels=l,shadow=True)
plt.legend(title ='Круговая')
plt.show()

#6.	Установите следующие пакеты и ознакомьтесь, для чего они предназначены:

#6.1.	Scipy

# SciPy (Scientific Python) — это библиотека для научных вычислений, расширяющая возможности NumPy. Она включает в себя:
# Линейную алгебру (scipy.linalg)
# Оптимизацию (scipy.optimize)
# Интерполяцию (scipy.interpolate)
# Обработку сигналов (scipy.signal)
# Статистику (scipy.stats)
# Решение дифференциальных уравнений (scipy.integrate)

x = np.array([0, 1, 2, 3])
y = np.array([0, 2, 4, 8])
f = interp1d(x, y, kind='linear')  # Линейная интерполяция
print(f(1.5))  # 3.0


#6.2.	IPython

# IPython — это интерактивная оболочка Python, обеспечивающая:
#
# Улучшенную автодополненную консоль
# Поддержку работы с Jupyter Notebook
# Поддержку работы с визуализациями
# Расширенные возможности отладки

#6.3.	Sklearn

# Scikit-learn — это мощная библиотека машинного обучения, включающая в себя:
#
# Методы классификации, регрессии и кластеризации
# Поддержку работы с данными (например, разбиение на обучающую и тестовую выборки)
# Оценку качества моделей
# Визуализацию результатов

# Логистическая регрессия на наборе данных

iris = load_iris() # Загружаем данные
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
#iris.data — признаки (размер лепестков и чашелистиков).
#iris.target — классы (0, 1, 2 → три вида ирисов).
#test_size=0.2 — 20% данных отводится на тест, 80% — на обучение.
#random_state=42 — фиксируем случайность для воспроизводимости.


model = LogisticRegression(max_iter=200) # Создаем модель логистической регрессии
#max_iter=200 — количество итераций для оптимизации модели.

model.fit(X_train, y_train) # Обучаем модель
print(model.score(X_test, y_test))  # Оценка точности модели

#6.4.	Mglearn

# Mglearn — это вспомогательная библиотека для визуализации и обучения Scikit-learn. Она содержит:
#
# Графические примеры работы алгоритмов машинного обучения
# Демонстрационные наборы данных
# Инструменты для удобной визуализации результатов

X, y = make_moons(n_samples=100, noise=0.1, random_state=42) # Генерируем набор данных (две группы точек в форме полумесяцев).
#make_moons(n_samples=100, noise=0.1)
#Создает 100 точек с двумя классами (красные и синие).
#noise=0.1 — добавляет случайный шум (разброс точек).
#random_state=42 — фиксируем случайност

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Разбивает данные на обучающую (80%) и тестовую (20%) выборку.

model = SVC(kernel='rbf', C=10, gamma=0.1) # Обучаем SVM (метод опорных векторов) с радиальным базисным ядром (rbf).
#C=10 — увеличиваем штраф за ошибки (более сложная граница разделения).
#gamma=0.1 — управляет размером влияния точек на границу.

model.fit(X_train, y_train) # Обучаем модель,Разбиваем его на обучающую и тестовую выборки.

mglearn.plots.plot_2d_separator(model, X_train, fill=True)  # Визуализируем границу решений
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k') # Рисуем границу разделения классов.
plt.show()