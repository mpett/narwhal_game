import pygame

class BaseClass(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.all_sprites.add(self)
        self.image = pygame.image.load(image_string)
        self.rect = pygame.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
