import pygame
import sys

def process(narwhal):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        narwhal.image = pygame.image.load("images/single_narwhal.png")
        narwhal.velx = 5
    elif keys[pygame.K_a]:
        narwhal.image = pygame.image.load("images/single_narwhal_flipped.png")
        narwhal.velx = -5
    else:
        narwhal.velx = 0