original_list = open('input.txt', 'r').readlines()
initial_list = [line.split() for line in original_list]
#print(initial_list)
score = 0
for value in initial_list:
    value_list = []
    zero_list = False
    temp_list = [int(i) for i in value]
    while zero_list == False:
        temp_list2 = []
        value_list.append(temp_list[0])
        for hist in range(1, len(temp_list)):
            temp_list2.append(temp_list[hist]-temp_list[hist-1])
        temp_list = temp_list2
        for a in temp_list:
            if a == 0:
                zero_list = True
            else:
                zero_list = False
                break
    temp = 0
    for number in reversed(value_list):
        temp = number - temp
    score += temp
print(score)