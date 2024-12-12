from collections import defaultdict

from solutions import helpers

filepath = 'input'
# filepath = 'test'

input_data = helpers.read_as_list_of_delimited_arrays(filepath, delimiter=' ', dtype=int)
initial_stones = input_data[0]

total_blinks = 75
stones_counter = {stone: 1 for stone in initial_stones}

for ix_blink in range(total_blinks):
    next_stones_counter = defaultdict(int)
    for stone in stones_counter:
        if stone == 0:
            next_stones_counter[1] += stones_counter[stone]
        elif len(str(stone)) % 2 == 0:
            new_stone_digit_length = len(str(stone)) // 2
            left_stone = int(str(stone)[:new_stone_digit_length])
            right_stone = int(str(stone)[new_stone_digit_length:])
            next_stones_counter[left_stone] += stones_counter[stone]
            next_stones_counter[right_stone] += stones_counter[stone]
        else:
            next_stones_counter[stone * 2024] += stones_counter[stone]

    stones_counter = next_stones_counter

print(sum(stones_counter.values()))