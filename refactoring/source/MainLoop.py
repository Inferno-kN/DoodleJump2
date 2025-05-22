import pygame
from refactoring.cfg.config import *
from refactoring.source.Score import Score
from refactoring.source.Game import Game
from refactoring.source.Field import Field

class MainLoop:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Little Alien")
        self.__clock = pygame.time.Clock()
        self.__score = Score()
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
            pygame.display.flip()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game.set_over(False)
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                self.__doodler.update_motion(keys, self.__platforms)
            elif event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                self.__doodler.update_motion(keys, self.__platforms)


    def draw(self):
        self.__field.draw(self.__screen)
        self.__doodler.draw(self.__screen)
        self.__score.draw(self.__screen)

    def update(self):
        keys = pygame.key.get_pressed()
        self.__doodler.update_motion(keys, self.__platforms)
        self.__field.update()
        self.__field.scroll_screen()



