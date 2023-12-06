list = open('test.txt', 'r').readlines()
seeds = []
a = 0
for x in list[0].strip().split(' ')[1:]:
    if a == 0:
        seed = []
        seed.append(int(x))
        a = 1
    else:
        seed .append(int(x))
        seeds.append(seed)
        a = 0

anzahl = 0
for irg in seeds:
    anzahl += irg[1]
print(anzahl)

transformations = []
transformation = []
transform = []
for i in list[3:]:
    for j in i.strip().split():
        if not j.isnumeric():
            transformations.append(transformation)
            transformation = []
            break
        else:
            transform.append(int(j))
    if transform != []:
        transformation.append(transform)
        transform = []
transformations.append(transformation)

minimum = 100000000000
for seed in seeds:
    for see in range(seed[1]):
        print(see)
        temp = seed[0]+see
        for a in transformations:
            for b in a:
                if temp >= b[1] and temp < b[1]+b[2]:
                    temp = b[0]+(temp-b[1])
                    break
        minimum = min(temp, minimum)
print(minimum)