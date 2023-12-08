from functools import cmp_to_key

from solutions import helpers
from collections import Counter
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

hand_rankings = [
    5,
    41,
    32,
    311,
    221,
    2111,
    11111
]
card_rankings = 'AKQJT98765432'

hands_bids = []
for line in strings:
    m = re.match(r'(\w+) (\d+)', line)
    hand, bid = m.groups()
    print(hand)
    hand_counts = sorted(Counter(hand).values(), reverse=True)
    print(hand_counts)
    hand_type = int("".join([str(x) for x in hand_counts]))
    print(hand_type)
    hand_ranking = hand_rankings.index(hand_type)
    print(hand_ranking)
    card_ranks = [card_rankings.index(x) for x in hand]

    hands_bids.append((hand, hand_ranking, card_ranks, int(bid)))


def compare_hands(a, b):
    a_hand_ranking = a[1]
    b_hand_ranking = b[1]

    if a_hand_ranking < b_hand_ranking:
        return 1
    if a_hand_ranking > b_hand_ranking:
        return -1

    a_card_ranks = a[2]
    b_card_ranks = b[2]
    winner = False
    ix = 0
    while not winner:
        if a_card_ranks[ix] != b_card_ranks[ix]:
            return b_card_ranks[ix] - a_card_ranks[ix]
        ix += 1
        if ix == len(a_card_ranks):
            return 0

    return 0


sorted_hands_bids = sorted(hands_bids, key=cmp_to_key(compare_hands))

total_winnings = sum((rank + 1) * hand_bid[3] for rank, hand_bid in enumerate(sorted_hands_bids))
print("total_winnings")
print(total_winnings)
