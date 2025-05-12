import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_graphviz
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import graphviz
from IPython.display import display, Image

# сколько раз каждый признак (в каждом столбце массива X)
# встречается в примерах разных классов.
# Это полезно, чтобы понять, какие признаки более значимы для разных классов.

# ==================== 1. АНАЛИЗ ЧАСТОТ ПРИЗНАКОВ ====================
print("\n1. Анализ частот признаков:")
X = np.array([[0, 1, 0, 1], [1, 0, 1, 1], [0, 0, 0, 1], [1, 0, 1, 0]])
y = np.array([0, 1, 0, 1])
counts = {}
for label in np.unique(y):
    counts[label] = X[y == label].sum(axis=0)
print("Частоты признаков:\n", counts)

# ==================== 2. КЛАССИФИКАЦИЯ РАКА ГРУДИ ====================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# ===== 1. Настройка отображения =====
plt.ion()  # Включение интерактивного режима
plt.style.use('seaborn-v0_8')  # Улучшенный стиль графиков

# ===== 2. Загрузка данных =====
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42)

# ===== 3. Обучение модели =====
tree = DecisionTreeClassifier(max_depth=3, random_state=0)
tree.fit(X_train, y_train)

# ===== 4. Текстовое представление дерева (работает всегда) =====
print("\nТекстовое представление дерева:")
tree_rules = export_text(tree, feature_names=list(cancer.feature_names))
print(tree_rules)

# ===== 5. Визуализация важности признаков =====
plt.figure(figsize=(12, 8))
importances = tree.feature_importances_
indices = np.argsort(importances)[-15:]  # Топ-15 признаков
plt.title("Важность признаков (топ-15)")
plt.barh(range(len(indices)), importances[indices], color='skyblue')
plt.yticks(range(len(indices)), [cancer.feature_names[i] for i in indices])
plt.xlabel("Относительная важность")
plt.tight_layout()
plt.show()
plt.pause(0.1)

# ===== 6. Альтернативная визуализация дерева (Matplotlib) =====
from sklearn.tree import plot_tree
plt.figure(figsize=(20, 12))
plot_tree(tree,
          filled=True,
          feature_names=cancer.feature_names,
          class_names=cancer.target_names,
          rounded=True,
          fontsize=10)
plt.title("Дерево решений для классификации рака груди")
plt.show()
plt.pause(0.1)

# ===== 7. Сохранение в файл =====
plt.figure(figsize=(20, 12))
plot_tree(tree,
          filled=True,
          feature_names=cancer.feature_names,
          class_names=cancer.target_names,
          rounded=True,
          fontsize=10)
plt.savefig('cancer.pdf', bbox_inches='tight')
#plt.savefig('breast_cancer_tree.png', dpi=300, bbox_inches='tight')
print("\nДерево сохранено в breast_cancer_tree.png")

# Фиксация всех графиков перед завершением
plt.show(block=True)

# ==================== 3. РЕГРЕССИЯ НА ДАННЫХ О ЦЕНАХ RAM ====================
print("\n3. Регрессия на данных о ценах RAM:")
try:
    # Создаем искусственные данные если файл отсутствует
    dates = np.arange(1950, 2020)
    prices = 1000 * np.exp(-0.02 * (dates - 1950)) * (1 + 0.1 * np.sin(0.1 * dates))
    ram_prices = pd.DataFrame({'date': dates, 'price': prices})

    # Подготовка данных
    data_train = ram_prices[ram_prices.date < 2000]
    data_test = ram_prices[ram_prices.date >= 2000]

    X_train = data_train.date.values.reshape(-1, 1)
    y_train = np.log(data_train.price)

    # Обучение моделей
    tree_reg = DecisionTreeRegressor(max_depth=3, random_state=0).fit(X_train, y_train)
    linear_reg = LinearRegression().fit(X_train, y_train)

    # Предсказания
    X_all = ram_prices.date.values.reshape(-1, 1)
    price_tree = np.exp(tree_reg.predict(X_all))
    price_lr = np.exp(linear_reg.predict(X_all))

    # Визуализация
    plt.figure(figsize=(12, 6))
    plt.semilogy(data_train.date, data_train.price, 'bo', label="Обучающие данные")
    plt.semilogy(data_test.date, data_test.price, 'go', label="Тестовые данные")
    plt.semilogy(ram_prices.date, price_tree, 'r-', label="Прогнозы дерева", linewidth=2)
    plt.semilogy(ram_prices.date, price_lr, 'm--', label="Прогнозы линейной регрессии", linewidth=2)
    plt.xlabel("Год", fontsize=12)
    plt.ylabel("Цена ($/Мбайт)", fontsize=12)
    plt.title("Динамика цен на оперативную память", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()
    plt.pause(0.1)  # Даем время на отрисовку

except Exception as e:
    print("Ошибка в части регрессии:", str(e))

# Фиксация всех графиков перед завершением
plt.show(block=True)  # Блокирующий вызов в конце