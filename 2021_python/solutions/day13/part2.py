from solutions import helpers
import numpy as np
import re

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

point_pattern = re.compile('(\d+),(\d+)')
fold_x_pattern = re.compile('fold along x=(\d+)')
fold_y_pattern = re.compile('fold along y=(\d+)')

points = []
folds = []
for string in strings:
    if point_pattern.match(string):
        x, y = point_pattern.match(string).groups()
        points.append((x, y))
    if fold_x_pattern.match(string):
        folds.append(('x', fold_x_pattern.match(string).group(1)))
    if fold_y_pattern.match(string):
        folds.append(('y', fold_y_pattern.match(string).group(1)))

first_fold = folds[0]

points = np.array(points, dtype=int)
for fold in folds:
    print(len(points))
    if fold[0] == 'x':
        line_location = int(fold[1])
        new_points = np.stack((line_location - np.abs(points[:, 0]-line_location), points[:, 1])).transpose()
        # print(len(np.unique(new_points, axis=0)))
        points = np.unique(new_points, axis=0)
    else:
        line_location = int(fold[1])
        new_points = np.stack((points[:, 0], line_location - np.abs(points[:, 1]-line_location))).transpose()
        # print(len(np.unique(new_points, axis=0)))
        points = np.unique(new_points, axis=0)

print(points)

matrix = np.zeros((39, 6), dtype=str)
np.set_printoptions(edgeitems=30, linewidth=100000)
for point in points:
    matrix[point[0], point[1]] = 'X'

t = matrix.transpose()
for row in t:
    row[row == ''] = '.'
    print(''.join(row))


