import pygame
from settings import *

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self):
        self.score += 50

