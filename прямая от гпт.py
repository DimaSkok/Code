import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Данные точек (x, y)

x = np.array([
0.20,
0.40,
0.61,
0.81,
0.92
])
y = np.array([
1.4,
2.8,
4.4,
5.8,
6.7
])

sum = 0

# Аппроксимация прямой
A = np.vstack([x, np.ones(len(x))]).T
#k, b = np.linalg.lstsq(A, y, rcond=None)[0]
k, b = np.sum(x * y) / np.sum(x**2), 0


fig, ax = plt.subplots()

for i in range(len(x)):
    sum += ((y[i] - k * x[i] - b) / (k * x[i] + b)) ** 2
pogr = str((sum / len(x)) ** (1/2))[:6]


print("Коэффициенты:")
print("k =", k)
print("b =", b)

print('Погрешнсть')
print(pogr)




# Построение графика
plt.plot(x, y, '+', color='red') # Точки
plt.plot(x, k*x + b) # Прямая

'''
plt.plot([175, 175], [26.6, 35], color='b', linestyle=':', linewidth=1)
plt.plot([226, 226], [26, 34], color='b', linestyle=':', linewidth=1)
plt.plot([200.5, 200.5], [26.6, 34.2], color='b', linestyle=':', linewidth=2)
'''

plt.text(0.3, 6, 'Погр. = ' + pogr, color='blue')
#plt.text(25, 22.45, 'R0 = ' + str(b)[:6], color='blue')
#plt.text(25, 22.3, 'k = ' + str(k)[:6], color='blue')

ax.set_axisbelow(True)
plt.grid(True, color='lightgray', linestyle='--')
plt.xlabel("N, Вт")
plt.ylabel("ΔT,⁰С")
title_text = 'Рисунок 2'
ax.set_title(title_text, wrap=True)
#plt.axis([0, 500, 26, 35])
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))
plt.show()

