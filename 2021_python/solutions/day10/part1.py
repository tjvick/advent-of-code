from solutions import helpers

filename = 'input'

char_sequences = helpers.read_each_line_as_char_sequence(filename)

openers_by_closer = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
openers = openers_by_closer.values()

illegals = []
for sequence in char_sequences:
    stack = []
    for char in sequence:
        if char in openers:
            stack.append(char)
        elif stack.pop() == openers_by_closer[char]:
            pass
        else:
            illegals.append(char)


points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

answer = sum(points[char] for char in illegals)
print(answer)
