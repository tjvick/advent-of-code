import re

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]


def apply_mask_to_character(mask_char, value_char):
    return mask_char if mask_char in '01' else value_char


def apply_mask_to_value(mask, value):
    binary_string = format(value, 'b').zfill(len(mask))
    masked_string = ''.join([
        apply_mask_to_character(mask[ix], char) for ix, char in enumerate(binary_string)
    ])
    masked_value = int(masked_string, 2)

    return masked_value


memory = {}


for row_contents in file_contents:
    mask_match = re.match(r'^mask = ([X\d]+)$', row_contents)
    if mask_match:
        mask_string = mask_match.group(1)
    else:
        mem_match = re.match(r'^mem\[(\d+)\] = (\d+)$', row_contents)
        mem_address = int(mem_match.group(1))
        mem_value = int(mem_match.group(2))

        masked_value = apply_mask_to_value(mask_string, mem_value)
        memory[mem_address] = masked_value

print(sum(memory.values()))

# 14683437866 too low
# 14722016054794
