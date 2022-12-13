from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

packet_pairs = []
current_pair = []
for string in strings:
    if string == "":
        packet_pairs.append(current_pair)
        current_pair = []
    else:
        current_pair.append(eval(string))

packet_pairs.append(current_pair)

print(packet_pairs)


def compare_lists(left, right):
    for ix, left_element in enumerate(left):
        if len(right) < ix+1:
            return 1
        right_element = right[ix]
        is_in_right_order = in_right_order(left_element, right_element)
        if is_in_right_order == -1:
            return -1
        elif is_in_right_order == 1:
            return 1

    if len(right) > len(left):
        return -1

    return 0


def in_right_order(left, right):
    print("comparing", left, "to", right)

    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        if left == right:
            return 0
        return 1
    elif type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]

    return compare_lists(left, right)


correct_packet_indices = []
for ix, packet_pair in enumerate(packet_pairs):
    packet_index = ix+1
    left = packet_pair[0]
    right = packet_pair[1]
    print("PACKET", packet_index, "LEFT", left, "RIGHT", right)
    if in_right_order(packet_pair[0], packet_pair[1]) < 1:
        print("IN RIGHT ORDER!")
        correct_packet_indices.append(packet_index)
    else:
        print("IN THE WRONG ORDER!!")


print(correct_packet_indices)
print(sum(correct_packet_indices))