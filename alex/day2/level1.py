def getLines():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

sum = 0
for line in getLines():
    gameSplit = line.split(':')
    gameId = int(gameSplit[0].replace("Game ", ""))
    sets = gameSplit[1].split(';')
    possible = True

    for set in sets:
        cubes = [element.lstrip() for element in set.split(",")]

        for cube in cubes:

            print

            amount = int(cube.split(' ')[0])
            color = cube.split(' ')[1]

            if color == "red" and amount > 12:
                possible = False
            if color == "green" and amount > 13:
                possible = False
            if color == "blue" and amount > 14:
                possible = False

    if possible:
        sum += gameId
    
print(sum)