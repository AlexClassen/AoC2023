lines = open('input.txt', 'r').readlines()

sum = 0

def arrizer(arrays):
    global sum
    lastArray = arrays[-1]
    if set(lastArray) == {0}:
        amountOfArrays = len(arrays)
        first = 0
        for i in range(amountOfArrays):
            array = arrays[amountOfArrays-i-1]
            first = array[0] - first
            array.insert(0,first)
            if i == amountOfArrays - 1:
                sum += first
    else:
        newArray = [None] * (len(lastArray)-1)
        for i in range(len(lastArray)-1):
            newArray[i] = int(lastArray[i+1])-int(lastArray[i])
        arrays.append(newArray)
        arrizer(arrays)

for line in lines:
    array = [int(num) for num in line.split(' ')]
    arrizer([array])
print(sum)