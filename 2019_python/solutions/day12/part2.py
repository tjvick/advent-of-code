import re
import numpy as np
from collections import defaultdict

combs = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def update(moon_velocities, moon_positions):
    # Calculate Velocities
    for comb in combs:
        moon_velocities[comb[0], :] += np.sign(moon_positions[comb[1], :] - moon_positions[comb[0], :])
        moon_velocities[comb[1], :] -= np.sign(moon_positions[comb[1], :] - moon_positions[comb[0], :])

    # Apply Velocity to calc positions
    return moon_velocities, moon_positions + moon_velocities


def update1d(moon_velocities, moon_positions):
    # Calculate Velocities
    for comb in combs:
        moon_velocities[comb[0]] += np.sign(moon_positions[comb[1]] - moon_positions[comb[0]])
        moon_velocities[comb[1]] -= np.sign(moon_positions[comb[1]] - moon_positions[comb[0]])

    # Apply Velocity to calc positions
    return moon_velocities, moon_positions + moon_velocities


def do_the_thing(moon_positions):
    moon_velocities = np.zeros_like(moon_positions)

    repeat_times = []
    for dim in range(3):
        state_history = set()

        moon_velocities_i = moon_velocities[:, dim]
        moon_positions_i = moon_positions[:, dim]

        n_steps = 0
        state = str(moon_velocities_i + moon_positions_i)
        while True:
            state_history.add(state)
            moon_velocities_i, moon_positions_i = update1d(moon_velocities_i, moon_positions_i)

            state = str(np.concatenate((moon_velocities_i, moon_positions_i)))
            if state in state_history:
                print(state)
                print(dim, n_steps)
                repeat_times.append(n_steps)
                break

            n_steps += 1

    print(repeat_times)
    return np.lcm.reduce(repeat_times)


def main():
    moon_positions = []
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')
            pattern = re.compile(r"^<x=(.*), y=(.*), z=(.*)>$")
            m = pattern.match(content)
            moon_position = list(int(x) for x in (m.group(1), m.group(2), m.group(3)))
            moon_positions.append(moon_position)

    return do_the_thing(np.array(moon_positions))


if __name__ == "__main__":
    print(main())
    # cProfile.run('main(100000)')
