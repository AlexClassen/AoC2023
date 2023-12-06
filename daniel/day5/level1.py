list = open('input.txt', 'r').readlines()
seeds = []
for x in list[0].strip().split(' ')[1:]:
    seeds.append(int(x))
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

index = 0
for seed in seeds:
    for a in transformations:
        for b in a:
            if seed >= b[1] and seed < b[1]+b[2]:
                seed = b[0]+(seed-b[1])
                seeds[index] = seed
                break
    index += 1
print(min(seeds))