def getLines():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

sum = 0
for line in getLines():
    gameSplit = line.split(':')
    gameId = int(gameSplit[0].replace("Game ", ""))
    sets = gameSplit[1].split(';')

    dict = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        cubes = [element.lstrip() for element in set.split(",")]

        for cube in cubes:
            amount = int(cube.split(' ')[0])
            color = cube.split(' ')[1]

            if amount > dict[color]:
                dict[color] = amount

    power = 1
    for key in dict:
        power *= dict[key]

    sum += power

print(sum)