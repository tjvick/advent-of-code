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

n_total_orbits = 0
for orbiter, center in data.items():
    n_orbits = 1
    x = center
    while x != "COM":
        print(x)
        if x in data:
            x = data[x]
            n_orbits += 1

    n_total_orbits += n_orbits

print(n_total_orbits)

