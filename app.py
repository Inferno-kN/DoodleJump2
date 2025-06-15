import pygame
from refactoring.source.MainLoop import MainLoop
#from src.main_loop import MainLoop # это для Разработки приложений в унике
if __name__ == "__main__":
    pygame.init()
    game = MainLoop()
    game.run()
    #pygame.quit()