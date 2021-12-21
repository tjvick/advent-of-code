from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

# filename = 'input'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

player_1_position = 4
player_2_position = 8
player_1_position = 9
player_2_position = 3
player_1_score = 0
player_2_score = 0


class DiracDie:
    def __init__(self):
        self.value = -1
        self.count = 0

    def roll(self):
        self.count += 1
        self.value = (self.value + 1) % 100
        return self.value + 1


freq_by_sum = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


def split_universes(position_1, score_1, position_2, score_2, turn, n_universes):
    if turn == 1:
        if score_1 == 20:
            return n_universes * 27, 0

        p1_wins_sum = 0
        p2_wins_sum = 0
        for val, freq in freq_by_sum.items():
            dice_total = val
            player_1_position = (position_1 + dice_total - 1) % 10 + 1
            player_1_score = score_1 + player_1_position
            if player_1_score >= 21:
                p1_wins_sum += freq
            else:
                p1_wins, p2_wins = split_universes(player_1_position, player_1_score, position_2, score_2, 2, freq)
                p1_wins_sum += p1_wins
                p2_wins_sum += p2_wins

        return n_universes * p1_wins_sum, n_universes * p2_wins_sum

    if turn == 2:
        if score_2 == 20:
            return 0, n_universes * 27

        p1_wins_sum = 0
        p2_wins_sum = 0
        for val, freq in freq_by_sum.items():
            dice_total = val
            player_2_position = (position_2 + dice_total - 1) % 10 + 1
            player_2_score = score_2 + player_2_position
            if player_2_score >= 21:
                p2_wins_sum += freq
            else:
                p1_wins, p2_wins = split_universes(position_1, score_1, player_2_position, player_2_score, 1, freq)
                p1_wins_sum += p1_wins
                p2_wins_sum += p2_wins
        return n_universes*p1_wins_sum, n_universes*p2_wins_sum


print(split_universes(player_1_position, 0, player_2_position, 0, 1, 1))

# (148747830493442, 89305072914203)
