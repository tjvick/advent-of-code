import re

nValid = 0
with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        pattern = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
        m = pattern.match(content)
        position1 = int(m.group(1))
        position2 = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)

        x = password[position1-1]
        y = password[position2-1]
        if x == letter or y == letter:
            if x != letter or y != letter:
                nValid += 1

print(nValid)
