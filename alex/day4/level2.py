lines = open('input.txt', 'r').readlines()

sum = 0
copies = [1] * len(lines)
index = 0
for line in lines:
    parts = line.split('|')

    winningNumbers = parts[0].split()[2:]
    winningNumbers = [int(num) if '.' not in num else float(num) for num in winningNumbers]

    ourNumbers = parts[1].split()
    ourNumbers = [int(num) if '.' not in num else float(num) for num in ourNumbers]

    amount = 0
    for n in ourNumbers:
        if n in winningNumbers:
            amount += 1

    for i in range(index, index+amount):
        copies[i+1] += copies[index]

    index += 1

for c in copies:
    sum += c
print(f"Answer = {sum}")