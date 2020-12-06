import re

with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

groups = []
group = []
with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        group.append(content)

        m = re.match(r"^$", content)
        if m:
            groups.append(group[:-1])
            group = []

groups.append(group)

total = 0
for group in groups:
    full_group = "".join(group)
    unique_group = "".join(set(full_group))
    total += len(unique_group)

print(total)