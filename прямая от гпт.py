import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Данные точек (x, y)

x = np.array([
0.5, 2, 3, 4, 5

])
y = np.array([
1.35,
1.30,
1.28,
1.27,
1.25


])

sum = 0

# Аппроксимация прямой
A = np.vstack([x, np.ones(len(x))]).T
k, b = np.linalg.lstsq(A, y, rcond=None)[0]
#k, b = np.sum(x * y) / np.sum(x**2), 0


fig, ax = plt.subplots()

for i in range(len(x)):
    sum += ((y[i] - k * x[i] - b) / (k * x[i] + b)) ** 2
pogr = str((sum / len(x)) ** (1/2))[:6]


print("Коэффициенты:")
print("k =", k)
print("b =", b)

print('Погрешнсть')
print(pogr)

print(k*0.1 + b)


# Построение графика
plt.plot(x, y, '+', color='red') # Точки
x = np.array([0,0.5,2,3,4,5,6,7])
plt.plot(x, k*x + b) # Прямая

'''
plt.plot([175, 175], [26.6, 35], color='b', linestyle=':', linewidth=1)
plt.plot([226, 226], [26, 34], color='b', linestyle=':', linewidth=1)
plt.plot([200.5, 200.5], [26.6, 34.2], color='b', linestyle=':', linewidth=2)
'''

plt.text(4, 1.3, 'Погр. = ' + pogr, color='blue')
#plt.text(310, 28, 'U/F = σ -T∙dσ/dT     U/F = ' + str(-K1 * x[0])[:5], color='blue')
#plt.text(310, 18, 'q = -T∙dσ/dT', color='blue')

ax.set_axisbelow(True)
plt.grid(True, color='lightgray', linestyle='--')
plt.xlabel("τ, с")
plt.ylabel("γ")
title_text = 'Рисунок 1'
ax.set_title(title_text, wrap=True)
plt.axis([0, 6, 1.2, 1.4])
ax.yaxis.set_major_locator(MultipleLocator(0.01))
ax.yaxis.set_minor_locator(MultipleLocator(0.002))
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
plt.show()

