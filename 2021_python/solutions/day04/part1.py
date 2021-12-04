from solutions import helpers
import numpy as np

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

BOARD_SIZE = 5


def pop_boards(strings, boards):
    if len(strings) == 0:
        return np.array(boards)

    board = np.array([row.split() for row in strings[:BOARD_SIZE]], dtype=int)
    boards.append(board)
    return pop_boards(strings[BOARD_SIZE + 1:], boards)


def winner(marking):
    return (
            np.any(np.sum(marking, axis=0) == BOARD_SIZE) or
            np.any(np.sum(marking, axis=1) == BOARD_SIZE)
    )


def play_bingo(boards, numbers):
    markings = np.zeros_like(boards)

    for number in numbers:
        for ix, board in enumerate(boards):
            markings[ix] += (board == number)
            if winner(markings[ix]):
                total_unmarked = np.sum((1 - markings[ix]) * board)
                score = total_unmarked * number
                return score


if __name__ == "__main__":
    numbers = map(int, strings[0].split(","))
    boards = pop_boards(strings[2:], [])

    print(play_bingo(boards, numbers))
