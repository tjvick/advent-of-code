from solutions import helpers
import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

digit_sequences = helpers.read_each_line_as_digit_sequence(filename)

cavern_map = np.array(digit_sequences, dtype=int)
# cavern_map = cavern_map[70:, 70:]
max_bound = sum(cavern_map[1:, 0]) + sum(cavern_map[-1, :])

cumulative_risk = np.ones_like(cavern_map) * max_bound

print(cavern_map)

neighbors = [
    (0, -1),
    (-1, 0),
    (1, 0),
    (0, 1),
]

size = cavern_map.shape[0]
end_location = (size-1, size-1)
cumulative_risk[end_location] = cavern_map[end_location]

locations_to_visit = []

current_location = end_location
x, y = current_location
for dx, dy in neighbors:
    if x + dx < 0 or y + dy < 0 or x + dx >= size or y + dy >= size:
        continue
    new_location = (x+dx, y+dy)
    cumulative_risk[new_location] = min(cumulative_risk[current_location] + cavern_map[new_location], cumulative_risk[new_location])
    locations_to_visit.append(new_location)

count = 0
while len(locations_to_visit) > 0:
    count += 1
    current_location = locations_to_visit.pop(0)
    x, y = current_location
    for dx, dy in neighbors:
        if x + dx < 0 or y + dy < 0 or x + dx >= size or y + dy >= size:
            continue
        new_location = (x + dx, y + dy)
        if cumulative_risk[current_location] + cavern_map[new_location] < cumulative_risk[new_location]:
            cumulative_risk[new_location] = cumulative_risk[current_location] + cavern_map[new_location]
            if new_location not in locations_to_visit:
                locations_to_visit.append(new_location)


print(cumulative_risk)
print(cumulative_risk[(0, 0)] - cavern_map[(0, 0)])
print('count', count)