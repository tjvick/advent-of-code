from solutions import helpers
import numpy as np
from abc import ABC
from itertools import cycle

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
filename = 'test'

char_sequences = helpers.read_each_line_as_char_sequence(filename)

LEFT = "<"
RIGHT = ">"

MINUS = []
PLUS = []
ELL = []
TETRIS = []
SQUARE = []


class Piece(ABC):
    def __init__(self, grid: set):
        self.grid = grid
        highest_point = max([y for x, y in grid])
        self.pos = np.array([2, highest_point + 4])
        self.blocks = []
        self.down_empty_spaces = []
        self.right_empty_spaces = []
        self.left_empty_spaces = []

    def move_left(self):
        if self.can_move_left():
            self.pos += [-1, 0]
            # print("MOVED LEFT")
        # else:
            # print("CANNOT MOVE LEFT")

    def move_right(self):
        if self.can_move_right():
            self.pos += [1, 0]
            # print("MOVED RIGHT")
        # else:
            # print("CANNOT MOVE RIGHT")

    def move_down(self):
        if self.can_move_down():
            self.pos += [0, -1]
            # print("MOVED DOWN")
            return False
        else:
            # print("CANNOT MOVE DOWN. COMING TO REST")
            self.update_grid()
            return True

    def update_grid(self):
        for block in self.blocks:
            grid_spot = tuple(self.pos + block)
            self.grid.add(grid_spot)

    def can_move_down(self):
        empty_space_required = np.array(self.down_empty_spaces) + self.pos
        if np.any([tuple(esr) in self.grid for esr in empty_space_required]):
            return False
        return True

    def can_move_right(self):
        empty_space_required = np.array(self.right_empty_spaces) + self.pos
        if np.any([x > 6 for x, y in empty_space_required]):
            return False
        if np.any([tuple(esr) in self.grid for esr in empty_space_required]):
            return False
        return True

    def can_move_left(self):
        empty_space_required = np.array(self.left_empty_spaces) + self.pos
        if np.any([x < 0 for [x, y] in empty_space_required]):
            return False
        if np.any([tuple(esr) in self.grid for esr in empty_space_required]):
            return False
        return True


class Minus(Piece):
    def __init__(self, grid: set):
        super().__init__(grid)
        self.blocks = [[0, 0], [1, 0], [2, 0], [3, 0]]
        self.down_empty_spaces = [[0, -1], [1, -1], [2, -1], [3, -1]]
        self.right_empty_spaces = [[4, 0]]
        self.left_empty_spaces = [[-1, 0]]


class Plus(Piece):
    def __init__(self, grid: set):
        super().__init__(grid)
        self.blocks = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
        self.down_empty_spaces = [[0, 0], [1, -1], [2, 0]]
        self.right_empty_spaces = [[2, 2], [3, 1], [2, 0]]
        self.left_empty_spaces = [[0, 0], [-1, 1], [0, 2]]


class Ell(Piece):
    def __init__(self, grid: set):
        super().__init__(grid)
        self.blocks = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]]
        self.down_empty_spaces = [[0, -1], [1, -1], [2, -1]]
        self.right_empty_spaces = [[3, 0], [3, 1], [3, 2]]
        self.left_empty_spaces = [[-1, 0], [1, 1], [1, 2]]


class Tetris(Piece):
    def __init__(self, grid: set):
        super().__init__(grid)
        self.blocks = [[0, 0], [0, 1], [0, 2], [0, 3]]
        self.down_empty_spaces = [[0, -1]]
        self.right_empty_spaces = [[1, 0], [1, 1], [1, 2], [1, 3]]
        self.left_empty_spaces = [[-1, 0], [-1, 1], [-1, 2], [-1, 3]]


class Square(Piece):
    def __init__(self, grid: set):
        super().__init__(grid)
        self.blocks = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.down_empty_spaces = [[0, -1], [1, -1]]
        self.right_empty_spaces = [[2, 0], [2, 1]]
        self.left_empty_spaces = [[-1, 0], [-1, 1]]


pieces = [
    Minus,
    Plus,
    Ell,
    Tetris,
    Square,
]

directions = char_sequences[0]


def directions_gen():
    idgen = 0
    while True:
        direction = directions[idgen]
        idgen += 1
        yield direction


directions_cycler = cycle(directions)


grid = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}

print((1000000000000-1000) % 7000)
print(1520 + np.floor((1000000000000-1000)/7000)*11600 + 1514+1514+1513+1516+1511)

for ix_piece in range(1000000000000):
    if ix_piece % 1000 == 0:
        max_y = max([y for x, y in grid])
        print(ix_piece, max_y)

    piece_type = pieces[ix_piece % len(pieces)]
    piece = piece_type(grid)

    landed = False
    while not landed:
        if next(directions_cycler) == RIGHT:
            # print("GO RIGHT")
            piece.move_right()
        else:
            # print("GO LEFT")
            piece.move_left()

        landed = piece.move_down()
        grid = piece.grid
        # print(grid)


max_y = max([y for x, y in grid])

print(max_y)
# grid_depiction = np.zeros((7, max_y+1), dtype=int)
# for block in grid:
#     grid_depiction[block] = 1
#
# for row in reversed(grid_depiction.transpose()):
#     print(str(row).replace('0', '.').replace('1', '#'))

print(len(range(22)))