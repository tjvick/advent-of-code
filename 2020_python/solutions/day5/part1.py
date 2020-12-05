with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]


def process_row(data):
    range = [0, 127]
    for char in data[0:7]:
        if char == "B":
            range = [(range[0]+range[1]+1)/2, range[1]]
        elif char == "F":
            range = [range[0], (range[0]+range[1]-1)/2]

    return range


def process_col(data):
    range = [0, 7]
    for char in data[7:]:
        if char == "R":
            range = [(range[0] + range[1] + 1) / 2, range[1]]
        elif char == "L":
            range = [range[0], (range[0] + range[1] - 1) / 2]

    return range


seat_ids = []
for data in file_contents:
    row_range = process_row(data)
    col_range = process_col(data)
    seat_ids.append(row_range[0]*8 + col_range[0])

print(max(seat_ids))
