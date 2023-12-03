def check (row, column, list, row_count, column_count, temp):
    #print(row_count)
    #print(column_count)
    if row > -1 and row+1 < row_count:
        for i in range(3):
            #print(i)
            if column > -1 and column+1 < column_count:
                for j in range(3):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True
            elif column+1 < column_count:
                for j in range(2):
                    if list[row+i][column+j+1].isnumeric() == False and list[row+i][column+j+1] != '.':
                        return True
            else:
                for j in range(2):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True
    elif row+1 < row_count:
        for i in range(2):
            if column > -1 and column+1 < column_count:
                for j in range(3):
                    if list[row+i+1][column+j].isnumeric() == False and list[row+i+1][column+j] != '.':
                        return True
            elif column+1 < column_count:
                for j in range(2):
                    if list[row+i+1][column+j+1].isnumeric() == False and list[row+i+1][column+j+1] != '.':
                        return True
            else:
                for j in range(2):
                    if list[row+i+1][column+j].isnumeric() == False and list[row+i+1][column+j] != '.':
                        return True
    else:
        for i in range(2):
            if column > -1 and column+1 < column_count:
                for j in range(3):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True
            elif column+1 < column_count:
                for j in range(2):
                    if list[row+i][column+j+1].isnumeric() == False and list[row+i][column+j+1] != '.':
                        return True
            else:
                for j in range(2):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True
    return False
def find_count(dateiname):
    datei = open(dateiname, 'r')
    list = datei.readlines()
    count = 0
    temp = ''
    bool = False
    a = 0
    b = 0
    for i in list:
        b = 0
        for j in i:
            if j.isnumeric():
                temp += j
                if check(a-1, b-1, list, len(list)-1, len(list[0])-2, j):
                    bool = True
                    #print(temp)
            elif temp != '':
                #print (temp)
                if bool != False:
                    print (temp)
                    count += int(temp)
                temp = ''
                bool = False
            b +=1
        a += 1
    datei.close()
    return count

print(find_count('input.txt'))