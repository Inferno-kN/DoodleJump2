import pygame
from configs import settings

class GameOver:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def draw(self, surface, score):
        


        text1 = self.font.render("Вы проиграли!", True, lose_text_color)
        text_rectangle1 = text1.get_rect(center=(settings.WIDTH / 2, settings.HEIGHT / 2 - 20))
        surface.blit(text1, text_rectangle1)

        score_text = self.font.render(f"Счёт: {score}", True, score_text_color)
        score_rect = score_text.get_rect(center=(settings.WIDTH / 2, settings.HEIGHT / 2 + 20))
        surface.blit(score_text, score_rect)

        restart_text = self.font.render("Нажмите R для рестарта", True, restart_text_color)
        restart_rect = restart_text.get_rect(center=(settings.WIDTH / 2, settings.HEIGHT / 2 + 60))
        surface.blit(restart_text, restart_rect)