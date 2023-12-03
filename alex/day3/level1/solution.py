def getLines():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def isSymbol(c):
    return not (c.isnumeric() or c == '.')

def hasSymbolAround(x, y):
    lines = getLines()

    middle = lines[y]

    if middle

    #bottom = lines[y+1]
    #top = lines[y-1]

for line in getLines():
    print(line)