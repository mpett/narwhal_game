from classes import *
from process import *

# Init
pygame.init()
SCREENWIDTH, SCREENHEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
background = pygame.image.load("images/underwater_background/background2.png")
narwhal1 = Narwhal(0, SCREENHEIGHT - 90, "images/single_narwhal.png", 7)
helmetfish = HelmetFish(30, 100, "images/helmetfish.png")
FPS = 24
total_frames = 0
# Colors
clr1 = (123, 23, 34)
clr2 = (55, 233, 12)
clr3 = (25, 44, 123)
changing_color = 0

# Main loop
while True:
    # Processes
    process(narwhal1, FPS, total_frames)
    # Logic
    narwhal1.motion(SCREENWIDTH)
    HelmetFish.movement(SCREENWIDTH)
    Projectile.movement()
    HelmetFish.update_all(SCREENWIDTH, SCREENHEIGHT)
    collisions()
    total_frames += 1
    #Draw
    screen.blit(background, (0, 0))
    BaseClass.all_sprites.draw(screen)
    Projectile.List.draw(screen)
    # Flip y-axis
    pygame.display.flip()
    # Clock
    clock.tick(FPS)