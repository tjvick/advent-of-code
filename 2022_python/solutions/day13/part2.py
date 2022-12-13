from solutions import helpers
import numpy as np
import re
from functools import cmp_to_key

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

packets = []
for string in strings:
    if string != "":
        packets.append(eval(string))

packets.append([[2]])
packets.append([[6]])

print(packets)


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


def comparer(left, right):
    return in_right_order(left, right)


sorted_packets = sorted(packets, key=cmp_to_key(comparer))
print("\n".join(str(packet) for packet in sorted_packets))

ix_two_packet = next(ix for ix, packet in enumerate(sorted_packets) if packet == [[2]]) + 1
ix_six_packet = next(ix for ix, packet in enumerate(sorted_packets) if packet == [[6]]) + 1

print(ix_two_packet * ix_six_packet)