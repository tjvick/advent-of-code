from solutions import helpers
from collections import defaultdict
import re

filename = 'input'

strings = helpers.read_each_line_as_string(filename)


def fill_in_along_line(x1, y1, x2, y2, filled):
    dx, dy = x2 - x1, y2 - y1
    length = max(abs(dx), abs(dy))
    for step in range(0, length + 1, 1):
        x = x1 + dx * step / length
        y = y1 + dy * step / length
        filled[(x, y)] += 1


pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

if __name__ == '__main__':
    filled = defaultdict(int)

    for string in strings:
        x1, y1, x2, y2 = map(int, pattern.match(string).groups())

        if x1 == x2 or y1 == y2:
            fill_in_along_line(x1, y1, x2, y2, filled)

    count = sum(1 for v in filled.values() if v >= 2)
    print(count)
