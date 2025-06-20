import pygame
from refactoring.source.Doodler import Doodler
from refactoring.source.Score import Score
from refactoring.cfg import config
from refactoring.source.Background import Background
from refactoring.source.StorageManager import StorageManager


class Game:
    def __init__(self):
        self.font = pygame.font.Font(None, 48)
        self.__running = True
        self.__score = Score()
        self.__background = Background()
        self.__doodler = Doodler(self.__score, 100, 100)
        self.__storage_manager = StorageManager()  # Создаем экземпляр StorageManager

    def draw(self, surface, score):
        lose_text_color = (255, 0, 0)  # красный
        score_text_color = (0, 255, 0)  # зеленый
        restart_text_color = (0, 0, 255)  # синий

        text1 = self.font.render("Вы проиграли!", True, lose_text_color)
        text_rectangle1 = text1.get_rect(center=(config.WIDTH / 2, config.HEIGHT / 2 - 20))
        surface.blit(text1, text_rectangle1)

        score_text = self.font.render(f"Счёт: {score.get_score()}", True, score_text_color)
        score_rect = score_text.get_rect(center=(config.WIDTH / 2, config.HEIGHT / 2 + 20))
        surface.blit(score_text, score_rect)

        restart_text = self.font.render("Нажмите R для рестарта", True, restart_text_color)
        restart_rect = restart_text.get_rect(center=(config.WIDTH / 2, config.HEIGHT / 2 + 60))
        surface.blit(restart_text, restart_rect)

    def get_is_running(self):
        return self.__running

    def game_over(self, score):
        self.__running = False
        #score = self.__score.get_score()  # получаем счёт
        self.__storage_manager.write(score)  # сохраняем счёт

    def restart_game(self):
        self.__score = Score()
        self.__doodler = Doodler(self.__score, 100, 100)
        self.__background = Background()
        self.__running = True

