import mglearn
import sklearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs


# Общераспространненный подход, позволяющий распространить
# алгоритм бинарной классификации на случай мультиклассовой классификации называет подходом
# один против остальных (one-vs.-rest). В подходе «один против остальных» для каждого класса
# строится бинарная модель, которая пытается отделить этот класс от всех остальных, в результате
# чего количество моделей определяется количеством классов. Для получения прогноза точка
# тестового набора подается на все бинарные классификаторы. Классификатор, который выдает по
# своему классу наибольшее значение, «побеждает» и метка этого класса возвращается в качестве
# прогноза.

X, y = make_blobs(random_state=42)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.legend(["Класс 0", "Класс 1", "Класс 2"])
plt.show()

# 𝑤[0]∗𝑥[0]	𝑤[1]∗𝑥[1] … 𝑤[𝑝]∗𝑥[𝑝] 𝑏

from sklearn.svm import LinearSVC
linear_svm = LinearSVC().fit(X, y)
print("Форма коэффициента: ", linear_svm.coef_.shape)
print("Форма константы: ", linear_svm.intercept_.shape)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
line = np.linspace(-15, 15)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, ['b', 'r', 'g']):
 plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
plt.ylim(-10, 15)
plt.xlim(-10, 8)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.legend(['Класс 0', 'Класс 1', 'Класс 2', 'Линия класса 0', 'Линия класса 1', 'Линия класса 2'], loc=(1.01, 0.3))
plt.show()


mglearn.plots.plot_2d_classification(linear_svm, X, fill=True, alpha=.7)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
line = np.linspace(-15, 15)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, ['b', 'r', 'g']):
 plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
plt.legend(['Класс 0', 'Класс 1', 'Класс 2', 'Линия класса 0', 'Линия класса 1',
'Линия класса 2'], loc=(1.01, 0.3))
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()