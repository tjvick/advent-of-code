from collections import defaultdict

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

garden_map = helpers.read_as_2d_array_of_characters(filepath, dtype=str)

plant_type_regions = defaultdict(list)
assigned_plots = set()

region_id_counter = 0
plant_regions = {}


neighbor_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def inbounds(idx_row, idx_col):
    if (
        0 <= idx_row < garden_map.shape[0] and
        0 <= idx_col < garden_map.shape[1]
    ):
        return True

def walk_region(ix_r, ix_c, plant_type):
    region = {(ix_r, ix_c)}
    region_edges = [(ix_r, ix_c)]
    fence_count = 0
    while len(region_edges) > 0:
        edge_plot = region_edges.pop()
        for (dr, dc) in neighbor_directions:
            neighbor_loc = (edge_plot[0] + dr, edge_plot[1] + dc)
            if not inbounds(*neighbor_loc):
                fence_count += 1
                continue

            neighbor_plot = garden_map[*neighbor_loc]
            if neighbor_plot == plant_type:
                if neighbor_loc in region:
                    continue
                else:
                    region.add(neighbor_loc)
                    region_edges.append(neighbor_loc)
            else:
                fence_count += 1

    return region, fence_count

for ix_row, row in enumerate(garden_map):
    for ix_col, plot in enumerate(row):
        if (ix_row, ix_col) in assigned_plots:
            continue
        else:
            new_region, fence_count = walk_region(ix_row, ix_col, plot)

            plant_type_regions[plot].append(new_region)
            assigned_plots.update(new_region)

            plant_regions[region_id_counter] = {
                'plant_type': str(plot),
                'area': len(new_region),
                'perimiter': fence_count,
                'cost': len(new_region) * fence_count,
                'plots': new_region
            }
            region_id_counter += 1


total_cost = sum(plant_region['cost'] for plant_region in plant_regions.values())
print(total_cost)

