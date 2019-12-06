import re

data = dict()

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        pattern = re.compile(r"^(.+)\)(.+)$")
        m = pattern.match(content)
        center = m.group(1)
        orbiter = m.group(2)
        data[orbiter] = center

x = data["YOU"]
you_set = [x]
while x != "COM":
    if x in data:
        x = data[x]
        you_set.insert(0, x)

x = data["SAN"]
san_set = [x]
while x != "COM":
    if x in data:
        x = data[x]
        san_set.insert(0, x)

print(you_set)
print(len(you_set))
print(san_set)
print(len(san_set))

shared_length = 0
for ix, elem in enumerate(you_set):
    if san_set[ix] == elem:
        shared_length += 1
    else:
        break

print(len(you_set) + len(san_set) - 2 * shared_length)