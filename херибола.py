import matplotlib.pyplot as math
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DAC = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [9, 10, 22, 27, 17, 4, 3, 2]
data = []
comp = 14
troyka = 13
GPIO.setup(DAC, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
GPIO.output(DAC, 0)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
    
def sar_adc():
    bin_val=[0, 0, 0, 0, 0, 0, 0, 0]
    res = 0
    for i in range(8):
        bin_val[i] = 1
        GPIO.output(DAC, bin_val)
        time.sleep(0.003)
        if GPIO.input(comp) == 1:
            bin_val[i] = 0
    for i in range(8):
        res += bin_val[i] * 2 ** (7 - i)
    return res

def voltage(num):
    return float('{:.4f}'.format(int(num) / 255 * 3.3))

try:
    GPIO.output(troyka, 1)
    print('charge')
    time_start = time.time()
    while(sar_adc() <= 206):
        value = sar_adc() / 256 * 3.3
        data.append((str(value)))
    GPIO.output(troyka, 0)
    print('discharge')
    while(sar_adc() >= 193):
        value = sar_adc() / 256 * 3.3
        data.append((str(value)))
    time_stop = time.time()
    print('stop')
    time_data = time_stop - time_start
    with open('/home/b03-301/data.txt', 'w') as f:
        f.write('\n'.join(data))
    f.close()
    cur = 1 / 255 * 3.3
    with open('/home/b03-301/setting.txt', 'w') as f:
        f.write('время ' + str(time_data) + ' sec' + '\n' + 'шаг квантования  ' + str(cur) + ' V' + '\n' + 'Частота дискретизации ' + str(1 / (time_data / len(data))) + ' Hz')
    f.close()
    math.plot(data)
    math.show()
    
finally:
    GPIO.output(DAC, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()