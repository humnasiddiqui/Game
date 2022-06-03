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
pygame.display.set_caption('Tetris, Project by Humna and Kainat')
# call main function here
main_menu(window)
