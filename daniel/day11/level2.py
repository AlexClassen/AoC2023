def check_distance(galaxy1, galaxy2, lines, columns):
    distance = abs(galaxy2[0]-galaxy1[0]) + abs(galaxy2[1]-galaxy1[1])
    for line in range(galaxy1[0], galaxy2[0]):
        if lines[line] == True:
            distance += 999999
    for column in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])):
        if columns[column] == True:
            distance += 999999
    return distance

original_list = open('input.txt', 'r').readlines()
lines = [True for b in original_list]
columns = [True for a in range(len(original_list[0].strip()))]
galaxys = []
ind1 = 0
for i in original_list:
    ind2 = 0
    for j in i:
        if j == '#':
            galaxys.append([ind1, ind2])
            lines[ind1] = False
            columns[ind2] = False
        ind2 += 1
    ind1 += 1

score = 0
for galaxy in galaxys:
    for a in range(galaxys.index(galaxy)+1, len(galaxys)):
        score += check_distance(galaxy, galaxys[a], lines, columns)

print(score)