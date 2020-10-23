# import pygame library and intialize the game engine
import pygame
pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

CENTER_OFFSET = 60
WIDTH = 40
FONT_SIZE = 14

# open a new window
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("X-Keyboard")

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()



def button(text, x, y, width, height, text_size, i_color, a_color, action = None ):
    pos_m = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > pos_m[0] > x and y+height > pos_m[1] > y:
        pygame.draw.rect(screen, a_color, (x, y, width, height))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, i_color, (x, y, width, height))

    button_text = pygame.font.Font("LCD_Solid.ttf", text_size)
    text_surf, text_rect = text_objects(text, button_text)
    text_rect.center = ( (x+(width/2)), (y+(height/2)) )
    screen.blit(text_surf, text_rect)




# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop

        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.
    screen.fill(WHITE)
    # The you can draw different shapes and lines or add text to your background stage.

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    layout = {
        "0": (0, 2 * CENTER_OFFSET),
        "1": (0 - CENTER_OFFSET, 2 * CENTER_OFFSET),
        "2": (0 + CENTER_OFFSET, 2 * CENTER_OFFSET),
        "3": (0, 3 * CENTER_OFFSET),
        "4": (0 - CENTER_OFFSET, 3 * CENTER_OFFSET),
        "5": (0 + CENTER_OFFSET, 3 * CENTER_OFFSET),
        "6": (0, 4 * CENTER_OFFSET),
    }
    center = (500, 500)
    pygame.draw.circle(screen, BLACK, center, WIDTH // 3)

    # for letter in alphabet:
    # for letter in alphabet:
    # case "A":
    for index in range(26):
        if index < 7:
            button(alphabet[index],
               center[0] + layout[str(index)][0] - (WIDTH // 2),
               center[1] + -(layout[str(index)][1]) - (WIDTH // 2),
               WIDTH,
               WIDTH,
               FONT_SIZE,
               RED,
               GREEN)
        elif index < 14:
            button(alphabet[index],
                   center[0] + layout[str(index - 7)][1] - (WIDTH // 2),
                   center[1] + -(layout[str(index - 7)][0]) - (WIDTH // 2),
                   WIDTH,
                   WIDTH,
                   FONT_SIZE,
                   RED,
                   GREEN)
        elif index < 21:
            button(alphabet[index],
                   center[0] + layout[str(index - 14)][0] - (WIDTH // 2),
                   center[1] - -(layout[str(index - 14)][1]) - (WIDTH // 2),
                   WIDTH,
                   WIDTH,
                   FONT_SIZE,
                   RED,
                   GREEN)
        elif index < 25:
            button(alphabet[index],
                   center[0] - layout[str(index - 21)][1] - (WIDTH // 2),
                   center[1] + layout[str(index - 21)][0] - (WIDTH // 2),
                   WIDTH,
                   WIDTH,
                   FONT_SIZE,
                   RED,
                   GREEN)
        elif index == 25:
            button(alphabet[index],
                   center[0] - layout[str(index - 21 + 2)][1] - (WIDTH // 2),
                   center[1] + layout[str(index - 21 + 2)][0] - (WIDTH // 2),
                   WIDTH,
                   WIDTH,
                   FONT_SIZE,
                   RED,
                   GREEN)
        else:
            pass

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()