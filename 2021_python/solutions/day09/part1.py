from solutions import helpers
import numpy as np

filename = 'input'

digit_sequences = helpers.read_each_line_as_digit_sequence(filename)

print(digit_sequences)

heatmap = np.array(digit_sequences)

total_risk_levels = 0
for ir, row in enumerate(heatmap):
    for ic, col in enumerate(row):
        print(ir, ic)

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
        print(searchset)
        lowest = min(heatmap[ir, ic] for ir, ic in searchset)
        if lowest > heatmap[ir, ic]:
            risk_level = 1 + heatmap[ir, ic]
            total_risk_levels += risk_level

print(total_risk_levels)


