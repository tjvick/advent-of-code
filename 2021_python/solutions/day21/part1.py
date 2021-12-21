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


class Die:
    def __init__(self):
        self.value = -1
        self.count = 0

    def roll(self):
        self.count += 1
        self.value = (self.value + 1) % 100
        return self.value + 1


die = Die()
for ix in range(200):
    dice_total = sum([die.roll(), die.roll(), die.roll()])
    player_1_position = (player_1_position + dice_total - 1) % 10 + 1
    player_1_score += player_1_position
    if player_1_score >= 1000:
        print(player_2_score * die.count)
        break
    dice_total = sum([die.roll(), die.roll(), die.roll()])
    player_2_position = (player_2_position + dice_total - 1) % 10 + 1
    player_2_score += player_2_position
    if player_2_score >= 1000:
        print(player_1_score * die.count)
        break

