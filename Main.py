import pygame
import sys

# Init
pygame.init()
WIDTH, HEIGHT = 640,360
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24
img_narwhal = pygame.image.load("single_narwhal.png")

# Colors
clr1 = (123, 23, 34)
clr2 = (55, 233, 12)
clr3 = (25, 44, 123)
changing_color = 0

# Main game loop
while True:
    # Processes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Logic
    changing_color += 10
    if changing_color >= 255:
        changing_color %= 255

    # Draw
    screen.fill((changing_color, 40, 243))
    screen.blit(img_narwhal, (200, 200))
    # Flip y-axis
    pygame.display.flip()

    # Clock
    clock.tick(FPS)