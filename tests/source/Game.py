import pygame
from src.Doodler import Doodler
from src.Score import Score
from configs import config
from src.Background import Background
from src.StorageManager import StorageManager


class Game:
    def __init__(self):
        self.font = pygame.font.Font(None, 48)
        self.__running = True


    def draw_game_over(self, surface, score):
        lose_text_color = (255, 0, 0)
        score_text_color = (0, 255, 0)
        restart_text_color = (0, 0, 255)

        text1 = self.font.render("Вы проиграли!", True, lose_text_color)
        text_rectangle1 = text1.get_rect(center=(config.WIDTH / 2, config.HEIGHT / 2 - 20))
        surface.blit(text1, text_rectangle1)

        score_text = self.font.render(f"Счёт: {score.get_score()}", True, score_text_color)
        score_rect = score_text.get_rect(center=(config.WIDTH / 2, config.HEIGHT / 2 + 20))
        surface.blit(score_text, score_rect)

        restart_text = self.font.render("Нажмите R для рестарта", True, restart_text_color)
        restart_rect = restart_text.get_rect(center=(config.WIDTH / 2, config.HEIGHT / 2 + 60))
        surface.blit(restart_text, restart_rect)

    def is_running(self):
        if not isinstance(self.__running, bool): raise TypeError
        return self.__running

    def set_running(self, value):
        self.__running = value

    def end_game(self, score):
        if not isinstance(score, int): raise TypeError
        self.__running = False
        self.__storage_manager = StorageManager(config.records)
        self.__storage_manager.write(score)  #пометка исправить на это StorageManager(config.records).write(score)
        return score

    def restart_game(self):
        self.__score = Score()
        Doodler(self.__score, 100, 100)
        Background()
        self.__running = True

