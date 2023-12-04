def getLines():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

lines = getLines()

def hasSymbolAround(x, y):
    rows, cols = len(lines), len(lines[0])
    for i in range(max(0,x-1), min(cols,x+2)):
        for j in range(max(0,y-1), min(rows,y+2)):
            if not lines[j][i].isnumeric() and lines[j][i] != '.':
                return True
    return False

sum = 0
lineIndex = 0
for line in lines:
    currentNumber = ""
    hasSymbol = False

    x = 0
    for c in line:
        hasSymbol = hasSymbol or hasSymbolAround(x, lineIndex)
        if not c.isnumeric():
            if hasSymbol and currentNumber.lstrip().isnumeric():
                sum += int(currentNumber)
            currentNumber = ""
            hasSymbol = False
        else:
            currentNumber += c
        x += 1

    lineIndex += 1
print("Result: " + str(sum))