visitation_sets = []

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        route = content.split(',')
        visited_locations = dict()
        current_location = (0, 0)
        n_steps = 0
        visited_locations[current_location] = n_steps
        for instruction in route:
            dir = instruction[0]
            dist = int(instruction[1:])
            for d in range(dist):
                if dir == 'R':
                    current_location = (current_location[0], current_location[1]+1)
                elif dir == 'L':
                    current_location = (current_location[0], current_location[1]-1)
                elif dir == 'U':
                    current_location = (current_location[0]+1, current_location[1])
                elif dir == 'D':
                    current_location = (current_location[0]-1, current_location[1])

                n_steps += 1
                if current_location in visited_locations.keys():
                    visited_locations[current_location] = min(visited_locations[current_location], n_steps)
                else:
                    visited_locations[current_location] = n_steps

        visitation_sets.append(visited_locations)

a = visitation_sets[0]
b = visitation_sets[1]
intersections = set(a.keys()).intersection(set(b.keys()))
print(sorted(list(map(lambda x: a[x]+b[x], intersections))))
