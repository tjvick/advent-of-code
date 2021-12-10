from solutions import helpers
import numpy as np

filename = 'input'

digit_sequences = helpers.read_each_line_as_digit_sequence(filename)

print(digit_sequences)

heatmap = np.array(digit_sequences)

basins = []
merges = []
for ir, row in enumerate(heatmap):
    for ic, col in enumerate(row):
        if heatmap[ir, ic] == 9:
            continue

        neighbors = [
            [ir - 1, ic],
            [ir + 1, ic],
            [ir, ic + 1],
            [ir, ic - 1],
        ]

        mask = [1, 1, 1, 1]
        if ir == 0:
            mask[0] = 0
        if ir == heatmap.shape[0]-1:
            mask[1] = 0
        if ic == 0:
            mask[3] = 0
        if ic == heatmap.shape[1]-1:
            mask[2] = 0

        searchset = [indices for ix, indices in enumerate(neighbors) if mask[ix] == 1]

        ix_basins_with_neighbors = []
        for irn, icn in searchset:
            for ixb, basin in enumerate(basins):
                if (irn, icn) in basin:
                    ix_basins_with_neighbors.append(ixb)

        if len(ix_basins_with_neighbors) == 1:
            basins[ix_basins_with_neighbors[0]].append((ir, ic))
        elif len(ix_basins_with_neighbors) > 0:
            basins[ix_basins_with_neighbors[0]].append((ir, ic))
            combined = []
            for ixb in ix_basins_with_neighbors:
                combined.extend(basins[ixb])
                basins[ixb] = []
            basins.append(combined)
        else:
            basins.append([(ir, ic)])


print(len(basins))
print([len(basin) for basin in basins])
gen = reversed(sorted([len(basin) for basin in basins]))
print(next(gen) * next(gen) * next(gen))

