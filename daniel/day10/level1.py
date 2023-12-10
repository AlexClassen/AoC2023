original_list = open('input.txt', 'r').readlines()
distance = 0
def find_direction(original_list, position, last_position):
    dir_dic = {
        '|01' : 'up', '|0-1' : 'down', '-10' : 'left', '--10' : 'right',
        'L0-1' : 'right', 'L10' : 'up', 'J0-1' : 'left', 'J-10' : 'up',
        '701' : 'left', '7-10' : 'down', 'F01' : 'right', 'F10' : 'down',
        'S01' : 'stop', 'S0-1' : 'stop', 'S10' : 'stop', 'S-10' : 'stop', 
               }
    return dir_dic[original_list[position[0]][position[1]] + str(last_position[1]-position[1]) + str(last_position[0]-position[0])]

def find_next(position, direction):
    if direction == 'up':
        return [position[0]-1,position[1]]
    elif direction == 'down':
        return [position[0]+1,position[1]]
    elif direction == 'left':
        return [position[0],position[1]-1]
    elif direction == 'right':
        return [position[0],position[1]+1]

def find_start(original_list):
    for a in original_list:
        if 'S' in a:
            direction = 'left'
            return [original_list.index(a), a.index('S')], direction

position, direction = find_start(original_list)
while True:
    last_position = position
    position = find_next(position, direction)
    direction = find_direction(original_list, position, last_position)
    distance += 1
    if direction == 'stop':
        break


print(distance/2)