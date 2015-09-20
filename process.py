import pygame
import sys, classes, random

def process(narwhal, FPS, total_frames):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        classes.Narwhal.going_right = True
        narwhal.image = pygame.image.load("images/single_narwhal.png")
        narwhal.velx = 15
    elif keys[pygame.K_a]:
        classes.Narwhal.going_right = False
        narwhal.image = pygame.image.load("images/single_narwhal_flipped.png")
        narwhal.velx = -15
    elif keys[pygame.K_s]:
        narwhal.vely = 15
    elif keys[pygame.K_w]:
        narwhal.vely = -15
    else:
        narwhal.velx = 0
        narwhal.vely = 0

    if keys[pygame.K_SPACE] and classes.Narwhal.going_right == True:
        p = classes.Projectile(narwhal.rect.x + 261, narwhal.rect.y, 60, 15, "images/projectiles/simple_shock.png")
        p.velx = 8
    elif keys[pygame.K_SPACE]:
        p = classes.Projectile(narwhal.rect.x - 60, narwhal.rect.y, 60, 15, "images/projectiles/simple_shock.png")
        p.image = pygame.transform.flip(p.image, True, False)
        p.velx = -8



    spawn(FPS, total_frames)

def spawn(FPS, total_frames):
    four_seconds = FPS * 4
    if total_frames % four_seconds == 0:
        r = random.randint(1, 2)
        x = 1
        if r == 2:
            x = 1280 - 78
        helmetfish = classes.HelmetFish(x, 130, 78, 36, "images/helmetfish.png")