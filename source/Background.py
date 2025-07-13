import pygame
from configs.config import WIDTH, HEIGHT, background


class Background:
    def __init__(self):
        self.__image = pygame.image.load(background).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (WIDTH, HEIGHT))
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (0, 0)
        self.__speed = 1
        if not isinstance(self.__speed, int): raise TypeError

    def draw_background(self, screen):
        screen.blit(self.__image, self.__rect)

    def update(self):
        pass