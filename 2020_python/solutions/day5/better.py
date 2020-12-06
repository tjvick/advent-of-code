import numpy as np

with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

translation = str.maketrans('BFRL', '1010')

seat_ids = []
for data in file_contents:
    seat_id = int(data.translate(translation), 2)
    seat_ids.append(seat_id)

print(max(seat_ids))

all_seats = sorted(seat_ids)
for ix, x in enumerate(all_seats):
    if x - ix != all_seats[0]:
        print(x-1)
        break
