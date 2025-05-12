import mglearn
import sklearn
import matplotlib.pyplot as plt
import numpy as np
import graphviz
from IPython.display import display

#  Многослойные персептроны (MLP) также называют
# простыми (vanilla) нейронными сетями прямого распространения

# MLP можно рассматривать как обобщение линейных моделей, которое прежде чем прийти
# к решению выполняет несколько этапов обработки данных.

 # Визуализация логистической регрессии, в которой входные признаки и прогнозы
# показаны в виде узлов, а коэффициенты – в виде соединений между узлами
display(mglearn.plots.plot_single_hidden_layer_graph())

# MLP процесс вычисления взвешенных сумм повторяется несколько раз. Сначала
# вычисляются скрытые элементы (hidden units), которые представляют собой промежуточный этап
# обработки. Они вновь объединяются с помощью взвешенных сумм для получения конечного
# результата

# С математической точки зрения вычисление серии взвешенных сумм – это то же самое, что
# вычисление лишь одной взвешенной суммы, таким образом, чтобы эта модель обладала более
# мощной прогнозной силой, чем линейная модель, нам нужен один дополнительный трюк.

#  функция активации – обычно используются нелинейные функции выпрямленный
# линейный элемент (rectified linear unit или relu) или гиперболический тангенс (hyperbolic tangent
# или tanh).

# В итоге получаем выходы нейронов скрытого слоя.

#  Relu отсекает значения ниже нуля, в то время как tanh принимает
# значения от –1 до 1 (соответственно для минимального и максимального значений входов). Любая
# из этих двух нелинейных функций позволяет нейронной сети в отличие от линейной модели
# вычислять гораздо более сложные зависимости.


line = np.linspace(-3, 3, 100)
plt.plot(line, np.tanh(line), label="tanh")
plt.plot(line, np.maximum(line, 0), label="relu")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel("relu(x), tanh(x)")
plt.show()

mglearn.plots.plot_two_hidden_layer_graph()
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons

# Настройка нейронных сетей
# MLPClassifier

X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
mlp = MLPClassifier(solver='lbfgs', random_state=0).fit(X_train, y_train)
mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()

# По умолчанию MLP использует 100 скрытых узлов, что довольно много для этого
# небольшого набора данных. Мы можем уменьшить число
# При использовании лишь 10 скрытых элементов граница принятия решений становится
# более неровной. По умолчанию используется функция активации relu,

mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[10])
mlp.fit(X_train, y_train)
mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()

# Если необходимо получить более гладкую решающую границу, можно добавить
# большее количество скрытых элементов
# использование двух скрытых слоев по 10 элементов в каждом
mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[10, 10])
mlp.fit(X_train, y_train)
mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()

# или использовать функцию активации tanh
# использование двух скрытых слоев по 10 элементов в каждом,
# на этот раз с функцией tanh

mlp = MLPClassifier(solver='lbfgs', activation='tanh',
 random_state=0, hidden_layer_sizes=[10, 10])
mlp.fit(X_train, y_train)
mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()

# помощью l2
# штрафа, чтобы сжать весовые коэффициенты до близких к нулю значений, как мы это делали в
# гребневой регрессии и линейных классификаторов. В MLPClassifier за это отвечает параметр alpha

# количество скрытых слоев, количество элементов в каждом скрытом слое и
# регуляризация (alpha).

fig, axes = plt.subplots(2, 4, figsize=(20, 8))
for axx, n_hidden_nodes in zip(axes, [10, 100]):
    for ax, alpha in zip(axx, [0.0001, 0.01, 0.1, 1]):
        mlp = MLPClassifier(
            solver='lbfgs',
            random_state=0,
            hidden_layer_sizes=[n_hidden_nodes, n_hidden_nodes],
            alpha=alpha
        )
        mlp.fit(X_train, y_train)
        mglearn.plots.plot_2d_separator(
            mlp, X_train, fill=True, alpha=.3, ax=ax
        )
        mglearn.discrete_scatter(
            X_train[:, 0], X_train[:, 1], y_train, ax=ax
        )
        ax.set_title("n_hidden=[{}, {}]\nalpha={:.4f}"
                     .format(n_hidden_nodes, n_hidden_nodes, alpha)
                     )
plt.show()

# Границы принятия решений, полученные с использованием тех же самых
# параметров, но разных стартовых значений

fig, axes = plt.subplots(2, 4, figsize=(20, 8))
for i, ax in enumerate(axes.ravel()):
 mlp = MLPClassifier(solver='lbfgs', random_state=i, hidden_layer_sizes=[100, 100])
 mlp.fit(X_train, y_train)
 mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3, ax=ax)
 mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, ax=ax)
plt.show()

# Чтобы лучше понять, как нейронная сеть работает на реальных данных, давайте применим
# MLPClassifier к набору данных Breast Cancer

# MLP демонстрирует довольно неплохую правильность, однако не столь хорошую, если
# сравнивать с другими моделями. Как и в предыдущем примере с SVC, это, вероятно, обусловлено
# масштабом данных.

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("Максимальные значения характеристик:\n{}".format(cancer.data.max(axis=0)))
X_train, X_test, y_train, y_test = train_test_split( cancer.data, cancer.target, random_state=0)
mlp = MLPClassifier(random_state=42)
mlp.fit(X_train, y_train)
print("Правильность на обучающем наборе: {:.2f}".format(mlp.score(X_train, y_train)))
print("Правильности на тестовом наборе: {:.2f}".format(mlp.score(X_test, y_test)))

# После масштабирования результаты стали намного лучше и теперь уже вполне могут
# конкурировать с результатами остальных моделей. Впрочем, мы получили предупреждение о том,
# что достигнуто максимальное число итераций


min_on_training = X_train.min(axis=0)
range_on_training = (X_train - min_on_training).max(axis=0)
X_train_scaled = (X_train - min_on_training) / range_on_training
mean_on_train = X_train.mean(axis=0)
std_on_train = X_train.std(axis=0)
X_test_scaled = (X_test - mean_on_train) / std_on_train
mlp = MLPClassifier(random_state=0)
mlp.fit(X_train_scaled, y_train)
print("Правильность на обучающем наборе: {:.3f}".format( mlp.score(X_train_scaled, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(mlp.score(X_test_scaled, y_test)))

# Оно является неотъемлемой частью алгоритма adam
# и сообщает нам о том, что мы должны увеличить число итераций:


mlp = MLPClassifier(max_iter=1000, random_state=0)
mlp.fit(X_train_scaled, y_train)
print("Правильность на обучающем наборе: {:.3f}".format( mlp.score(X_train_scaled, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(mlp.score(X_test_scaled, y_test)))
mlp = MLPClassifier(max_iter=1000, alpha=1, random_state=0)
mlp.fit(X_train_scaled, y_train)
print("Правильность на обучающем наборе: {:.3f}".format( mlp.score(X_train_scaled, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(mlp.score(X_test_scaled, y_test)))

#  Один из способов анализа нейронной
# сети заключается в том, чтобы исследовать веса модели. Образец такого анализа вы можете
# увидеть в галерее примеров scikit-learn. Применительно к набору данных Breast Cancer такой
# анализ может быть немного сложен. Следующий график (рис. 11) показывает весовые
# коэффициенты, которые были вычислены при подключении входного слоя к первому скрытому
# слою

plt.figure(figsize=(20, 5))
plt.imshow(mlp.coefs_[0], interpolation='none', cmap='viridis')
plt.yticks(range(30), cancer.feature_names)
plt.xlabel("Столбцы матрицы весов")
plt.ylabel("Входная характеристика")
plt.colorbar()
plt.show()
