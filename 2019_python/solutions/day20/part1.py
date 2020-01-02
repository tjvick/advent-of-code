import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Maze:
    def __init__(self, lines):
        g = nx.Graph()

        print('adding nodes...')
        letters = defaultdict(list)
        for ir, line in enumerate(lines):
            for ic, element in enumerate(line):
                if element == ".":
                    g.add_node((ir, ic), letter=element)
                if ord('A') <= ord(element) <= ord('Z'):
                    letters[(ir, ic)] = element

        print('adding edges...')
        for node in g.nodes:
            for dr, dc in zip((0, 0, 1, -1), (1, -1, 0, 0)):
                neighbor = (node[0] + dr, node[1] + dc)
                if neighbor in g:
                    g.add_edge(node, neighbor)

        print('finding portals...')
        portals = defaultdict(list)
        for position, letter in letters.items():
            for dr, dc in zip((0, 1), (1, 0)):
                neighbor = (position[0] + dr, position[1] + dc)
                if neighbor in letters:
                    portal_label = letter + letters[neighbor]
                    nn = (position[0] + 2*dr, position[1] + 2*dc)
                    if nn in g:
                        portals[portal_label].append(nn)

                    pn = (position[0] - 1*dr, position[1] - 1*dc)
                    if pn in g:
                        portals[portal_label].append(pn)

        print('adding portal edges...')
        for portal_label, nodes in portals.items():
            if len(nodes) > 1:
                g.add_edge(nodes[0], nodes[1])
            elif portal_label == 'AA':
                self.start = nodes[0]
            elif portal_label == 'ZZ':
                self.end = nodes[0]

        self.g = g


def do_the_thing(lines):
    M = Maze(lines)

    print('solving maze...')
    return nx.shortest_path_length(M.g, M.start, M.end)


def main(filename):
    with open(filename, 'r') as f:
        lines = [line.strip('\n') for line in f]

    return do_the_thing(lines)


if __name__ == "__main__":
    print(
        main('./input.txt')
    )
