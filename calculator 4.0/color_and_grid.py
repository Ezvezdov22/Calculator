COLOR_WAY = "files/data/color.txt"
GRID_WAY = "files/data/grid.txt"

colors0 = (
        (0, 0, 0),
        (215, 215, 215),
        (255, 0, 0),
        (255, 165, 0),
        (255, 255, 0),
        (0, 128, 0),
        (0, 255, 0),
        (66, 170, 255),
        (0, 0, 255),
        (139, 0, 255),
        (75, 0, 130),
        (150, 75, 0),
        (255, 119, 255),
        (155, 45, 48),
        (145, 30, 66),
        (48, 213, 200),
        (77, 113, 152)
    )
colors1 = (
        (255, 255, 255),
        (215, 215, 215),
        (255, 0, 0),
        (255, 165, 0),
        (255, 255, 0),
        (0, 128, 0),
        (0, 255, 0),
        (66, 170, 255),
        (0, 0, 255),
        (139, 0, 255),
        (75, 0, 130),
        (150, 75, 0),
        (255, 119, 255),
        (155, 45, 48),
        (145, 30, 66),
        (48, 213, 200),
        (77, 113, 152),
    )
colors = colors0
def color_change(screen):
    '''
    Change background color
    '''
    global colors
    with open(COLOR_WAY) as file_object:
        color = file_object.read()
    color = int(color)
    color+=1
    if color == 17:
        color = 0
    with open(COLOR_WAY, 'w') as file_object:
         file_object.write(str(color))
    screen.fill(colors[color])


def start_color(screen):
    """
     Leave the background color of the last run
    """
    global colors
    with open('files/data/color.txt') as file_object:
        color = file_object.read()
    color = int(color)
    screen.fill(colors[color])


def change_grid_way():
    global colors
    global calculator_img
    with open(GRID_WAY) as file_object:
        grid = file_object.read()
    if grid == "0":
        CALCULATOR_WAY = "files/images/calculator1.png"
        colors = colors1
        grid = "1"
    else:
        CALCULATOR_WAY = "files/images/calculator0.png"
        colors = colors0
        grid = "0"
    with open(GRID_WAY, 'w') as file_object:
         file_object.write(grid)
    return CALCULATOR_WAY

def change_grid_fontcolor():
    global colors
    global calculator_img
    with open(GRID_WAY) as file_object:
        grid = file_object.read()
    if grid == "0":
        fontColor = (255, 255, 255)
        colors = colors1
        grid = "1"
    else:
        fontColor = (0, 0, 0)
        colors = colors0
        grid = "0"
    with open(GRID_WAY, 'w') as file_object:
         file_object.write(grid)
    return fontColor

def start_grid_way():
    """
    Leave the grid color of the last run
    """
    with open(GRID_WAY) as file_object:
        grid = file_object.read()
    if grid == "0":
        CALCULATOR_WAY = "files/images/calculator1.png"
    else:
        CALCULATOR_WAY = "files/images/calculator0.png"
    return CALCULATOR_WAY

def start_grid_fontcolor():
    """
     Leave the font color of the last run
    """
    with open(GRID_WAY) as file_object:
        grid = file_object.read()
    if grid == "0":
        fontColor = (255, 255, 255)
    else:
        fontColor = (0, 0, 0)
    return fontColor
