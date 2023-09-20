import RPi.GPIO as GP

GP.setmode(GP.BCM)
gpio = [2, 3, 4, 17, 27, 22, 10, 9]
gpio_m = [21, 20, 26, 16, 19, 25, 23, 24]
while True:
    for i in range(8):
        GP.setup(gpio[i], GP.OUT)
        GP.setup(gpio_m[i], GP.IN)
        GP.output(gpio[i], GP.input(gpio_m[i]))
    i = 0
    break
