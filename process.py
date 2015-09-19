import pygame
import sys, classes, random

def process(narwhal, FPS, total_frames):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        narwhal.image = pygame.image.load("images/single_narwhal.png")
        narwhal.velx = 15
    elif keys[pygame.K_a]:
        narwhal.image = pygame.image.load("images/single_narwhal_flipped.png")
        narwhal.velx = -15
    elif keys[pygame.K_s]:
        narwhal.vely = 15
    elif keys[pygame.K_w]:
        narwhal.vely = -15
    else:
        narwhal.velx = 0
        narwhal.vely = 0

    spawn(FPS, total_frames)

def spawn(FPS, total_frames):
    four_seconds = FPS * 4
    if total_frames % four_seconds == 0:
        r = random.randint(1, 2)
        x = 1
        if r == 2:
            x = 1280 - 78
        helmetfish = classes.HelmetFish(x, 130, 78, 36, "images/helmetfish.png")