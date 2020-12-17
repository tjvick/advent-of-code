import numpy as np
import math
import re
import collections

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

all_actives = []
all_inactives = []
for ir, row in enumerate(file_contents):
    for ic, char in enumerate(row):
        if (char == '#'):
            all_actives.append((ir, ic, 0))
        else:
            all_inactives.append((ir, ic, 0))


neighbors = []
for ix in [-1, 0, 1]:
    for iy in [-1, 0, 1]:
        for iz in [-1, 0, 1]:
            if not (ix == iy == iz == 0):
                neighbors.append((ix, iy, iz))

new_cubes = set()
all_cubes = all_actives + all_inactives
for cube in all_cubes:
    for neighbor in neighbors:
        target = tuple(np.array(neighbor) + np.array(cube))
        if target not in all_cubes:
            new_cubes.add(target)

print(new_cubes)
print(len(new_cubes), 'new cubes')

all_inactives += list(new_cubes)

print(neighbors)
print(all_actives)
print(all_inactives)
print(len(all_actives), 'active')
print(len(all_inactives), 'inactive')

for ix in range(6):
    print('after', ix+1, 'cycles')
    new_actives = []
    new_inactives = []
    for active_cube in all_actives:
        n_active_neighbors = 0
        for neighbor in neighbors:
            target = tuple(np.array(neighbor) + np.array(active_cube))
            if target in all_actives:
                n_active_neighbors += 1

        if n_active_neighbors == 2 or n_active_neighbors == 3:
            new_actives.append(active_cube)
        else:
            new_inactives.append(active_cube)

    for inactive_cube in all_inactives:
        n_active_neighbors = 0
        for neighbor in neighbors:
            target = tuple(np.array(neighbor) + np.array(inactive_cube))
            if target in all_actives:
                n_active_neighbors += 1

        if n_active_neighbors == 3:
            new_actives.append(inactive_cube)
        else:
            new_inactives.append(inactive_cube)

    print(new_actives)
    print(new_inactives)
    all_actives = new_actives
    all_inactives = new_inactives
    print(len(all_actives), 'active')
    print(len(all_inactives), 'inactive')

    new_cubes = set()
    all_cubes = all_actives + all_inactives
    for cube in all_cubes:
        for neighbor in neighbors:
            target = tuple(np.array(neighbor) + np.array(cube))
            if target not in all_cubes:
                new_cubes.add(target)

    all_inactives += list(new_cubes)
