import re

with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

edges = []
rule_re = re.compile(r'^([\w\s]+) bags contain (\d+ .* bags?[,.])+$')
for rule in file_contents:
    m = rule_re.match(rule)
    if m:
        outer_color = m.group(1)
        inner_colors = re.findall(r'\d+ ([\w\s]+) bags?', m.group(2))

        for inner_color in inner_colors:
            edges.append((outer_color, inner_color))


nodes_to_check = ['shiny gold']
all_visited_nodes = []
while len(nodes_to_check) > 0:
    node = nodes_to_check.pop()
    all_visited_nodes.append(node)
    containing_nodes = [outer_node for outer_node, inner_node in edges if inner_node == node]
    nodes_to_check += containing_nodes

unique_containing_nodes = set(all_visited_nodes)
unique_containing_nodes.remove('shiny gold')
print(len(unique_containing_nodes))

