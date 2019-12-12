import re
import numpy as np
from itertools import combinations
import cProfile
from collections import defaultdict
from update import update_bunch, update


def do_the_thing(moon_positions, stop_after=None):
    sd = defaultdict(set)
    state_history = set()
    energy_lookup = dict()
    moon_velocities = np.zeros_like(moon_positions)

    n_steps = 0
    while True:
        if n_steps % 10000 == 0:
            print('step', n_steps+1)

        moon_velocities, moon_positions, pot, kin = update(moon_velocities, moon_positions)

        if pot in sd:
            if kin in sd[pot]:
                print('wow')
                print('step', n_steps)
                break

        sd[pot].add(kin)

        n_steps += 1
        if stop_after is not None and n_steps+1 > stop_after:
            break

    return None


def main(*args):
    moon_positions = []
    with open('./scratch.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')
            pattern = re.compile(r"^<x=(.*), y=(.*), z=(.*)>$")
            m = pattern.match(content)
            moon_position = list(int(x) for x in (m.group(1), m.group(2), m.group(3)))
            moon_positions.append(moon_position)

    return do_the_thing(np.array(moon_positions), *args)


if __name__ == "__main__":
    print(main())
    # cProfile.run('main(100000)')
