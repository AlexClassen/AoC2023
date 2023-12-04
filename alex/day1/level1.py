file = open('input.txt', 'r')
lines = file.readlines()

def getSum(text):
    first = -1
    second = -1
    for c in text:
        if c.isnumeric():
            if first == -1:
                first = c
            else:
                second = c
    if second == -1:
        second = first
    return first + second

sum = 0
for line in lines:
    text = line.strip()
    result = int(getSum(text))
    sum += result
print(sum)