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

def compute_fence_segment(direction, a_loc, b_loc):
    a_row, a_col = a_loc
    b_row, b_col = b_loc
    if direction in [(1, 0), (-1, 0)]:
        row_val = max(a_row, b_row)
        endpoints = [(row_val, a_col), (row_val, a_col + 1)]
    else:
        col_val = max(a_col, b_col)
        endpoints = [(a_row, col_val), (a_row+1, col_val)]

    fence_segment = {
        'normal': direction,
        'endpoints': endpoints
    }

    return fence_segment

def fences_to_sides(fence_segments):
    sides = []

    current_side = fence_segments.pop(0)
    current_endpoint = current_side['endpoints'][1]

    while len(fence_segments) > 0:

        try:
            next_fence = next(f for f in fence_segments if current_endpoint in f['endpoints'])
        except StopIteration:
            break

        if current_side['normal'] == next_fence['normal']:
            fence_segments.remove(next_fence)

            curr_minus_next = set(current_side['endpoints']).difference(next_fence['endpoints'])
            next_minus_curr = set(next_fence['endpoints']).difference(current_side['endpoints'])

            current_side['endpoints'] = list(curr_minus_next.union(next_minus_curr))
            current_endpoint = next(e for e in next_fence['endpoints'] if e != current_endpoint)
        else:
            fence_segments.remove(next_fence)

            sides.append(current_side)

            current_side = next_fence
            current_endpoint = next(e for e in next_fence['endpoints'] if e != current_endpoint)

    if current_side['normal'] == sides[0]['normal']:
        curr_minus_next = set(current_side['endpoints']).difference(sides[0]['endpoints'])
        next_minus_curr = set(sides[0]['endpoints']).difference(current_side['endpoints'])
        current_side['endpoints'] = list(curr_minus_next.union(next_minus_curr))
    else:
        sides.append(current_side)

    if len(fence_segments) > 0:
        return sides + fences_to_sides(fence_segments)

    return sides


def walk_region(ix_r, ix_c, plant_type):
    region = {(ix_r, ix_c)}
    region_edges = [(ix_r, ix_c)]
    region_fence_segments = []
    while len(region_edges) > 0:
        edge_plot = region_edges.pop()
        for (dr, dc) in neighbor_directions:
            neighbor_loc = (edge_plot[0] + dr, edge_plot[1] + dc)
            if not inbounds(*neighbor_loc):
                fence_segment = compute_fence_segment((dr, dc), edge_plot, neighbor_loc)
                region_fence_segments.append(fence_segment)
                continue

            neighbor_plot = garden_map[*neighbor_loc]
            if neighbor_plot == plant_type:
                if neighbor_loc in region:
                    continue
                else:
                    region.add(neighbor_loc)
                    region_edges.insert(0,neighbor_loc)
            else:
                fence_segment = compute_fence_segment((dr, dc), edge_plot, neighbor_loc)
                region_fence_segments.append(fence_segment)

    region_sides = fences_to_sides(region_fence_segments)

    return region, len(region_sides)


for ix_row, row in enumerate(garden_map):
    for ix_col, plot in enumerate(row):
        if (ix_row, ix_col) in assigned_plots:
            continue
        else:
            new_region, face_count = walk_region(ix_row, ix_col, plot)

            plant_type_regions[plot].append(new_region)
            assigned_plots.update(new_region)

            plant_regions[region_id_counter] = {
                'plant_type': str(plot),
                'area': len(new_region),
                'face_count': face_count,
                'cost': len(new_region) * face_count,
            }
            region_id_counter += 1


total_cost = sum(plant_region['cost'] for plant_region in plant_regions.values())

print(total_cost)
