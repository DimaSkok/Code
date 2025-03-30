import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math as mt
from scipy.optimize import minimize

# Определяем функцию для минимизации (сумма квадратов отклонений)
def objective(params, x, y):
    a, b = params
    return np.sum((a / x + b - y)**2)

# Определяем ограничения (y >= 0 и y <= kx + b)
def constraint(params, x, k):
    a, b = params
    return a / x + b - k * x
def differential_permeability(H, B):
    mu_d = []
    for i in range(1, len(H)-1):
        dB = B[i+1] - B[i-1]
        dH = H[i+1] - H[i-1]
        mu_d.append(dB / dH)
    return mu_d


# Заданные точки
x = np.array([
     	-2,	-1,	0,	1,	2,		3,	4,	5,		6,	10,	11,	12,	22,
32,	42,	52,	57,	58,	59,	60,	61,	62,	63,	64,	65,	66,		68



])



y = np.array([

    0.721749007,
    0.740743747,
    0.839146392,
    0.90544161,
    0.913043478,

    0.909902561,
    0.832050294,
    0.898323147,

    0.801277221,
    0.48602144,
    0.416031812,
    0.375260694,
    0.085749293,

0.116213309,
    0.125436302,
    0.096786784,
    0.471125705,
    0.474970346,
    0.533760513,
    0.527639397,
    0.714434508,
    0.715541753,
    0.757240185,
    0.857493639,
    0.88165855,
    0.894427191,

    0.835484874







])

'''
dy = np.array([0.01,	0.01,	0.01,	0.01,	0.01,	0.01



])
'''
x1 = np.array([


])

y1 = np.zeros(len(x))

y2 = np.zeros(len(x))

y3 = np.zeros(len(x))

y4 = np.zeros(len(x))


'''
for i in range(len(x)):

    y1[i] = 10 ** 6/(mt.sqrt(1 + (0.0015 * 0.0435 * 4.3 * 4 * 3.14 ** 2 * x[i]) ** 2))
    y2[i] = 10 ** 6/(mt.sqrt(1 + (0.0015 * 0.0435 * 26.8 * 4 * 3.14 ** 2 * x[i]) ** 2))


x1 = x
x2 = x


y3 = np.array([
2.4,	1.6,	0,	0,	0,	1.2,	3.2,	5.6,	8,	11.6

])


ex = 0
ey = 0.4

# Погрешности точек
dx = x * 0.2
dy = y * 32

x = x * 58.6
y = y * 494

sumary = 0
for i in range(len(x)):
    sumary += (dy[i]/y[i])**2 + (dx[i]/x[i])**2

print((sumary/len(x))**0.5)
'''
'''

# Аппроксимация прямой (линейная)
coefficients = np.polyfit(x, y, deg=1)
# coefficients = np.array([np.sum(x * y) / np.sum(x**2), 0])
poly = np.poly1d(coefficients)
coefficients1 = np.polyfit(x1, y1, deg=1)
#coefficients1 = np.array([np.sum(x1 * y1) / np.sum(x**2), 0])
poly1 = np.poly1d(coefficients)
'''



A = np.vstack([x, np.ones(len(x))]).T
w = np.linalg.lstsq(A, y)[0]
'''
A1 = np.vstack([x1, np.ones(len(x1))]).T
w1 = np.linalg.lstsq(A1, y1)[0]

A2 = np.vstack([x2, np.ones(len(x2))]).T
w2 = np.linalg.lstsq(A2, y2)[0]
'''



print("k =", w[0])
print("b =", w[1])
'''
print("k1 =", w1[0])
print("b1 =", w1[1])
print("k2 =", w2[0])
print("b2 =", w2[1])
'''
''''''
coefficients = np.polyfit(x, y, 11)

x_values = np.linspace(min(x), max(x), 10000)
y_values = np.polyval(coefficients, x_values)

print(min(y_values), max(y_values))
print(coefficients)
'''
# Вызов функции и получение значения дифференциальной магнитной проницаемости
mu_d_values = differential_permeability(x_values, y_values)

print("Значения дифференциальной магнитной проницаемости:")
print(max(mu_d_values))
'''

'''
derivative_coefficients = np.polyder(coefficients)

# Находим значение производной dy/dx в конкретной точке (например, x=2)
x_value = 24
derivative_value = np.polyval(derivative_coefficients, x_value)

print("Значение производной dy/dx в точке x =", x_value, "равно", derivative_value)
x_value = x[0]
derivative_value = np.polyval(derivative_coefficients, x_value)

print("Значение производной dy/dx в точке x =", x_value, "равно", derivative_value)


'''
# Начальные значения параметров и коэффициент наклона прямой k
params_init = [1.0, 1.0]
params1_init = [1.0, 1.0]
params2_init = [1.0, 1.0]

k = 0
b = 0.052
# Минимизация с учетом ограничений
cons = {'type': 'ineq', 'fun': constraint, 'args': (x, k)}
result = minimize(objective, params_init, args=(x,y), constraints=cons)

a_optimal, b_optimal = result.x

cons = {'type': 'ineq', 'fun': constraint, 'args': (x, k)}
result = minimize(objective, params1_init, args=(x,y1), constraints=cons)

a1_optimal, b1_optimal = result.x

cons = {'type': 'ineq', 'fun': constraint, 'args': (x, k)}
result = minimize(objective, params2_init, args=(x,y2), constraints=cons)

a2_optimal, b2_optimal = result.x




# Погрешность графика
residuals = y - w[0]*x + w[1]
var_res = sum(residuals**2) / (len(x) - 2)
std_err = np.sqrt(var_res / sum((x - np.mean(x))**2))

print(f"Погрешность графика: ±{std_err:.6f}")
'''
residuals = y1 - w1[0]*x1 + w1[1]
var_res = sum(residuals**2) / (len(x1) - 2)
std_err = np.sqrt(var_res / sum((x1 - np.mean(x1))**2))

print(f"Погрешность графика: ±{std_err:.6f}")
'''


# Погрешность коэффициента k
x_bar = np.sum(x)/len(x)
sum_sq_diff = np.sum((x - x_bar)**2)
std_err_k = np.sqrt(var_res / (len(x) * sum_sq_diff))
print(f"Погрешность коэффициента k: ±{std_err_k:.6f}")

# График
fig, ax = plt.subplots()

plt.errorbar(x, y, fmt='+')

# plt.errorbar(x1, y1, xerr=dx, yerr=dy2,  fmt='+')
#plt.errorbar(x, y1, yerr=dy1, fmt='+')
#plt.errorbar(x, y2, yerr=dy2, fmt='+')

#plt.plot(x, w[0]*x + w[1], color='red')

plt.plot(x_values, y_values, color='red')
plt.plot([2.4, 2.4], [0, 1], color='blue')
plt.plot([2.4, 66.5], [0.46, 0.46], color='blue')
plt.plot([66.5, 66.5], [0, 1], color='blue')

#plt.plot(x,(a_optimal)/x+ k*x + b)
#plt.plot(x,(a1_optimal)/x+ k*x + b,label='значение - 2')
#plt.plot(x,(a2_optimal)/x+ k*x + b,label='значение - 1')

#z = (a_optimal)/x+ k*x + b
#print(min(z), max(z))
# plt.plot(x,k*x + 2.7,color='green',linestyle='--')
# plt.plot(x, w[0]*x + w[1], color='red')

'''
plt.plot([0, 25], [0.124, 0.124], color='red')
plt.plot([6.23, 6.23], [0, 3.93], color='blue')

plt.plot([1.031, 1.031], [0.4, 0.7071])
plt.plot([0.978, 0.978], [0.4, 0.7071])
plt.plot([1.021, 1.021], [0.4, 0.7071])
'''
#plt.text(0.0031, -1.15, 'Погрешность: ' + str(residual_error)[:4], color='blue')
title_text = 'Рисунок 3'
ax.set_axisbelow(True)
plt.grid(True, color='lightgray', linestyle='--')
plt.ylabel("V₂")
plt.xlabel("l, см")
plt.legend()
ax.set_title(title_text)

# plt.axis([0.24, 0.41, 93 , 123])

#plt.xscale('log')

#plt.yscale('log')

ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.02))
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.xaxis.set_minor_locator(MultipleLocator(5))

plt.show()