import pygame
from configs import settings

class Background:
    def __init__(self):
        self.image = pygame.image.load('resources/fonts/background.png')
        self.image = pygame.transform.scale(self.image, (settings.WIDTH, settings.HEIGHT))
        self.rectangle = self.image.get_rect()
        self.rectangle.topleft = (0, 0)
        self.speed = 1

    def update(self):
       pass

    def draw(self, surface):
        surface.blit(self.image, self.rectangle)