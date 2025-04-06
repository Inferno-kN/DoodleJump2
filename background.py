import pygame
import settings

class Background:
    def __init__(self):
        self.image = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        self.image.fill((100, 149, 237))
        self.rectangle = self.image.get_rect()
        self.rectangle.topleft = (0, 0)
        self.speed = 1

    def update(self):
       pass

    def draw(self, surface):
        surface.blit(self.image, self.rectangle)