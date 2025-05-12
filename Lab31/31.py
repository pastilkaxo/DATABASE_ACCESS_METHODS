import mglearn
import sklearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

# PCA визуализировать их с помощью диаграммы рассеяния
# Существует класс алгоритмов визуализации, называемых
# алгоритмами множественного обучения (manifold learning algorithms), которые используют
# гораздо более сложные графические представления данных и позволяют получить визуализации
# лучшего качества. Особенно полезным является алгоритм t-SNE.

# 1) Алгоритмы множественного обучения в основном направлены на визуализацию
# 2)  создают новое представление обучающих данных, но при этом не осуществляют
# преобразования новых данных
# 3)  t-SNE, заключается в том, чтобы найти двумерное
# представление данных, сохраняющее расстояния между точками наилучшим образом.
# t-SNE
# начинает свою работу со случайного двумерного представления каждой точки данных, а затем
# пытается сблизить точки, которые в пространстве исходных признаков находятся близко друг к
# другу, и отдаляет друг от друга точки, которые находятся далеко друг от друга.


# укописные цифры
from sklearn.datasets import load_digits
digits = load_digits()
fig, axes = plt.subplots(2, 5, figsize=(10, 5), subplot_kw={'xticks': (), 'yticks': ()})
for ax, img in zip(axes.ravel(), digits.images):
    ax.imshow(img)
plt.show()


#  Диаграмма рассеяния для набора данных digits, использующая первые две
# главные компоненты
# строим модель PCA
pca = PCA(n_components=2)
pca.fit(digits.data)
# преобразуем данные рукописных цифр к первым двум компонентам
digits_pca = pca.transform(digits.data)
colors = ["#476A2A", "#7851B8", "#BD3430", "#4A2D4E", "#875525", "#A83683", "#4E655E", "#853541", "#3A3120", "#535D8E"]
plt.figure(figsize=(10, 10))
plt.xlim(digits_pca[:, 0].min(), digits_pca[:, 0].max())
plt.ylim(digits_pca[:, 1].min(), digits_pca[:, 1].max())
for i in range(len(digits.data)):
    #  строим  график,  где  цифры  представлены  символами  вместо  точек
    plt.text(digits_pca[i, 0], digits_pca[i, 1],
        str(digits.target[i]),
        color=colors[digits.target[i]],
        fontdict={'weight': 'bold', 'size': 9})
plt.xlabel("Первая главная компонента")
plt.ylabel("Вторая главная компонента")
plt.show()

# Давайте применим t-SNE к этому же набору данных и сравним результаты. Поскольку t-SNE
# не поддерживает преобразование новых данных, в классе TSNE нет метода transform. Вместо этого
# мы можем вызвать метод fit_transform, который построит модель и немедленно вернет
# преобразованные данные


from sklearn.manifold import TSNE
tsne = TSNE(random_state=42)
#  используем  метод  fit_transform  вместо  fit,  т.к.  класс  TSNE  не  использует  метод  transform
digits_tsne = tsne.fit_transform(digits.data)
plt.figure(figsize=(10, 10))
plt.xlim(digits_tsne[:, 0].min(), digits_tsne[:, 0].max() + 1)
plt.ylim(digits_tsne[:, 1].min(), digits_tsne[:, 1].max() + 1)
for i in range(len(digits.data)):
    # строим  график,  где  цифры  представлены  символами  вместо  точек
    plt.text(digits_tsne[i, 0], digits_tsne[i, 1],
        str(digits.target[i]),
        color=colors[digits.target[i]],
        fontdict={'weight': 'bold', 'size': 9})
plt.xlabel("t-SNE признак 0")
plt.xlabel("t-SNE признак 1")
plt.show()


# Результат, полученный с помощью t-SNE, весьма примечателен. Все классы довольно четко
# разделены. Единицы и девятки в некоторой степени распались, однако большинство классов
# образуют отдельные сплоченные группы. Имейте в виду, что этот метод не использует информацию
# о метках классов: он является полностью неконтролируемым. Тем не менее он может найти
# двумерное представление данных, которое четко разграничивает классы, используя лишь
# информацию о расстояниях между точками данных в исходном пространстве.