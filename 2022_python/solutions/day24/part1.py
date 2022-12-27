import dataclasses
from enum import Enum
from functools import cache

from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
WIDTH = 100
HEIGHT = 35

# filename = 'test'
# WIDTH = 6
# HEIGHT = 4

UP = "^"
LEFT = "<"
RIGHT = ">"
DOWN = "v"


class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


char_sequences = helpers.read_each_line_as_char_sequence(filename)


class Blizzard:
    def __init__(self, direction_char, position: tuple):
        if direction_char == UP:
            self.direction = Direction.UP
        elif direction_char == DOWN:
            self.direction = Direction.DOWN
        elif direction_char == RIGHT:
            self.direction = Direction.RIGHT
        else:
            self.direction = Direction.LEFT

        self.starting_position = position

    @cache
    def go_to_time(self, time):
        if self.direction == Direction.UP:
            irow = (self.starting_position[0]-1*time) % HEIGHT
            return irow, self.starting_position[1]

        if self.direction == Direction.DOWN:
            irow = (self.starting_position[0]+1*time) % HEIGHT
            return irow, self.starting_position[1]

        if self.direction == Direction.RIGHT:
            icol = (self.starting_position[1]+1*time) % WIDTH
            return self.starting_position[0], icol

        if self.direction == Direction.LEFT:
            icol = (self.starting_position[1]-1*time) % WIDTH
            return self.starting_position[0], icol


class Blizzards:
    def __init__(self, blizzards: list[Blizzard]):
        self.blizzards = blizzards

    @cache
    def go_to_time(self, time):
        print('Going to time', time)
        return {blizzard.go_to_time(time) for blizzard in self.blizzards}


all_blizzards = []
starting_point = None
ending_point = None
for irow, char_sequence in enumerate(char_sequences):
    if irow == 0:
        starting_col = char_sequence.index(".")
        starting_point = (irow-1, starting_col-1)
        continue

    if irow == len(char_sequences)-1:
        ending_col = char_sequence.index(".")
        ending_point = (irow-1, ending_col-1)
        continue

    for icol, char in enumerate(char_sequence):
        if char in [UP, LEFT, RIGHT, DOWN]:
            blizzard = Blizzard(direction_char=char, position=(irow-1, icol-1))
            all_blizzards.append(blizzard)

# print(starting_point)
# print(ending_point)
# print(all_blizzards)
# print(len(all_blizzards)*200)

possible_steps = [
    np.array([0, 0]),
    np.array([0, -1]),
    np.array([-1, 0]),
    np.array([0, 1]),
    np.array([1, 0]),
]

blizzards = Blizzards(all_blizzards)


@dataclasses.dataclass
class Path:
    time: int
    last_point: tuple


@cache
def in_grid(position):
    y, x = position
    return (0 <= x < WIDTH and 0 <= y < HEIGHT) or position == ending_point or position == starting_point


@cache
def distance_from_end(position):
    return abs(ending_point[0] - position[0]) + abs(ending_point[1] - position[1])


visits = set()

paths = [Path(last_point=starting_point, time=0)]
min_time = 226
while len(paths):
    # print(paths)
    path = paths.pop()
    if dataclasses.astuple(path) in visits:
        continue

    if path.time >= min_time:
        continue

    if path.time + distance_from_end(path.last_point) >= min_time:
        continue

    if path.last_point == ending_point:
        print("Found a path!", path.time)
        min_time = min(min_time, path.time)
        continue

    blizzard_positions = blizzards.go_to_time(path.time+1)
    # try to move
    for step in possible_steps:
        next_step = tuple(step + path.last_point)
        if in_grid(next_step) and next_step not in blizzard_positions:
            new_path = Path(last_point=next_step, time=path.time+1)
            paths.append(new_path)

    visits.add(dataclasses.astuple(path))



# print(paths)
print(min_time)

# Less than 791
