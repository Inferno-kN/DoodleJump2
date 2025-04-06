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


    def run(self):
        while self.is_game_starting:
            self.clock.tick(FPS)  # Используем self.clock
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_starting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not self.game_running:
                    self.restart_game()

    def update(self):
        if self.game_running:
            self.player.update(self.platforms)
            self.background.update()


        if self.player.rectangle.top <= HEIGHT / 3: # добавляем прокрутку экрана
            scroll_amount = abs(self.player.velocity.y)
            self.player.position.y += scroll_amount
            self.player.rectangle.y = self.player.position.y

            for platform in self.platforms:  # проверка на приземление на платформу
                platform.rectangle.y += scroll_amount
                