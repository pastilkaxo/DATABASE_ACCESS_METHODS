import mglearn
import sklearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB

# они имеют тенденцию обучаться быстрее. Цена, которую приходится платить за такую
# эффективность – немного более низкая обобщающая способность моделей Байеса по сравнению
# с линейными классификаторами
# они оценивают параметры, рассматривая каждый признак отдельно и по каждому признаку
# собирают простые статистики классов.
#  В scikit-learn реализованы три вида наивных байесовских
# классификаторов: GaussianNB, BernoulliNB и MultinomialNB. GaussianNB можно применить к
# любым непрерывным данным, в то время как BernoulliNB принимает бинарные данные,
# MultinomialNB принимает счетные или дискретные данные
# BernoulliNB и MultinomialNB в основном
# используются для классификации текстовых данных.


# Классификатор BernoulliNB
X = np.array([[0, 1, 0, 1], [1, 0, 1, 1], [0, 0, 0, 1], [1, 0, 1, 0]])
y = np.array([0, 1, 0, 1])
counts = {}
for label in np.unique(y):
 counts[label] = X[y == label].sum(axis=0)
print("Частоты признаков:\n{}".format(counts))
clf = BernoulliNB()
clf.fit(X, y)
print(clf.predict(X[2:3]))

# MultinomialNB принимает в расчет среднее значение
# каждого признака для каждого класса, в то время как GaussianNB записывает среднее значение, а
# также стандартное отклонение каждого признака для каждого класса.

# Классификатор MultinomialNB
rng = np.random.RandomState(1)  # создается объект случайного числа с фиксированным начальным значением
X = rng.randint(5, size=(6, 100)) # 0 - 4
y = np.array([1, 2, 3, 4, 5, 6]) # метки классов
clf = MultinomialNB()
clf.fit(X, y)
print(clf.predict(X[2:3]))

# Классификатор GaussianNB
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[-0.8, -1]]))
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
print(clf_pf.predict([[-0.8, -1]]))