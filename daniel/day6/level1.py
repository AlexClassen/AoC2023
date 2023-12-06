list = open('input.txt', 'r').readlines()
time = list[0].strip().split()[1:]
distance = list[1].strip().split()[1:]
score = 1
for a in range(len(time)):
    temp = 0
    for ms in range(int(time[a])):
        if (int(time[a])-ms)*ms > int(distance[a]):
            #print(time[a], ' time', ms, 'button', distance[a], 'distance')
            temp += 1
    score *= temp
print(score)