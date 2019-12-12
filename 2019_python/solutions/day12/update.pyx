import numpy as np
from itertools import combinations

combs = ((0,1), (0,2), (0,3), (1, 2), (1, 3), (2, 3))

def update(moon_velocities, moon_positions):
    # Calculate Velocities
    for comb in combs:
        moon_velocities[comb[0], :] += np.sign(moon_positions[comb[1], :] - moon_positions[comb[0], :])
        moon_velocities[comb[1], :] -= np.sign(moon_positions[comb[1], :] - moon_positions[comb[0], :])

    # h = xxhash.xxh64()
    # h.update(moon_positions)
    # sa = h.intdigest()
    # h.reset()

    # h.update(moon_velocities)
    # sb = h.intdigest()
    # h.reset()

    pot = np.sum(np.abs(moon_positions), 1)
    kin = np.sum(np.abs(moon_velocities), 1)
    # energy = np.multiply(pot, kin)

    # Apply Velocity to calc positions
    return moon_velocities, moon_positions + moon_velocities, tuple(pot), tuple(kin)


def update_bunch(moon_velocities, moon_positions, n_steps):
    for ix in range(n_steps):
        moon_velocities, moon_positions, _, _ = update(moon_velocities, moon_positions)

    return moon_velocities, moon_positions
