import mglearn
import sklearn
import matplotlib.pyplot as plt


# группа алгоритмов машинного обучения, которую мы будем
# рассматривать, – это машинное обучение без учителя. Машинное обучение без учителя
# включает в себя все виды машинного обучения, когда ответ неизвестен и отсутствует
# учитель, указывающий ответ алгоритму. В машинном обучении без учителя есть лишь
# входные данные и алгоритму необходимо извлечь знания из этих данных

# Неконтролируемые преобразования (unsupervised transformations) – это
# алгоритмы, создающие новое представление данных, которое в отличие от исходного
# представления человеку или алгоритму машинного обучения будет обработать легче.


#  алгоритмы кластеризации (clustering algorithms) разбивают
# данные на отдельные группы схожих между собой элементов.


# 1. Предварительная обработка и масштабирование

# Поэтому обычной
# практикой является преобразование признаков с тем, чтобы итоговое представление
# данных было более подходящим для использования вышеупомянутых алгоритмов.

"In[2]:"
mglearn.plots.plot_scaling()
plt.show()

# 2. Применение преобразований данных

"In[3]:"
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=1)
print(X_train.shape)
print(X_test.shape)

# MinMaxScaler сдвигает данные таким образом, что все признаки
# находились строго в диапазоне от 0 до 1
"In[4]:"
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
"In[5]:"

scaler.fit(X_train)  # fit мы подгоняем scaler на обучающих данных.
"In[6]:"
min_on_training = X_train.min(axis=0)
range_on_training = (X_train - min_on_training).max(axis=0)
X_train_scaled = (X_train - min_on_training) / range_on_training
print("форма преобразованного массива: {}".format(X_train_scaled.shape))
print("min значение признака до масштабирования:\n {}".format(X_train.min(axis=0)))
print("max значение признака до масштабирования:\n {}".format(X_train.max(axis=0)))
print("min значение признака после масштабирования:\n {}".format( X_train_scaled.min(axis=0)))
print("max значение признака после масштабирования:\n {}".format( X_train_scaled.max(axis=0)))


# Преобразованные данные имеют такую же форму, что и исходные данные – признаки
# просто смещены и масштабированы. Видно, что теперь все признаки принимают значения в
# диапазоне от 0 до 1, как нам и требовалось.

"In[7]:"

# Чтобы применить SVM к масштабированным данным, мы должны преобразовать еще
# тестовый набор. Это снова делается с помощью вызова метода transform, на этот раз для X_test:

X_test_scaled = (X_test - min_on_training) / range_on_training
print("min значение признака после масштабирования:\n{}".format(X_test_scaled.min(axis=0)))
print("max значение признака после масштабирования:\n{}".format(X_test_scaled.max(axis=0)))

# MinMaxScaler
# (и все остальные типы масштабирования) всегда применяют одинаковое преобразование к
# обучающему и тестовому наборам. Это означает, что метод transform всегда вычитает
# минимальное значение, вычисленное для обучающего набора, и делит на ширину диапазона,
# вычисленную также для обучающего набора. Минимальное значение и ширина диапазона для
# обучающего набора могут отличаться от минимального значения и ширины диапазона для
# тестового набора.



# 3. Масштабирование обучающего и тестового наборов одинаковым образом


# ЧТО БЫ РАБОТАЛО С ТЕСТОВЫМ НАБОРОМ
# минимальное значение и ширину
# диапазона, отдельно вычисленные для тестового набора

"In[8]:"
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=50, centers=5, random_state=4, cluster_std=2)
X_train, X_test = train_test_split(X, random_state=5, test_size=.1)
fig, axes = plt.subplots(1, 3, figsize=(13, 4))
axes[0].scatter(X_train[:, 0], X_train[:, 1],
c=mglearn.cm2(0), label="Обучающий набор", s=60)
axes[0].scatter(X_test[:, 0], X_test[:, 1], marker='^',
c=mglearn.cm2(1), label="Тестовый набор", s=60)
axes[0].legend(loc='upper left')
axes[0].set_title("Исходные данные")
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
axes[1].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
c=mglearn.cm2(0), label="Обучающий набор", s=60)
axes[1].scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], marker='^', c=mglearn.cm2(1), label="Тестовый набор", s=60)
axes[1].set_title("Масштабированные данные")
test_scaler = MinMaxScaler()
test_scaler.fit(X_test)
X_test_scaled_badly = test_scaler.transform(X_test)
axes[2].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
c=mglearn.cm2(0), label="Обучающий набор", s=60)
axes[2].scatter(X_test_scaled_badly[:, 0], X_test_scaled_badly[:, 1], marker='^', c=mglearn.cm2(1), label="Тестовый набор", s=60)
axes[2].set_title("Неправильно масштабированные данные")
for ax in axes:
    ax.set_xlabel("Признак 0")
    ax.set_ylabel("Признак 1")
plt.show()


# Первый график – это немасштабированный двумерный массив данных, наблюдения
# обучающего набора показаны кружками, а наблюдения тестового набора показаны
# треугольниками.

# Второй график – те же самые данные, но масштабированы с помощью
# MinMaxScaler. Здесь мы вызвали метод
# для обучающего набора, а затем вызвали метод
# transform для обучающего и тестового наборов. Как видите, набор данных на втором графике
# идентичен набору, приведенному на первом графике, изменились лишь метки осей. Теперь все
# признаки принимают значения в диапазоне от 0 до 1. Кроме того, видно, что минимальные и
# максимальные значения признаков в тестовом наборе (треугольники) не равны 0 и 1.

# Третий график показывает, что произойдет, если отмасштабируем обучающий и тестовый
# наборы по отдельности. В этом случае минимальные и максимальные значения признаков в
# обучающем и тестовом наборах равны 0 и 1. Но теперь набор данных выглядит иначе. Тестовые
# точки причудливым образом сместились, поскольку масштабированы по-другому. Мы изменили
# расположение данных произвольным образом. Очевидно, это совсем не то. что нам нужно.


# Быстрые и эффективные альтернативные способы подгонки
# моделей

#   StandardScaler
#  гарантирует, что для каждого признака среднее будет равно 0, а дисперсия будет равна 1, в
# результате чего все признаки будут иметь один и тот же масштаб. Однако это масштабирование не
# гарантирует получение каких-то конкретных минимальных и максимальных значений признаков.


"In[9]:"
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit(X).transform(X)
X_scaled_d = scaler.fit_transform(X)

"In[10]:"
from sklearn.svm import SVC
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
svm = SVC(C=100)
svm.fit(X_train, y_train)
print("Правильность на тестовом наборе: {:.2f}".format(svm.score(X_test, y_test)))
"In[11]:"
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
svm.fit(X_train_scaled, y_train)
print("Правильность на масштабированном тестовом наборе: {:.2f}"
    .format( svm.score(X_test_scaled, y_test))
)
"In[12]:"
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
svm.fit(X_train_scaled, y_train)
print("Правильность SVM на тестовом наборе: {:.2f}".format(svm.score(X_test_scaled, y_test)))

