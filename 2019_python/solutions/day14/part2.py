import re
import math
from collections import defaultdict


def convert_once(conversions, bag, elements):
    for element in elements:
        for kr, vr in conversions[element]['requirements'].items():
            n_of_these = math.ceil(bag[element]/int(conversions[element]['count']))*int(vr)
            bag[kr] += n_of_these

    return bag


def n_ore_required(conversions, max_distance, n_fuel):
    chemical_bag = defaultdict(int)
    chemical_bag['FUEL'] = n_fuel
    current_depth = max_distance
    while current_depth > 0:
        elements = [k for k, v in conversions.items() if v['distance'] == current_depth]
        chemical_bag = convert_once(conversions, chemical_bag, elements)
        current_depth += -1
    return chemical_bag['ORE']


def create_fuel(conversions, max_distance, n_ore):
    x = n_ore_required(conversions, max_distance, 1)
    lb = math.floor(n_ore / x)
    ub = lb * 2
    cp = math.floor((ub + lb) / 2)
    while cp not in [lb, ub]:
        print(lb, ub)
        x = n_ore_required(conversions, max_distance, cp)
        if x > n_ore:
            ub = cp
        elif x < n_ore:
            lb = cp
        cp = math.floor((ub + lb) / 2)

    return cp


def distance_from_ore(conversions, key, d):
    bag = conversions[key]
    if list(bag['requirements'].keys()) == ['ORE']:
        return d + 1
    else:
        return max(distance_from_ore(conversions, r, d+1) for r in bag['requirements'].keys())


def do_the_thing(content):
    pattern = re.compile(r"^(\d+) (\w+)$")

    conversions = dict()
    for line in content:
        csv = [x.strip(', ') for x in line.split(',')]
        inputs = csv[0:-1]
        ending = csv[-1].split(' => ')
        inputs.append(ending[0])
        requirements = dict()
        for input in inputs:
            m = pattern.match(input)
            requirements[m.group(2)] = m.group(1)

        output = ending[1]
        m = pattern.match(output)
        conversions[m.group(2)] = {
            'count': m.group(1),
            'requirements': requirements
        }

    max_distance = 0
    for k, v in conversions.items():
        d = distance_from_ore(conversions, k, 0)
        if d > max_distance:
            max_distance = d
        v['distance'] = d

    print(conversions)

    return create_fuel(conversions, max_distance, 1000000000000)


def main(fname):
    with open(fname, 'r') as f:
        lines = [line.strip('\n') for line in f]

    return do_the_thing(lines)


if __name__ == "__main__":
    print(main('./input.txt'))
