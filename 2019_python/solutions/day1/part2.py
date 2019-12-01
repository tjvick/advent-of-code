import math
sum = 0

with open('input.txt', 'r') as f:
    for line in f:
        mass = int(line.strip('\n'))
        added_fuel = math.floor(mass / 3) - 2
        module_sum = added_fuel
        while added_fuel > 0:
            added_fuel = max(math.floor(added_fuel / 3) - 2, 0)
            module_sum += added_fuel

        sum += module_sum

print(sum)
