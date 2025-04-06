import pygame
import settings
from Score import Score


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/images/doodle.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (settings.WIDTH / 2, settings.HEIGHT / 2)
        