from solutions import helpers
import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

digit_sequences = helpers.read_each_line_as_digit_sequence(filename)

cavern_map = np.array(digit_sequences, dtype=int)
size = cavern_map.shape[0]

big_map = np.zeros((cavern_map.shape[0] * 5, cavern_map.shape[1] * 5), dtype=int)

for ix in range(5):
    for iy in range(5):
        big_map[ix*size:(ix+1)*size, iy*size:(iy+1)*size] = (cavern_map + ix + iy - 1) % 9 + 1

print(big_map.shape)

max_bound = sum(big_map[1:, 0]) + sum(big_map[-1, :])
cumulative_risk = np.ones_like(big_map) * max_bound

neighbors = [
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0),
]

size = big_map.shape[0]
end_location = (size-1, size-1)
cumulative_risk[end_location] = big_map[end_location]

locations_to_visit = set()

current_location = end_location
x, y = current_location
for dx, dy in neighbors:
    if x + dx < 0 or y + dy < 0 or x + dx >= size or y + dy >= size:
        continue
    new_location = (x+dx, y+dy)
    cumulative_risk[new_location] = min(cumulative_risk[current_location] + big_map[new_location], cumulative_risk[new_location])
    locations_to_visit.add(new_location)

count = 0
while len(locations_to_visit) > 0:
    count += 1
    current_location = locations_to_visit.pop()
    x, y = current_location
    for dx, dy in neighbors:
        if x + dx < 0 or y + dy < 0 or x + dx >= size or y + dy >= size:
            continue
        new_location = (x + dx, y + dy)
        possible_new_value = cumulative_risk[current_location] + big_map[new_location]
        if possible_new_value < cumulative_risk[new_location]:
            cumulative_risk[new_location] = possible_new_value
            locations_to_visit.add(new_location)


print(cumulative_risk)
print(cumulative_risk[(0, 0)] - big_map[(0, 0)])
print('count', count)