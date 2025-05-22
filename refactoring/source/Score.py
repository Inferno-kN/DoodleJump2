import pygame
from refactoring.cfg.config import BLACK

class Score:
    def __init__(self):
        self.__score = 0
        self.__font = pygame.font.Font(None, 36)

    def update(self):
        self.__score += 30


    def draw(self, surface):
        text = self.__font.render(f"Счёт: {self.__score}", True, BLACK)
        surface.blit(text, (10, 10))

    def get_score(self):
        return self.__score