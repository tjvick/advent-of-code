from solutions import helpers
import numpy as np
import re
from collections import Counter

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'


rotations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (-z, -x, y),
]


class Scanner:
    def __init__(self, index):
        self.index = index
        self.system = index
        self.origin = np.array([0, 0, 0])
        self.beacons = []

    def add_beacon(self, beacon_position):
        self.beacons.append(beacon_position)

    def rotate_into_system(self, destination_scanner):
        scanner_a = destination_scanner
        scanner_b = self
        for rot in rotations:
            rotated_beacons = []
            for beacon in scanner_b.beacons:
                rotated_beacons.append(np.array(rot(*beacon)))

            delta_matrix = np.zeros((len(scanner_a.beacons), len(scanner_b.beacons)), dtype=tuple)
            for ix1, scanner_a_beacon in enumerate(scanner_a.beacons):
                for ix2, scanner_b_beacon in enumerate(rotated_beacons):
                    delta_matrix[ix1, ix2] = tuple(scanner_b_beacon - scanner_a_beacon)

            c = Counter(delta_matrix.flatten())
            most_common_delta, n_shared_deltas = c.most_common()[0]
            if n_shared_deltas >= 12:
                self.beacons = rotated_beacons - np.array(most_common_delta)
                self.origin = np.array(rot(*self.origin)) - np.array(most_common_delta)
                self.system = destination_scanner.system
                return


def have_common_beacons(scanner_a: Scanner, scanner_b: Scanner):
    for rot in rotations:
        rotated_beacons = []
        for beacon in scanner_b.beacons:
            rotated_beacons.append(np.array(rot(*beacon)))

        delta_matrix = np.zeros((len(scanner_a.beacons), len(scanner_b.beacons)), dtype=tuple)
        for ix1, scanner_a_beacon in enumerate(scanner_a.beacons):
            for ix2, scanner_b_beacon in enumerate(rotated_beacons):
                delta_matrix[ix1, ix2] = tuple(scanner_b_beacon - scanner_a_beacon)

        c = Counter(delta_matrix.flatten())
        n_shared_deltas = c.most_common()[0][1]
        if n_shared_deltas >= 12:
            return True

    return False


def rotate_into_common_system(scanner_1: Scanner, scanner_2: Scanner):
    if scanner_1.system == 0 and scanner_2.system != 0:
        scanner_2.rotate_into_system(scanner_1)
    elif scanner_2.system == 0 and scanner_1.system != 0:
        scanner_1.rotate_into_system(scanner_2)
    else:
        scanner_2.rotate_into_system(scanner_1)


strings = helpers.read_each_line_as_string(filename)

scanners = []
scanner = None
for row in strings:
    m = re.match(f'--- scanner (\d+) ---', row)
    if m:
        scanner_index = int(m.group(1))
        scanner = Scanner(scanner_index)
        scanners.append(scanner)
    elif len(row) > 0:
        beacon_position = np.fromiter(map(int, row.split(',')), dtype=int)
        scanner.add_beacon(beacon_position)


n_scanners = len(scanners)
n_scanners_not_in_zero = sum([scanner.system != 0 for scanner in scanners])
while n_scanners_not_in_zero > 0:
    for ix1 in range(0, n_scanners):
        for ix2 in range(ix1 + 1, n_scanners):
            scanner_1 = scanners[ix1]
            scanner_2 = scanners[ix2]
            if (scanner_1.system != 0 or scanner_2.system != 0) and have_common_beacons(scanner_1, scanner_2):
                print(ix1, ix2)
                rotate_into_common_system(scanner_1, scanner_2)

    n_scanners_not_in_zero = sum([scanner.system != 0 for scanner in scanners])
    for scanner in scanners:
        print(f'Scanner {scanner.index} is in system {scanner.system}')

all_beacons = set()
for scanner in scanners:
    all_beacons = all_beacons.union(list(map(tuple, scanner.beacons)))


print(len(all_beacons))
