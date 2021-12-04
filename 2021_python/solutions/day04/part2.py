from solutions import helpers
import numpy as np

from part1 import pop_boards, winner

filename = 'test'

strings = helpers.read_each_line_as_string(filename)


def play_bingo_until_all_win(boards, numbers):
    markings = np.zeros_like(boards)

    winners = np.zeros(len(boards))
    for number in numbers:
        for ix, board in enumerate(boards):
            markings[ix] += (board == number)
            if winner(markings[ix]):
                winners[ix] = 1

        if sum(1 - winners) == 1:
            loser = np.argmin(winners)

        if sum(1 - winners) == 0:
            total_unmarked = np.sum((1 - markings[loser]) * boards[loser])
            score = total_unmarked * number
            return score


if __name__ == "__main__":
    numbers = map(int, strings[0].split(","))
    boards = pop_boards(strings[2:], [])

    print(play_bingo_until_all_win(boards, numbers))


