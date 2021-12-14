from solutions import helpers
import numpy as np
import re
from collections import defaultdict, Counter

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

adjacencies = defaultdict(set)
pattern = re.compile('([^-]+)-([^-]+)')
for connection in strings:
    first, second = pattern.match(connection).groups()
    adjacencies[first].add(second)
    adjacencies[second].add(first)

print(adjacencies)

unfinished_paths = [['start']]
finished_paths = set()


def small_cave_visited_twice(path):
    counter = dict(Counter(path))
    return any(v >= 2 for k, v in counter.items() if k.lower() == k)


while len(unfinished_paths) > 0:
    path = unfinished_paths.pop()
    current_location = path[-1]
    if current_location == 'end':
        finished_paths.add(','.join(path))
        continue
    neighbors = adjacencies[current_location]
    for neighbor in list(neighbors):
        if neighbor == neighbor.lower() and neighbor in path:
            if neighbor == 'start' or neighbor == 'end':
                continue
            if small_cave_visited_twice(path):
                continue
            unfinished_paths.append(path + [neighbor])
        unfinished_paths.append(path + [neighbor])

print(len(finished_paths))
