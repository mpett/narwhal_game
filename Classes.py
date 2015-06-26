import pygame

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
    def __init__(self, x, y, width, height, image_string, velocity):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Narwhal.Narwhals.add(self)
        self.velx = 2
    def motion(self):
        self.rect.x += self.velx


