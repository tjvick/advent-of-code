import numpy as np
import math
import re
import collections

puzzle_input = "156794823"
# puzzle_input = "389125467"

n_moves = 100

cups = [int(c) for c in puzzle_input]
current_cup_ix = 0
for ix_move in range(n_moves):
    print('cups', cups)
    current_cup = cups[current_cup_ix]
    side_cups = cups[current_cup_ix+1:current_cup_ix+4]
    remaining_cups = cups[current_cup_ix+4:] + [cups[current_cup_ix]]
    cups[current_cup_ix + 1:current_cup_ix + 4] = []
    print('side cups', side_cups)
    print('remaining', remaining_cups)
    destination_ix = remaining_cups.index(max(remaining_cups))
    for ix in range(1, current_cup):
        try:
            destination_ix = remaining_cups.index(current_cup - ix)
            break
        except:
            pass

    cups = [remaining_cups[destination_ix]] + side_cups + remaining_cups[destination_ix+1:] + remaining_cups[:destination_ix]
    current_cup_ix = len(cups) - destination_ix
    cups = cups[current_cup_ix:] + cups[:current_cup_ix]
    current_cup_ix = 0

print("".join([str(c) for c in cups]))