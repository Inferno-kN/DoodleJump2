import random

import pygame

from GameOver import GameOver
from Platform import Platform
from Player import Player
from settings import WIDTH, HEIGHT, FPS, PLATFORM_WIDTH, clock, PLATFORM_HEIGHT, screen
from Background import Background
from Score import Score

class MainLoop:
    def __init__(self):
        self.screen = screen # Экран инициализируется здесь
        self.clock = clock # Clock инициализируется здесь
        self.player = Player()
        self.platforms = [Platform(WIDTH / 2 - PLATFORM_WIDTH / 2, 100)]
        self.platforms.extend([Platform(random.randint(0, WIDTH - PLATFORM_WIDTH), random.randint(50, 400)) for _ in range(8)])
        self.game_over = GameOver()
        self.background = Background()
        self.score = Score()
        self.is_game_starting = True
        self.game_running = True


