from collections import defaultdict

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test1'

maze_map = helpers.read_as_2d_array_of_characters(filepath)

starting_location = np.argwhere(maze_map == 'S')[0]


def get_next_directions(current_dir: np.array):
    all_directions = [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]
    return [d for d in all_directions if not np.array_equal(d, -current_dir)]

def delta_score(direction_a, direction_b):
    if np.array_equal(direction_a, direction_b):
        return 1
    return 1001

def inbounds(location):
    return 0 <= location[0] < maze_map.shape[0] and 0 <= location[1] < maze_map.shape[1]

print(starting_location)
paths = [([tuple(starting_location)], np.array([0, 1]), 0)]

min_scores_by_location = defaultdict(lambda: np.inf)

min_score = 1e7
while len(paths) > 0:
    path = paths.pop(0)

    past_locations, current_direction, current_score = path
    current_location = np.array(past_locations[-1])

    if current_score > min_score:
        continue

    if current_score > min_scores_by_location[past_locations[-1]]:
        continue

    if current_score < min_scores_by_location[past_locations[-1]]:
        min_scores_by_location[past_locations[-1]] = current_score

    next_directions = get_next_directions(current_direction)
    for next_direction in next_directions:
        next_location = current_location + next_direction
        if tuple(next_location) in past_locations:
            continue
        if maze_map[*next_location] == '.':
            paths.append((past_locations + [tuple(next_location)], next_direction, current_score + delta_score(current_direction, next_direction)))
            continue
        elif maze_map[*next_location] == '#':
            continue
        elif maze_map[*next_location] == 'E':
            total_score = current_score + delta_score(current_direction, next_direction)
            if total_score < min_score:
                print("NEW BEST SCORE", total_score)
                min_score = total_score


print(min_score)

