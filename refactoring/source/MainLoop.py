import pygame
from refactoring.cfg.config import *
from refactoring.source.Score import Score
from refactoring.source.Game import Game
from refactoring.source.Field import Field
from refactoring.source.Background import Background
from refactoring.source.StorageManager import StorageManager

class MainLoop:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Little Alien")
        self.__clock = pygame.time.Clock()
        self.__score = Score()
        self.__background = Background()
        self.__game = Game()
        self.__field = Field(self.__score)
        self.__doodler = self.__field.get_doodler()
        self.__platforms = self.__field.get_platforms()
        self.__game_score = 0

    def run(self):
        while self.__game.get_is_running():
            self.__clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
            #self.check_is_running()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game.game_over()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart()
            elif event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                self.__doodler.update_motion(keys, self.__platforms)


    def update(self):
        keys = pygame.key.get_pressed()
        self.__doodler.update_motion(keys, self.__platforms)
        self.__field.update()
        self.__field.scroll_screen()


    def draw(self):
        self.__field.draw(self.__screen)
        self.__doodler.draw(self.__screen)
        self.__score.draw(self.__screen)

        self.check_is_running()

        pygame.display.flip()


    def check_is_running(self):
        if self.__doodler.get_position()[1] > HEIGHT:
            #self.__game.game_over()
            self.__game.draw(self.__screen, self.__score)

    def restart(self):
        self.__game.restart_game()
        self.__score = Score()
        self.__background = Background()
        self.__field = Field(self.__score)
        self.__doodler = self.__field.get_doodler()
        self.__platforms = self.__field.get_platforms()
        self.__game_score = 0

        self.run()






