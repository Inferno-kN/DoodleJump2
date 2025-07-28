import pygame
from configs.config import *
from src.Score import Score
from src.Game import Game
from src.Field import Field
from src.InputSystem import InputSystem


class MainLoop:

    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Little Alien")
        self.__clock = pygame.time.Clock()
        self.__score = Score()
        self.__game = Game()
        self.__is_game_over_show = False
        self.__field = Field(self.__score)
        self.__doodler = self.__field.get_doodler()
        self.__platforms = self.__field.get_platforms()
        self.__game_score = 0
        self.__input_system = InputSystem(self.__game, self.__score, self.__field, self)


    def run(self):
        while True:
            self.process_handle_events()

            if self.__game.is_running():
                if self.__is_game_over_show:
                    self.__is_game_over_show = False
                self.__clock.tick(FPS)
                self.update()
                self.draw_objects()

            if not self.__game.is_running() and self.__is_game_over_show is False:
                self.__is_game_over_show = True
                self.process_handle_events()
                self.__game.draw_game_over(self.__screen, self.__score)
                pygame.display.flip()


    def process_handle_events(self):
        self.__input_system.get_handle_events()


    def update(self):
        keys = pygame.key.get_pressed()
        self.__doodler.update_motion(keys, self.__platforms)
        broken_platforms = self.__doodler.check_collision(self.__platforms)

        for broken in broken_platforms:
            self.__field.regenerate_broken_platforms(broken)

        self.__field.update()
        self.__field.scroll_screen()


    def draw_objects(self):
        self.__field.draw_background_on_field(self.__screen)
        self.__doodler.draw_doodler(self.__screen)
        self.__score.draw_score(self.__screen)
        self.check_is_running()
        pygame.display.flip()


    def check_is_running(self):
        if self.__doodler.get_position()[1] > HEIGHT:
            self.__game.end_game(self.__score.get_score())


    def restart(self):
        self.__game.restart_game()
        self.__score.reset()
        self.__field = Field(self.__score)
        self.__doodler = self.__field.get_doodler()
        self.__platforms = self.__field.get_platforms()
        self.__input_system = InputSystem(self.__game, self.__score, self.__field, self)