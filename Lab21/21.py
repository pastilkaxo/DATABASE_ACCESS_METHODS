import mglearn
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC



# yˆ 𝑤[0]∗𝑥[0]	𝑤[1]∗𝑥[1] … 𝑤[𝑝]∗𝑥[𝑝] 𝑏
#  для прогнозируемого значения
# порог, равный нулю. Если функция меньше нуля, мы прогнозируем класс –1, если она больше
# нуля, мы прогнозируем класс +1.
#

# Для линейных
# моделей классификации граница принятия решений (decision boundary) является линейной
# функцией аргумента. Другими словами, (бинарный) линейный классификатор – это
# классификатор, который разделяет два класса с помощью линии, плоскости или гиперплоскости. В
# этом разделе мы приведем кокретные примеры.

# Двумя наиболее распространенными алгоритмами линейной классификации являются
# логистическая регрессия (logistic regression), реализованная в классе
# linear_model.LogisticRegression, и линейный метод опорных векторов (linear support vector
# machines) или линейный SVM, реализованный в классе svm.LinearSVC (SVC расшифровывается как
# support vector classifier – классификатор опорных векторов).
#

X, y = mglearn.datasets.make_forge()
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
 clf = model.fit(X, y)
 mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5,
 ax=ax, alpha=.7)
 mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
 ax.set_title("{}".format(clf.__class__.__name__))
 ax.set_xlabel("Признак 0")
 ax.set_ylabel("Признак 1")
axes[0].legend()
plt.show()




mglearn.plots.plot_linear_svc_regularization()
plt.show()

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
 cancer.data, cancer.target, stratify=cancer.target, random_state=42)
logreg = LogisticRegression().fit(X_train, y_train)
print("============== C = 1 =======")
print("Правильность на обучающем наборе: {:.3f}".format(logreg.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(logreg.score(X_test, y_test)))
print("============== C = 100 =======")
logreg100 = LogisticRegression(C=100).fit(X_train, y_train)
print("Правильность на обучающем наборе: {:.3f}".format(logreg100.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(logreg100.score(X_test, y_test)))
print("============== C = 0.01 =======")
logreg001 = LogisticRegression(C=0.01).fit(X_train, y_train)
print("Правильность на обучающем наборе: {:.3f}".format(logreg001.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(logreg001.score(X_test, y_test)))
plt.plot(logreg.coef_.T, 'o', label="C=1")
plt.plot(logreg100.coef_.T, '^', label="C=100")
plt.plot(logreg001.coef_.T, 'v', label="C=0.001")
plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
plt.hlines(0, 0, cancer.data.shape[1])
plt.ylim(-5, 5)
plt.xlabel("Индекс коэффициента")
plt.ylabel("Оценка коэффициента")
plt.legend()
plt.show()


