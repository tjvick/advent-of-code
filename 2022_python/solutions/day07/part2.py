from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

pos = []
structure = {"/": {}}
reading = False


def navigate_structure(pos):
    print(pos)
    a = structure
    for p in pos:
        print(p)
        a = a[p]

    return a


for string in strings:
    print(string)

    cd = re.match('\$ cd (.+)', string)
    ls = re.match('\$ ls', string)
    if cd:
        newdir = cd.group(1)
        if newdir == "..":
            pos.pop()
        else:
            pos.append(newdir)
        reading = False
    elif ls:
        reading = True
    elif reading:
        dir = re.match('dir (.+)', string)
        if dir:
            navigate_structure(pos)[dir.group(1)] = {}
        else:
            file = re.match('(\d+) (.+)', string)
            filesize = file.group(1)
            filename = file.group(2)
            navigate_structure(pos)[filename] = filesize


directories = []

print(structure)


def compute_dir_size(dir_dict):
    total_size = 0
    for key, val in dir_dict.items():
        print(type(val))
        print(key,val)
        if type(val) == str:
            total_size += int(val)
        else:
            total_size += compute_dir_size(val)

    directories.append(total_size)
    return total_size


total_size = compute_dir_size(structure)

goal = 30000000 - 70000000 + total_size

print([x for x in sorted(directories) if x > goal][0])