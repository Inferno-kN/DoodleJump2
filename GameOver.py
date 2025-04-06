import pygame
import settings

class GameOver:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def draw(self, surface, score):
        text1 = self.font.render("Вы проиграли!", True, settings.WHITE)
        text_rectangle1 = text1.get_rect(center=(settings.WIDTH / 2, settings.HEIGHT / 2 - 20))
        surface.blit(text1, text_rectangle1)

