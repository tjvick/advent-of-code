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

total_disk_space = sum(disk_map)
total_file_space = sum(v for v in file_block_sizes.values())
total_free_space = total_disk_space - total_file_space


contents_of_each_span = {}

forward_file_id_pointer = 0
backward_file_id_pointer = n_file_blocks - 1
read_direction = 'FWD'
while len(spans_of_disk_space) > 0 and forward_file_id_pointer <= backward_file_id_pointer:
    span_of_disk_space = spans_of_disk_space.pop(0)
    a, b = span_of_disk_space
    span_size = b - a
    if read_direction == 'FWD':
        file_block_size = file_block_sizes[forward_file_id_pointer]
        if file_block_size == span_size:
            contents_of_each_span[span_of_disk_space] = forward_file_id_pointer
            forward_file_id_pointer += 1
            read_direction = 'BWD'
        elif file_block_size > span_size:
            contents_of_each_span[span_of_disk_space] = forward_file_id_pointer
            file_block_sizes[forward_file_id_pointer] -= span_size
            read_direction = 'BWD'
        elif file_block_size < span_size:
            span_being_filled = (span_of_disk_space[0], span_of_disk_space[0] + file_block_size)
            new_span = (span_of_disk_space[0] + file_block_size, span_of_disk_space[1])
            contents_of_each_span[span_being_filled] = forward_file_id_pointer
            spans_of_disk_space.insert(0, new_span)
            forward_file_id_pointer += 1
    elif read_direction == 'BWD':
        file_block_size = file_block_sizes[backward_file_id_pointer]
        if file_block_size == span_size:
            contents_of_each_span[span_of_disk_space] = backward_file_id_pointer
            backward_file_id_pointer -= 1
            read_direction = 'FWD'
        elif file_block_size > span_size:
            contents_of_each_span[span_of_disk_space] = backward_file_id_pointer
            file_block_sizes[backward_file_id_pointer] -= span_size
            read_direction = 'FWD'
        elif file_block_size < span_size:
            span_being_filled = (span_of_disk_space[0], span_of_disk_space[0] + file_block_size)
            new_span = (span_of_disk_space[0] + file_block_size, span_of_disk_space[1])
            contents_of_each_span[span_being_filled] = backward_file_id_pointer
            spans_of_disk_space.insert(0, new_span)
            backward_file_id_pointer -= 1


# print(contents_of_each_span)

checksum = 0
for span in contents_of_each_span:
    for idx in range(*span):
        checksum += idx * contents_of_each_span[span]

print(checksum)