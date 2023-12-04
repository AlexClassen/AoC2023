datei = open('input.txt', 'r')
list = datei.readlines()
temp, sum = 0, 0
for i in list:
    for j in i.split('|')[1].split(' '):
        if j.strip() in i.split('|')[0].split(':')[1].split(' ') and j.strip().isnumeric():
            temp += 1
    sum += int(pow(2, temp-1))
    temp = 0
print(sum)