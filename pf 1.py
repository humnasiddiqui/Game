def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False


def get_shape():
    return Piece(7, 0, random.choice(shapes))


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("Times New Roman", 80, bold=True)
    label = font.render(text, 1,(0,225,225))
    surface.blit(label,(80,280))


def draw_grid(surface, grid):
    grid_from_x = 280
    grid_from_y = 80
#30 = block size
    for i in range(len(grid)):
        pygame.draw.line(surface, (0,0,0), (grid_from_x, grid_from_y + i*30), (grid_from_x+300, grid_from_y+ i*30))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (0, 0, 0), (grid_from_x + j*30, grid_from_y),(grid_from_x + j*30, grid_from_y + 600))

#variable change krny hen
def clear_rows(grid, locked):

    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0,255,255) not in row:
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


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('Times New Roman', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    grid_from_x = top_left_x + play_width + 50
    grid_from_y = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (grid_from_x + j*block_size, grid_from_y + i*block_size, block_size, block_size), 0)

    surface.blit(label, (grid_from_x + 10, grid_from_y - 30))

