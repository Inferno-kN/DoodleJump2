import pygame
from main_loop import MainLoop

if __name__ == "__main__":
    pygame.init()
    game = MainLoop()
    game.run()
    pygame.quit()