import numpy as np
from part1 import simulate

# x_bounds = [20, 30]
# y_bounds = [-10, -5]
x_bounds = [211, 232]
y_bounds = [-124, -69]

v0x_min = int(np.floor((x_bounds[0]*2)**0.5))
v0x_max = x_bounds[1]
v0y_min = y_bounds[0]
v0y_max = -y_bounds[0]

count_landings = 0
for v0y in range(v0y_min, v0y_max + 1):
    for v0x in range(v0x_min, v0x_max + 1):
        result = simulate(np.array([v0x, v0y]))
        if result >= 0:
            count_landings += 1

print(count_landings)

