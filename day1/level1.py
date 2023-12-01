import time
def einlesen_himmel(dateiname):
    letter_numbers = [['one', 'one1one'], ['two', 'two2two'], ['three', 'three3three'], ['four', 'four4four'], ['five', 'five5five'], ['six', 'six6six'], ['seven', 'seven7seven'], ['eight', 'eight8eight'], ['nine', 'nine9nine']]
    datei = open(dateiname, 'r')
    himmel_list = datei.readlines()
    himmel_zeilen = []
    for i in himmel_list:
        himmel = []
        for k in letter_numbers:
            if k[0] in i:
                i = i.replace(k[0], k[1])
        for j in i.strip():
            himmel.append(j)
        himmel_zeilen.append(himmel)
    datei.close()
    return himmel_zeilen

def number_finder(himmel):
    vordere_zahl = []
    for i in himmel:
        for j in i:
            if j.isnumeric():
                vordere_zahl.append(int(j)*10)
                break
    a = 0
    for i in himmel:
        for j in range(len(i)):
            if i[len(i)-j-1].isnumeric():
                vordere_zahl[a] += int(i[len(i)-j-1])
                break
        a += 1
    zahl = 0
    for i in vordere_zahl:
        zahl += i
        
    return zahl
    



if __name__ == "__main__":
    start_time = time.time()
    dateiname = 'level1_1.txt'
    himmel = einlesen_himmel(dateiname)
    numbers = number_finder(himmel)
    print(numbers)
    print("--- %s seconds ---" % (time.time() - start_time))