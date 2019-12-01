import math
sum = 0

with open('input.txt', 'r') as f:
    for line in f:
        mass = int(line.strip('\n'))
        fuel = math.floor(mass / 3) - 2
        sum += fuel

print(sum)
