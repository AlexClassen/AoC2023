import numpy as np
list = open('input.txt', 'r').readlines()
time = ''
for a in list[0].strip().split()[1:]:
    time += a
distance = ''
for a in list[1].strip().split()[1:]:
    distance += a
time = int(time)
distance = int(distance)
h1 = int(time/2 + np.sqrt((time**2)/4-distance))
h2 = int(time/2 - np.sqrt((time**2)/4-distance))
print(h1-h2)