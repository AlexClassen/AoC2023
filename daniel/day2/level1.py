def einlesen_games(dateiname):
    colors = [['blue', 'b'], ['red', 'r'], ['green', 'g']]
    datei = open(dateiname, 'r')
    game_list = datei.readlines()
    temp = 0
    game_index = 0
    blue = 0
    red = 0
    green = 0
    possible = 0
    for i in game_list:
        blue = 0
        red = 0
        green = 0
        sub_list = i[i.index(':')+1:]
        game_index += 1
        for k in colors:
            if k[0] in i:
                i = i.replace(k[0], k[1])

        for j in sub_list:
            if j.isnumeric():
                temp = temp*10+int(j)
            elif j == 'b':
                if temp > blue:
                    blue = temp
                temp = 0
            elif j == 'g':
                if temp > green:
                    green = temp
                temp = 0
            elif j == 'r':
                if temp > red:
                    red = temp
                temp = 0
        possible += red*blue*green
    datei.close()
    return possible

print(einlesen_games('input.txt'))