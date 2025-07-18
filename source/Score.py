import pygame
from configs.config import BLACK

class Score:
    def __init__(self):
        self.__score = 0
        self.__font = pygame.font.Font(None, 36)

    def update(self):
        if not isinstance(self.__score, int): raise TypeError
        self.__score += 30

    def draw_score(self, surface):
        text = self.__font.render(f"Счёт: {self.__score}", True, BLACK)
        surface.blit(text, (10, 10))

    def get_score(self):
        if not isinstance(self.__score, int): raise TypeError
        return self.__score

    def reset(self):
        self.__score = 0