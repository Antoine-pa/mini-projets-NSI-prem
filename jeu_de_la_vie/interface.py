# -*- coding: utf-8 -*-

import pygame
from core import *
import time

pygame.init()

#Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 230, 240)
GREY_WHITE = (200, 200, 200)
GREY = (100, 100, 100)
dic_grid_color = {0 : GREY, 1 : GREY_WHITE}

#MENU
SIZE_TEXT = 20
active = None

#input box x
text_input_box_x = "15"
RECT_INPUT_BOX_X = (100, 150, 140, 32)
THICKNESS_INPUT_BOX_X = 2

#input box y
text_input_box_y = "10"
RECT_INPUT_BOX_Y = (100, 220, 140, 32)
THICKNESS_INPUT_BOX_Y = 2

#clear grid
RECT_CLEAR_GRID = (100, 290, 140, 32)
THICKNESS_CLEAR_GRID = 2

#stop/start
RECT_STOP_START = (100, 360, 140, 32)
THICKNESS_STOP_START = 2

#step_by_step
RECT_SBS = (100, 430, 140, 32)
THICKNESS_SBS = 2

#speed
text_speed = "1"
RECT_SPEED = (100, 500, 140, 32)
THICKNESS_SPEED = 2

#quit
RECT_QUIT = (100, 570, 140, 32)
THICKNESS_QUIT = 2

#quit
RECT_SAVE = (100, 640, 140, 32)
THICKNESS_SAVE = 2

#quit
RECT_OPEN = (100, 710, 140, 32)
THICKNESS_OPEN = 2

#initialisation de la grille
grid = new_grid(int(text_input_box_x), int(text_input_box_y))
SPEED = float(text_speed)

#Dimensions
screen_info = pygame.display.Info()
THICKNESS = 3

SIZE_MENU_X = screen_info.current_w // 5

WINDOW_X = screen_info.current_w - SIZE_MENU_X
WINDOW_Y = screen_info.current_h

NUMBER_COLUMN = len(grid[0])
NUMBER_LINE = len(grid)

SPACE_X = WINDOW_X/NUMBER_COLUMN - THICKNESS
SPACE_Y = WINDOW_Y/NUMBER_LINE - THICKNESS

#Initialisation de la fenêtre
screen = pygame.display.set_mode((SIZE_MENU_X + WINDOW_X, WINDOW_Y))
screen.fill(BLACK)

pygame.draw.rect(screen, WHITE, (0, 0, SIZE_MENU_X - THICKNESS, WINDOW_Y - THICKNESS))

def clear_text_box(box, thickness_box):
    pygame.draw.rect(screen, WHITE, pygame.Rect(box[0]+thickness_box, box[1]+thickness_box, box[2]-2*thickness_box, box[3]-2*thickness_box), 0)

def pos_text(box, thickness_box):
    return (box[0]+thickness_box+3, box[1]+box[3]-thickness_box-SIZE_TEXT)

def title_box(box, title):
    pos = (box[0], box[1]-SIZE_TEXT-2)
    Text(title, BLACK, pos, SIZE_TEXT)

def refresh(grid):
    for y in range(NUMBER_LINE):
        for x in range(NUMBER_COLUMN):
            pygame.draw.rect(screen, dic_grid_color[get_element(x, y, grid)], (SIZE_MENU_X+x*(SPACE_X+THICKNESS)+THICKNESS, y*(SPACE_Y+THICKNESS), SPACE_X, SPACE_Y))
    pygame.display.update()

def Save():
    print("save")

def Open():
    print("open")

def update_settings_grid(x, y):
    grid = new_grid(x, y)
    NUMBER_COLUMN = len(grid[0])
    NUMBER_LINE = len(grid)

    SPACE_X = WINDOW_X/NUMBER_COLUMN - THICKNESS
    SPACE_Y = WINDOW_Y//NUMBER_LINE - THICKNESS

    pygame.draw.rect(screen, BLACK, (SIZE_MENU_X, 0, SIZE_MENU_X + WINDOW_X, WINDOW_Y))

    return grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y

def Box(coord, thickness, text, title=None):
    box = pygame.Rect(*coord)
    pygame.draw.rect(screen, BLACK, box, thickness)
    Text(text, BLACK, pos_text(coord, thickness), SIZE_TEXT)
    if title is not None:
        title_box(coord, title)
    return box

def Text(text, color, pos: tuple, size):
    FONT = pygame.font.Font("Melon Honey.ttf", size)
    screen.blit(FONT.render(text, True, color), pos)
    pygame.display.update()
    del FONT


refresh(grid)

#init menu
Text("le jeu de la vie", BLACK, (40, 30), 40)

input_box_x = Box(RECT_INPUT_BOX_X, THICKNESS_INPUT_BOX_X, text_input_box_x, "Nombre de colonnes:")
input_box_y = Box(RECT_INPUT_BOX_Y, THICKNESS_INPUT_BOX_Y, text_input_box_y, "Nombre de lignes:")
input_speed =  Box(RECT_SPEED, THICKNESS_SPEED, text_speed, "Vitesse (s):")

clear_grid = Box(RECT_CLEAR_GRID, THICKNESS_CLEAR_GRID, "Effacer")
stop_start_grid = Box(RECT_STOP_START, THICKNESS_STOP_START, "Start")
sbs_grid = Box(RECT_SBS, THICKNESS_SBS, "Step by step")
quit_game = Box(RECT_QUIT, THICKNESS_QUIT, "Quitter")
save_file = Box(RECT_SAVE, THICKNESS_SAVE, "Save")
open_file = Box(RECT_OPEN, THICKNESS_OPEN, "Open")

#Initialisation des variables
continuer = True
start_generation = False
start_at = time.time()
#Boucle infinie
while continuer:
    #Evénements
    for event in pygame.event.get():
        #Quitter
        if event.type == pygame.QUIT:
            pygame.quit()
            continuer = False

        #Remplacer les cases
        if event.type == pygame.MOUSEBUTTONUP and start_generation == False:
            pos = list(pygame.mouse.get_pos())
            if pos[0] > SIZE_MENU_X:
                pos[0] -= SIZE_MENU_X
                pos[0] //= SPACE_X + THICKNESS
                pos[1] //= SPACE_Y + THICKNESS
                grid = click(pos, grid)
                refresh(grid)
            else:
                pass


        #Mettre en pause
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: #lancer le jeu
                start_generation = not start_generation

            if event.key == pygame.K_ESCAPE: #quitter
                pygame.display.quit()
                continuer = False

            if active == "input_box_x": #si il écrit dans la zone de texte
                if event.key == pygame.K_BACKSPACE: #si il supp
                    text_input_box_x = text_input_box_x[:-1]

                elif event.key == pygame.K_RETURN:
                    grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y = update_settings_grid(int(text_input_box_x), int(text_input_box_y))
                    Text(str(NUMBER_COLUMN), BLACK, pos_text(RECT_INPUT_BOX_X, THICKNESS_INPUT_BOX_X), SIZE_TEXT)
                    refresh(grid)
                else:
                    el = event.unicode
                    if el.isdigit():
                        text_input_box_x += el

                if event.key != pygame.K_RETURN:
                    clear_text_box(RECT_INPUT_BOX_X, THICKNESS_INPUT_BOX_X)
                    Text(text_input_box_x, BLACK, pos_text(RECT_INPUT_BOX_X, THICKNESS_INPUT_BOX_X), SIZE_TEXT)
                    pygame.display.update()

            elif active == "input_box_y": #si il écrit dans la zone de texte
                if event.key == pygame.K_BACKSPACE: #si il supp
                    text_input_box_y = text_input_box_y[:-1]

                elif event.key == pygame.K_RETURN:
                    grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y = update_settings_grid(int(text_input_box_x), int(text_input_box_y))
                    refresh(grid)
                else:
                    el = event.unicode
                    if el.isdigit():
                        text_input_box_y += el

                if event.key != pygame.K_RETURN:
                    clear_text_box(RECT_INPUT_BOX_Y, THICKNESS_INPUT_BOX_Y)
                    Text(text_input_box_y, BLACK, pos_text(RECT_INPUT_BOX_Y, THICKNESS_INPUT_BOX_Y), SIZE_TEXT)
                    pygame.display.update()

            elif active == "input_speed": #si il écrit dans la zone de texte
                if event.key == pygame.K_BACKSPACE: #si il supp
                    text_speed = text_speed[:-1]

                elif event.key == pygame.K_RETURN:
                    SPEED = float(text_speed)
                else:
                    el = event.unicode
                    if el.isdigit() or el in (".", ","):
                        if el == ",":
                            el = "."
                        text_speed += el

                if event.key != pygame.K_RETURN:
                    clear_text_box(RECT_SPEED, THICKNESS_SPEED)
                    Text(text_speed, BLACK, pos_text(RECT_SPEED, THICKNESS_SPEED), SIZE_TEXT)
                    pygame.display.update()



        if event.type == pygame.MOUSEBUTTONUP:
            if input_box_x.collidepoint(event.pos):
                active = "input_box_x"
            elif input_box_y.collidepoint(event.pos):
                active = "input_box_y"
            elif input_speed.collidepoint(event.pos):
                active = "input_speed"
            elif clear_grid.collidepoint(event.pos):
                grid = new_grid(NUMBER_COLUMN, NUMBER_LINE)
                refresh(grid)
            elif stop_start_grid.collidepoint(event.pos): #lancer le jeu
                start_generation = not start_generation
                clear_text_box(RECT_STOP_START, THICKNESS_STOP_START)
                if start_generation:
                    text = "Stop"
                else:
                    text = "Start"
                Text(text, BLACK, pos_text(RECT_STOP_START, THICKNESS_STOP_START), SIZE_TEXT)
            elif sbs_grid.collidepoint(event.pos):
                grid = gen(grid)
                refresh(grid)
            elif quit_game.collidepoint(event.pos):
                pygame.display.quit()
                continuer = False
            elif save_file.collidepoint(event.pos):
                Save()
            elif open_file.collidepoint(event.pos):
                Open()
            else:
                active = None



    #Le jeu se lance
    if start_generation:
        t = time.time()-start_at
        if t>SPEED:
            start_at = time.time()
            grid = gen(grid)
            refresh(grid)
            pygame.display.update()


pygame.quit()
