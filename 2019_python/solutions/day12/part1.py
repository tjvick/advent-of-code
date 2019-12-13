import re
import numpy as np
from itertools import combinations


def do_the_thing(moon_positions):
    moon_velocities = np.zeros_like(moon_positions)
    n_steps = 100
    for ix in range(n_steps):
        print('step', ix+1)
        # Calculate Velocities
        combs = combinations(range(4), 2)
        for comb in combs:
            for dim in range(3):
                xa = moon_positions[comb[0]][dim]
                xb = moon_positions[comb[1]][dim]
                vxa = 1 if xb > xa else (-1 if xb < xa else 0)
                vxb = -vxa

                moon_velocities[comb[0]][dim] += vxa
                moon_velocities[comb[1]][dim] += vxb

        # Apply Velocity to calc positions
        moon_positions += moon_velocities

        print(moon_positions)
        print(moon_velocities)

    pot = np.sum(np.abs(moon_positions), 1)
    kin = np.sum(np.abs(moon_velocities), 1)
    energy = np.multiply(pot, kin)
    print(sum(energy))
    return None


def main():
    moon_positions = []
    with open('./scratch1.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')
            pattern = re.compile(r"^<x=(.*), y=(.*), z=(.*)>$")
            m = pattern.match(content)
            moon_position = list(int(x) for x in (m.group(1), m.group(2), m.group(3)))
            moon_positions.append(moon_position)

    return do_the_thing(np.array(moon_positions))


if __name__ == "__main__":
    print(main())
