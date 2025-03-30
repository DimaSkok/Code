import random as rand

data = []

for i in range(45 * 16):
    data.append((int(rand.randint(0, 255))))
print(data)