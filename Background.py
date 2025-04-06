import pygame
import settings

class Background:
    def __init__(self):
        self.image = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        self.image.fill((100, 149, 237))
