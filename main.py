import matplotlib.pyplot as plt

# Заданные данные
xi = [-6, -5, -2, 2, 5, 7]
ni = [90, 50, 40, 50, 60, 70]

# Построение гистограммы
plt.bar(xi, ni, width=1, align='center', edgecolor='black')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.show()

import numpy as np

# Вычисление эмпирической функции распределения
cumulative_prob = np.cumsum(ni) / sum(ni)

# Построение эмпирической функции распределения
plt.step(xi, cumulative_prob, where='post')
plt.xlabel('Значения')
plt.ylabel('ЭФР')
plt.title('Эмпирическая функция распределения')
plt.show()

# Вычисление выборочного среднего
mean = sum(xi[i] * ni[i] for i in range(len(xi))) / sum(ni)
print("Выборочное среднее:", mean)

# Вычисление исправленной выборочной дисперсии
n_total = sum(ni)
corrected_variance = sum((xi[i] - mean)**2 * ni[i] for i in range(len(xi))) / (n_total - 1)
print("Исправленная выборочная дисперсия:", corrected_variance)
