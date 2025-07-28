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
        self.subscriptions = {}
        self.events = []
        self.key_states = {}


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

    def sub(self, key_code, callback):
        self.subscriptions[key_code] = callback

    def add_event(self, event):
        self.events.append(event)

    def update(self):
        for event in self.events:
            event_type = event.get('type')

            if event_type == 'QUIT':
                self.quit_game()
            elif event_type == 'KEYDOWN':
                key_code = event.get('key')
                self.key_states[key_code] = True
                if key_code in self.subscriptions:
                    self.subscriptions[key_code]()
            elif event_type == 'KEYUP':
                key_code = event.get('key')
                self.key_states[key_code] = False

        self.events.clear()

    def quit_game(self):
        self.__game.end_game(self.__score.get_score())