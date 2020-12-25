from collections import defaultdict
from datetime import datetime

puzzle_input = "156794823"
# puzzle_input = "389125467"

cups = [int(x) for x in puzzle_input]

now = datetime.now()

cups_ll = defaultdict(int)
for ic in range(len(cups)-1):
    cups_ll[cups[ic]] = cups[ic+1]

cups_ll[cups[-1]] = len(cups) + 1

n_cups = 1000000
for ic in range(len(cups) + 1, n_cups):
    cups_ll[ic] = ic + 1

cups_ll[n_cups] = cups[0]


def get_destination_cup(current_cup, side_cups):
    targets = [
        current_cup - 1,
        current_cup - 2,
        current_cup - 3,
        current_cup - 4,
        n_cups,
        n_cups - 1,
        n_cups - 2,
        n_cups - 3
    ]
    for t in targets:
        if t > 0 and t not in side_cups:
            return t


n_moves = 10000000
current_cup = cups[0]
for ix_move in range(n_moves):
    if ix_move % (n_moves/100) == 0:
        print(ix_move)

    first_side_cup = cups_ll[current_cup]
    second_side_cup = cups_ll[first_side_cup]
    third_side_cup = cups_ll[second_side_cup]

    destination_cup = get_destination_cup(current_cup, [first_side_cup, second_side_cup, third_side_cup])

    cups_ll[current_cup] = cups_ll[third_side_cup]
    cups_ll[third_side_cup] = cups_ll[destination_cup]
    cups_ll[destination_cup] = first_side_cup

    current_cup = cups_ll[current_cup]


print(cups_ll[1])
print(cups_ll[cups_ll[1]])
print(cups_ll[1] * cups_ll[cups_ll[1]])
print(datetime.now() - now)
