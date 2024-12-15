from abc import ABC
from dataclasses import dataclass

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test0'

input_lines = helpers.read_each_line_as_string(filepath)

warehouse_map = []
movements = ''
for line in input_lines:
    if line == '':
        continue

    if line[0] == '#':
        warehouse_map.append(list(line))
    else:
        movements += line

@dataclass
class Direction:
    top: int
    left: int

directions = {
    '^': Direction(-1, 0),
    'v': Direction(1, 0),
    '>': Direction(0, 1),
    '<': Direction(0, -1)
}


@dataclass
class WarehouseSpace(ABC):
    top: int
    left: int
    map: dict

    def compute_new_position(self, direction: Direction):
        new_top = self.top + direction.top
        new_left = self.left + direction.left
        return new_top, new_left

    def relocate(self, top: int, left: int):
        self.top = top
        self.left = left
        self.map[(self.top, self.left)] = self

    def attempt_move(self, direction: Direction) -> bool:
        pass

    def gps_coordinate(self):
        return self.top * 100 + self.left


@dataclass
class EmptySpace(WarehouseSpace):
    def attempt_move(self, direction: Direction):
        return True


@dataclass
class Wall(WarehouseSpace):
    def attempt_move(self, direction: Direction):
        return False

@dataclass
class Box(WarehouseSpace):
    def attempt_move(self, direction: Direction):
        new_top, new_left = self.compute_new_position(direction)
        occupant = self.map[(new_top, new_left)]
        did_move = occupant.attempt_move(direction)
        if did_move:
            self.relocate(new_top, new_left)
            return True
        else:
            return False

@dataclass
class Robot(WarehouseSpace):
    def attempt_move(self, direction: Direction):
        new_top, new_left = self.compute_new_position(direction)
        occupant = self.map[(new_top, new_left)]
        did_move = occupant.attempt_move(direction)
        if did_move:
            self.map[(self.top, self.left)] = EmptySpace(self.top, self.left, self.map)
            self.relocate(new_top, new_left)
            return True
        else:
            return False


warehouse_lookup = {}
robot = Robot(-1, -1, warehouse_lookup)
for ix_row, row in enumerate(warehouse_map):
    for ix_col, element in enumerate(row):
        warehouse_space = EmptySpace(ix_row, ix_col, warehouse_lookup)
        if element == '#':
            warehouse_space = Wall(ix_row, ix_col, warehouse_lookup)
        elif element == 'O':
            warehouse_space = Box(ix_row, ix_col, warehouse_lookup)
        elif element == '@':
            robot = Robot(ix_row, ix_col, warehouse_lookup)

        warehouse_lookup[(ix_row, ix_col)] = warehouse_space



for movement in movements:
    d = directions[movement]
    moved = robot.attempt_move(d)


gps_coordinate_sum = 0
for warehouse_space in warehouse_lookup.values():
    if isinstance(warehouse_space, Box):
        gps_coordinate_sum += warehouse_space.gps_coordinate()

print(gps_coordinate_sum)