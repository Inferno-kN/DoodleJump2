import pygame
from refactoring.cfg.config import *
from refactoring.source.Doodler import Doodler


class Game:
    def __init__(self):
        self.font = pygame.font.Font(None, 48)
        self.__running = True

    def draw(self, screen):
        text = self.font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    def get_is_running(self):
        return self.__running

    def set_over(self, value) -> bool:
        self.__running = value




