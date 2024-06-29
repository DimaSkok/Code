from scipy.io import wavfile
from scipy.signal import hilbert, resample
import matplotlib.pyplot as plt
import numpy as np

rate = 2080
samplerate, data = wavfile.read('lw2.wav')

data = np.array(data, dtype=float)
data += 32768
data //= 256
data = data - 128
data = data / 128
data_h = hilbert(data)
A_data_h = np.abs(data_h)



resampled = resample(A_data_h, int(A_data_h.shape[0] * rate * 2 / samplerate))
A_data_h = ((resampled - min(resampled)) / (max(resampled) - min(resampled)))


high = len(A_data_h) // rate
x = len(A_data_h) - high * rate
NA_data_h = A_data_h[:-x]
data_temp = NA_data_h * 255
data_pre = data_temp.astype(int).reshape(-1, rate)

'''
plt.imshow(data_pre, cmap='gray', aspect='auto')
plt.axis('off')
plt.show()
'''

sync = '00001100110011001100110011001100'
sync_arr = np.array([int(bit) - 0.5 for bit in sync])

data = np.zeros((high, rate), dtype=int)

for i in range(201):
    scalar_products = np.zeros((2080 - len(sync_arr)))
    for j in range(rate - len(sync_arr)):
        check = data_pre[i][j:j + len(sync_arr)]
        scalar_products[j] = np.dot(check, sync_arr)
    max_index = np.argmax(scalar_products)
    data[i] = np.roll(data_pre[i], -max_index, axis=0)


sync = '000011000110001100011000110001100011000'
sync_arr = np.array([int(bit) - 0.5 for bit in sync])

for i in range(200, high):
    scalar_products = np.zeros((2080 - len(sync_arr)))
    for j in range(rate - len(sync_arr)):
        check = data_pre[i][j:j + len(sync_arr)]
        scalar_products[j] = np.dot(check, sync_arr)
    max_index = np.argmax(scalar_products)
    data[i] = np.roll(data_pre[i], -max_index, axis=0)
for i in range(200, high):
    data[i] = np.roll(data[i], -1040, axis=0)



min_val = np.min(data[200][30:80])
max_val = np.max(data[200][1080:1126])

data = np.array((data - min_val) * 255 / (max_val - min_val), dtype=int)

for i in range(high):
    for j in range(rate):
        if data[i][j] <= 0: data[i][j] = 0
        if data[i][j] >= 255: data[i][j] = 255


"""
res = np.zeros((39))
for i in range(76, 177):
    res += data[i][0:39]
res = res / 100
res = np.array(res, dtype=int)
print(res)
print(sync)
"""
for i in range(high):
    plt.imshow(data[i][30:80], cmap='gray', aspect='auto')


plt.axis('off')
plt.show()