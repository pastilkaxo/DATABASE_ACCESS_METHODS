# Алгоритм К ближайших соседей


import pandas as pds
import mglearn
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_iris

iris_dataset = load_iris()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

print("форма массива X_train: {}".format(X_train.shape))
print("форма массива y_train: {}".format(y_train.shape))
print("форма массива X_test: {}".format(X_test.shape))
print("форма массива y_test: {}".format(y_test.shape))

iris_dataframe = pds.DataFrame(X_train, columns=iris_dataset.feature_names)

from pandas.plotting import scatter_matrix

grr = scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                     hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)


# Построение этой
# модели заключается лишь в запоминании обучающего набора. Для того,
# чтобы сделать прогноз для новой точки данных, алгоритм находит точку в
# обучающем наборе, которая находится ближе всего к новой точке. Затем он
# присваивает метку, принадлежащую этой точке обучающего набора, новой
# точке данных.

# К может быть много

from sklearn.neighbors import KNeighborsClassifier # Классификатор метода К ближ. соседей.
knn = KNeighborsClassifier( ## knn - алгоритм, который будет использоваться для построения модели
algorithm='auto', # Алгоритм для вычисления ближайших соседей.
leaf_size=30, # Размер листа в деревьях
metric='minkowski', #  Метрика расстояния между объектами.
metric_params=None,
n_jobs=1, # : Количество ядер CPU для параллельных вычислений.
n_neighbors=1, # Количество соседей (k), учитываемых при классификации.
p=2, # евклидово расстояние
weights='uniform' # Определяет, как учитываются веса соседей. 'uniform' → все соседи имеют одинаковый вес.
)

# Алгоритм запоминает все обучающие данные.
# Для нового объекта находит k ближайших соседей (по выбранной метрике расстояния).
# Класс определяется голосованием (либо учитываются веса соседей).


knn.fit(X_train, y_train) # строим нашу модель классификации на обуч. наборе

X_new = np.array([[5, 2.9, 1, 0.2]])
print("форма массива X_new: {}".format(X_new.shape))

prediction = knn.predict(X_new) # прогноз

print("Прогноз класса: {}".format(prediction))
print("Спрогнозированная метка: {}".format(
iris_dataset['target_names'][prediction])
)

# Таким образом, мы можем сделать прогноз для каждого ириса в
# тестовом наборе и сравнить его с фактической меткой (уже известным
# сортом). Мы можем оценить качество модели, вычислив правильность
# (accuracy) – процент цветов, для которых модель правильно спрогнозировала
# сорта:

y_pred = knn.predict(X_test)
print("Прогнозы для тестового набора:\n {}".format(y_pred))
print("Правильность на тестовом наборе: {:.2f}".format(np.mean(y_pred == y_test)))
print("Правильность на тестовом наборе: {:.2f}".format(knn.score(X_test, y_test))) # вычисляет правильность модели для тестового набора

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print("Правильность на тестовом наборе: {:.2f}".format(knn.score(X_test, y_test)))