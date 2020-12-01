values = []
with open('input.txt', 'r') as f:
    for line in f:
        value = int(line.strip('\n'))
        values.append(value)

values.sort()
print(values)

for value1 in values:
    for value2 in values:
        if (value1 + value2) == 2020:
            print(value1 * value2)