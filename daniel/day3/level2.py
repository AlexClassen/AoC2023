import re
def ersetze_nicht_passende_elemente(input_string):
    # Ersetze alle Zeichen, die nicht '*', '.', oder eine Zahl sind, durch einen Platzhalter (z.B. Leerzeichen)
    result = re.sub(r'[^*.0-9]', '.', input_string)
    return result
def score_berechnen(rc):
    score = 0
    board = []
    for i in range(140):
        for j in range(139):
            boardtup = []
            boardtup.append(i)
            boardtup.append(j)
            board.append(boardtup)
    for a in rc:
        for b in board:
            if b[0] == a[0] and b[1] == a[1]:
                b.append(a[2])
    for c in board:
        if len(c) == 4:
            score += int(c[2])*int(c[3])
    #print(board)
    return score

def check (row, column, list, row_count, column_count, temp):
    if row > -1 and row+1 < row_count:
        for i in range(3):
            if column > -1 and column+1 < column_count:
                for j in range(3):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True, row+i, column+j
            elif column+1 < column_count:
                for j in range(2):
                    if list[row+i][column+j+1].isnumeric() == False and list[row+i][column+j+1] != '.':
                        return True, row+i, column+j+1
            else:
                for j in range(2):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True, row+i, column+j
    elif row+1 < row_count:
        for i in range(2):
            if column > -1 and column+1 < column_count:
                for j in range(3):
                    if list[row+i+1][column+j].isnumeric() == False and list[row+i+1][column+j] != '.':
                        return True, row+i+1, column+j
            elif column+1 < column_count:
                for j in range(2):
                    if list[row+i+1][column+j+1].isnumeric() == False and list[row+i+1][column+j+1] != '.':
                        return True, row+i+1, column+j+1
            else:
                for j in range(2):
                    if list[row+i+1][column+j].isnumeric() == False and list[row+i+1][column+j] != '.':
                        return True, row+i+1, column+j
    else:
        for i in range(2):
            if column > -1 and column+1 < column_count:
                for j in range(3):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True, row+i, column+j
            elif column+1 < column_count:
                for j in range(2):
                    if list[row+i][column+j+1].isnumeric() == False and list[row+i][column+j+1] != '.':
                        return True, row+i, column+j+1
            else:
                for j in range(2):
                    if list[row+i][column+j].isnumeric() == False and list[row+i][column+j] != '.':
                        return True, row+i, column+j
    return False, 0, 0
def find_count(dateiname):
    datei = open(dateiname, 'r')
    list = datei.readlines()
    m = 0
    for a in list:
        list[m] = ersetze_nicht_passende_elemente(a)
        m += 1
    count = 0
    temp = ''
    bool = False
    a = 0
    b = 0
    rc = []
    for i in list:
        b = 0
        rc2 = []
        for j in i:
            if j.isnumeric():
                temp += j
                bool2, row, column = check(a-1, b-1, list, len(list)-1, len(list[0])-2, j)
                if bool2:
                    bool = True
                    rc2 = [row, column]
            elif temp != '':
                if bool != False:
                    rc2.append(temp)
                    rc.append(rc2)
                    rc2 = []
                temp = ''
                bool = False
            b +=1
        a += 1
    datei.close()
    #print(rc)
    count = score_berechnen(rc)
    return count

print(find_count('input.txt'))