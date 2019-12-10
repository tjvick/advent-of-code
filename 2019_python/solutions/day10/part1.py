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


def main():
    asteroid_grid = []
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')
            is_asteroid = list(map(lambda x: x == '#', list(content)))
            asteroid_grid.append(is_asteroid)

    return find_best_asteroid(asteroid_grid)


if __name__ == "__main__":
    print(main())
