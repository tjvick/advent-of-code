import math


def find_best_asteroid(grid):
    asteroids = set()
    for ir, row in enumerate(grid):
        for ic, el in enumerate(row):
            if el:
                asteroids.add((ic, ir))

    max_unique_slopes = 0
    for asteroid in asteroids:
        slopes = set()
        for other in asteroids:
            dx = asteroid[0] - other[0]
            dy = asteroid[1] - other[1]
            norm = (dx**2 + dy**2)**0.5
            if norm != 0:
                slope = (int(dx/norm*10000000), int(dy/norm*10000000))
                slopes.add(slope)
        if len(slopes) > max_unique_slopes:
            best_asteroid = asteroid
            max_unique_slopes = len(slopes)

    return best_asteroid


def vaporize(grid, station_coordinates):
    print(grid)
    asteroids = set()
    for ir, row in enumerate(grid):
        for ic, el in enumerate(row):
            if el:
                asteroids.add((ic, ir))

    asteroid = station_coordinates
    grouped_by_angle = dict()
    for other in asteroids:
        dx = other[0] - asteroid[0]
        dy = other[1] - asteroid[1]
        norm = (dx**2 + dy**2)**0.5
        if norm != 0:
            angle = int(math.atan2(dy, dx)*10000000)/10000000
            vector_description = (angle, norm, other)
            if angle in grouped_by_angle:
                grouped_by_angle[angle].append(vector_description)
            else:
                grouped_by_angle[angle] = [vector_description]

    aiming_details = []
    for angle, descriptions in grouped_by_angle.items():
        grouped_by_angle[angle] = sorted(descriptions, key=lambda v: (v[1]))
        for ix, el in enumerate(grouped_by_angle[angle]):
            angle_from_top = angle + math.pi/2
            angle_from_top_wraparound = angle_from_top if angle_from_top > 0 else angle_from_top + 2*math.pi
            aiming_details.append((ix, angle_from_top_wraparound, el[2]))

    vaporizing_order = sorted(aiming_details, key=lambda v: (v[0], v[1]))
    print(vaporizing_order)
    print(vaporizing_order[199])

    return vaporizing_order[199][2]


def main():
    asteroid_grid = []
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')
            is_asteroid = list(map(lambda x: x == '#', list(content)))
            asteroid_grid.append(is_asteroid)

    best_asteroid = find_best_asteroid(asteroid_grid)
    return vaporize(asteroid_grid, best_asteroid)


if __name__ == "__main__":
    print(main())
