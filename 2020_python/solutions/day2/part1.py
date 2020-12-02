import re

nValid = 0
with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        pattern = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
        m = pattern.match(content)
        minCount = int(m.group(1))
        maxCount = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)

        realCount = password.count(letter)
        if minCount <= realCount <= maxCount:
           nValid += 1

print(nValid)
