def new_grid(len_x, len_y): #pour créer une nouvelle grille
    grid = []
    for y in range(len_y):
        grid.append([])
        for _ in range(len_x):
            grid[y].append(0)
    return grid


def get_element(x, y, grid): #pour récupérer un élément

    return grid[round(y)][round(x)]

def set_element(x, y, value, grid): #pour enregister un élément
    grid[round(y)][round(x)] = value
    return grid

def click(coord : tuple, grid):
    x, y = coord
    grid = set_element(x, y, int(not bool(get_element(x, y, grid))), grid)
    return grid

def display_cli_grid(grid):
    for line in grid:
        print(line)


def gen(old_grid): #pour faire une nouvelle génération de cellule
    grid = new_grid(len(old_grid[0]), len(old_grid))
    for y, line in enumerate(old_grid): #ligne par ligne
        for x, el in enumerate(line): #colonne par colonne
            nb_in_alive = 0 #nombre de cellules voisines en vie
            for y2 in range(y-1, y+2): #on parcours les voisines
                for x2 in range(x-1, x+2): #on parcours les voisines
                    if x2 >= 0 and x2 < len(old_grid[0]) and y2 >= 0 and y2 < len(old_grid):
                        nb_in_alive += get_element(x2, y2, old_grid)
            if el == 1: #si la cellule actuelle est en vie
                nb_in_alive -= 1 #on la remet à 0
                grid = set_element(x, y, int(nb_in_alive in (2, 3)), grid) #on change son état
            else: #si elle était morte
                grid = set_element(x, y, int(nb_in_alive == 3), grid) #on change son état

    return grid
