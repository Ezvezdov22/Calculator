import sys
import pygame
import color_and_grid as cag

DOT = "dot"
SUM = "sum"
SIGN_CHANGE = "sign_change"
PLUS = "+"
MINUS = "-"
MULTIPLY = "*"
CLEAR = "clear"
BACKSPACE = "backspace"
SQRT = "sqrt"
DIVISION = "/"
COLOR = "color"
GRID = "grid"
ICON_WAY = "files/images/icon.png"
SCREENSIZE = (325,685)

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
cag.start_color(screen)
pygame.image.load(cag.start_grid_way())
calculator_img = pygame.image.load(cag.start_grid_way()).convert_alpha()
screen.blit(calculator_img, [0, 0])
pygame.display.set_caption("Calculator 4.0")
pygame.display.set_icon(pygame.image.load(ICON_WAY))


def handle_button(x,y):
    """
    Select button and it's type
    """
    Buttons = [[CLEAR,BACKSPACE,SQRT,DIVISION],[7,8,9,MULTIPLY],[4,5,6,MINUS],[1,2,3,PLUS],[0,DOT,SUM,SIGN_CHANGE]]
    buttonx = x//80
    buttony = (y-45)//80 - 3
    symbol = Buttons[buttony][buttonx]
    value = ""
    if type(symbol) == int:
        value = "number"
    elif symbol == PLUS or symbol ==  MINUS or symbol ==  MULTIPLY or symbol ==  DIVISION:
        value = "act"
    return Buttons[buttony][buttonx], value

def main_cycle():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Checking mouse clicks
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        if y > 285:
                            return handle_button(x,y)
                        elif y < 45 and x < 163:
                            return COLOR , ""
                        elif y <45 and x > 163:
                            return GRID , ""
numbers = ""
numbers1 = ""
numbers2 = ""
numbers3 = ""
act = ""
xy = (10,62)
xy1 = (10,62)
actxy = (10,147)
xy2 = (40,147)
xy3 = (10,227)

fontSize = 55
myFont = pygame.font.SysFont("None", fontSize)

def drawer():
    """
     Display the image on the screen
    """
    global numbers
    global CALCULATOR_WAY
    global calculator_img
    global myFont

    if len(numbers) > 2:
        if numbers[-1] == "0" and numbers[-2] == ".":
            numbers = numbers[:-2]
    fontColor = cag.start_grid_fontcolor()
    if fontColor == (255,255,255):
        cag.colors = cag.colors0
    else:
        cag.colors = cag.colors1

    cag.start_color(screen)
    cag.start_grid_fontcolor()

    screen.blit(calculator_img, [0, 0])
    image_numbers = myFont.render(numbers, 0, (fontColor))
    image_numbers1 = myFont.render(numbers1, 0, (fontColor))
    image_numbers2 = myFont.render(numbers2, 0, (fontColor))
    image_numbers3 = myFont.render(numbers3, 0, (fontColor))
    image_act= myFont.render(act,0,(fontColor))
    screen.blit(image_numbers, xy)
    screen.blit(image_numbers1, xy1)
    screen.blit(image_numbers2, xy2)
    screen.blit(image_numbers3, xy3)
    screen.blit(image_act, actxy)
    pygame.display.flip()

def clearall():
    '''
    Clear all text
    '''
    global numbers
    global numbers1
    global numbers2
    global numbers3
    global xy
    global act

    numbers = ""
    numbers1 = ""
    numbers2 = ""
    numbers3 = ""
    act = ""
    xy = [10,62]

def clearonce():
    '''
    Clear last symbol
    '''
    global numbers
    if len(numbers) != 0:
        numbers = numbers[:-1]

def color_change():
    """
     Change display color
    """
    with open(cag.GRID_WAY) as file_object:
        grid = file_object.read()
    if grid == "0":
        cag.colors = cag.colors0
    else:
        cag.colors = cag.colors1
    cag.color_change(screen)
    screen.blit(calculator_img, [0, 0])

def change_grid():
    """
     Change grid color
    """
    global fontColor
    global calculator_img
    pygame.image.load(cag.change_grid_way())
    calculator_img = pygame.image.load(cag.start_grid_way()).convert_alpha()
    screen.blit(calculator_img, [0, 0])