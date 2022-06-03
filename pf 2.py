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
    label = font.render('Tetris by Humna and Kainat', 1, (0,0,0))

    win.blit(background_image, [0, 0])
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

#calling draw grid function tw dra grid inside rectangle
    draw_grid(surface, grid)
    #pygame.display.update()
