import numpy as np
import re
from collections import Counter

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

tiles = {}
tile_id = -1
tile_contents = []
for row in file_contents:
    if 'Tile' in row:
        m = re.match(r'^Tile (\d+):$', row)
        tile_id = int(m.group(1))
        tile_contents = []
    elif '.' in row:
        tile_contents.append(row.replace('#', '1').replace('.', '0'))
    else:
        tile_content_matrix = [[int(x) for x in r] for r in tile_contents]
        tiles[tile_id] = np.array(tile_content_matrix)

tile_content_matrix = [[int(x) for x in r] for r in tile_contents]
tiles[tile_id] = np.array(tile_content_matrix)


def stringify(x):
    return ''.join([str(el) for el in list(x)])


def cycle(tile):
    t = tile
    for n_flips in range(2):
        for n_rotates in range(4):
            yield t
            t = np.rot90(t)
        t = np.fliplr(t)


tile_top_rows = {}
all_top_rows = []
for tile_id, tile in tiles.items():
    top_rows = []
    for t in cycle(tile):
        top_rows.append(t[0, :])

    tile_top_rows[tile_id] = [stringify(top_row) for top_row in top_rows]
    all_top_rows += [stringify(top_row) for top_row in top_rows]


top_row_occurrences = dict(Counter(all_top_rows))

corner_tiles = []
for tile_id, top_rows in tile_top_rows.items():
    n_row_duplicates = sum([top_row_occurrences[row] > 1 for row in top_rows])
    if n_row_duplicates == 4:
        corner_tiles.append(tile_id)


print(corner_tiles)
print(np.prod(corner_tiles))