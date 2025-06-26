import pygame
from refactoring.cfg.config import *

class AbstractPlatform:
    def __init__(self, x, y, image_path=None):
        self.__rectangle = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.__type = 'normal'
        self.__image = pygame.image.load(image_path).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (PLATFORM_WIDTH, PLATFORM_HEIGHT))

    def update(self, scroll_amount):
        self.__rectangle.y += scroll_amount

    def get_top(self):
        return self.__rectangle.top

    def draw(self, screen):
        screen.blit(self.__image, self.__rectangle)

    def get_position(self):
        return self.__rectangle.x, self.__rectangle.y

    def get_size(self):
        return self.__rectangle.size

    def get_type(self):
        return self.__type