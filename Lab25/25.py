import sklearn
import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons


X, y = make_moons(n_samples=100, noise=0.25, random_state=3)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
forest = RandomForestClassifier(n_estimators=5, random_state=2) # Создаём случайный лес из 5 деревьев (n_estimators=5).
forest.fit(X_train, y_train) # Обучаем его на тренировочных данных


fig, axes = plt.subplots(2, 3, figsize=(20, 10))
for i, (ax, tree) in enumerate(zip(axes.ravel(), forest.estimators_)): # Рисуем каждое дерево отдельно — видим, как каждое дерево делит пространство.
 ax.set_title("Дерево {}".format(i))
 mglearn.plots.plot_tree_partition(X_train, y_train, tree, ax=ax)
 mglearn.plots.plot_2d_separator(forest, X_train, fill=True, ax=axes[-1, -1], alpha=.4)  # В последнем подграфике рисуем решающую границу всего случайного леса.
axes[-1, -1].set_title("Случайный лес")
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.show()

# случайный лес переобучается в меньшей степени и дает
# гораздо более чувствительную (гибкую) границу принятия решений. В реальных примерах
# используется гораздо большее количество деревьев (часто сотни или тысячи), что приводит к
# получению еще более чувствительной границы.


# 100 деревьев

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)
print("1 Правильность на обучающем наборе: {:.3f}".format(forest.score(X_train, y_train)))
print("1 Правильность на тестовом наборе: {:.3f}".format(forest.score(X_test, y_test)))


# позволят вычислить важности признаков, которые
# рассчитываются путем агрегирования значений важности по всем деревьям леса

def plot_feature_importances_cancer(model):
 n_features = cancer.data.shape[1]
 plt.barh(range(n_features), model.feature_importances_, align='center')
 plt.yticks(np.arange(n_features), cancer.feature_names)
 plt.xlabel("Важность признака")
 plt.ylabel("Признак")
 plt.show()


plot_feature_importances_cancer(forest)


# Градиентный бустинг деревьев регрессии – еще один ансамблевый метод, который
# объединяет в себе множество деревьев для создания более мощной модели.

#Основная идея градиентного бустинга заключается в объединении множества простых
# моделей (в данном контексте известных под названием слабые ученики или weak learners),
# деревьев небольшой глубины. Каждое дерево может дать хорошие прогнозы только для части
# данных и таким образом для итеративного улучшения качества добавляется все большее
# количество деревьев.


from sklearn.ensemble import GradientBoostingClassifier
X_train, X_test, y_train, y_test = train_test_split( cancer.data, cancer.target, random_state=0)

#Ансамбли (ensembles)  – это методы, которые сочетают в себе множество моделей машинного обучения
#  learning_rate, который контролирует, насколько сильно
# каждое дерево будет пытаться исправить ошибки предыдущих деревьев

gbrt = GradientBoostingClassifier(random_state=0)
gbrt.fit(X_train, y_train)
print("2 Правильность на обучающем наборе: {:.3f}".format(gbrt.score(X_train, y_train)))
print("2 Правильность на тестовом наборе: {:.3f}".format(gbrt.score(X_test, y_test)))

gbrt = GradientBoostingClassifier(random_state=0, max_depth=1)
gbrt.fit(X_train, y_train)
print("3 Правильность на обучающем наборе: {:.3f}".format(gbrt.score(X_train, y_train)))
print("3 Правильность на тестовом наборе: {:.3f}".format(gbrt.score(X_test, y_test)))

gbrt = GradientBoostingClassifier(random_state=0, learning_rate=0.01)
gbrt.fit(X_train, y_train)
print("4 Правильность на обучающем наборе: {:.3f}".format(gbrt.score(X_train, y_train)))
print("4 Правильность на тестовом наборе: {:.3f}".format(gbrt.score(X_test, y_test)))


