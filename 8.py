import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

with open('E:/Загрузки/volt.txt', 'r') as FtoP:
    data = FtoP.read().split()
FtoP.close()
time = float(data[len(data) - 1][:4])
for i in range(len(data) - 1):
    data[i] = float(data[i][:4])
T = time / len(data)
data_t = []
for i in range(1, len(data) + 1):
    data_t.append(time * i / len(data))
fig, ax = plt.subplots(figsize = (16, 9), dpi = 100)
ax.plot(data_t, data, color='red', label='V(t)')
for i in range(0, len(data), 5):
    ax.scatter(data_t[i], data[i], marker='.', color='red')
ax.set_title('График зав-ти напряжения на конденсаторе от времени', loc='center')
ax.grid(True, which='both', color='grey')    # сетка
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
#plt.text(-0.42, 2.75, '^')
#plt.text(-0.3, 2.74, 'V,В', color='blue')
#plt.text(8.9, 0.08, '>')
#plt.text(8.9, 0.02, 't,с', color='blue')
ax.legend()
fig.savefig('E:/Загрузки/graphic.svg')
plt.show()