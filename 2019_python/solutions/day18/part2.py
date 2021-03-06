import networkx as nx
import matplotlib.pyplot as plt


class Maze:
    def __init__(self, lines):
        g = nx.Graph()
        labels = dict()
        for ir, line in enumerate(lines):
            for ic, element in enumerate(line):
                if element != "#":
                    g.add_node((ir, ic), letter=element)
                    if element != ".":
                        labels[(ir, ic)] = element

        for node in g.nodes:
            for dr, dc in zip((0, 0, 1, -1), (1, -1, 0, 0)):
                neighbor = (node[0] + dr, node[1] + dc)
                if neighbor in g:
                    g.add_edge(node, neighbor)

        self.g = g
        self.labels = labels
        self.keys = self.find_keys()
        self.doors = self.find_doors()
        self.starts = self.get_nodes_by_label('@')
        self.all_keys_bitarray = (1 << len(self.keys)) - 1

    def find_keys(self):
        keys = dict()
        for k, v in self.labels.items():
            if v.islower():
                keys[k] = v

        return keys

    def find_doors(self):
        doors = dict()
        for k, v in self.labels.items():
            if v.isupper():
                doors[k] = v

        return doors

    def get_nodes_by_label(self, label):
        nodes = []
        for node, lab in self.labels.items():
            if lab == label:
                nodes.append(node)
        return nodes

    def get_inaccessible_keys(self, node):
        inaccessible_keys = 0
        for key_node, key_char in self.keys.items():
            if not nx.has_path(self.g, node, key_node):
                inaccessible_keys |= 1 << key_index(key_char)
        return inaccessible_keys


def key_index(key_char):
    return ord(key_char) - ord('a')


def can_unlock(keychain, door_char):
    door_bit = 1 << key_index(door_char.lower())
    return keychain & door_bit


def run_around(M, start_node, keychain):
    things_to_do = [(start_node, keychain, 0)]

    already_did = dict()
    progress = 0
    while things_to_do:
        node, keychain, distance = things_to_do.pop(0)
        # print("node", node, "keychain", bin(keychain), "distance", distance)

        # check cache
        already_distance = already_did.get((node, keychain), 999999)
        if distance >= already_distance:
            continue
        already_did[(node, keychain)] = distance

        # pick up key
        if node in M.keys:
            key_bit = 1 << key_index(M.keys[node])
            keychain |= key_bit

        # check if done
        if keychain == M.all_keys_bitarray:
            print("hey!", distance)
            return distance

        # dissolve if run into door
        if node in M.doors and not can_unlock(keychain, M.doors[node]):
            continue

        distance += 1
        things_to_do += [(edge[1], keychain, distance) for edge in M.g.edges(node)]

        progress += 1
        if progress % 10000 == 0:
            print("\r%d" % (progress / 10000), 'things to do', len(things_to_do), 'distance', distance)


def do_the_thing(lines):
    M = Maze(lines)
    draw_graph(M.g, 'maze.png', M.labels)

    total_distance = 0
    for starting_position in M.starts:
        distance = run_around(M, starting_position, M.get_inaccessible_keys(starting_position))
        print('starting_position', starting_position, 'distance', distance)
        total_distance += distance

    return total_distance


def draw_graph(g, name, labels=None, edge_labels=None):
    fig = plt.figure()
    fig.add_subplot(111)
    pos = nx.spring_layout(g)
    nx.draw(g, pos=pos, with_labels=True, node_size=5, labels=labels, edge_color='gray')
    if edge_labels is not None:
        nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=edge_labels)
    plt.savefig(name)


def main(filename):
    with open(filename, 'r') as f:
        lines = [line.strip('\n') for line in f]

    return do_the_thing(lines)


if __name__ == "__main__":
    print(
        main('./input2.txt')
    )
