import pygame
import sys, classes, random

def process(narwhal, FPS, total_frames):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    classes.Projectile.fire = not classes.Projectile.fire
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

    if keys[pygame.K_SPACE]:
        def direction(p):
            if classes.Narwhal.going_right:
                p.velx = 8
            else:
                p.velx = -8
                p.image = pygame.transform.flip(p.image, True, False)

        if classes.Projectile.fire and classes.Narwhal.going_right:
            p = classes.Projectile(narwhal.rect.x + 261, narwhal.rect.y, "images/projectiles/simple_shock_fire.png")
            direction(p)
        elif not classes.Projectile.fire and classes.Narwhal.going_right:
            p = classes.Projectile(narwhal.rect.x + 261, narwhal.rect.y, "images/projectiles/simple_shock.png")
            direction(p)
        elif not classes.Narwhal.going_right and classes.Projectile.fire:
            p = classes.Projectile(narwhal.rect.x - 60, narwhal.rect.y, "images/projectiles/simple_shock_fire.png")
            direction(p)
        else:
            p = classes.Projectile(narwhal.rect.x - 60, narwhal.rect.y, "images/projectiles/simple_shock.png")
            direction(p)

    spawn(FPS, total_frames)

def spawn(FPS, total_frames):
    four_seconds = FPS * 4
    if total_frames % four_seconds == 0:
        r = random.randint(1, 2)
        x = 1
        if r == 2:
            x = 1280 - 78
        classes.HelmetFish(x, 130, "images/helmetfish.png")

def collisions():
    for helmetfish in classes.HelmetFish.List:
        helemtfish_projectile = pygame.sprite.spritecollide(helmetfish, classes.Projectile.List, True)
        if len(helemtfish_projectile) > 0:
            for hit in helemtfish_projectile:
                helmetfish.health -= helmetfish.half_health


