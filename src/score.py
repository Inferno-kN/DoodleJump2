import pygame
from configs.settings import *

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self):
        self.score += 50

    def draw(self, surface, player_bottom):
        text = self.font.render(f"Текущий счёт: {self.score}", True, BLACK)
        surface.blit(text, (10, 10))