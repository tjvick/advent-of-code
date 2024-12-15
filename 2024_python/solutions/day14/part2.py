import re
from dataclasses import dataclass

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

data = helpers.read_each_line_as_string(filepath)

pattern = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

# x_limit, y_limit = 11, 7
x_limit, y_limit = 101, 103

@dataclass
class Robot:
    x_0: int
    y_0: int
    v_x: int
    v_y: int

    def move(self, n_seconds):
        x_n = (self.x_0 + self.v_x * n_seconds) % x_limit
        y_n = (self.y_0 + self.v_y * n_seconds) % y_limit

        return x_n, y_n


robots = []
for line in data:
    m = pattern.match(line)
    robot = Robot(*(int(_) for _ in m.groups()))
    robots.append(robot)


def render(positions):
    image = np.full((y_limit, x_limit), ' ')
    for (x, y) in positions:
        image[y, x] = '#'
    for row in image:
        print(''.join(row))


def is_tree_shaped(positions):
    variance = np.var(positions, axis=0)
    return np.all(variance < 600)


for seconds in range(0,10000):
    robot_positions = []
    for robot in robots:
        x_n, y_n = robot.move(seconds)
        robot_positions.append([x_n, y_n])

    if is_tree_shaped(robot_positions):
        render(robot_positions)
        print("POSSIBLE CHRISTMAS TREE AFTER", seconds, "SECONDS")
        input()

