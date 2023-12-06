lines = open('input.txt', 'r').readlines()

time = ''.join(lines[0].split()[1:])
record = ''.join(lines[1].split()[1:])

def possibilitiesToWin(time, record):
    possibilities = 0
    for i in range(time):
        if (time-i) * i > record:
            possibilities += 1
    return possibilities

result = possibilitiesToWin(int(time), int(record))
print(result)