original_list = open('input.txt', 'r').readlines()
directions = original_list[0].strip()
location_in = []
location_l = []
location_r = []
for i in original_list[2:]:
    location_in.append(i.split('=')[0].strip())
    location_l.append(i.split('=')[1].split(',')[0][2:])
    location_r.append(i.split('=')[1].split(',')[1][1:4])

index_directions = []
for a in location_in:
    if a[2] == 'A':
        index_directions.append(location_in.index(a))
counts = []
for index_direction in index_directions:
    found = False
    count = 0
    while found == False:
        for direction in directions:
            count += 1
            if direction == 'L':
                temp = location_l[index_direction]
                index_direction = location_in.index(temp)
            else:
                temp = location_r[index_direction]
                index_direction = location_in.index(temp)
            if temp[2] == 'Z':
                found = True
                break
    counts.append(count)
max0 = max(counts)
max = max(counts)
found2 = False
while found2 == False:
    for count in counts:
        if (max % count) != 0:
            found2 = False
            max += max0
            break
        else:
            found2 = True
print(max)
