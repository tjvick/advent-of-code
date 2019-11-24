import re

fabric = [0] * 1210000
with open('input.txt', 'r') as f:
    for line in f:
        # pattern = re.compile(r"^\#(\d+)\w+@\w+(\d+),(\d+):\w+(\d+)x(\d+)$")
        pattern = re.compile(r"^#(\d+)\s+@\s+(\d+),(\d+):\s(\d+)x(\d+)$")
        m = pattern.match(line.strip('\n'))
        corner_left = int(m.group(2))
        corner_top = int(m.group(3))
        width = int(m.group(4))
        height = int(m.group(5))
        for x in range(width):
            for y in range(height):
                X = corner_left+x
                Y = corner_top+y
                fabric[X*1100+Y] += 1

n_overlaps = 0
for s in fabric:
    if s > 1:
        n_overlaps += 1

print(n_overlaps)


