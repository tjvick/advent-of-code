import re
from collections import defaultdict
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


def determine_quadrant(x, y):
    x_middle = (x_limit-1) / 2
    y_middle = (y_limit-1) / 2
    if x < x_middle and y < y_middle:
        return 1
    if x > x_middle and y < y_middle:
        return 2
    if x < x_middle and y > y_middle:
        return 3
    if x > x_middle and y > y_middle:
        return 4

    return 0

robots = []
for line in data:
    m = pattern.match(line)
    robot = Robot(*(int(_) for _ in m.groups()))
    robots.append(robot)


quadrant_counter = defaultdict(int)
for robot in robots:
    x_n, y_n = robot.move(100)
    quadrant = determine_quadrant(x_n, y_n)
    quadrant_counter[quadrant] += 1

quadrant_counter[0] = 1
safety_factor = np.prod(list(quadrant_counter.values()))

print(safety_factor)
