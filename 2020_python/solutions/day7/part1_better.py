import re


def build_tree_edges(file_contents):
    edges = []
    rule_re = re.compile(r'^([\w\s]+) bags contain (\d+ .* bags?[,.])+$')
    for rule in file_contents:
        m = rule_re.match(rule)
        if m:
            outer_color = m.group(1)
            inner_colors = re.findall(r'\d+ ([\w\s]+) bags?', m.group(2))

            for inner_color in inner_colors:
                edges.append((outer_color, inner_color))

    return edges


def travel_up_tree(unweighted_edges, starting_node):
    target_nodes = [starting_node]
    visited_nodes = []
    while len(target_nodes) > 0:
        node = target_nodes.pop()
        visited_nodes.append(node)
        target_nodes += [source_node for source_node, target_node in unweighted_edges if target_node == node]

    return visited_nodes


with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

edges = build_tree_edges(file_contents)
all_visited_nodes = travel_up_tree(edges, 'shiny gold')

unique_containing_nodes = set(all_visited_nodes)
unique_containing_nodes.remove('shiny gold')
print(len(unique_containing_nodes))