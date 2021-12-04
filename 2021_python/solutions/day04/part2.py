from solutions import helpers
import numpy as np

filename = 'input'

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

print(strings)

numbers = list(map(int, strings[0].split(",")))

board = []
boards = []
for string_row in strings[2:]:
    if string_row == "":
        boards.append(np.array(board))
        board = []
    else:
        row = list(map(int, string_row.split()))
        board.append(row)

boards.append(np.array(board))

print(boards)

markings = []
for board in boards:
    markings.append(np.zeros(np.shape(board)))


def winner(markings):
    return np.any(np.sum(markings, axis=0) == 5) or np.any(np.sum(markings, axis=1) == 5)


winners = np.zeros((len(boards), 1))

score = 0
for number in numbers:
    print(number)
    for ix, board in enumerate(boards):
        markings[ix] = markings[ix] + 1*(board == number)
        if winner(markings[ix]):
            winners[ix] = 1

    if sum(winners) == len(winners) - 1:
        loser = np.argmin(winners)
        print('loser:', loser)

    if sum(winners) == len(winners):
        print(markings[loser])
        total_unmarked = np.sum(np.sum((1 - markings[loser]) * boards[loser]))
        print('total_unmarked', total_unmarked)
        score = total_unmarked * number
        print(score)

    if score > 0:
        break

