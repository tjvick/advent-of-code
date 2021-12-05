from solutions import helpers
from collections import defaultdict

from part1 import fill_in_along_line, pattern

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

filled = defaultdict(int)

for string in strings:
    line = map(int, pattern.match(string).groups())
    fill_in_along_line(*line, filled)

count = sum(1 for v in filled.values() if v >= 2)
print(count)
