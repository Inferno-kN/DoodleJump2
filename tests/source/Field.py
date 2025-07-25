import random
from configs.config import *
from src.AbstractPlatform import AbstractPlatform
from src.BrokenPlatform import BrokenPlatform
from src.SimplePlatform import SimplePlatform
from src.Background import Background
from src.Doodler import Doodler
from src.Score import Score

class Field:

    __broken_platform_count = 2
    __simple_platform_count = 18

    def __init__(self, score: Score):
        self.__score = score
        self.__width = WIDTH
        self.__height = HEIGHT
        self.__count_platforms = 0
        self.__background = Background()
        self.__doodler = Doodler(score,100, 100)
        self.__platforms = self.generate_platforms(self.__simple_platform_count)


    def generate_platforms(self, platform_count: int) -> list[AbstractPlatform]:
        if not isinstance(platform_count, int): raise TypeError
        current_x = WIDTH / 2 - PLATFORM_WIDTH / 2
        current_y = HEIGHT - PLATFORM_HEIGHT

        platforms = [SimplePlatform(current_x, current_y)]

        for i in range(self.__broken_platform_count):
            salt = random.randint(-200, 200)
            new_x = current_x + salt

            if new_x < 0:
                new_x = 0
            elif new_x + PLATFORM_WIDTH > WIDTH:
                new_x = WIDTH - PLATFORM_WIDTH

            current_y -= 40
            if current_y < 0:
                break

            new_platform = BrokenPlatform(new_x, current_y)
            platforms.append(new_platform)
            current_x = new_x

        for i in range(platform_count - 1):
            salt = random.randint(-200, 200)
            new_x = current_x + salt

            if new_x < 0:
                new_x = 0
            elif new_x + PLATFORM_WIDTH > WIDTH:
                new_x = WIDTH - PLATFORM_WIDTH

            current_y -= 40
            if current_y < 0:
                break

            new_platform = SimplePlatform(new_x, current_y)
            platforms.append(new_platform)
            current_x = new_x

        return platforms


    def draw_background_on_field(self, screen):
        self.__background.draw_background(screen)
        for platform in self.__platforms:
            platform.draw(screen)

    def get_platforms(self):
        return self.__platforms

    def get_background(self):
        return self.__background

    def get_doodler(self):
        return self.__doodler

    def update(self): pass

    def reset_platforms(self):
        for platform in self.__platforms[:]:
            if platform.get_top() > HEIGHT:
                self.__platforms.remove(platform)
                new_x = random.randint(0, WIDTH - PLATFORM_WIDTH)
                new_y = random.randint(-100, -20)
                if isinstance(platform, BrokenPlatform):
                    self.__platforms.append(BrokenPlatform(new_x, new_y))
                else:
                    self.__platforms.append(SimplePlatform(new_x, new_y))

    def should_scroll(self):
        return self.__doodler.get_doodle_rect().top <= HEIGHT / 3

    def update_platforms_positions(self, scroll_amount):
        for platform in self.__platforms:
            platform.update(scroll_amount)

    def balance_platforms(self):
        diff = (self.__simple_platform_count + self.__broken_platform_count) - len(self.__platforms)
        if not isinstance(diff, int):
            raise TypeError
        for _ in range(diff):
            new_x = random.randint(0, WIDTH - PLATFORM_WIDTH)
            new_y = random.randint(-100, -20)
            self.__platforms.append(BrokenPlatform(new_x, new_y))

    def update_doodler_position(self, scroll_amount):
        self.__doodler.get_doodle_rect().y += scroll_amount
        self.__doodler.set_y(self.__doodler.get_doodle_rect().y)

    def scroll_screen(self):
        if self.should_scroll():
            scroll_amount = abs(self.__doodler.get_y_speed())

            self.update_platforms_positions(scroll_amount)
            self.reset_platforms()
            self.balance_platforms()
            self.update_doodler_position(scroll_amount)


    def regenerate_broken_platforms(self, platform):
        self.__platforms.remove(platform)
        new_x = random.randint(0, WIDTH - PLATFORM_WIDTH)
        new_y = random.randint(-100, -20)
        self.__platforms.append(BrokenPlatform(new_x, new_y))











