import pygame
import sys


class InputSystem:

    def __init__(self, game, score, field, mainloop):
        self.__game = game
        self.__score = score
        self.__field = field
        self.__mainloop = mainloop
        self.__doodler = self.__field.get_doodler()
        self.__platforms = self.__field.get_platforms()


    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.__game.end_game(self.__score.get_score())
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r and self.__game.is_running() is False:
                    self.__mainloop.restart()

            elif event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                self.__doodler.update_motion(keys, self.__platforms)

    def get_handle_events(self):
        return self.handle_events()
