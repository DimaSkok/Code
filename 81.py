import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

with open('/home/b03-301/data.txt', 'r') as FtoP:
    data = FtoP.read().split()
FtoP.close()
for i in range(len(data)):
    data[i] = float(data[i])
with open('/home/b03-301/setting.txt', 'r') as FtoP:
    info = FtoP.read().split()
    time = float(info[0])
FtoP.close()
T = time / len(data)
data_t = []
for i in range(len(data)):
    data_t.append(time * i / len(data))
fig, ax = plt.subplots(figsize = (16, 8), dpi = 100)
ax.plot(data_t, data, color='red', label='V(t)')
for i in range(0, len(data), 4):
    ax.scatter(data_t[i], data[i], marker='.', color='red')
ax.set_title('График зав-ти напряжения на конденсаторе от времени', loc='center')
#ax.grid(True, which='both', color='grey')    # сетка
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.grid(True, which='minor', color='#b3b3b3')
ax.yaxis.grid(True, which='major', color='black')
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.grid(True, which='minor', color='#b3b3b3')
ax.xaxis.grid(True, which='major', color='black')
ax.set_xlabel('Время')
ax.set_ylabel('Напряжение')
plt.text(6.6, 0.95, 'Время разрядки = 1.04 с')
plt.text(6.6, 1.05, 'Время зарядки = 7.44 с')
plt.text(-0.47, 2.75, '^')
plt.text(-0.37, 2.74, 'V,В', color='blue')
plt.text(8.85, -0.155, '>')
plt.text(8.85, -0.21, 't,с', color='blue')
ax.legend()
fig.savefig('/home/b03-301/graphic.svg')
plt.show()