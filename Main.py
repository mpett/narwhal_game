import sys
from Classes import *

# Init
pygame.init()
SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
narwhal1 = Narwhal(0, 50, 261, 92, "images/single_narwhal.png")
narwhal2 = Narwhal(0, 150, 261, 92, "images/single_narwhal.png")
narwhal2 = Narwhal(0, 250, 261, 92, "images/single_narwhal.png")
FPS = 24

# Colors
clr1 = (123, 23, 34)
clr2 = (55, 233, 12)
clr3 = (25, 44, 123)
changing_color = 0

# ----------- Main game loop -----------
while True:
    # Processes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Logic
    narwhal1.motion()
    narwhal2.motion()
    changing_color += 10
    if changing_color >= 255:
        changing_color %= 255

    # Draw
    screen.fill((changing_color, 40, 243))
    BaseClass.all_sprites.draw(screen)
    # Flip y-axis
    pygame.display.flip()

    # Clock
    clock.tick(FPS)
# ----------- Main game loop -----------