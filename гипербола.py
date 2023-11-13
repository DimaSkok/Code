import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

data = []
with open('E:/Загрузки/volt4.txt', 'r') as FtoP:
    data1 = FtoP.read().split()
FtoP.close()
for i in range(len(data1) - 1):
    data.append(data1[i])
time = int(data1[len(data1) - 1][:2])
for i in range(len(data)):
    data[i] = float(data[i][:4]) * 78.1 - (i) / 13      # коэффициенты тут
T = time / len(data)
print(len(data))
data_t = []
data_t1 = []
counter = 0
data2 = []
data3 = []
data_t3 = []
for i in range(1, len(data) + 1):
    data_t.append(time * i / len(data))
for i in range(len(data_t)):
    if data_t[i] >= 1.4:    # время простоя
        data_t1.append(data_t[i])
        counter += 1
for i in range(len(data) - counter, len(data)):
    data2.append(data[i])
for i in range(0, len(data) - counter):
    data3.append(data[i])
for i in range(0, len(data) - counter):
    data_t3.append(data_t[i])
t = np.polyfit(data_t1, data2, 6)
f = np.poly1d(t)
t1 = np.polyfit(data_t3, data3, 1)
f1 = np.poly1d(t1)

a, at = [data_t1[0], data_t1[6]], [(data2[0]), (data2[6])]      # прямая
k, kt = a[1] - a[0], at[1] - at[0]
for i in range(1, len(data_t1)):
    a.append(a[i] + k)
    at.append(at[i] + kt)
fig, ax = plt.subplots(figsize = (16, 9), dpi = 100)
ax.plot(data_t, data3 + data2, data_t1, f(data_t1), color='red')
ax.plot(data_t, f1(data_t), color='black', linewidth=1)
ax.plot(a, at, color='black', linewidth=1)
ax.set_title('График зав-ти высоты воды в ёмкости от времени', loc='center')
ax.grid(True, which='both', color='grey')    # сетка
plt.axis([0, 16.2, 8, 101])
plt.text(14.8, 99, 'V = 99 см/с', color='blue')     # скорость
ax.plot(1.4, 95.65, '.', color='blue')  # точка
ax.set_xlabel('Время')
ax.set_ylabel('Высота воды')
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.legend()
fig.savefig('E:/Загрузки/graphic4.svg')
plt.show()