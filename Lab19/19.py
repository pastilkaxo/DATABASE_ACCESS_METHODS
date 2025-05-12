import sklearn
import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer, fetch_california_housing, fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

#
# #рассмотрим наиболее популярные алгоритмы машинного обучения и
# объясним, как они обучаются на основе данных и как вычисляют прогнозы.
#


# 1) Набор данных

# генерируем набор данных
# строим график для набора данных

# Примером синтетического набора данных для двухклассовой классификации
# является набор данных forge, который содержит два признака.

#  создает диаграмму рассеяния  визуализируя все точки
# данных в этом наборе. На графике первый признак отложен на оси х, а второй – по оси у.
# Как это всегда бывает в диаграммах рассяения, каждая точка данных представлена в виде
# одного маркера.

# для классификации

X, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Класс 0", "Класс 1"], loc=4)
plt.xlabel("Первый признак")
plt.ylabel("Второй признак")
print("форма массива X: {}".format(X.shape))
plt.show()

# Для иллюстрации алгоритмов регрессии, мы воспользуемся синтетическим
# набором wave. Набор данных имеет единственный входной признак и непрерывную
# целевую переменную или отклик (response), который мы хотим смоделировать. На
# рисунке, построенном здесь (рис. 2.3), по оси x располагается единственный признак,
# а по оси y – целевая переменная (ответ).

X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Признак")
plt.ylabel("Целевая переменная")
plt.show()

# Мы дополним эти небольшие синтетические наборы данных двумя реальными
# наборами, которые включены в scikit-learn. Один из них – набор данных по раку молочной
# железы Университета Висконсин (cancer для краткости),


# на основании измерений ткани дать
# прогноз, является ли опухоль злокачественной.
# !!! Для классификации

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("Ключи cancer(): \n{}".format(cancer.keys()))
# Набор данных включает 569 точек данных и 30 признаков.
print("Форма массива data для набора cancer: {}".format(cancer.data.shape))

# Из 569 точек данных 212 помечены как злокачественные, а 357 как доброкачественные.
print("Количество примеров для каждого класса:\n{}".format(
    {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))

# Чтобы получить содержательное описание каждого признака, взглянем на атрибут
#feature_names:
print("Имена признаков:\n{}".format(cancer.feature_names))


# !!! для регрессии спрогнозировать медианную стоимость домов в нескольких районах
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
print("форма массива data для набора California: {}".format(housing.data.shape))
from sklearn.datasets import fetch_openml
housing = fetch_openml(name="house_prices", as_frame=True)


# Алгоритм k ближайших соседей, возможно, является самым простым алгоритмом
# машинного обучения. Построение модели заключается в запоминании обучающего
# набора данных. Для того, чтобы сделать прогноз для новой точки данных, алгоритм
# находит ближайшие к ней точки обучающего набора, то есть находит «ближайших
# соседей».

# Прогнозы, полученные для набора данных forge с помощью модели
# одного ближайшего соседа
mglearn.plots.plot_knn_classification(n_neighbors=1)
plt.show()

# Здесь мы добавили три новые точки данных, показанные в виде звездочек. Для
# каждой мы отметили ближайшую точку обучающего набора. Прогноз, который дает
# алгоритм одного ближайшего соседа – метка этой точки (показана цветом маркера).

# --------------------------

# произвольное количество (k) соседей.

mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.show()

# Когда мы рассматриваем более одного соседа, для
# присвоения метки используется голосование (voting).
#  для каждой точки
# тестового набора мы подсчитываем количество соседей, относящихся к классу 0, и
# количество соседей, относящихся к классу 1. Затем мы присваиваем точке тестового
# набора наиболее часто встречающийся класс: другими словами, мы выбираем класс,
# набравший большинство среди k ближайших соседей.


# mультиклассовой классификации мы подсчитываем количество соседей, принадлежащих к
# каждому классу, и снова прогнозируем наиболее часто встречающийся класс


# ------------------------

# разделим наши данные на обучающий и тестовый
# наборы, чтобы оценить обобщающую способность модели

from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


#импорт и создаем объект-экземпляр класса

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
#  запоминание набора данных
clf.fit(X_train, y_train)
print("Прогнозы на тестовом наборе: {}".format(clf.predict(X_test)))
print("Правильность на тестовом наборе: {:.2f}".format(clf.score(X_test, y_test)))

# 2) Анализ KNeughborsClassifier

#  показать прогнозы для
# всех возможных точек тестового набора, разместив в плоскости ху. Мы зададим цвет
# плоскости в соответствии с тем классом, который будет присвоен точке в этой области.
# Это позволит нам сформировать границу принятия решений (decision boundary), которая
# разбивает плоскость на две области: область, где алгоритм присваивает класс 0, и
# область, где алгоритм присваивает класс 1.


fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for n_neighbors, ax in zip([1, 3, 9], axes):
# создаем объект-классификатор и подгоняем в одной строке
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("количество соседей:{}".format(n_neighbors))
    ax.set_xlabel("признак 0")
    ax.set_ylabel("признак 1")
axes[0].legend(loc=3)
plt.show()


# ------------

# существует ли взаимосвязь между сложностью модели и
# обобщающей способностью

#  разобьем данные на обучающий и
# тестовый наборы. Затем мы оценим качество работы модели на обучающем и тестовом
# наборах с использованием разного количества соседей

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=66)

training_accuracy = []
test_accuracy = []

# пробуем n_neighbors от 1 до 10
neighbors_settings = range(1, 11)

for n_neighbors in neighbors_settings:
    # строим модель
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    # записываем правильность на обучающем наборе
    training_accuracy.append(clf.score(X_train, y_train))
    # записываем правильность на тестовом наборе
    test_accuracy.append(clf.score(X_test, y_test))

plt.plot(neighbors_settings, training_accuracy, label="правильность на обучающем наборе")
plt.plot(neighbors_settings, test_accuracy, label="правильность на тестовом наборе")
plt.ylabel("Правильность")
plt.xlabel("количество соседей")
plt.legend()
plt.show()



# 3) Регрессия k ближайших соседий

mglearn.plots.plot_knn_regression(n_neighbors=1)
plt.show()


mglearn.plots.plot_knn_regression(n_neighbors=3)
plt.show()


# Алгоритм регрессии k ближайших соседей реализован в классе
# KNeighborsRegressor

from sklearn.neighbors import KNeighborsRegressor
X, y = mglearn.datasets.make_wave(n_samples=40)
# разбиваем набор данных wave на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# создаем экземпляр модели и устанавливаем количество соседей равным 3
reg = KNeighborsRegressor(n_neighbors=3)
#подгоняем модель с использованием обучающих данных и обучающих ответов
reg.fit(X_train, y_train)
#получим прогнозы для тестового набора
print("Прогнозы для тестового набора:\n{}".format(reg.predict(X_test)))

#  качество модели  R2, также известный как коэффициент
# детерминации, является показателем качества регрессионной модели и принимает
# значения от 0 до 1. Значение 1 соответствует идеальной прогнозирующей способности, а значение 0 соответствует константе модели, которая лишь предсказывает среднее
# значение ответов в обучающем наборе, y_train:
print("R^2 на тестовом наборе: {:.2f}".format(reg.score(X_test, y_test)))


# 4) Анализ модели KNeighborsRegressor

# Применительно к нашему одномерному массиву данных мы можем увидеть
# прогнозы для всех возможных значений признаков

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
line = np.linspace(-3, 3, 1000).reshape(-1, 1)
for n_neighbors, ax in zip([1, 3, 9], axes):
    reg = KNeighborsRegressor(n_neighbors=n_neighbors)
    reg.fit(X_train, y_train)
    ax.plot(line, reg.predict(line))
    ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
    ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)
    ax.set_title(
        "{} neighbor(s)\n train score: {:.2f} test score: {:.2f}".format(
        n_neighbors, reg.score(X_train, y_train), reg.score(X_test, y_test)))
    ax.set_xlabel("Признак")
    ax.set_ylabel("Целевая переменная")
axes[0].legend(["Прогнозы модели", "Обучающие данные/ответы","Тестовые данные/ответы"], loc="best")
plt.show()


# Как видно на графике, при использовании лишь одного соседа каждая точка
# обучающего набора имеет очевидное влияние на прогнозы, и предсказанные значения
# проходят через все точки данных. Это приводит к очень неустойчивым прогнозам.
# Увеличение числа соседей приводит к получению более сглаженных прогнозов, но при
# этом снижается правильность подгонки к обучающим данным. 