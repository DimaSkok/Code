import RPi.GPIO as GP

GP.setmode(GP.BCM)
gpio = [2, 3, 4, 17, 27, 22, 10, 9]
print(gpio + gpio)
for i in gpio:
    GP.setup(i, GP.OUT)
    GP.output(i, 1)
    for j in range(1000000):
        pass
    GP.output(i, 0)