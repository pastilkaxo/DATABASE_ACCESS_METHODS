import mglearn
import sklearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA

# Анализ главных компонент (PSA)

# метод, который осуществляет
# вращение данных с тем, чтобы преобразованные признаки не коррелировали между
# собой. Часто это вращение сопровождается выбором подмножества новых признаков в
# зависимости от их важности с точки зрения интерпретации данных

mglearn.plots.plot_pca_illustration()
plt.show()

# 1 график
# комп 1 - напрвление дисперсии данных , большая часть инфы
# комп 2 - ортогональная юольшая часть инфы (90 град)
#  Направления, найденные с помощью этого
# алгоритма, называются главными компонентами
# 2 график
# 1 комп совдаает с Ох
# 2 комп совпадает с Оу
# Все элементы будут равны нулю
# 3 график
# тольк 1 главная компонента
# 4 график
# без вращения
# конкретный одномерный массив


# Применение PCA к набору данных cancer для визуализации

# Одним из наиболее распространенных применений PCA является визуализация
# высокоразмерных наборов данных, довольно сложно построить диаграммы рассеяния
# для данных, которые включают больше двух признаков.

# для каждого признака гистограмму, подсчитывая
# частоту встречаемости точек данных в пределах границ интервалов (этот интервал еще
# называют бином).
# Однако этот график не дает нам никакой информации о взаимодействии между
# переменными и взаимосвязях между признаками и классами

# без PCA
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
fig, axes = plt.subplots(15, 2, figsize=(10, 20))
malignant = cancer.data[cancer.target == 0]
benign = cancer.data[cancer.target == 1]
ax = axes.ravel()
for i in range(30):
    _, bins = np.histogram(cancer.data[:, i], bins=50)
    ax[i].hist(malignant[:, i], bins=bins, color=mglearn.cm3(0), alpha=.5)
    ax[i].hist(benign[:, i], bins=bins, color=mglearn.cm3(2), alpha=.5)
    ax[i].set_title(cancer.feature_names[i])
    ax[i].set_yticks(())
    ax[0].set_xlabel("Значение признака")
    ax[0].set_ylabel("Частота")
ax[0].legend(["доброкачественная", "злокачественная"], loc="best")
fig.tight_layout()
plt.show()


# Перед тем, как применить PCA, мы отмасштабируем наши данные таким образом,
# чтобы каждый признак имел единичную дисперсию, воспользовавшись StandardScaler

# PCA
cancer = load_breast_cancer()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(cancer.data)
X_scaled = scaler.transform(cancer.data)



from sklearn.decomposition import PCA
# оставляем первые две главные компоненты
pca = PCA(n_components=2)
# подгоняем модель PCA на наборе данных breast cancer
pca.fit(X_scaled)
# преобразуем данные к первым двум главным компонентам
X_pca = pca.transform(X_scaled)
print("Форма исходного массива: {}".format(str(X_scaled.shape)))
print("Форма массива после сокращения размерности: {}".format(str(X_pca.shape)))

# строим график первых двух главных компонент, классы выделены цветом

# мы построили график, где по оси x отложена первая главная компонента, по оси y –
# вторая главная компонента, а затем воспользовались информацией о классах, чтобы
# выделить точки разным цветом.

plt.figure(figsize=(8, 8))
mglearn.discrete_scatter(X_pca[:, 0], X_pca[:, 1], cancer.target)
plt.legend(cancer.target_names, loc="best")
plt.gca().set_aspect("equal")
plt.xlabel("Первая главная компонента")
plt.ylabel("Вторая главная компонента")
plt.show()

# Недостаток PCA заключается в том, что эти две оси графика часто бывает сложно
# интерпретировать. Главные компоненты соответствуют направлениям данных, поэтому
# они представляют собой комбинации исходных признаков.

# tепловая карта первых двух главных компонент для набора данных рака
# Breast Cancer

print("форма главных компонент: {}".format(pca.components_.shape))
print("компоненты PCA:\n{}".format(pca.components_))
plt.matshow(pca.components_, cmap='viridis')
plt.yticks([0, 1], ["Первая компонента", "Вторая компонента"])
plt.colorbar()
plt.xticks(range(len(cancer.feature_names)), cancer.feature_names, rotation=60, ha='left')
plt.xlabel("Характеристика")
plt.ylabel("Главные компоненты")
plt.show()

# Вы можете увидеть, что в первой компоненте коэффициенты всех признаков
# имеют одинаковый знак (они положительные, но, как мы уже говорили ранее, не имеет
# значения, какое направление указывает стрелка). Это означает, что существует общая
# корреляция между всеми признаками. Высоким значениям одного признака будут
# соответствовать высокие значения остальных признаков. Во второй компоненте
# коэффициенты признаков имеют разные знаки. Обе компоненты включают все 30
# признаков. Смешивание всех признаков – это как раз то, что усложняет
# интерпретацию


# 3. Метод «Собственых лиц» (eigenfaces) для выделения
# характерисtuk

# Еще одно применение PCA, о котором мы уже упоминали ранее, – это выделение
# признаков. Идея, лежащая в основе выделения признаков, заключается в поиске нового
# представления данных, которое в отличие от исходного лучше подходит для анализа.

# Мы приведем очень простой пример того, как можно применить выделение
# признаков к изображениям с помощью PCA


# Общая задача распознавания лиц заключается в том, чтобы спросить, не
# принадлежит ли незнакомое фото уже известному человеку из базы данных. Она
# применяется при составлении фотоколлекций, в социальных сетях и программах
# обеспечения безопасности. Один из способов решения этой задачи заключается в
# построении классификатора, в котором каждый человек представляет собой отдельный
# класс. Однако изображения, записанные в базах лиц, обычно принадлежат большому
# количеству самых различных людей и при этом очень мало фотографий принадлежат
# одному и тому же человеку (то есть очень мало обучающих примеров, принадлежащих
# одному классу). Для большинства классификаторов это представляет проблему. Кроме
# того, часто необходимо добавить фотографии новых людей, при этом не перестраивая
# заново огромную модель.


# модель PCA основана на пикселях, выравнивание изображения лица (положения глаз,
# подбородка и носа) и освещенность оказывают сильное влияние на степень сходства

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
image_shape = people.images[0].shape

# Нормализация данных
X_people = people.data / 255.
y_people = people.target

# Балансировка классов
mask = np.zeros(y_people.shape, dtype=bool)
for target in np.unique(y_people):
    mask[np.where(y_people == target)[0][:50]] = 1
X_people = X_people[mask]
y_people = y_people[mask]

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X_people, y_people, stratify=y_people, random_state=0)


# И вот именно здесь применяется PCA. Вычисление расстояний в исходном
# пиксельном пространстве – , мы
# сравниваем значение каждого отдельного пикселя по шкале градаций серого со
# значением пикселя в соответствующем положении на другом изображении.

# Функция для визуализации реконструкции трёх лиц
def plot_pca_reconstruction_3faces(X, n_components_list=[10, 50, 100, 500]):
    # Выбираем три разных лица (можно изменить индексы)
    face_indices = [10, 20, 30]  # Индексы лиц в наборе данных

    plt.figure(figsize=(15, 8))

    for i, idx in enumerate(face_indices):
        original = X[idx]

        # Оригинальное изображение
        plt.subplot(3, len(n_components_list) + 1, i * (len(n_components_list) + 1) + 1)
        plt.imshow(original.reshape(image_shape), cmap='gray')
        if i == 0:
            plt.title("Original", pad=10)
        plt.axis('off')

        # Реконструкции с разным числом компонент
        for j, n_components in enumerate(n_components_list):
            pca = PCA(n_components=n_components, whiten=True, random_state=0)
            pca.fit(X_train)

            transformed = pca.transform(original.reshape(1, -1))
            reconstructed = pca.inverse_transform(transformed)
            reconstructed = np.clip(reconstructed, 0, 1)  # Гарантируем диапазон [0, 1]

            plt.subplot(3, len(n_components_list) + 1, i * (len(n_components_list) + 1) + j + 2)
            plt.imshow(reconstructed.reshape(image_shape), cmap='gray')
            if i == 0:
                plt.title(f"{n_components}\ncomponents", pad=10)
            plt.axis('off')

    plt.tight_layout()
    plt.show()




# Визуализация примеров оригинальных лиц
def plot_sample_faces():
    fig, axes = plt.subplots(2, 5, figsize=(15, 6),
                             subplot_kw={'xticks': (), 'yticks': ()})
    for ax, img, target in zip(axes.ravel(), people.images[:10], people.target[:10]):
        ax.imshow(img)
        ax.set_title(people.target_names[target])
    plt.tight_layout()
    plt.show()


# Работая с изображениями, мы можем легко визуализировать найденные главные
# компоненты. Вспомним, что компоненты соответствуют направлениям в пространстве
# входных данных. Пространство входных данных здесь представляет собой изображения
# в градациях серого размером 87x65 пикселей, поэтому направления внутри этого
# пространства также являются изображениями в градациях серого размером 87x65
# пикселей.

# ы можете увидеть, что, когда мы используем лишь первые 10 главных компонент,
# фиксируется лишь общая суть картинки, например, ориентация лица и освещенность. По
# мере увеличения количества используемых компонент сохраняется все больше деталей
# изображения. Это соответствует включению большего числа слагаемых в сумму,
# показанную на рис. 8. Использование числа компонент, равного числу имеющихся
# пикселей, означало бы, что мы, осуществив поворот, сохранили всю информацию и
# можем идеально реконструировать изображение.



# Визуализация главных компонент
def plot_pca_components(pca):
    fig, axes = plt.subplots(3, 5, figsize=(15, 12),
                             subplot_kw={'xticks': (), 'yticks': ()})
    for ax, component in zip(axes.ravel(), pca.components_[:15]):
        ax.imshow(component.reshape(image_shape), cmap='viridis')
    plt.tight_layout()
    plt.show()




# Основное выполнение
plot_sample_faces()

# Создаем и обучаем PCA
pca = PCA(n_components=100, whiten=True, random_state=0).fit(X_train)

# Визуализация реконструкции для трёх лиц
plot_pca_reconstruction_3faces(X_train)

# Визуализация компонент
plot_pca_components(pca)

# Преобразование данных и визуализация в пространстве PCA
X_train_pca = pca.transform(X_train)
plt.figure(figsize=(8, 8))
for i, label in enumerate(np.unique(y_train)):
    plt.scatter(X_train_pca[y_train == label, 0],
                X_train_pca[y_train == label, 1],
                label=people.target_names[label])
plt.xlabel("Первая главная компонента")
plt.ylabel("Вторая главная компонента")
#plt.legend()
plt.show()

# визуализации всех лиц набора
# когда мы используем лишь первые две главные компоненты, все
# данные представляют собой просто одно большое скопление данных без видимого
# разделения классов.