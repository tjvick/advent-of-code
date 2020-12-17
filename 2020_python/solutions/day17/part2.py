import numpy as np
from collections import defaultdict

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

all_actives = []
for ir, row in enumerate(file_contents):
    for ic, char in enumerate(row):
        if char == '#':
            all_actives.append((ir, ic, 0, 0))

starting_max_x = len(file_contents)
starting_max_y = len(file_contents[0])

neighbors = []
for ix in [-1, 0, 1]:
    for iy in [-1, 0, 1]:
        for iz in [-1, 0, 1]:
            for iw in [-1, 0, 1]:
                if not (ix == iy == iz == iw == 0):
                    neighbors.append(np.array([ix, iy, iz, iw]))

print('before any cycles:')
print(len(all_actives), 'active')

for ix in range(6):
    print('after', ix+1, 'cycles:')
    new_actives = []
    neighbor_counts = defaultdict(int)
    for active_cube in all_actives:
        for target in neighbors + np.array(active_cube):
            neighbor_counts[tuple(target)] += 1

    for target, n_active_neighbors in neighbor_counts.items():
        if n_active_neighbors == 3:
            new_actives.append(target)
        elif n_active_neighbors == 2 and target in all_actives:
            new_actives.append(target)

    all_actives = new_actives
    print(len(all_actives), 'active')