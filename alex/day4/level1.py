lines = open('input.txt', 'r').readlines()

sum = 0
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

    if amount != 0:
        sum += pow(2, max(0,amount-1))

print(f"Answer = {sum}")