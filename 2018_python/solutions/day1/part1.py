total = 0
with open('input.txt', 'r') as f:
    for line in f:
        val = int(line.strip('\n'))
        total += val

print(total)
