import re

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

breakpoint = file_contents.index('')
rules = file_contents[:breakpoint]
my_ticket = file_contents[breakpoint + 2:breakpoint + 3]
other_tickets = file_contents[breakpoint + 5:]

print(rules)

valid_range_pairs = []
rule_names = []
for rule_assignment in rules:
    m = re.match(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$', rule_assignment)
    rule_names.append(m.group(1))
    valid_range_pairs.append((
        (int(m.group(2)), int(m.group(3))),
        (int(m.group(4)), int(m.group(5)))
    ))

all_valid_ranges = []
for range_pair in valid_range_pairs:
    all_valid_ranges += [range_pair[0], range_pair[1]]

print(all_valid_ranges)

valid_tickets = []
invalid_ticket_numbers = []
for other_ticket in other_tickets:
    is_valid_ticket = True
    ticket_values = [int(x) for x in other_ticket.split(',')]
    for ticket_value in ticket_values:
        is_valid_value = False
        for valid_range in all_valid_ranges:
            if valid_range[0] < ticket_value < valid_range[1]:
                is_valid_value = True
                break

        if not is_valid_value:
            is_valid_ticket = False
            invalid_ticket_numbers.append(ticket_value)

    if is_valid_ticket:
        valid_tickets.append(ticket_values)


possible_rule_assignments = [set(range(len(rule_names))) for _ in range(len(valid_tickets[0]))]
for ticket_values in valid_tickets:
    for ticket_ix, ticket_value in enumerate(ticket_values):
        for rule_ix, valid_range_pair in enumerate(valid_range_pairs):
            if not valid_range_pair[0][0] <= ticket_value <= valid_range_pair[0][1]:
                if not valid_range_pair[1][0] <= ticket_value <= valid_range_pair[1][1]:
                    # print('ticket value', ticket_value, 'not in', valid_range_pair, 'with rule index', rule_ix)
                    possible_rule_assignments[ticket_ix].remove(rule_ix)

print(possible_rule_assignments)
actual_rule_assignments = [-1 for _ in range(len(valid_tickets[0]))]
fully_deduced = False
while not fully_deduced:
    for ix, rule_assignment in enumerate(possible_rule_assignments):
        if len(rule_assignment) == 1:
            actual_assignment = list(rule_assignment)[0]
            print("We know the rule for ticket value index", ix, '-> rule number', actual_assignment)
            actual_rule_assignments[ix] = actual_assignment
            new_rule_assignments = [rule_assignment.discard(actual_assignment) for rule_assignment in possible_rule_assignments]
            break

    fully_deduced = not any([x == -1 for x in actual_rule_assignments])

print(actual_rule_assignments)

departure_rule_indices = [ix for ix, rule_name in enumerate(rule_names) if 'departure' in rule_name]
print(departure_rule_indices)

my_ticket_values = [int(x) for x in my_ticket[0].split(",")]
p = 1
for departure_rule_index in departure_rule_indices:
    ticket_value_index = actual_rule_assignments.index(departure_rule_index)
    p *= my_ticket_values[ticket_value_index]

print(p)