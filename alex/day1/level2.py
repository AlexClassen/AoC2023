numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def number(text):
    i = 1
    for num in numbers:
        if text == num:
            return i
        i += 1
    return -1

file = open('input.txt', 'r')
lines = file.readlines()

def getSum(text):
    first = -1
    second = -1
    i = 0
    for c in text:
        if c.isnumeric():
            if first == -1:
                first = c
            else:
                second = c
        else:
            substring = text[i:]
            for num in numbers:
                if substring.startswith(num):
                    if first == -1:
                        first = str(number(num))
                    else:
                        second = str(number(num))
                    break
        i += 1
    if second == -1:
        second = first
    return first + second

sum = 0
for line in lines:
    text = line.strip()
    result = int(getSum(text))
    sum += result
print(sum)