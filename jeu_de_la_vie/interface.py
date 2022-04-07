import pygame
from core import *
import time
import json
import tkinter
import tkinter.filedialog

pygame.init()

#INITIALISATION DES VARIABLES---------------------------------------------------
PATH = None

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

#sauvegarder
RECT_SAVE = (100, 640, 140, 32)
THICKNESS_SAVE = 2

#ouvrir
RECT_OPEN = (100, 710, 140, 32)
THICKNESS_OPEN = 2

#sauvegarder comme
RECT_SAVE_AS = (100, 780, 140, 32)
THICKNESS_SAVE_AS = 2

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

#-------------------------------------------------------------------------------

#Initialisation de la fenêtre
screen = pygame.display.set_mode((SIZE_MENU_X + WINDOW_X, WINDOW_Y))
screen.fill(BLACK)

pygame.draw.rect(screen, WHITE, (0, 0, SIZE_MENU_X - THICKNESS, WINDOW_Y - THICKNESS))

#VARIABLES DIVERSES-------------------------------------------------------------

#fonction pour supprimer du text
def clear_text_box(box, thickness_box):
    pygame.draw.rect(screen, WHITE, pygame.Rect(box[0]+thickness_box, box[1]+thickness_box, box[2]-2*thickness_box, box[3]-2*thickness_box), 0)

#fonction pour récuperer la position d'un text en fonction de sa boîte
def pos_text(box, thickness_box):
    return (box[0]+thickness_box+3, box[1]+box[3]-thickness_box-SIZE_TEXT)

#fonction pour afficher le titre d'une boîte
def title_box(box, title):
    pos = (box[0], box[1]-SIZE_TEXT-2)
    Text(title, BLACK, pos, SIZE_TEXT)

#fonction pour rafraichir le jeu
def refresh(grid):
    for y in range(NUMBER_LINE):
        for x in range(NUMBER_COLUMN):
            pygame.draw.rect(screen, dic_grid_color[get_element(x, y, grid)], (SIZE_MENU_X+x*(SPACE_X+THICKNESS)+THICKNESS, y*(SPACE_Y+THICKNESS), SPACE_X, SPACE_Y))
    pygame.display.update()

#fonction pour sauvegarder un fichier
def Save():
    if PATH is None:
        path = Save_as()
        return path
    else:
        with open(PATH, "w") as f:
            f.write(json.dumps({"data":grid}, indent=4))

#fonction pour sauvegarder un fichier comme
def Save_as():
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.asksaveasfilename(parent=top, filetypes=[('json files', '.json')])
    if not file_name.endswith(".json"):
        file_name += ".json"
    top.destroy()
    with open(file_name, "w") as f:
        f.write(json.dumps({"data":grid}, indent=4))
    return PATH

#fonction pour ouvrir un fichier
def Open():
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top, filetypes=[('json files', '.json')])
    top.destroy()
    if file_name == "":
        return
    with open(file_name) as f:
        data = json.load(f)
        data = data.get("data")
    text_input_box_x, text_input_box_y = str(len(data[0])), str(len(data))
    grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y = update_settings_grid(int(text_input_box_x), int(text_input_box_y))
    for y in enumerate(data):
        for x in enumerate(y[1]):
            grid[y[0]][x[0]] = x[1]
    return grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y, file_name

#fonction pour rafraichir les données
def update_settings_grid(x, y):
    grid = new_grid(x, y)
    NUMBER_COLUMN = len(grid[0])
    NUMBER_LINE = len(grid)

    SPACE_X = WINDOW_X/NUMBER_COLUMN - THICKNESS
    SPACE_Y = WINDOW_Y//NUMBER_LINE - THICKNESS

    pygame.draw.rect(screen, BLACK, (SIZE_MENU_X, 0, SIZE_MENU_X + WINDOW_X, WINDOW_Y))

    return grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y

#fonction pour afficher un boutton ou une zone d'entrée avec tout ses texts
def Box(coord, thickness, text, title=None):
    box = pygame.Rect(*coord)
    pygame.draw.rect(screen, BLACK, box, thickness)
    Text(text, BLACK, pos_text(coord, thickness), SIZE_TEXT)
    if title is not None:
        title_box(coord, title)
    return box

#fonction pour afficher du text
def Text(text, color, pos: tuple, size):
    FONT = pygame.font.Font("Melon Honey.ttf", size)
    screen.blit(FONT.render(text, True, color), pos)
    pygame.display.update()
    del FONT
    
refresh(grid)


#INITIALISATION DU MENU---------------------------------------------------------

Text("le jeu de la vie", BLACK, (40, 30), 40)

#Champ d'entré des colonnes
input_box_x = Box(RECT_INPUT_BOX_X, THICKNESS_INPUT_BOX_X, text_input_box_x, "Nombre de colonnes:")
#Champ d'entré des lignes
input_box_y = Box(RECT_INPUT_BOX_Y, THICKNESS_INPUT_BOX_Y, text_input_box_y, "Nombre de lignes:")
#Champ d'entré de la vitesse
input_speed =  Box(RECT_SPEED, THICKNESS_SPEED, text_speed, "Vitesse (s):")
#Boutton pour effacer
clear_grid = Box(RECT_CLEAR_GRID, THICKNESS_CLEAR_GRID, "Effacer")
#Boutton pour mettre en pause
stop_start_grid = Box(RECT_STOP_START, THICKNESS_STOP_START, "Start")
#Boutton pour faire du step by step
sbs_grid = Box(RECT_SBS, THICKNESS_SBS, "Step by step")
#Boutton pour quitter
quit_game = Box(RECT_QUIT, THICKNESS_QUIT, "Quitter")
#Boutton pour sauvegarder
save_file = Box(RECT_SAVE, THICKNESS_SAVE, "Save")
#Boutton pour ouvrir un  fichier
open_file = Box(RECT_OPEN, THICKNESS_OPEN, "Open")

save_as_file = Box(RECT_SAVE_AS, THICKNESS_SAVE_AS, "Save as")

#Initialisation des variables pour la boucle infinie
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

            
        if event.type == pygame.KEYUP:
            #Mettre en pause
            if event.key == pygame.K_SPACE: 
                start_generation = not start_generation
                
            #quitter
            if event.key == pygame.K_ESCAPE: 
                pygame.display.quit()
                continuer = False
                
            #si la zone de texte est cliquée
            if active == "input_box_x": #si il écrit dans la zone de texte
                
                #supprimer
                if event.key == pygame.K_BACKSPACE: 
                    text_input_box_x = text_input_box_x[:-1]
                    
                #valider
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
                output = Save()
                if output is not None:
                    PATH = output
            elif open_file.collidepoint(event.pos):
                output = Open()
                if output is not None:
                    grid, NUMBER_COLUMN, NUMBER_LINE, SPACE_X, SPACE_Y, PATH = output
                refresh(grid)
            elif save_as_file.collidepoint(event.pos):
                PATH = Save_as()
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
