import re
import collections

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
    n_members = len(group)
    full_group = "".join(group)
    c = dict(collections.Counter(full_group))
    all_yes = [item[1] == n_members for item in c.items()]
    total += sum(all_yes)

print(total)
