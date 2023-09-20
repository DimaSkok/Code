import RPi.GPIO as GP

GP.setmode(GP.BCM)
gpio = [8, 11, 7, 1, 0, 5, 12, 6]
num_d = [1, 0, 1, 0, 1, 0, 1, 0]
for i in range(8):
    GP.setup(gpio[i], GP.OUT)
    GP.output(gpio[i], num_d[i])