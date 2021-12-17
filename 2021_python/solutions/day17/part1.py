import numpy as np

# x_bounds = [20, 30]
# y_bounds = [-10, -5]
x_bounds = [211, 232]
y_bounds = [-124, -69]

v0x_min = int(np.floor((x_bounds[0]*2)**0.5))
v0x_max = int(np.ceil((x_bounds[0]*2)**0.5))
v0y_min = 1
v0y_max = -y_bounds[0]


def simulate(v0):
    v = np.array(v0)
    p = np.array([0, 0])
    peak = 0
    while True:
        p += v
        v[0] -= np.sign(v[0])
        v[1] -= 1
        peak = max(peak, p[1])

        if x_bounds[0] <= p[0] <= x_bounds[1] and y_bounds[0] <= p[1] <= y_bounds[1]:
            # landed
            return peak

        if v[0] == 0 and p[0] < x_bounds[0]:
            # stopped short
            return -3

        if p[0] > x_bounds[1]:
            # too far
            return -1

        if p[1] < y_bounds[0]:
            # too low
            return -2


if __name__ == "__main__":
    # Analytical solution
    max_peak = (v0y_max - 1) * v0y_max / 2
    print(max_peak)

    # Bounded Numerical Solution
    max_peak = 0
    for v0y in range(0, v0y_max + 1):
        valid_vx0 = []
        for v0x in range(v0x_min, v0x_max + 1):
            result = simulate([v0x, v0y])
            if result >= 0:
                valid_vx0.append(v0x)
                max_peak = max(result, max_peak)

    print(max_peak)


