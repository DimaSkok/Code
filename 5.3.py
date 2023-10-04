import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DAC = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(DAC, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
GPIO.output(DAC, 0)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds,GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
    
def sar_adc():
    bin_val=[0, 0, 0, 0, 0, 0, 0, 0]
    res = 0
    for i in range(0,8):
        bin_val[i]=1
        GPIO.output(DAC,bin_val)
        time.sleep(0.005)
        if GPIO.input(comp) == 1:
            bin_val[i] = 0
    for i in range(8):
        res += bin_val[i] * 2 ** (7 - i)
    return res

try:
    while(True):
        num_leds = int((sar_adc() + 3) / 256 * 8)
        print("V", (sar_adc() / 256 * 3.3), sar_adc(), num_leds)
        GPIO.output(leds, [0] * (8 - num_leds) + [1] * num_leds)

finally:
    GPIO.output(DAC, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()