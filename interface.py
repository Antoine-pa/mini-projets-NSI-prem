import pygame
from jeu_de_la_vie import *
import time

pygame.init()

SPEED = 1
FONT = pygame.font.Font("Melon Honey.ttf", 40)

#Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 230, 240)
GREY_WHITE = (200, 200, 200)
GREY = (100, 100, 100)
dic_grid_color = {0 : GREY, 1 : GREY_WHITE}

#initialisation de la grille
grid = new_grid(15, 10)

#Dimensions
screen_info = pygame.display.Info()
THICKNESS = 3

WINDOW_Y = screen_info.current_h
NUMBER_LINE = len(grid)
SPACE_Y = WINDOW_Y//NUMBER_LINE - THICKNESS

WINDOW_X = screen_info.current_w
SIZE_MENU_X = WINDOW_X // 5
WINDOW_X -= SIZE_MENU_X
NUMBER_COLUMN = len(grid[0])
SPACE_X = WINDOW_X//NUMBER_COLUMN - THICKNESS

#Initialisation de la fenêtre
screen = pygame.display.set_mode((SIZE_MENU_X + WINDOW_X, WINDOW_Y))
screen.fill(BLACK)

pygame.draw.rect(screen, WHITE, (0, 0, SIZE_MENU_X - THICKNESS, WINDOW_Y - THICKNESS))



def refresh(grid):
    for y in range(NUMBER_LINE):
        for x in range(NUMBER_COLUMN):
            pygame.draw.rect(screen, dic_grid_color[get_element(x, y, grid)], (SIZE_MENU_X+x*(SPACE_X+THICKNESS), y*(SPACE_Y+THICKNESS), SPACE_X, SPACE_Y))

    pygame.display.update()

refresh(grid)

def Text(text, color, pos):
    screen.blit(FONT.render(text, True, color), pos)



#menu
Text("le jeu de la vie", BLACK, (40, 30))
active = None
input_box_x = pygame.Rect(100, 100, 140, 32)
text_input_box_x = "15"
pygame.draw.rect(screen, BLACK, input_box, 2)
pygame.display.update()


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
            if event.key == pygame.K_SPACE:
                start_generation = not start_generation

            if event.key == pygame.K_ESCAPE:
                del FONT
                pygame.display.quit()
                continuer = False

            if active == "input_box_x":
                if event.key == pygame.K_BACKSPACE:
                    text_input_box_x = text_input_box_x[:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    el = event.unicode
                    print(el)
                    if el.isdigit():
                        text_input_box_x += el
                        print(text_input_box_x)


        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box_x rect.
            if input_box_x.collidepoint(event.pos):
                # Toggle the active variable.
                active = "input_box_x"
            else:
                active = None


    #Le jeu se joue
    if start_generation:
        t = time.time()-start_at
        if t>SPEED:
            start_at = time.time()
            grid = gen(grid)
            refresh(grid)


pygame.quit()



