import pygame
import math
import classes
from random import randint


class BaseClass(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.all_sprites.add(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

class Narwhal(BaseClass):
    Narwhals = pygame.sprite.Group()
    going_right = True

    def __init__(self, x, y, width, height, image_string, velocity):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Narwhal.Narwhals.add(self)
        self.velx = 0
        self.vely = 0

    def motion(self, SCREENWIDTH):
        predicted_location = self.rect.x + self.velx
        if predicted_location < 0:
            self.velx = 0
        elif predicted_location + self.width > SCREENWIDTH:
            self.velx = 0
        self.rect.x += self.velx
        self.rect.y += self.vely

class HelmetFish(BaseClass):
    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        HelmetFish.List.add(self)
        self.velx = randint(1, 4)
        self.amplitude, self.period = randint(20, 320), randint(4, 6) / 100.0

    def swim(self, SCREENWIDTH):
        if self.rect.x + self.width > SCREENWIDTH or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velx = -self.velx
        self.rect.x += self.velx
        self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) + 340

    @staticmethod
    def movement(SCREENWIDTH):
        for fish in HelmetFish.List:
            fish.swim(SCREENWIDTH)

class Projectile(BaseClass):
    List = pygame.sprite.Group()
    def __init__(self, x, y, height, width, image_string):
        BaseClass.__init__(self, x , y, height, width, image_string)
        Projectile.List.add(self)
        self.velx = None

    @staticmethod
    def movement():
        for projectile in Projectile.List:
            projectile.rect.x += projectile.velx
