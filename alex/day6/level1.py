lines = open('input.txt', 'r').readlines()

times = lines[0].split()[1:]
distances = lines[1].split()[1:]

def possibilitiesToWin(time, record):
    possibilities = 0
    for i in range(time):
        if (time-i) * i > record:
            possibilities += 1
    return possibilities

result = 1
for time, record in zip(times, distances):
    result *= possibilitiesToWin(int(time), int(record))
print(result)