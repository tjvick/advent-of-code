import re
import math
import numpy as np
import collections

with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

all_pairs = []

rule_re = re.compile(r'^([\w\s]+) bags contain (\d+ .* bags?[,.])+$')
emptry_rule_re = re.compile(r'^([\w\s]+) bags contain no other bags.$')
for rule in file_contents:
    m = rule_re.match(rule)
    if m:
        outer_color = m.group(1)
        inner_colors = re.findall(r'\d+ ([\w\s]+) bags?', m.group(2))

        for inner_color in inner_colors:
            all_pairs.append((outer_color, inner_color))

print(all_pairs)

things_to_check = []
for outer, inner in all_pairs:
    if inner == "shiny gold":
        things_to_check.append(outer)

all_containers = [x for x in things_to_check]
print(things_to_check)

while len(things_to_check) > 0:
    x = things_to_check.pop()
    containers = [outer for outer, inner in all_pairs if inner == x]
    things_to_check += containers
    all_containers += containers

print(things_to_check)
print(set(all_containers))
print(len(set(all_containers)))

