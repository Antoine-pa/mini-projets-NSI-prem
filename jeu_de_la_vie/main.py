def new_grid(len_x = 500, len_y = 500):
    grid = []
    for y in range(len_y):
        grid.append([])
        for _ in range(len_x):
            grid[y].append(0)
    return grid

grid = new_grid()

def get_element(x, y, grid):
    return grid[y][x]

def set_element(x, y, value, grid):
    grid[y][x] = value
    

for i in range(3):
    set_element(1, i+1, 1, grid)

def gen(old_grid):
    grid = new_grid()
    for y, line in enumerate(old_grid):
        for x, el in enumerate(line):
            nb_in_alive = 0
            for y2 in range(y-1, y+2):
                for x2 in range(x-1, x+2):
                    if x2 >= 0 and x2 < 10 and y2 >= 0 and y2 < 10:
                        nb_in_alive += get_element(x2, y2, old_grid)
            if el == 1:
                nb_in_alive -= 1
                set_element(x, y, int(nb_in_alive in (2, 3)), grid)
            else:
                set_element(x, y, int(nb_in_alive == 3), grid)

    return grid


nb_gen = 3
for generation in range(nb_gen):
    print(f"========== gen {generation + 1}")
    for line in grid:
        print(line)
    grid = gen(grid)
print(f"========== gen {nb_gen + 1}")
for line in grid:
    print(line)