import pygame
import sys

# Init
pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)
clock = pygame.time.Clock()
FPS = 24

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
    pygame.draw.circle(screen, clr2, (350, 200), 80, 30)
    pygame.draw.line(screen, clr1, (0, 0), (640, 360), 5)
    pygame.draw.rect(screen, clr3, (40, 40, 300, 45))

    # Flip y-axis
    pygame.display.flip()

    # Clock
    clock.tick(FPS)