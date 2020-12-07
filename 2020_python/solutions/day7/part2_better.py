import re

with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

edges = []
rule_re = re.compile(r'^([\w\s]+) bags contain (\d+ .*)$')
empty_rule_re = re.compile(r'^([\w\s]+) bags contain no other bags.$')
for rule in file_contents:
    rule_match = rule_re.match(rule)
    if rule_match:
        outer_color = rule_match.group(1)
        inner_colors = re.findall(r'(\d+) ([\w\s]+) bags?', rule_match.group(2))
        for inner_color in inner_colors:
            edges.append((outer_color, inner_color[1], int(inner_color[0])))
    else:
        empty_rule_match = empty_rule_re.match(rule)
        outer_color = empty_rule_match.group(1)


source_nodes = [('shiny gold', 1)]

all_node_visits = []
while len(source_nodes) > 0:
    source_node, weight = source_nodes.pop()
    all_node_visits.append((source_node, weight))
    attached_edges = [edge for edge in edges if edge[0] == source_node]
    for edge in attached_edges:
        source_nodes.append((edge[1], edge[2] * weight))

sum_of_all_bags = sum([count for _, count in all_node_visits])
print(sum_of_all_bags - 1)


