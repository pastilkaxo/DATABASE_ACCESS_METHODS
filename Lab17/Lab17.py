# Предположим, что ботаник-любитель хочет классифицировать сорта ирисов,
# которые он собрал. Он измерил в сантиметрах некоторые характеристики
# ирисов: длину и ширину лепестков, а также длину и ширину чашелистиков

# Наша цель заключается в построении модели машинного обучения, которая
# сможет обучиться на основе характеристик ирисов, уже классифицированных
# по сортам, и затем предскажет сорт для нового цветка ириса

#  setosa, versicolor, virginica

# Задача Трёхклассовой Классификация:
# Возможный Ответ (сорт ириса) - класс
#  Метка - сорт к которому принадлежит цветок

import sys
import pandas as pd
import numpy as np
import mglearn
import matplotlib
import scipy as sp
import matplotlib.pyplot as plt
import IPython
import sklearn
from sklearn.datasets import load_iris

# iris - набор данных в ml , загрузка:
iris_dataset = load_iris() # возвр. Bunch - структура типа ключ_значение (словарь)
print("========= Ключи Iris: =========\n{}".format(iris_dataset.keys()))
print("========= Описание набора данных [DESCR]: =========\n{}".format(iris_dataset['DESCR']))
print("========= Названия Сортов: =========\n{}".format(iris_dataset.target_names)) # target_names - массив строк предсказания
print("========= Описание каждого признака: =========\n{}".format(iris_dataset.feature_names))

#  data - массив NumPy, содержит количественные измерения длины и ширины

print("========= Тип Data: =========\n{}".format(type(iris_dataset.data)))
print("========= Тип Target: =========\n{}".format(type(iris_dataset.target)))

# Форма = строки - примеры * столбцы - признаки
print("========= Форма Data: =========\n{}".format(iris_dataset.data.shape))
print("========= Признаки первых 5: =========\n{}".format(iris_dataset.data[:5]))

# target - массив измеренных сортов, по 1 элементу на каждый цветок
print("========= Форма Target: =========\n{}".format(iris_dataset.target.shape))
# Сорта закодированы, 0 - setosa, 1 - versicolor, 3- virginica
print("========= Target: =========\n{}".format(iris_dataset.target))

#  модель машинног о обучения,
# которая предскажет сорта ириса для нового набора измерений

# просто запомнит весь обучающий набор и поэтому она
# всегда будет предсказывать правильную метку для любой точки данных в
# обучающем наборе

# действия для оценки эфф-сти модели:
# 1) Разбиваем размеченные данные на 2 части ( 150 )
# 2)  1 часть training data(set) - для построения модели машинного обучения
# 3)  2 часть test data(set)- для оценки качества модели

from sklearn.model_selection import train_test_split
# перемешивает набор данных и разбивает его на 2 части
# 1 часть 75% 2 часть 25%
# X - данные Y - метки
# перемешиваем наши данные, чтобы тестовые данные содержали все три класса.

# обучающие данные, обучающие метки, тестовые данные, тестовые метки, генератор  псевдослучайных чисел
X_train, X_test, y_train, y_test = train_test_split(iris_dataset.data,iris_dataset.target,random_state=0)

print("========= X_train Shape: =========\n{}".format(X_train.shape))
print("========= y_train Shape: =========\n{}".format(y_train.shape))
print("========= X_test Shape: =========\n{}".format(X_test.shape))
print("========= y_test Shape: =========\n{}".format(y_test.shape))


# просмотр данных - способ обнаружить
# аномалии и особенности

# scatter plot - признаки раскладываются по Х и У и каждому соответсует точка (только 2-3 признака на экране)
# scatter plot matrix ,pair plots -    ! не
# показывает взаимодействие между всеми признаками сразу


# создаем dataframe из данных X_train
# макеруем столбцы с помощью iris_dataset_fetures_names
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
print("========= iris_dataframe Shape: =========\n{}".format(iris_dataframe))

from pandas.plotting import scatter_matrix

# создаем матрицу рассеяния из df, y_train - цвет точек
grr = scatter_matrix(
    iris_dataframe, # данные для построения
    c=y_train, # цвеи точек
    figsize=(25, 25), # размер матрицы
    marker='o', # стиль маркера
    hist_kwds=dict(bins=20), # параметры гистограммы
    s=60, # размер маркера
    alpha=0.8, # прозрачность маркера
    cmap=mglearn.cm3, # цветовая карта для точек
)
plt.show()


# диагональ - гистограммы каждого признака
# точки данных окрашены в соответсвии с сортами

