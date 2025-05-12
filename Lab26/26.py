import sklearn
import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

#Набор данных с двух классовой классификацией, в котором классы линейно
# неразделимы

X, y = make_blobs(centers=4, random_state=8)
y = y % 2
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()

# Линейная модель классификации может отделить точки только с помощью прямой линии
# и не может дать хорошее качество для этого набора данных

from sklearn.svm import LinearSVC
linear_svm = LinearSVC().fit(X, y)
mglearn.plots.plot_2d_separator(linear_svm, X)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mglearn

#  Расширение набора данных, показанного на рис. 2, за счет добавления третьего
# признака, полученного на основе признака 1

# В новом представлении данных уже можно отделить два класса друг от друга, используя
# линейную модель, плоскость в трехмерном пространстве. Мы можем убедиться в этом, подогнав
# линейную модель к дополненным данным

# Добавляем квадрат второго признака как третье измерение
X_new = np.hstack([X, X[:, 1:] ** 2])

# Создаём 3D-график
figure = plt.figure()
ax = figure.add_subplot(111, projection='3d')
ax.view_init(elev=-152, azim=-26)  # Угол обзора

# Разделяем данные по классам
is_class_0 = (y == 0)

# Визуализация (с явными цветами)
ax.scatter(
    X_new[is_class_0, 0], X_new[is_class_0, 1], X_new[is_class_0, 2],
    c='blue', s=60, label='Класс 0'
)
ax.scatter(
    X_new[~is_class_0, 0], X_new[~is_class_0, 1], X_new[~is_class_0, 2],
    c='red', marker='^', s=60, label='Класс 1'
)

# Подписи осей
ax.set_xlabel("Признак 0")
ax.set_ylabel("Признак 1")
ax.set_zlabel("Признак 1²")

# Легенда (если нужно)
ax.legend()

plt.show()


# Граница принятия решений, найденная линейным SVM для расширенного
# трехмерного набора данных

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.svm import LinearSVC
import mglearn

# Обучение модели SVM на 3D-данных
linear_svm_3d = LinearSVC().fit(X_new, y)
coef, intercept = linear_svm_3d.coef_.ravel(), linear_svm_3d.intercept_

# Создание 3D-графика
figure = plt.figure()
ax = figure.add_subplot(111, projection='3d')
ax.view_init(elev=-152, azim=-26)  # Угол обзора

# Построение разделяющей гиперплоскости
xx = np.linspace(X_new[:, 0].min() - 2, X_new[:, 0].max() + 2, 50)
yy = np.linspace(X_new[:, 1].min() - 2, X_new[:, 1].max() + 2, 50)
XX, YY = np.meshgrid(xx, yy)
ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]

# Визуализация гиперплоскости (полупрозрачная)
ax.plot_surface(XX, YY, ZZ, rstride=8, cstride=8, alpha=0.3, color='gray')

# Разделение данных по классам
is_class_0 = (y == 0)

# Точечная визуализация (с явными цветами)
ax.scatter(
    X_new[is_class_0, 0], X_new[is_class_0, 1], X_new[is_class_0, 2],
    c='blue', s=60, label='Класс 0'
)
ax.scatter(
    X_new[~is_class_0, 0], X_new[~is_class_0, 1], X_new[~is_class_0, 2],
    c='red', marker='^', s=60, label='Класс 1'
)

# Подписи осей
ax.set_xlabel("Признак 0")
ax.set_ylabel("Признак 1")
ax.set_zlabel("Признак 1²")

# Легенда
ax.legend()

plt.show()

# Фактически модель линейного SVM как функция исходных признаков не является больше
# линейной. Это скорее эллипс, как можно увидеть на графике, построенном ниже


ZZ = YY**2
dec = linear_svm_3d.decision_function(np.c_[XX.ravel(), YY.ravel(), ZZ.ravel()])
plt.contourf(XX, YY, dec.reshape(XX.shape), levels=[dec.min(), 0, dec.max()],
 cmap=mglearn.cm2, alpha=0.5)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()


# В ходе обучения SVM вычисляет важность каждой точки обучающих данных с точки зрения
# определения решающей границы между двумя классами. Обычно лишь часть точек обучающего
# набора важна для определения границы принятия решений: точки, которые лежат на границе
# между классами. Они называются опорными векторами (support vectors) и дали свое название
# машине опорных векторов.


# Чтобы получить прогноз для новой точки, измеряется расстояние до каждого опорного
# вектора.

# . Классификационное решение принимается, исходя из расстояний до опорных векторов, а
# также важности опорных векторов, полученных в процессе обучения (хранятся в атрибуте
# dual_coef_ к

from sklearn.svm import SVC
X, y = mglearn.tools.make_handcrafted_dataset()
svm = SVC(kernel='rbf', C=10, gamma=0.1).fit(X, y)
mglearn.plots.plot_2d_separator(svm, X, eps=.5)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
sv = svm.support_vectors_
sv_labels = svm.dual_coef_.ravel() > 0
mglearn.discrete_scatter(sv[:, 0], sv[:, 1], sv_labels, s=15, markeredgewidth=3)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()

# Параметр gamma – это параметр формулы,
# Параметр С представляет собой параметр регуляризации, аналогичный тому, что
# использовался в линейных моделях.

fig, axes = plt.subplots(3, 3, figsize=(15, 10))
for ax, C in zip(axes, [-1, 0, 3]):
    for a, gamma in zip(ax, range(-1, 2)):
        mglearn.plots.plot_svm(log_C=C, log_gamma=gamma, ax=a)

axes[0, 0].legend(["class 0", "class 1", "sv class 0", "sv class 1"], ncol=4,
loc=(.9, 1.2))
plt.show()


#  Диапазоны значений признаков для набора данных Breast Cancer (обратите
# внимание, что ось у имеет логарифмическую шкалу)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
 cancer.data,
 cancer.target,
 random_state=0
)
svc = SVC()
svc.fit(X_train, y_train)
print("Правильность на обучающем наборе: {:.2f}".format(
 svc.score(X_train, y_train)
))
print("Правильность на тестовом наборе: {:.2f}".format(
 svc.score(X_test, y_test)
))
plt.show()
plt.plot(X_train.min(axis=0), 'o', label="min")
plt.plot(X_train.max(axis=0), '^', label="max")
plt.legend(loc=4)
plt.xlabel("Индекс признака")
plt.ylabel("Величина признака")
plt.yscale("log")
plt.show()

min_on_training = X_train.min(axis=0)
range_on_training = (X_train - min_on_training).max(axis=0)
X_train_scaled = (X_train - min_on_training) / range_on_training

import numpy as np
from sklearn.svm import SVC

# Масштабирование данных
X_train_scaled = (X_train - min_on_training) / range_on_training
X_test_scaled = (X_test - min_on_training) / range_on_training

# Вывод минимальных и максимальных значений (исправлено)
print("Минимальное значение для каждого признака:\n", np.round(X_train_scaled.min(axis=0), 3))
print("Максимальное значение для каждого признака:\n", np.round(X_train_scaled.max(axis=0), 3))

# Обучение модели SVC (C=1 по умолчанию)
svc = SVC()
svc.fit(X_train_scaled, y_train)
print("Правильность на обучающем наборе: {:.3f}".format(svc.score(X_train_scaled, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(svc.score(X_test_scaled, y_test)))

# Обучение модели SVC с C=1000 (более жесткая регуляризация)
svc = SVC(C=1000)
svc.fit(X_train_scaled, y_train)
print("Правильность на обучающем наборе (C=1000): {:.3f}".format(svc.score(X_train_scaled, y_train)))
print("Правильность на тестовом наборе (C=1000): {:.3f}".format(svc.score(X_test_scaled, y_test)))
# Проверяем масштабирование
print("Минимальное значение для каждого признака:", X_train_scaled.min(axis=0))
print("Максимальное значение для каждого признака:", X_train_scaled.max(axis=0))

# Обучаем модель SVC (C=1 по умолчанию)
svc = SVC()
svc.fit(X_train_scaled, y_train)
print("Правильность на обучающем наборе (C=1): {:.3f}".format(svc.score(X_train_scaled, y_train)))
print("Правильность на тестовом наборе (C=1): {:.3f}".format(svc.score(X_test_scaled, y_test)))

# Обучаем модель SVC (C=1000)
svc = SVC(C=1000)
svc.fit(X_train_scaled, y_train)
print("Правильность на обучающем наборе (C=1000): {:.3f}".format(svc.score(X_train_scaled, y_train)))
print("Правильность на тестовом наборе (C=1000): {:.3f}".format(svc.score(X_test_scaled, y_test)))

