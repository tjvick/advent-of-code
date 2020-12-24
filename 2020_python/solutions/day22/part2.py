import numpy as np
import math
import re
import collections

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

break_point = file_contents.index('')
hand_1 = list(map(int, file_contents[1:break_point]))
hand_2 = list(map(int, file_contents[break_point+2:]))


def play_game(hand_1, hand_2):
    previous_hands_1 = []
    previous_hands_2 = []

    while len(hand_1) > 0 and len(hand_2) > 0:
        if hand_1 in previous_hands_1 and hand_2 in previous_hands_2:
            return 0, hand_1

        previous_hands_1.append(hand_1.copy())
        previous_hands_2.append(hand_2.copy())

        card_1 = hand_1.pop(0)
        card_2 = hand_2.pop(0)

        if card_1 <= len(hand_1) and card_2 <= len(hand_2):
            new_hand_1 = hand_1[:card_1]
            new_hand_2 = hand_2[:card_2]
            ix_winner, _ = play_game(new_hand_1, new_hand_2)
        else:
            ix_winner = 0 if card_1 > card_2 else 1

        if ix_winner == 0:
            hand_1 += [card_1, card_2]
        else:
            hand_2 += [card_2, card_1]

    return (0, hand_1) if len(hand_1) > len(hand_2) else (1, hand_2)


_, winning_hand = play_game(hand_1, hand_2)


def score(hand):
    return np.dot(np.array(hand), np.arange(len(hand), 0, -1))


print(score(winning_hand))

