from solutions import helpers
import re
from collections import Counter, defaultdict

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

polymer = strings[0]

pattern = re.compile('(\w+) -> (\w+)')
insertion_rules = {}
for string in strings[2:]:
    k, v  = pattern.match(string).groups()
    insertion_rules[k] = v


def pairwise(thing):
    a, b = iter(thing), iter(thing)
    next(b)

    return zip(a, b)


mappings = {}
for pair, inserted in insertion_rules.items():
    key = pair
    value = {''.join(chars): 1 for chars in pairwise([pair[0], inserted, pair[1]])}
    mappings[key] = value

print(mappings)


all_counts = defaultdict(int)
for pair in pairwise(polymer):
    all_counts[''.join(pair)] += 1

print('all_counts', all_counts)

for istep in range(40):
    new_all_counts = defaultdict(int)
    for k, v in all_counts.items():
        for resulting_pair, resulting_quantity in mappings[k].items():
            new_all_counts[resulting_pair] += v*resulting_quantity

    all_counts = new_all_counts
    print('all_counts', all_counts)

print(sum(dict(all_counts).values()))


def count_for_letter(all_counts, letter):
    count_for_letter = 0
    for pair, count in all_counts.items():
        if letter in pair:
            if pair == letter+letter:
                count_for_letter += 2*count
            else:
                count_for_letter += count

    if polymer[0] == letter or polymer[-1] == letter:
        count_for_letter += 1

    return count_for_letter / 2


all_letters = set(''.join(list(dict(all_counts).keys())))
letter_counts = {}
for letter in all_letters:
    letter_counts[letter] = count_for_letter(all_counts, letter)

final_counter = Counter(letter_counts)
print(final_counter.most_common())
most = final_counter.most_common()
print(most[0][1] - most[-1][1])


# 4209548416842 not right
