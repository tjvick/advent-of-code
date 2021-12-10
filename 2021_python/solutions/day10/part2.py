from solutions import helpers
import numpy as np

filename = 'input'

char_sequences = helpers.read_each_line_as_char_sequence(filename)

openers_by_closer = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
openers = openers_by_closer.values()

closers_by_opener = {v: k for k, v in openers_by_closer.items()}

points_by_closer = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

total_scores = []
for sequence in char_sequences:
    stack = []
    bad = False
    for char in sequence:
        if char in openers:
            stack.append(char)
        elif stack.pop() == openers_by_closer[char]:
            pass
        else:
            bad = True

    if not bad and len(stack) > 0:
        total_score = 0
        for char in reversed(stack):
            total_score = total_score * 5 + points_by_closer[closers_by_opener[char]]
        total_scores.append(total_score)

print(np.median(total_scores))

