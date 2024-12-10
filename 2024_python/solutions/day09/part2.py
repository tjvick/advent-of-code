from solutions import helpers

filepath = 'input'
# filepath = 'test'

data = helpers.read_each_line_as_string(filepath)[0]

disk_map = [int(x) for x in data]

def get_spans_of_disk_space(disk_map):
    spans_of_disk_space = []

    cumulative_sum = 0
    for size in disk_map:
        span = (cumulative_sum, cumulative_sum + size)
        spans_of_disk_space.append(span)
        cumulative_sum += size

    return spans_of_disk_space

def get_file_block_sizes(disk_map):
    file_block_sizes = {}
    for file_id in range(0, int(len(disk_map) / 2) + 1):
        file_block_size = disk_map[file_id * 2]
        file_block_sizes[file_id] = file_block_size

    return file_block_sizes


spans_of_disk_space = get_spans_of_disk_space(disk_map)
file_block_sizes = get_file_block_sizes(disk_map)
n_file_blocks = len(file_block_sizes)

file_locations = {}
for file_id in file_block_sizes:
    file_locations[file_id] = spans_of_disk_space[file_id*2]

empty_spans = []
for idx_span in range(1, len(disk_map), 2):
    empty_spans.append(spans_of_disk_space[idx_span])


for file_id in range(n_file_blocks-1, 0, -1):
    file_size = file_block_sizes[file_id]

    for empty_span in empty_spans:
        a, b = empty_span
        if a >= file_locations[file_id][0]:
            break

        span_size = b - a
        if span_size == file_size:
            file_locations[file_id] = empty_span
            empty_spans.remove(empty_span)
            break
        elif span_size > file_size:
            file_locations[file_id] = (a, a+file_size)
            empty_spans[empty_spans.index(empty_span)] = (a+file_size, b)
            break


checksum = 0
for file_id in file_locations:
    for loc in range(*file_locations[file_id]):
        checksum += file_id * loc

print(checksum)
