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

        score_text = self.font.render(f"Счёт: {score}", True, settings.WHITE)
        score_rect = score_text.get_rect(center=(settings.WIDTH / 2, settings.HEIGHT / 2 + 20))
        surface.blit(score_text, score_rect)

        restart_text = self.font.render("Нажмите R для рестарта", True, settings.WHITE)
        restart_rect = restart_text.get_rect(center=(settings.WIDTH / 2, settings.HEIGHT / 2 + 60))
        surface.blit(restart_text, restart_rect)