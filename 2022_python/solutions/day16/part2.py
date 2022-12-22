from solutions import helpers
import numpy as np
from itertools import combinations
from part1 import extract_graph_and_flow_rates, get_valves_worth_visiting, distance_between, find_best_total_flow

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

N_MINUTES = 26

strings = helpers.read_each_line_as_string(filename)

G, flow_rates = extract_graph_and_flow_rates()
valves_worth_visiting = get_valves_worth_visiting(flow_rates)
set_of_valves_worth_visiting = set(valves_worth_visiting)


def find_farthest_pair():
    farthest_distance = 0
    farthest_pair = ('AA', 'AA')
    for pair in combinations(valves_worth_visiting, 2):
        distance = distance_between(pair[0], pair[1])
        if distance > farthest_distance:
            farthest_distance = distance
            farthest_pair = pair

    return farthest_pair


def find_best_combined_flow(path1_valves, path2_valves, min_split):
    unassigned_valves = set_of_valves_worth_visiting.difference(path1_valves).difference(path2_valves)

    best_combined_flow = 0
    for ix in range(min_split, len(unassigned_valves)-min_split):
        for combo in combinations(unassigned_valves, ix):
            additional_path1_valves = set(combo)
            additional_path2_valves = unassigned_valves.difference(additional_path1_valves)
            best_flow_path1 = find_best_total_flow(valves=additional_path1_valves.union(path1_valves), n_minutes=N_MINUTES)
            best_flow_path2 = find_best_total_flow(valves=additional_path2_valves.union(path2_valves), n_minutes=N_MINUTES)
            total_combined_flow = best_flow_path1 + best_flow_path2
            if total_combined_flow > best_combined_flow:
                best_combined_flow = total_combined_flow
                print(best_combined_flow)

    return best_combined_flow


farthest_pair = find_farthest_pair()
print('Most Distant Pair', farthest_pair)
best_combined_flow = find_best_combined_flow([farthest_pair[0]], [farthest_pair[1]], 6)
print('Best Combined Flow:', best_combined_flow)




