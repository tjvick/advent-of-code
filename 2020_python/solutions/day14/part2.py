import re

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]


def apply_mask_to_character(mask_char, value_char):
    if mask_char == '1':
        return '1'
    elif mask_char == '0':
        return value_char

    return mask_char


def expand_masked_address(masked_string):
    address_values = []
    strings_to_expand = [masked_string]
    while len(strings_to_expand) > 0:
        string_to_expand = strings_to_expand.pop()
        x_found = False
        for ix, char in enumerate(string_to_expand):
            if char == 'X':
                x_found = True
                strings_to_expand.append(string_to_expand[0:ix] + '0' + string_to_expand[ix + 1:])
                strings_to_expand.append(string_to_expand[0:ix] + '1' + string_to_expand[ix + 1:])
                break

        if not x_found:
            address_values.append(int(string_to_expand, 2))

    return address_values


def apply_mask_to_value(mask, value):
    binary_string = format(value, 'b').zfill(len(mask))
    masked_string = ''.join([
        apply_mask_to_character(mask[ix], char) for ix, char in enumerate(binary_string)
    ])

    return expand_masked_address(masked_string)


memory = {}

for row_contents in file_contents:
    mask_match = re.match(r'^mask = ([X\d]+)$', row_contents)
    if mask_match:
        mask_string = mask_match.group(1)
    else:
        mem_match = re.match(r'^mem\[(\d+)] = (\d+)$', row_contents)
        mem_address = int(mem_match.group(1))
        mem_value = int(mem_match.group(2))

        masked_addresses = apply_mask_to_value(mask_string, mem_address)
        for address in masked_addresses:
            memory[address] = mem_value

print(sum(memory.values()))