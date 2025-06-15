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
        self.screen = screen # экран инициализируется здесь
        self.clock = clock # clock инициализируется здесь - управляет частотой кадров
        self.player = Player()
        self.platforms = generate_simple_platform(20)
        self.game_over = GameOver()
        self.background = Background()
        self.score = Score()
        self.is_game_starting = True # игра запускается
        self.game_running = True # игра активно идет (игрок играет до тех пор, пока не упал вне игровую зону)

        with open("records.json") as file:
            self.records = json.load(file)


    def run(self): #игровой цикл
        while self.is_game_starting:
            self.clock.tick(FPS)  # ограничение до FPS
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self): # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_starting = False #выход из игры
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not self.game_running: #рестарт игры
                    self.restart_game()

    def update(self):
        if self.game_running: #если игра запущена то
            self.player.update(self.platforms) #обнова состояния игрока
            self.background.update()#а тут обнова фона нашего


        if self.player.rectangle.top <= HEIGHT / 3: # добавляем прокрутку экрана
            scroll_amount = abs(self.player.velocity.y) #величина игрока, и скорость перса нашего всегда положительная
            self.player.position.y += scroll_amount # идет прокрутка экрана вверх - значит позиция игрока обновляется
            self.player.rectangle.y = self.player.position.y

            for platform in self.platforms:  # проверка на приземление на платформу
                platform.rectangle.y += scroll_amount #обновляется положение платформы если прокрутка идёт вверх
                if platform.rectangle.top > HEIGHT:
                    self.platforms.remove(platform)
                    self.platforms.append(Platform(random.randint(0, WIDTH - PLATFORM_WIDTH), random.randint(-100, -20)))
                    self.score.update()  # идёт увеличение счёта

        if self.game_running and self.player.rectangle.top > HEIGHT: # если игрок падает вне игровую зону
            self.game_running = False # то игровой процесс завершается
            self.records["records"].append(self.score.score)

            with open("records.json", "w") as file:
                json.dump(self.records, file)


    def draw(self):
        self.background.draw(self.screen)#рисовка фона

        if self.game_running: #если игра запустилась
            self.player.draw(self.screen)#рисовка ПИ
            for platform in self.platforms:
                platform.draw(self.screen)#рисовка платформ
            self.score.draw(self.screen, self.player.rectangle.bottom)#рисовка счёта
        else:
            self.game_over.draw(self.screen, self.score.score) #рисовка окончания ира с полученным счётом

        pygame.display.flip()


    def restart_game(self): # сбрасываем игру
        self.player = Player()
        self.platforms = generate_simple_platform(20)
        self.background = Background()
        self.score = Score()
        self.game_running = True #выше создавали экземпляры обьектов и игра при рестарте запускается