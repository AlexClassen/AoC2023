from operator import itemgetter
def remove_chars(list_rem):
    new_list = []
    for game in list_rem:
        x = game.replace('T', 'V')
        y = x.replace('J', '1')
        z = y.replace('Q', 'X')
        a = z.replace('K', 'Y')
        b = a.replace('A', 'Z')
        new_list.append(b)
    return new_list
                

def find_type(list_type):
    new_list = list_type
    for game in list_type:
        temp = [0]
        count = 0
        joker = game.split(' ')[0].count('1')
        for card in list(game.split(' ')[0]):
            if card != '1':
                temp.append(game.split(' ')[0].count(card))
        if max(temp)+joker == 5:
            count = 7
        elif max(temp)+joker == 4:
            count = 6
        elif max(temp)+joker == 3:
            if joker == 0 and 2 in temp:
                count = 5
            elif temp.count(2) == 4:
                count = 5
            else:
                count = 4
        elif max(temp)+joker == 2:
            if temp.count(2) == 4:
                count = 3
            else:
                count = 2
        else:
            count = 1
        new_list[list_type.index(game)]=str(count)+new_list[list_type.index(game)]
    return new_list
        

original_list = open('input.txt', 'r').readlines()
new_list = remove_chars(original_list)
new_list = find_type(new_list)
sorted_list = sorted(new_list, key=itemgetter(0, 1, 2, 3, 4, 5))

score = 0
index = 0
for game in sorted_list:
    index += 1
    score += int(game.split(' ')[1])*index

print(score)