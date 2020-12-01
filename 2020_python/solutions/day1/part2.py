values = []
with open('input.txt', 'r') as f:
    for line in f:
        value = int(line.strip('\n'))
        values.append(value)

for value1 in values:
    for value2 in values:
        for value3 in values:
            if (value1 + value2 + value3) == 2020:
                print(value1 * value2 * value3)