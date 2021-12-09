from solutions import helpers

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

easy_numbers_by_length = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def determine_output_number_value(row):
    observed_digits, output_digits = (s.split() for s in row.split(' | '))

    segment_definitions = {
        easy_numbers_by_length.get(len(digit)): set(digit)
        for digit in observed_digits
    }

    _1, _4, _7, _8 = (segment_definitions[ix] for ix in [1, 4, 7, 8])

    segment_subsets_by_length = {
        5: {
            3: _7,
            5: _4 - _1,
            2: _8 - _4
        },
        6: {
            0: (_8 - _4) | _1,
            6: _8 - _1,
            9: _4,
        }
    }

    def determine_number_value(digit):
        if len(digit) in easy_numbers_by_length:
            return easy_numbers_by_length[len(digit)]

        for ix, subset in segment_subsets_by_length[len(digit)].items():
            if subset.issubset(digit):
                return ix

    return int(''.join(map(str, map(determine_number_value, output_digits))))


output_value_sum = sum(map(determine_output_number_value, strings))
print(output_value_sum)
