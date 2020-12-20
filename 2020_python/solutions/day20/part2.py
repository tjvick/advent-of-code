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

# print(tiles)

def stringify(x):
    return ''.join([str(v) for v in list(x)])


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

    tile_top_rows[id] = [stringify(x) for x in top_rows]
    all_top_rows += [stringify(x) for x in top_rows]


print(tile_top_rows)

c = dict(Counter(all_top_rows))
print(c)

corner_tiles = []
for id, top_rows in tile_top_rows.items():
    n_duplicates = 0
    for row in top_rows:
        if c[row] > 1:
            n_duplicates += 1

    if n_duplicates == 4:
        corner_tiles.append(id)

print(corner_tiles)


def get_tile_below(current_tile_id):
    bottom_row = stringify(tiles[current_tile_id][-1, :])
    if c[bottom_row] == 1:
        return -1

    if c[bottom_row] > 1:
        for id, top_rows in tile_top_rows.items():
            if bottom_row in top_rows and id != current_tile_id:
                next_tile_id = id

    idx = tile_top_rows[next_tile_id].index(bottom_row)
    next_tile_top_row = stringify(tiles[next_tile_id][0, :])
    if idx >= 4:
        tiles[next_tile_id] = np.fliplr(tiles[next_tile_id])

    while next_tile_top_row != bottom_row:
        tiles[next_tile_id] = np.rot90(tiles[next_tile_id])
        next_tile_top_row = stringify(tiles[next_tile_id][0, :])

    return next_tile_id


def get_tile_right_of(current_tile_id):
    print(current_tile_id)
    right_col = stringify(tiles[current_tile_id][:, -1])
    if c[right_col] == 1:
        return -1

    if c[right_col] > 1:
        for id, top_rows in tile_top_rows.items():
            if right_col in top_rows and id != current_tile_id:
                next_tile_id = id

    idx = tile_top_rows[next_tile_id].index(right_col)
    next_tile_left_col = stringify(tiles[next_tile_id][:, 0])
    if idx < 4:
        tiles[next_tile_id] = np.fliplr(tiles[next_tile_id])

    while next_tile_left_col != right_col:
        tiles[next_tile_id] = np.rot90(tiles[next_tile_id])
        next_tile_left_col = stringify(tiles[next_tile_id][:, 0])

    return next_tile_id



n_per_side = int(math.sqrt(len(tiles)))
tile_id_grid = np.zeros((n_per_side, n_per_side), dtype=int)
col_idx = 0
row_idx = 0


# Rotate and flip first corner into place
current_tile_id = corner_tiles[0]
bottom_row = stringify(tiles[current_tile_id][-1, :])
while c[bottom_row] == 1:
    tiles[current_tile_id] = np.rot90(tiles[current_tile_id])
    bottom_row = stringify(tiles[current_tile_id][-1, :])

right_col = stringify(tiles[current_tile_id][:, -1])
while c[right_col] == 1:
    tiles[current_tile_id] = np.fliplr(tiles[current_tile_id])
    right_col = stringify(tiles[current_tile_id][:, -1])

# Build tile grid
while current_tile_id > -1:
    while current_tile_id > -1:
        tile_id_grid[row_idx, col_idx] = current_tile_id
        current_tile_id = get_tile_below(current_tile_id)
        row_idx += 1

    current_tile_id = get_tile_right_of(tile_id_grid[0, col_idx])

    row_idx = 0
    col_idx += 1

print(tile_id_grid)


def build_photo(tile_id_grid):
    shrunken_tiles = {}
    for id, tile in tiles.items():
        shrunken_tiles[id] = tile[1:-1, 1:-1]

    n_pixels = shrunken_tiles[id].shape[0]
    photo = np.zeros((shrunken_tiles[id].shape[0]*n_per_side, shrunken_tiles[id].shape[1]*n_per_side))

    row_idx = 0
    col_idx = 0
    while col_idx < n_per_side:
        while row_idx < n_per_side:
            photo[row_idx*n_pixels:(row_idx+1)*n_pixels, col_idx*n_pixels:(col_idx+1)*n_pixels] = shrunken_tiles[tile_id_grid[row_idx, col_idx]]
            row_idx += 1

        row_idx = 0
        col_idx += 1

    return photo

photo = build_photo(tile_id_grid)
# print(photo)

with open('sea_monster', 'r') as f:
    monster_contents = [line.strip('\n') for line in f]

monster = []
for row in monster_contents:
    monster.append([int(x) for x in row.replace('#', '1').replace('.', '0').replace(' ', '0')])

monster = np.array(monster)

# print(monster)

def count_monsters(photo, monster):
    monster_shape = monster.shape
    photo_shape = photo.shape

    monster_sum = np.sum(monster)

    monster_count = 0
    for row_idx in range(photo_shape[0] - monster_shape[0] + 1):
        for col_idx in range(photo_shape[1] - monster_shape[1] + 1):
            window = photo[row_idx:row_idx+monster_shape[0], col_idx:col_idx+monster_shape[1]]
            if np.sum(window * monster) == monster_sum:
                monster_count += 1

    sea = np.sum(photo) - monster_count * monster_sum
    return monster_count, sea


monster_count, sea = count_monsters(photo, monster)
n_flips = 0
while monster_count == 0 and n_flips <= 2:
    n_flips += 1
    photo = np.fliplr(photo)
    monster_count, sea = count_monsters(photo, monster)

    n_rotations = 0
    while monster_count == 0 and n_rotations < 4:
        n_rotations += 1
        photo = np.rot90(photo)
        monster_count, sea = count_monsters(photo, monster)


print(count_monsters(photo, monster))
