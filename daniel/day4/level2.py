datei = open('input.txt', 'r')
list = datei.readlines()
temp, sum = 0, 0
number_of_cards = [1] * len(list)
for i in list:
    for j in i.split('|')[1].split(' '):
        if j.strip() in i.split('|')[0].split(':')[1].split(' ') and j.strip().isnumeric():
            temp += 1
    for k in range(number_of_cards[list.index(i)]):
        for l in range(temp):
            number_of_cards[list.index(i)+1+l] += 1
    temp = 0
for m in number_of_cards:
    sum += m
print(sum)