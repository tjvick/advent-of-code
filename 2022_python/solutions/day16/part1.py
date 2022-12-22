import dataclasses
import functools

from solutions import helpers
import numpy as np
import re
import networkx as nx
from functools import cache
import matplotlib.pyplot as plt

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

N_MINUTES = 30


def extract_graph_and_flow_rates():
    strings = helpers.read_each_line_as_string(filename)

    nodes = []
    edges = []
    flow_rates = {}
    for string in strings:
        m = re.match(r'^Valve (.{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$', string)
        valve_id, flow_rate_str, other_valves_str = m.groups()
        flow_rate = int(flow_rate_str)
        connected_valve_ids = other_valves_str.replace(' ', '').split(',')

        flow_rates[valve_id] = flow_rate
        nodes.append(valve_id)
        for connected_valve_id in connected_valve_ids:
            edges.append((valve_id, connected_valve_id))

    G = nx.Graph()
    for node in nodes:
        G.add_node(node)

    for edge in edges:
        G.add_edge(*edge)

    return G, flow_rates


def get_valves_worth_visiting(flow_rates):
    return [valve_id for valve_id, flow_rate in flow_rates.items() if flow_rate > 0]


G, flow_rates = extract_graph_and_flow_rates()
valves_worth_visiting = get_valves_worth_visiting(flow_rates)
set_of_valves_worth_visiting = set(valves_worth_visiting)


def show_graph(graph):
    plt.figure(figsize=(10, 10))
    nx.draw(
        graph,
        nodelist=valves_worth_visiting + ["AA"],
        labels={node: f"{node}/{flow_rate}" for node, flow_rate in flow_rates.items()},
        font_weight='normal'
    )
    plt.show()


# show_graph(G)


@cache
def distance_between(valve_1, valve_2):
    return nx.shortest_path_length(G, valve_1, valve_2)


@dataclasses.dataclass(frozen=True)
class ValvePath:
    path: tuple
    length: int
    total_flow: int
    n_minutes: int

    @property
    def last_valve(self):
        return self.path[-1]

    def unvisited_valves(self, valves=None):
        if valves is None:
            return set_of_valves_worth_visiting.difference(self.path)
        else:
            return set(valves).difference(self.path)

    def compute_new_path_length(self, new_valve):
        return self.length + distance_between(self.last_valve, new_valve) + 1

    def compute_new_valve_path(self, new_valve):
        new_path = self.path + (new_valve,)
        new_length = self.compute_new_path_length(new_valve)
        new_total_flow = self.total_flow + self.compute_delta_total_flow(new_valve)
        return ValvePath(path=new_path, length=new_length, total_flow=new_total_flow, n_minutes=self.n_minutes)

    def compute_delta_total_flow(self, new_valve):
        distance = distance_between(self.last_valve, new_valve)
        time_to_go_turn_on_valve = distance + 1
        total_time_valve_is_on = self.n_minutes - self.length - time_to_go_turn_on_valve
        return total_time_valve_is_on * flow_rates[new_valve]


def find_best_total_flow(valves=None, n_minutes=30):
    max_total_flow = 0
    paths = [ValvePath(path=('AA',), length=0, total_flow=0, n_minutes=n_minutes)]
    while len(paths):
        valve_path = paths.pop()
        if valve_path.total_flow > max_total_flow:
            max_total_flow = valve_path.total_flow

        for unvisited_valve in valve_path.unvisited_valves(valves):
            new_valve_path_length = valve_path.compute_new_path_length(unvisited_valve)
            if new_valve_path_length <= n_minutes:
                new_valve_path = valve_path.compute_new_valve_path(unvisited_valve)
                paths.append(new_valve_path)

    return max_total_flow


if __name__ == '__main__':
    max_total_flow = find_best_total_flow(n_minutes=N_MINUTES)
    print(max_total_flow)