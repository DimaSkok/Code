import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import wave


interval = 11025

w = wave.open('signal (1).wav', 'r')
for i in range(0, w.getnframes(), interval):
    frame = w.readframes(i)
    plt.plot(i, frame)


plt.show()