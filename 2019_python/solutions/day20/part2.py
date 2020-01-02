import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Maze:
    def __init__(self, lines):
        g = nx.Graph()

        print('adding nodes...')
        max_line_width = 0
        letters = defaultdict(list)
        for ir, line in enumerate(lines):
            max_line_width = max(max_line_width, len(line))
            for ic, element in enumerate(line):
                if element == ".":
                    g.add_node((ir, ic), letter=element)
                if ord('A') <= ord(element) <= ord('Z'):
                    letters[(ir, ic)] = element

        outer_row_boundaries = [2, len(lines)-3]
        outer_col_boundaries = [2, max_line_width-3]
        for node in g.nodes:
            if node[0] in outer_row_boundaries or node[1] in outer_col_boundaries:
                g.nodes[node]['surface'] = -1

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
                        if g.nodes[nn].get('surface', 0) == 0:
                            g.nodes[nn]['surface'] = 1

                    pn = (position[0] - 1*dr, position[1] - 1*dc)
                    if pn in g:
                        portals[portal_label].append(pn)
                        if g.nodes[pn].get('surface', 0) == 0:
                            g.nodes[pn]['surface'] = 1


        print('adding portal edges...')
        portal_nodes = []
        for portal_label, nodes in portals.items():
            if len(nodes) > 1:
                g.add_edge(nodes[0], nodes[1])
            elif portal_label == 'AA':
                self.start = nodes[0]
            elif portal_label == 'ZZ':
                self.end = nodes[0]

            portal_nodes += nodes

        self.g = g
        self.portals = set(portal_nodes)
        self.lines = lines

    def print(self, p, x):
        lines_copy = []
        for ir, line in enumerate(self.lines):
            line_list = list(line)
            for ic, char in enumerate(line_list):
                if (ir, ic) in x:
                    line_list[ic] = '@'
                if (ir, ic) == p:
                    line_list[ic] = '$'
            lines_copy.append(''.join(line_list))

        return "\n".join(lines_copy)

    def solve(self):
        things_to_do = [(self.start, 0, 0)]

        already_did = dict()
        progress = 0
        while things_to_do:
            node, distance, depth = things_to_do.pop(0)

            # maze = self.print(node, [x[0] for x in things_to_do])
            # print(maze)
            # input("Press Enter to continue...")

            # check cache
            already_distance = already_did.get((node, depth), 9999999)
            if distance >= already_distance:
                continue
            already_did[(node, depth)] = distance

            # check if done
            if node == self.end:
                if depth == 0:
                    return distance
                continue

            depth_change = self.g.nodes[node].get('surface', 0)

            for edge in self.g.edges(node):
                next_node = edge[1]
                next_distance = distance + 1
                next_depth = depth
                if edge[1] in self.portals:
                    next_depth += depth_change

                if next_depth >= 0 and already_did.get((next_node, next_depth), 999999) >= next_distance:
                    things_to_do.append((next_node, next_distance, next_depth))

            progress += 1
            if progress % 10000 == 0:
                print('things to do', len(things_to_do), 'distance', distance)


def do_the_thing(lines):
    M = Maze(lines)
    print('solving maze...')
    return M.solve()


def main(filename):
    with open(filename, 'r') as f:
        lines = [line.strip('\n') for line in f]

    return do_the_thing(lines)


if __name__ == "__main__":
    print(
        main('./input.txt')
    )
