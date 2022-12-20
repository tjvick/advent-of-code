from solutions import helpers
import numpy as np
import re
import networkx as nx
from itertools import permutations
import matplotlib.pyplot as plt

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

n_minutes = 30

strings = helpers.read_each_line_as_string(filename)

nodes = []
edges = []
flow_rates = {}

for string in strings:
    m = re.match(r'^Valve (.{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$', string)
    valve_id, flow_rate_str, other_valves_str = m.groups()
    flow_rate = int(flow_rate_str)
    connected_valve_ids = other_valves_str.replace(' ', '').split(',')

    print(valve_id, flow_rate, connected_valve_ids)

    flow_rates[valve_id] = flow_rate
    nodes.append(valve_id)
    for connected_valve_id in connected_valve_ids:
        edges.append((valve_id, connected_valve_id))

print(nodes)
print(edges)

G = nx.Graph()
for node in nodes:
    G.add_node(node)

for edge in edges:
    G.add_edge(*edge)

print(G)

lengths = dict(nx.all_pairs_shortest_path_length(G))

print(lengths)

valves_worth_visiting = [valve_id for valve_id, flow_rate in flow_rates.items() if flow_rate > 0]

print(valves_worth_visiting)


def length(pth):
    total_distance = 0
    for ix, valve in enumerate(pth[:-1]):
        distance = nx.shortest_path_length(G, pth[ix], pth[ix + 1])
        total_distance += (distance + 1)

    return total_distance


def compute_total_flow(pth):
    total_distance = 0
    total_flow = 0
    current_flow = 0
    for ix, valve in enumerate(pth[:-1]):
        distance = nx.shortest_path_length(G, pth[ix], pth[ix + 1])
        total_flow += current_flow * (distance + 1)
        current_flow += flow_rates[pth[ix+1]]
        total_distance += (distance + 1)

    total_flow += (n_minutes - total_distance)*current_flow

    return total_flow


# print(compute_total_flow(['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']))


max_total_flow = 0
current_valve = 'AA'
paths = [['AA']]
while len(paths):
    path = paths.pop()
    total_flow = compute_total_flow(path)
    if total_flow > max_total_flow:
        max_total_flow = total_flow
        print('NEW MAX!', max_total_flow, path)
    unvisited_valves = [v for v in valves_worth_visiting if v not in path]
    for unvisited_valve in unvisited_valves:
        possible_path = path + [unvisited_valve]
        # print("Length", length(possible_path), "Possible Path", possible_path)
        if length(possible_path) <= n_minutes:
            paths.append(possible_path)

print(len(paths))

# print(length(['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']))
# print(compute_total_flow(['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']))


