import numpy as np


class LifeGrid:
    def __init__(self, input_grid):
        self.grid = np.array(input_grid)
        self.n_living_neighbors = np.empty_like(input_grid, dtype=int)
        [self.nr, self.nc] = self.grid.shape

    def update(self):
        self.count_living_neighbors()
        self.grid = self.live_or_die()
        return self.grid

    def count_living_neighbors(self):
        [nr, nc] = self.grid.shape
        expanded_grid = np.zeros((nr+2, nc+2))
        expanded_grid[1:-1, 1:-1] = self.grid
        window = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
        for ir in range(nr):
            for ic in range(nc):
                self.n_living_neighbors[ir, ic] = np.sum(window*expanded_grid[ir:ir+3, ic:ic+3])

    def live_or_die(self):
        x = []
        for alive, n_neighbors in zip(self.grid.flatten(), self.n_living_neighbors.flatten()):
            if alive and n_neighbors == 1:
                x.append(1)
            elif not alive and (n_neighbors == 1 or n_neighbors == 2):
                x.append(1)
            else:
                x.append(0)

        self.grid = np.reshape(x, (self.nr, self.nc))
        return self.grid


def parse(content):
    grid = []
    for line in content:
        status = [c == '#' for c in line.strip('\n')]
        grid.append(status)

    return grid


def render(grid):
    for row in grid:
        print(''.join("#" if c else "." for c in row))


def do_the_thing(content):
    input_grid = parse(content)

    life_grid = LifeGrid(input_grid)

    history = set()
    while True:
        life_status = life_grid.update()
        life_status_hashable = tuple(map(tuple, life_status))
        if life_status_hashable in history:
            render(life_status)
            biodiversity = sum([alive*2**ix for ix, alive in enumerate(life_status.flatten())])
            print('biodiversity', biodiversity)
            break
        history.add(life_status_hashable)



    return None


def main():
    with open('./input.txt', 'r') as f:
        content = [line for line in f]

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
