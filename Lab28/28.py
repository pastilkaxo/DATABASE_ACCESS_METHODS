import mglearn
import sklearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import make_blobs, make_circles
from sklearn.model_selection import train_test_split

#
# Еще одна полезная деталь интерфейса scikit-learn, о которой мы еще не говорили – это
# возможность вычислить оценки неопределенности прогнозов. Часто вас интересует не только
# класс, спрогнозированный моделью для определенной точки тестового набора, но и степень
# уверенности модели в правильности прогноза.

# существует две различные функции, с помощью которых можно
# оценить неопределенность прогнозов: decision_function и predict_proba. Большая часть
# классификаторов (но не все) позволяет использовать по крайней мере одну из этих функций.

X, y = make_circles(noise=0.25, factor=0.5, random_state=1)
# мы переименовываем классы в «blue» и «red» для удобства
y_named = np.array(["blue", "red"])[y]
# мы можем вызвать train_test_split с любым количеством массивов,
# все будут разбиты одинаковым образом
X_train, X_test, y_train_named, y_test_named, y_train, y_test = \
train_test_split(X, y_named, y, random_state=0)
# строим модель градиентного бустинга
gbrt = GradientBoostingClassifier(random_state=0)
gbrt.fit(X_train, y_train_named)


print("Форма массива X_test: {}".format(X_test.shape))
print("Форма решающей функции: {}".format(gbrt.decision_function(X_test).shape))

# # выведем несколько первых элементов решающей функции
# Значение показывает, насколько сильно модель уверена в том, что точка данных
# принадлежит «положительному» классу, в данном случае, классу 1. Положительное значение
# указывает на предпочтение в пользу позиционного класса, а отрицательное значение – на
# предпочтение в пользу «отрицательного» (другого) класса.

print("Решающая функция:\n{}".format(gbrt.decision_function(X_test)[:6]))
print("Решающая функция с порогом отсечения:\n{}".format( gbrt.decision_function(X_test) > 0))
print("Прогнозы:\n{}".format(gbrt.predict(X_test)))


# Для бинарной классификации «отрицательный» класс – это всегда первый элемент атрибута
# classes_, а «положительный» класс – второй элемент атрибута classes_. Таким образом, если вы
# хотите полностью просмотреть вывод метода predict, вам нужно воспользоваться атрибутом
# classes_:

# переделаем булевы значения True/False в 0 и 1
greater_zero = (gbrt.decision_function(X_test) > 0).astype(int)
# используем 0 и 1 в качестве индексов атрибута classes_
pred = gbrt.classes_[greater_zero]
# pred идентичен выводу gbrt.predict
print("pred идентичен прогнозам: {}".format(
np.all(pred == gbrt.predict(X_test))))
decision_function = gbrt.decision_function(X_test)
print("Решающая функция минимум: {:.2f} максимум: {:.2f}".format( np.min(decision_function),
np.max(decision_function)))


# построим decision_function для всех точек двумерной
# плоскости, используя цветовую кодировку и уже знакомую визуализацию решающей границы.

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
mglearn.tools.plot_2d_separator(gbrt, X, ax=axes[0], alpha=.4, fill=True, cm=mglearn.cm2)
scores_image = mglearn.tools.plot_2d_scores(gbrt, X, ax=axes[1],
 alpha=.4, cm=mglearn.ReBl)
for ax in axes:
    mglearn.discrete_scatter(X_test[:, 0], X_test[:, 1], y_test,markers='^', ax=ax)
    mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, markers='o', ax=ax)
    ax.set_xlabel("Характеристика 0")
    ax.set_ylabel("Характеристика 1")
    cbar = plt.colorbar(scores_image, ax=axes.tolist())
    axes[0].legend(["Тест класс 0", "Тест класс 1", "Обучение класс 0", "Обучение класс 1"], ncol=4,
loc=(.1, 1.1))
plt.show()

# --------------

# Вывод метода predict_proba – это вероятность каждого класса и часто его легче понять, чем
# вывод метода decision_function.

print("Форма вероятностей: {}".format(gbrt.predict_proba(X_test).shape))
print("Спрогнозированные вероятности:\n{}".format(gbrt.predict_proba(X_test[:6])))
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
mglearn.tools.plot_2d_separator(gbrt, X, ax=axes[0], alpha=.4, fill=True, cm=mglearn.cm2)
scores_image = mglearn.tools.plot_2d_scores(gbrt, X, ax=axes[1], alpha=.5, cm=mglearn.ReBl, function='predict_proba')
for ax in axes:
    mglearn.discrete_scatter(X_test[:, 0], X_test[:, 1], y_test, markers='^', ax=ax)
    mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, markers='o', ax=ax)
    ax.set_xlabel("Характеристика 0")
    ax.set_ylabel("Характеристика 1")
cbar = plt.colorbar(scores_image, ax=axes.tolist())
axes[0].legend(["Тест класс 0", "Тест класс 1", "Обуч класс 0", "Обуч класс 1"], ncol=4, loc=(.1,
1.1))
plt.show()
# Границы на этом рисунке определены гораздо более четко, а небольшие участки
# неопределенности отчетливо видны.

#------------------

# До сих пор мы говорили только об оценках неопределенности в бинарной классификации.
# Однако методы decision_function и predict_proba также можно применять в мультиклассовой
# классификации. Давайте применим их к набору данных Iris, который представляет собой пример 3
# классовой классификации:

from sklearn.datasets import load_iris
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split( iris.data, iris.target, random_state=42)
gbrt = GradientBoostingClassifier(learning_rate=0.01, random_state=0)
gbrt.fit(X_train, y_train)

print("Форма решающей функции: {}".format(gbrt.decision_function(X_test).shape))
print("Решающая функция:\n{}".format(gbrt.decision_function(X_test)[:6, :]))


print("Argmax решающей функции:\n{}".format(np.argmax(gbrt.decision_function(X_test), axis=1)))
print("Прогнозы:\n{}".format(gbrt.predict(X_test)))

print("Спрогнозированные вероятности:\n{}".format(gbrt.predict_proba(X_test)[:6]))
print("Суммы: {}".format(gbrt.predict_proba(X_test)[:6].sum(axis=1)))
print("Argmax спрогнозированных вероятностей:\n{}".format( np.argmax(gbrt.predict_proba(X_test),
axis=1)))
print("Прогнозы:\n{}".format(gbrt.predict(X_test)))

# predict_proba и decision_function всегда имеют форму
# (n_samples, n_classes), за исключением decision_function в случае бинарной классификации. В
# бинарной классификации decision_function имеет только один столбец, соответствующий
# «положительному» классу classes_[1].


# Если вы хотите сравнить
# результаты, полученные с помощью predict, с результатами decision_function или predict_proba,
# убедитесь, что используете атрибут classes_ для получения фактических названий классов

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
named_target = iris.target_names[y_train]
logreg.fit(X_train, named_target)
print("уникальные классы в обучающем наборе: {}".format(logreg.classes_))
print("прогнозы: {}".format(logreg.predict(X_test)[:10]))
argmax_dec_func = np.argmax(logreg.decision_function(X_test), axis=1)
print("argmax решающей функции: {}".format(argmax_dec_func[:10]))
print("argmax объединенный с классами_: {}".format(logreg.classes_[argmax_dec_func][:10]))
