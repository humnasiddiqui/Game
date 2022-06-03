#link of site
#https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/
# main library for game environment
import pygame
# library to use randomness
import random

#Initializing game fonts - text
pygame.font.init()

# GLOBALS VARS
#screen width
s_width = 800
#screen height
s_height = 700
# meaning 300 // 10 = 30 width per block
play_width = 300
 # meaning 600 // 20 = 30 height per block
play_height = 600 
block_size = 30

top_left_x = 280
top_left_y = 80


#s = shapes
# initializing different shapes that will appear in game
s1 = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

s2 = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

s3 = [['..0..',
       '..0..',
       '..0..',
       '..0..',
       '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

s4 = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

s5 = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

s6 = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

s7 = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [s1 , s2 , s3 , s4 , s5 , s6 , s7]
# Assigning different colors to shapes
# Color = (R, G, B) - R is Red, G is Green and B is Blue
shape_colors = [(0, 200, 0), (200, 0, 0), (255, 87, 101), (255, 255, 0), (255, 100, 0), (0, 0, 150), (128, 0, 100)]
# index 0 - 6 represent shape



#Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor for creating objects.
# class to initialize game piece
# each peice consist of x coordinate and y coordinate
# The shape of piece and color of shape
# There is also rotation of shape 
class Piece(object):
    #"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.
    #This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
    def __init__(self, x, y, shape):
        #With this keyword, you can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0



#this function have 1 parameter that is dictionery
def create_grid(locked_pos={}):
    # make grid, where grid removed because of clear rows
    grid = [[(200,200,200) for x in range(10)] for y in range(20)]
    # iterate through each row in grid
    for i in range(len(grid)):
        # iterate through each column in grid
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                #make tuple inside the list
                c = locked_pos[(j,i)]
                # grid is initializing 
                grid[i][j] = c
    return grid



#this function have 1 parameter that is shape
def convert_shape_format(shape):
    #create an empty list
    positions = []
    # this method is used to rotate and change shape
    format = shape.shape[shape.rotation % len(shape.shape)]
# enumerate counts of iterations
# i = counts of iteration
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            # if the position is designated as locked, then don't change
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions




#this function have 2 parameter 
def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (200,200,200)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]
#in convert_shape_format we have rotated shape
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


#this function have 1 parameter 
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            #means there are some space left
            return True
    # If no position left, mean lost
    return False

#this function have no parameter 
def get_shape():
    # This method get random shape from available shapes
    return Piece(6, 0, random.choice(shapes))



#this function have 4 parameter 
def draw_text_middle(surface, text, size, color):
    #in this function we set all those which are necessary to display text
    font = pygame.font.SysFont("Times New Roman", 80, bold=True ,italic = True)
    label = font.render(text, 1,color)
    surface.blit(label,(80,280))


#this function have 2 parameter 
def draw_grid(surface, grid):
    #this function draw grid where game pieces will be displayed
    grid_from_x = 280
    grid_from_y = 80
#30 = block size
    for i in range(len(grid)):
        pygame.draw.line(surface, (0,0,0), (grid_from_x, grid_from_y + i*30), (grid_from_x+300, grid_from_y+ i*30))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (0, 0, 0), (grid_from_x + j*30, grid_from_y),(grid_from_x + j*30, grid_from_y + 600))



#this function have 2 parameter
def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (200,200,200) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j,i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc


#this function have 2 parameter
def draw_next_shape(shape, surface):
    # once shape is place, new will be created
    font = pygame.font.SysFont('Times New Roman', 30 , bold = True)
    label = font.render('Next Shape', 1, (0,0,0))

    grid_from_x = top_left_x + play_width + 50
    grid_from_y = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (grid_from_x + j*block_size, grid_from_y + i*block_size, block_size, block_size), 0)
    surface.blit(label, (grid_from_x + 10, grid_from_y - 30))



# update score in file
def update_score(Score):
    score = max_score()
    with open('scores.txt', 'w') as file:
        if int(score) > Score:
            file.write(str(score))
        else:
            file.write(str(Score))

#reading score from file
def max_score():
    try:
        file = open('scores.txt', 'r')
        lines = file.readlines()
#the whitespaces from the start and end of the string will be removed by strip method.
        score = lines[0].strip()
    except IOError:
        print("file not found")
        score = str(0)
    return score 



# this function draw the game window
def draw_window(surface, grid, score=0, last_score = 0):
    surface.fill((0, 0, 0))
# uploading background image
    background_image = pygame.image.load("img3.jpg").convert()
    background_image = pygame.transform.scale(background_image, (1280, 720))
 # initializing and styling font   
    pygame.font.init()
    font = pygame.font.SysFont('Times New Roman', 50 , bold = True, italic = True )
    label = font.render('              Tetris ', 1, (0,0,0))
    window.blit(background_image, [0, 0])
    surface.blit(label,(90, 20))

    # current score
    font = pygame.font.SysFont('Times New Roman', 30 , bold = True)
    label = font.render('Score: ' + str(score), 1, (0,0,0))

    grid_from_x = top_left_x + play_width + 50
    grid_from_y = top_left_y + play_height/2 - 100
    surface.blit(label, (grid_from_x + 20, grid_from_y + 160))
    # last score
    label = font.render('High Score: ' + last_score, 1, (0,0,0))
    surface.blit(label, (30,350))

# drawing rectangle around grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)
    pygame.draw.rect(surface, (0, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

#calling draw grid function to draw grid inside rectangle
    draw_grid(surface, grid)
    #pygame.display.update()


#this function have 1 parameter
def main(window):
    # store last maximum score
    last_score = max_score()
    # zero locked positions
    locked_positions = {}
    # create grid first
    grid = create_grid(locked_positions)
#set some variable
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

#runs till run = True
    while run:
        grid = create_grid(locked_positions)
        # the game piece will move with time clock
        #The number of milliseconds that passed between the previous two calls to Clock.tick().
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        #Returns the number of millisconds since pygame.init() was called. Before pygame is initialized this will always be 0.
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time/1000 > fall_speed: 
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        #Pygame will register all events from the user into an event queue which can be received with the code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            # perform different actions on different key events
            if event.type == pygame.KEYDOWN:
                # on left key move toward left side
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1
                # on right key, move toward right side
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1
                # move down on down key
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                # rotate piece on up key
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
        # convert shape
        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                # Set current piece color to grid
                grid[y][x] = current_piece.color
        #execute if change piece is equal to true
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10
        # Once piece placed, now update grid
        draw_window(window, grid, score, last_score)
        draw_next_shape(next_piece, window)
        pygame.display.update()
        # condition to check whether you loose, all position locked
        if check_lost(locked_positions):
            draw_text_middle(window, "    YOU LOST!", 100, (0,0,0))
            pygame.display.update()
            pygame.time.delay(10000)
            run = False
            update_score(score)

#this function have 1 parameter
def main_menu(window):  
    run = True
    # this will be continue untill run become false
    while run:
        window.fill((0,0,0))
        draw_text_middle(window, 'Press Enter To Play', 60, (0,255,255))
        # this is used to update display
        pygame.display.update()
        # take event from pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #game starts on pressing enter key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    main(window)
                elif event.key == pygame.K_RETURN:
                    main(window)
                    
    # stop the game display
    pygame.display.quit()

# initialize windows with defined height and width
window = pygame.display.set_mode((s_width, s_height))
# set the title of game window
pygame.display.set_caption('Tetris')
# call main function here
main_menu(window)
