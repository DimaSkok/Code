import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Данные точек (x, y)

y = np.array([
580,
560,
430,
360,
330,
260,
220,
190,
160,
140,
130,
110,
100,
93,
86,
80,
76,
72,


])
const = 600
x = np.ones([len(y)])
y = np.log(const/y)


sum = 0
for i in range(1, len(x)):
    x[i] += x[i - 1]

# Аппроксимация прямой
A = np.vstack([x, np.ones(len(x))]).T
#k, b = np.linalg.lstsq(A, y, rcond=None)[0]
k, b = np.sum(x * y) / np.sum(x**2), 0

fig, ax = plt.subplots()

for i in range(len(x)):
    sum += (y[i] - k * x[i] + b) ** 2
pogr = str((sum / len(x)) ** 1/2)[:6]


print("Коэффициенты:")
print("k =", k)
print("b =", b)

print('Погрешнсть')
print(pogr)


# Построение графика
plt.plot(x, y, '+', color='red') # Точки
plt.plot(x, k*x + b) # Прямая
plt.text(1, 2, 'Погр. = ' + pogr, color='blue')
ax.set_axisbelow(True)
plt.grid(True, color='lightgray', linestyle='--')
plt.xlabel("t,c")
plt.ylabel("ln(P0/P)")
title_text = 'Рисунок 2'
ax.set_title(title_text, wrap=True)
#plt.axis([0, 0.6, 0, 300])
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(1))
plt.show()

