import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Заданные точки
x = np.array([
20,
30, 40, 50

])
x += 273
x = 1/x
y = np.array([
-1.15,
-1.01,
-0.95,
-0.90

])


# Погрешности точек
errors = np.array([
0.06,
0.04,
0.04,
0.03

])

# Аппроксимация прямой (линейная)
coefficients = np.polyfit(x, y, deg=1)
#coefficients = np.array([np.sum(x * y) / np.sum(x**2), 0])
poly = np.poly1d(coefficients)


# Коэффициенты прямой
k = coefficients[0]
b = coefficients[1]
print("k =", k)
print("b =", b)

# Погрешность графика
residuals = y - poly(x)
residual_error = np.sqrt(np.sum(residuals**2) / (len(x) - 2))
print(f"Погрешность графика: ±{residual_error:.4f}")

# График
fig, ax = plt.subplots()
plt.errorbar(x, y, yerr=errors, fmt='+')
plt.plot(x, poly(x), color='red')
plt.text(0.0031, -1.15, 'Погрешность: ' + str(residual_error)[:4], color='blue')

ax.set_axisbelow(True)
plt.grid(True, color='lightgray', linestyle='--')
plt.xlabel("1/t, 1/K")
plt.ylabel("μ, K/атм")
title_text = 'Рисунок 5'
ax.set_title(title_text)

plt.axis([1/330 , 1/290, -0.85, -1.25])
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(0.01))
ax.xaxis.set_major_locator(MultipleLocator(0.00005))
ax.xaxis.set_minor_locator(MultipleLocator(0.00001))

plt.show()