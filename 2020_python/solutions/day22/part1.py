import numpy as np
import math
import re
import collections

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

break_point = file_contents.index('')
hand_1 = list(map(int, file_contents[1:break_point]))
hand_2 = list(map(int, file_contents[break_point+2:]))

while len(hand_1) > 0 and len(hand_2) > 0:
    card_1 = hand_1.pop(0)
    card_2 = hand_2.pop(0)
    print(hand_1)
    print(hand_2)
    print(card_1)
    print(card_2)
    if card_1 > card_2:
        hand_1 += [card_1, card_2]
    else:
        hand_2 += [card_2, card_1]

print(hand_1)
print(hand_2)


def score(hand):
    return np.dot(np.array(hand), np.arange(len(hand), 0, -1))


print(score(hand_1))
print(score(hand_2))

