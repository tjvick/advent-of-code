import numpy as np
import math
import re
import collections

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

breakpoint = file_contents.index('')
rules = file_contents[:breakpoint]
my_ticket = file_contents[breakpoint + 2:breakpoint + 3]
other_tickets = file_contents[breakpoint + 5:]

print(rules)
print(my_ticket)
print(other_tickets)

valid_range_pairs = []
for rule in rules:
    m = re.match(r'^.+: (\d+)-(\d+) or (\d+)-(\d+)$', rule)
    print(m.groups())
    valid_range_pairs.append((
        (int(m.group(1)), int(m.group(2))),
        (int(m.group(3)), int(m.group(4)))
    ))

all_valid_ranges = []
for range_pair in valid_range_pairs:
    all_valid_ranges += [range_pair[0], range_pair[1]]

print(all_valid_ranges)

invalid_ticket_numbers = []
for other_ticket in other_tickets:
    ticket_values = [int(x) for x in other_ticket.split(',')]
    for ticket_value in ticket_values:
        is_valid = False
        for valid_range in all_valid_ranges:
            if valid_range[0] < ticket_value < valid_range[1]:
                is_valid = True
                break

        if not is_valid:
            invalid_ticket_numbers.append(ticket_value)


print(invalid_ticket_numbers)
print(sum(invalid_ticket_numbers))
