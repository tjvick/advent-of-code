import json
from copy import copy
from functools import cache

from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

monkeys = []
monkey_idx = 0

for string in strings:
    if "Monkey" in string:
        monkey_idx = int(string.strip(':').split()[1])
        monkeys.append({})
        continue

    starting_items = re.match(r'\s+Starting items: (.+)', string)
    if starting_items:
        current_items = [int(item) for item in starting_items.group(1).replace(' ', '').split(',')]
        monkeys[monkey_idx]["items"] = current_items
        continue

    operation = re.match(r'\s+Operation: new = (.+)', string)
    if operation:
        expression = operation.group(1)
        monkeys[monkey_idx]["operation"] = expression

    test = re.match(r'\s+Test: divisible by (\d+)', string)
    if test:
        divisor = test.group(1)
        monkeys[monkey_idx]["divisor"] = int(divisor)

    true_con = re.match(r'\s+If true: throw to monkey (\d+)', string)
    if true_con:
        true_monkey_idx = true_con.group(1)
        monkeys[monkey_idx]["true_monkey_idx"] = int(true_monkey_idx)

    false_con = re.match(r'\s+If false: throw to monkey (\d+)', string)
    if false_con:
        false_monkey_idx = false_con.group(1)
        monkeys[monkey_idx]["false_monkey_idx"] = int(false_monkey_idx)

divisors = [monkey["divisor"] for monkey in monkeys]
divisor = np.product(divisors)


inspection_counter = np.zeros((len(monkeys),), dtype=int)
for round_idx in range(10000):
    for monkey_idx, monkey in enumerate(monkeys):
        while monkey["items"]:
            inspection_counter[monkey_idx] += 1
            worry_level = monkey["items"].pop(0)
            operation = lambda old: eval(monkey["operation"])
            worry_level = operation(worry_level)
            worry_level = worry_level % divisor
            if worry_level % monkey["divisor"] == 0:
                monkeys[monkey["true_monkey_idx"]]["items"].append(worry_level)
            else:
                monkeys[monkey["false_monkey_idx"]]["items"].append(worry_level)

print(inspection_counter)
print(np.product(sorted(inspection_counter, reverse=True)[0:2]))
