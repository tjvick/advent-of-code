import numpy as np

combs = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def update(moon_velocities, moon_positions):
    # Calculate Velocities
    for comb in combs:
        moon_velocities[comb[0], :] += np.sign(moon_positions[comb[1], :] - moon_positions[comb[0], :])
        moon_velocities[comb[1], :] -= np.sign(moon_positions[comb[1], :] - moon_positions[comb[0], :])

    # Apply Velocity to calc positions
    return moon_velocities, moon_positions + moon_velocities