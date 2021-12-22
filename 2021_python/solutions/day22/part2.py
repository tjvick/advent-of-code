from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

pattern = re.compile('(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')

all_cubes = []
x_points = set()
y_points = set()
z_points = set()
for row in strings[:]:
    m = pattern.match(row)
    is_on = m.group(1) == 'on'
    xmin, xmax, ymin, ymax, zmin, zmax = list(map(int, m.group(*range(2, 8))))

    current_cube = [is_on, [(xmin, xmax+1), (ymin, ymax+1), (zmin, zmax+1)]]
    all_cubes.append(current_cube)

    x_points.update((xmin, xmax+1))
    y_points.update((ymin, ymax+1))
    z_points.update((zmin, zmax+1))

n_x = len(x_points)
n_y = len(y_points)
n_z = len(z_points)

x_list = np.array(sorted(list(x_points)))
y_list = np.array(sorted(list(y_points)))
z_list = np.array(sorted(list(z_points)))

state_matrix = np.zeros((n_x-1, n_y-1, n_z-1), dtype=bool)

X, Y, Z = np.ix_(
    x_list[1:] - x_list[:-1],
    y_list[1:] - y_list[:-1],
    z_list[1:] - z_list[:-1]
)
size_matrix = X*Y*Z

for is_on, current_cube in all_cubes:
    print("current_cube", current_cube)
    ix_set = list(filter(lambda ix: current_cube[0][0] <= x_list[ix] <= current_cube[0][1], range(n_x)))
    iy_set = list(filter(lambda iy: current_cube[1][0] <= y_list[iy] <= current_cube[1][1], range(n_y)))
    iz_set = list(filter(lambda iz: current_cube[2][0] <= z_list[iz] <= current_cube[2][1], range(n_z)))
    state_matrix[ix_set[0]:ix_set[-1], iy_set[0]:iy_set[-1], iz_set[0]:iz_set[-1]] = is_on

print(np.sum(state_matrix * size_matrix))

'''
1211172281877240
'''
