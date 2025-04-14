import random
import json
import pygame
from src.game_over import GameOver
from src.platform import Platform
from src.player import Player
from configs.settings import WIDTH, HEIGHT, FPS, PLATFORM_WIDTH, clock, PLATFORM_HEIGHT, screen
from src.background import Background
from src.score import Score
from configs.platforms import generate_simple_platform

class MainLoop:
    def __init__(self):
        self.screen = screen # Экран инициализируется здесь
        self.clock = clock # Clock инициализируется здесь
        self.player = Player()
        self.platforms = generate_simple_platform(20)
        self.game_over = GameOver()
        self.background = Background()
        self.score = Score()
        self.is_game_starting = True
        self.game_running = True

        with open("records.json") as file:
            self.records = json.load(file)


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

            #for platform in self.platforms:
            #    if player.is_on_platform(platform):
            #        ...

            for platform in self.platforms:  # проверка на приземление на платформу
                platform.rectangle.y += scroll_amount
                if platform.rectangle.top > HEIGHT:
                    self.platforms.remove(platform)
                    self.platforms.append(Platform(random.randint(0, WIDTH - PLATFORM_WIDTH), random.randint(-100, -20)))
                    self.score.update()  # идёт увеличение счёта

        if self.game_running and self.player.rectangle.top > HEIGHT:
            self.game_running = False
            self.records["records"].append(self.score.score)

            with open("records.json", "w") as file:
                json.dump(self.records, file)


    def draw(self):
        self.background.draw(self.screen)

        if self.game_running:
            self.player.draw(self.screen)
            for platform in self.platforms:
                platform.draw(self.screen)
            self.score.draw(self.screen, self.player.rectangle.bottom)
        else:
            self.game_over.draw(self.screen, self.score.score)

        pygame.display.flip()


    def restart_game(self): # сбрасываем игру
        self.player = Player()
        self.platforms = generate_simple_platform(20)
        self.background = Background()
        self.score = Score()
        self.game_running = True