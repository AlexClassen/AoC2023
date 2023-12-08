original_list = open('input.txt', 'r').readlines()
directions = original_list[0].strip()
location_in = []
location_l = []
location_r = []
for i in original_list[2:]:
    location_in.append(i.split('=')[0].strip())
    location_l.append(i.split('=')[1].split(',')[0][2:])
    location_r.append(i.split('=')[1].split(',')[1][1:4])

index_direction = location_in.index('AAA')
count = 0
found = False
while found == False:
    for direction in directions:
        count += 1
        if direction == 'L':
            temp = location_l[index_direction]
            index_direction = location_in.index(temp)
        else:
            temp = location_r[index_direction]
            index_direction = location_in.index(temp)
        if temp == 'ZZZ':
            found = True
            break
print(count)
