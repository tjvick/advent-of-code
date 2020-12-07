import re


def build_tree_edges(file_contents):
    edges = []
    rule_re = re.compile(r'^([\w\s]+) bags contain (\d+ .*)$')
    for rule in file_contents:
        rule_match = rule_re.match(rule)
        if rule_match:
            outer_color = rule_match.group(1)
            inner_colors = re.findall(r'(\d+) ([\w\s]+) bags?', rule_match.group(2))
            for (count, inner_color) in inner_colors:
                edges.append((outer_color, inner_color, int(count)))

    return edges


def travel_down_tree(weighted_edges, starting_node, starting_weight):
    source_nodes = [(starting_node, starting_weight)]
    visited_nodes = []
    while len(source_nodes) > 0:
        source_node, weight = source_nodes.pop()
        visited_nodes.append((source_node, weight))
        attached_edges = [edge for edge in weighted_edges if edge[0] == source_node]
        source_nodes += [(target_node, count*weight) for _, target_node, count in attached_edges]

    return visited_nodes


with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

edges = build_tree_edges(file_contents)
all_visited_nodes = travel_down_tree(edges, 'shiny gold', 1)

sum_of_all_bags = sum([count for _, count in all_visited_nodes])
print(sum_of_all_bags - 1)


