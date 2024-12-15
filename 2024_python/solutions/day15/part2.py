from abc import ABC
from dataclasses import dataclass

from solutions import helpers

filepath = 'input'
# filepath = 'test'

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

    def can_move(self, direction: Direction) -> bool:
        pass

    def attempt_move(self, direction: Direction) -> bool:
        pass

    def gps_coordinate(self):
        return self.top * 100 + self.left


@dataclass
class EmptySpace(WarehouseSpace):
    def attempt_move(self, direction: Direction):
        return True

    def can_move(self, direction: Direction):
        return True


@dataclass
class Wall(WarehouseSpace):
    def attempt_move(self, direction: Direction):
        return False

    def can_move(self, direction: Direction):
        return False

@dataclass
class Box(WarehouseSpace):
    def can_move(self, direction: Direction):
        new_top, new_left = self.compute_new_position(direction)
        occupants = self.find_occupants(new_top, new_left)
        return all(occupant.can_move(direction) for occupant in occupants)

    def attempt_move(self, direction: Direction):
        new_top, new_left = self.compute_new_position(direction)
        occupants = self.find_occupants(new_top, new_left)
        can_move = all(occupant.can_move(direction) for occupant in occupants)
        if can_move:
            for occupant in occupants:
                occupant.attempt_move(direction)
            self.relocate(new_top, new_left)
            return True
        else:
            return False

    def find_occupants(self, top, left):
        a = self.map[(top, left)]
        b = self.map[(top, left+1)]
        if isinstance(a, Box) and a.top == self.top and a.left == self.left:
            return [b]
        if isinstance(b, Box) and b.top == self.top and b.left == self.left:
            return [a]
        if isinstance(a, Box) and isinstance(b, Box) and a.top == b.top and a.left == b.left:
            return [a]
        return [a, b]

    def relocate(self, top: int, left: int):
        self.map[(self.top, self.left)] = EmptySpace(self.top, self.left, self.map)
        self.map[(self.top, self.left + 1)] = EmptySpace(self.top, self.left, self.map)
        self.top = top
        self.left = left
        self.map[(self.top, self.left)] = self
        self.map[(self.top, self.left+1)] = self


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
        warehouse_lookup[(ix_row, ix_col*2)] = EmptySpace(ix_row, ix_col*2, warehouse_lookup)
        warehouse_lookup[(ix_row, ix_col*2+1)] = EmptySpace(ix_row, ix_col * 2 + 1, warehouse_lookup)
        if element == '#':
            warehouse_lookup[(ix_row, ix_col*2)] = Wall(ix_row, ix_col*2, warehouse_lookup)
            warehouse_lookup[(ix_row, ix_col*2+1)] = Wall(ix_row, ix_col*2+1, warehouse_lookup)
        elif element == 'O':
            box = Box(ix_row, ix_col*2, warehouse_lookup)
            warehouse_lookup[(ix_row, ix_col * 2)] = box
            warehouse_lookup[(ix_row, ix_col * 2 + 1)] = box
        elif element == '@':
            robot = Robot(ix_row, ix_col * 2, warehouse_lookup)


for movement in movements:
    d = directions[movement]
    moved = robot.attempt_move(d)


gps_coordinate_sum = 0
for warehouse_space in warehouse_lookup.values():
    if isinstance(warehouse_space, Box):
        gps_coordinate_sum += warehouse_space.gps_coordinate()

print(gps_coordinate_sum // 2)