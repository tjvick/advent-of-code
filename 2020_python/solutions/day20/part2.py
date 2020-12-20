import numpy as np
import math
import re
from collections import Counter

def load_tiles():
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

    return tiles


def load_monster():
    with open('sea_monster', 'r') as f:
        monster_contents = [line.strip('\n') for line in f]

    monster = []
    for row in monster_contents:
        monster.append([int(x) for x in row.replace('#', '1').replace('.', '0').replace(' ', '0')])

    return np.array(monster)


def stringify(x):
    return ''.join([str(v) for v in list(x)])


def cycle(tile):
    t = tile
    for n_flips in range(2):
        for n_rotates in range(4):
            yield t
            t = np.rot90(t)
        t = np.fliplr(t)


tiles = load_tiles()
n_tile_per_side = int(math.sqrt(len(tiles)))

tile_top_rows = {}
all_top_rows = []
for tile_id, tile in tiles.items():
    top_rows = []
    for t in cycle(tile):
        top_rows.append(t[0, :])

    tile_top_rows[tile_id] = [stringify(top_row) for top_row in top_rows]
    all_top_rows += [stringify(top_row) for top_row in top_rows]


top_row_occurrences = dict(Counter(all_top_rows))


def get_tile_below(current_tile_id):
    bottom_row = stringify(tiles[current_tile_id][-1, :])
    if top_row_occurrences[bottom_row] == 1:
        return -1

    if top_row_occurrences[bottom_row] > 1:
        for tile_id, top_rows in tile_top_rows.items():
            if bottom_row in top_rows and tile_id != current_tile_id:
                next_tile_id = tile_id

    for t in cycle(tiles[next_tile_id]):
        if stringify(t[0, :]) == bottom_row:
            tiles[next_tile_id] = t
            break

    return next_tile_id


def get_tile_on_right(current_tile_id):
    right_col = stringify(tiles[current_tile_id][:, -1])
    if top_row_occurrences[right_col] == 1:
        return -1

    if top_row_occurrences[right_col] > 1:
        for tile_id, top_rows in tile_top_rows.items():
            if right_col in top_rows and tile_id != current_tile_id:
                next_tile_id = tile_id

    for t in cycle(tiles[next_tile_id]):
        if stringify(t[:, 0]) == right_col:
            tiles[next_tile_id] = t
            break

    return next_tile_id


def build_tile_grid():
    # get corner tiles
    corner_tiles = []
    for tile_id, top_rows in tile_top_rows.items():
        n_row_duplicates = sum([top_row_occurrences[row] > 1 for row in top_rows])
        if n_row_duplicates == 4:
            corner_tiles.append(tile_id)

    # Rotate and flip first corner into place
    for t in cycle(tiles[corner_tiles[0]]):
        bottom_row = stringify(t[-1, :])
        right_col = stringify(t[:, -1])
        if top_row_occurrences[bottom_row] > 1 and top_row_occurrences[right_col] > 1:
            tiles[corner_tiles[0]] = t
            break


    tile_id_grid = np.zeros((n_tile_per_side, n_tile_per_side), dtype=int)
    col_idx = 0
    row_idx = 0

    current_tile_id = corner_tiles[0]
    while current_tile_id > -1:
        while current_tile_id > -1:
            tile_id_grid[row_idx, col_idx] = current_tile_id
            current_tile_id = get_tile_below(current_tile_id)
            row_idx += 1

        current_tile_id = get_tile_on_right(tile_id_grid[0, col_idx])

        row_idx = 0
        col_idx += 1

    return tile_id_grid


def build_photo(tile_id_grid):
    trimmed_tiles = {}
    for tile_id, tile in tiles.items():
        trimmed_tiles[tile_id] = tile[1:-1, 1:-1]

    tile_size = trimmed_tiles[tile_id].shape[0]
    photo = np.zeros((tile_size * n_tile_per_side, tile_size * n_tile_per_side))
    for row_idx in range(n_tile_per_side):
        for col_idx in range(n_tile_per_side):
            photo[row_idx*tile_size:(row_idx+1)*tile_size, col_idx*tile_size:(col_idx+1)*tile_size] = trimmed_tiles[tile_id_grid[row_idx, col_idx]]

    return photo


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

    sea_roughness = np.sum(photo) - monster_count * monster_sum
    return monster_count, sea_roughness


tile_id_grid = build_tile_grid()
photo = build_photo(tile_id_grid)

monster = load_monster()

for p in cycle(photo):
    monster_count, sea_roughness = count_monsters(p, monster)
    if monster_count > 0:
        print(sea_roughness)
