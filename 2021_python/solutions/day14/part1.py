from solutions import helpers
import numpy as np
import re
from collections import Counter

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

polymer = strings[0]

pattern = re.compile('(\w+) -> (\w+)')
insertion_rules = {}
for string in strings[2:]:
    k, v  = pattern.match(string).groups()
    insertion_rules[k] = v


def pairwise(thing):
    a, b = iter(thing), iter(thing)
    next(b)

    return zip(a, b)

for ix in range(10):
    insertions_to_perform = []
    for ix, (a, b) in enumerate(reversed(list(pairwise(polymer)))):
        pair = ''.join([a, b])
        if pair in insertion_rules:
            # print(pair)
            # insertion_rules[pair]
            # print(len(polymer) - ix - 1)
            insertions_to_perform.append((len(polymer) - ix - 1, insertion_rules[pair]))

    # print(insertions_to_perform)
    poly_list = list(polymer)
    for insertion_to_perform in insertions_to_perform:
        poly_list.insert(*insertion_to_perform)

    polymer = ''.join(poly_list)

    # print(polymer)
    print(len(polymer))

c = Counter(list(polymer))
most = c.most_common()
print(most)
print(most[0][1] - most[-1][1])

