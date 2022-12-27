from collections import defaultdict

from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)


def digit_to_decimal(char):
    if char == "=":
        return -2
    if char == "-":
        return -1

    return int(char)


def snafu_to_decimal(snafu_str):
    chars = list(snafu_str)
    n_digits = len(chars) - 1
    total = 0
    for idig, digit in enumerate(chars):
        power = n_digits - idig
        decimal_digit = digit_to_decimal(digit)
        component = decimal_digit * (5**power)
        total += component

    return total


def decimal_to_snafu(decimal_int):
    position_summands = defaultdict(list)
    remainder = decimal_int
    power = 0
    while remainder != 0:
        divisor = 5 ** power
        modulo = 5 ** (power + 1)
        modulus = remainder % modulo
        fives = modulus // divisor
        if fives == 3:
            position_summands[power].append(-2)
            position_summands[power+1].append(1)
        elif fives == 4:
            position_summands[power].append(-1)
            position_summands[power+1].append(1)
        else:
            position_summands[power].append(fives)

        remainder -= modulus
        power += 1

    snafu_string = ""
    for ix_digit in range(max(position_summands.keys())+1):
        total = sum(position_summands[ix_digit])
        if total == -2:
            char = "="
        elif total == -1:
            char = "-"
        elif total == 0:
            char = '0'
        elif total == 1:
            char = "1"
        elif total == 2:
            char = "2"
        elif total == 3:
            char = "="
            position_summands[ix_digit+1].append(1)
        elif total == 4:
            char = "1"
            position_summands[ix_digit+1].append(1)
        snafu_string += char

    snafu_string = "".join(reversed(snafu_string))
    return snafu_string



total_sum = 0
for string in strings:
    decimal = snafu_to_decimal(string)
    print(string, '::', decimal)
    total_sum += decimal

print(total_sum)
snafu_answer = decimal_to_snafu(total_sum)
print(snafu_answer)


