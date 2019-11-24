import re

fabric = [set() for _ in range(1000*1000)]
claim_set = set()
conflict_set = set()
with open('input.txt', 'r') as f:
    for line in f:
        pattern = re.compile(r"^#(\d+)\s+@\s+(\d+),(\d+):\s(\d+)x(\d+)$")
        m = pattern.match(line.strip('\n'))
        claim_id = m.group(1)
        corner_left = int(m.group(2))
        corner_top = int(m.group(3))
        width = int(m.group(4))
        height = int(m.group(5))
        n_claimed = 0
        print(claim_id)
        claim_set.add(claim_id)
        for x in range(width):
            for y in range(height):
                X = corner_left+x
                Y = corner_top+y
                existing_ids = fabric[X*1000 + Y]
                conflict_set.update(existing_ids)
                if len(existing_ids) > 0:
                    conflict_set.add(claim_id)
                fabric[X*1000+Y].add(claim_id)

print(conflict_set)
print(len(conflict_set))
print(len(claim_set))
print('answer:')
print(claim_set.difference(conflict_set))
