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

RECT_INPUT_BOX_X = (100, 100, 140, 32)
RECT_CLEAR_INPUT_BOX_X = (RECT_INPUT_BOX_X[0]+3, RECT_INPUT_BOX_X[1]+3, RECT_INPUT_BOX_X[2]-6, RECT_INPUT_BOX_X[3]-6)
POS_TEXT_BOX_X = (RECT_INPUT_BOX_X[0] + 5, RECT_INPUT_BOX_X[1]+9)
THICKNESS_INPUT_BOX_X = 2
#input box y
text_input_box_y = "10"

RECT_INPUT_BOX_Y = (100, 150, 140, 32)
RECT_CLEAR_INPUT_BOX_Y = (RECT_INPUT_BOX_Y[0]+3, RECT_INPUT_BOX_Y[1]+3, RECT_INPUT_BOX_Y[2]-6, RECT_INPUT_BOX_Y[3]-6)
POS_TEXT_BOX_Y = (RECT_INPUT_BOX_Y[0] + 5, RECT_INPUT_BOX_Y[1]+9)
THICKNESS_INPUT_BOX_Y = 2

#initialisation de la grille
grid = new_grid(int(text_input_box_x), int(text_input_box_y))
SPEED = 1

#Dimensions
screen_info = pygame.display.Info()
THICKNESS = 3

SIZE_MENU_X = screen_info.current_w // 5

WINDOW_X = screen_info.current_w - SIZE_MENU_X
WINDOW_Y = screen_info.current_h

NUMBER_COLUMN = len(grid[0])
NUMBER_LINE = len(grid)

SPACE_X = WINDOW_X//NUMBER_COLUMN - THICKNESS
SPACE_Y = WINDOW_Y//NUMBER_LINE - THICKNESS

#Initialisation de la fenêtre
screen = pygame.display.set_mode((SIZE_MENU_X + WINDOW_X, WINDOW_Y))
screen.fill(BLACK)

pygame.draw.rect(screen, WHITE, (0, 0, SIZE_MENU_X - THICKNESS, WINDOW_Y - THICKNESS))



def refresh(grid):
    for y in range(NUMBER_LINE):
        for x in range(NUMBER_COLUMN):
            pygame.draw.rect(screen, dic_grid_color[get_element(x, y, grid)], (SIZE_MENU_X+x*(SPACE_X+THICKNESS), y*(SPACE_Y+THICKNESS), SPACE_X, SPACE_Y))
    pygame.display.update()

def update_settings_grid(x, y):
    grid = new_grid(x, y)
    NUMBER_COLUMN = len(grid[0])
    NUMBER_LINE = len(grid)

    SPACE_X = WINDOW_X//NUMBER_COLUMN - THICKNESS
    SPACE_Y = WINDOW_Y//NUMBER_LINE - THICKNESS

    pygame.draw.rect(screen, BLACK, (SIZE_MENU_X, 0, SIZE_MENU_X + WINDOW_X, WINDOW_Y))

    return grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y




refresh(grid)

def Text(text, color, pos, size):
    FONT = pygame.font.Font("Melon Honey.ttf", size)
    screen.blit(FONT.render(text, True, color), pos)
    pygame.display.update()
    del FONT



#init menu
Text("le jeu de la vie", BLACK, (40, 30), 40)
input_box_x = pygame.Rect(*RECT_INPUT_BOX_X)
pygame.draw.rect(screen, BLACK, input_box_x, THICKNESS_INPUT_BOX_X)
Text(text_input_box_x, BLACK, POS_TEXT_BOX_X, SIZE_TEXT)

input_box_y = pygame.Rect(*RECT_INPUT_BOX_Y)
pygame.draw.rect(screen, BLACK, input_box_y, THICKNESS_INPUT_BOX_Y)
Text(text_input_box_y, BLACK, POS_TEXT_BOX_Y, SIZE_TEXT)


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
                    refresh(grid)
                else:
                    el = event.unicode
                    if el.isdigit():
                        text_input_box_x += el

                if event.key != pygame.K_RETURN:
                    pygame.draw.rect(screen, WHITE, pygame.Rect(*RECT_CLEAR_INPUT_BOX_X), 0)
                    Text(text_input_box_x, BLACK, POS_TEXT_BOX_X, SIZE_TEXT)
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
                    pygame.draw.rect(screen, WHITE, pygame.Rect(*RECT_CLEAR_INPUT_BOX_Y), 0)
                    Text(text_input_box_y, BLACK, POS_TEXT_BOX_Y, SIZE_TEXT)
                    pygame.display.update()



        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box_x.collidepoint(event.pos):
                active = "input_box_x"
            elif input_box_y.collidepoint(event.pos):
                active = "input_box_y"
            else:
                active = None



    #Le jeu se joue
    if start_generation:
        t = time.time()-start_at
        if t>SPEED:
            start_at = time.time()
            grid = gen(grid)
            refresh(grid)
            pygame.display.update()


pygame.quit()
