import pygame
import sys

pygame.init()
pygame.display.set_mode((640, 360), 0, 32)

clock = pygame.time.Clock()
FPS = 24

while True:
    # Processes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

    # Logic

    # Draw
    clock.tick(FPS)