from solutions import helpers

filepath = 'input'
# filepath = 'test'

input_data = helpers.read_as_list_of_delimited_arrays(filepath, delimiter=' ', dtype=int)
initial_stones = input_data[0]

stone_history = []
for stone in initial_stones:
    stone_history.append((0, int(stone)))

final_stone_count = 0

while len(stone_history) > 0:
    current_stone_history = stone_history.pop(0)
    n_blinks, stone_number = current_stone_history

    if n_blinks == 25:
        final_stone_count += 1
        continue

    stone_digit_length = len(str(stone_number))

    if stone_number == 0:
        stone_history.insert(0, (n_blinks+1, 1))
    elif stone_digit_length % 2 == 0:
        left_stone = int(str(stone_number)[:stone_digit_length//2])
        right_stone = int(str(stone_number)[stone_digit_length//2:])
        stone_history.insert(0, (n_blinks+1, right_stone))
        stone_history.insert(0, (n_blinks+1, left_stone))
    else:
        stone_history.insert(0, (n_blinks+1, stone_number * 2024))


print(final_stone_count)
