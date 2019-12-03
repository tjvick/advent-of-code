visitation_sets = []

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        route = content.split(',')
        visited_locations = set()
        current_location = (0, 0)
        visited_locations.add(current_location)
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
                visited_locations.add(current_location)

        visitation_sets.append(visited_locations)

a = visitation_sets[0]
b = visitation_sets[1]
print(a.intersection(b))
print(sorted(list(map(lambda x: abs(x[0]) + abs(x[1]), a.intersection(b)))))
