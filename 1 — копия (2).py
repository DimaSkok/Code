from scipy.io import wavfile
from scipy.signal import hilbert, resample
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

rate = 2080 * 2
samplerate, data = wavfile.read('signal (1).wav')
data = np.array(data, dtype=float)
data = data - 128
data = data / 128
data_h = hilbert(data)
A_data_h = np.abs(data_h)

resampled = resample(A_data_h, int(A_data_h.shape[0] * rate / samplerate))
normalized = ((resampled - min(resampled)) / ((max(resampled) - min(resampled))))

A_data_h = normalized

synh = np.array((0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0)) * 255
skip = 909
high = len(A_data_h) // 2080
x = len(A_data_h) - high * 2080

NA_data_h = A_data_h[:-x]

data_temp = NA_data_h * 255
data = data_temp.astype(int).reshape(-1, 2080)

checker = True
for i in range(high):
    for j in range(5512):
        flag = False
        check = data[i][j:j + 40] == synh
        for ch in synh:
            checker = checker and ch
        if (checker == True) and (flag == False):
            j += skip
        if (checker == True):
            data[i] = data[i][j:-1].append(data[i][0:j])





plt.imshow(data, cmap='gray', aspect='auto')
plt.axis('off')
plt.show()





#figsize = (16, 5)
#plt.figure(figsize=figsize)
#plt.plot(data[229*samplerate: 230*samplerate])
#plt.plot(data_h[229*samplerate: 230*samplerate])
#plt.plot(A_data_h)
#plt.show()
