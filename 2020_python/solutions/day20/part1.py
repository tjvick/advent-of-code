import numpy as np
import math
import re
from collections import Counter

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

tiles = {}
for row in file_contents:
    if 'Tile' in row:
        m = re.match(r'^Tile (\d+):$', row)
        tile_id = int(m.group(1))
        tile_contents = []
    elif '.' in row:
        tile_contents.append(row.replace('#', '1').replace('.', '0'))
    else:
        mat = []
        for r in tile_contents:
            mat.append([int(x) for x in r])
        tiles[tile_id] = np.array(mat)

mat = []
for r in tile_contents:
    mat.append([int(x) for x in r])
tiles[tile_id] = np.array(mat)

print(tiles)

tile_top_rows = {}
all_top_rows = []
for id, tile in tiles.items():
    top_rows = []
    t = tile
    top_rows.append(t[0][:])
    for ix in range(3):
        t = np.rot90(t)
        top_rows.append(t[0][:])
    t = np.fliplr(tile)
    top_rows.append(t[0][:])
    for ix in range(3):
        t = np.rot90(t)
        top_rows.append(t[0][:])

    tile_top_rows[id] = [''.join([str(v) for v in list(x)]) for x in top_rows]
    all_top_rows += [''.join([str(v) for v in list(x)]) for x in top_rows]


print(tile_top_rows)
print(all_top_rows)

all_stringified_top_rows = [''.join([str(v) for v in list(x)]) for x in all_top_rows]
print(all_stringified_top_rows)

c = dict(Counter(all_stringified_top_rows))
print(c)

corner_tiles = []
for id, tile_top_rows in tile_top_rows.items():
    tile_stringified_top_rows = [''.join([str(v) for v in list(x)]) for x in tile_top_rows]
    n_duplicates = 0
    print(id)
    for row in tile_stringified_top_rows:
        # print(row)
        # print(c[row])
        if c[row] > 1:
            n_duplicates += 1

    if n_duplicates == 4:
        corner_tiles.append(id)


print(corner_tiles)
print(np.prod(corner_tiles))