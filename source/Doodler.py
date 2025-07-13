import pygame
from configs.config import *
from source.Score import Score
from source.BrokenPlatform import BrokenPlatform


class Doodler:
    def __init__(self, score: Score, x, y):
        self.__score_update = score
        self.__x = x
        self.__y = y
        self.__x_speed = 0
        self.__y_speed = 0
        self.__visited_platform = []
        self.__width = DOODLER_WIDTH
        self.__height = DOODLER_HEIGHT
        self.__gravity = DOODLER_GRAVITY
        self.__jump_power = DOODLER_JUMP_POWER
        self.__image = pygame.image.load(doodler).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (self.__width, self.__height))
        self.__doodler_rect = pygame.Rect(self.__x, self.__y, self.__width, self.__height)


    def get_rect(self):
        return self.__doodler_rect

    def update_motion(self, keys, platforms):
        self.__x_speed = 0

        if keys[pygame.K_LEFT]:
            self.__x_speed = -5
        elif keys[pygame.K_RIGHT]:
            self.__x_speed = 5

        self.__x += self.__x_speed
        self.limit_by_screen()

        self.__y_speed += self.__gravity
        self.__y += self.__y_speed

        self.__doodler_rect.x = self.__x
        self.__doodler_rect.y = self.__y

        self.check_collision(platforms)

    def limit_by_screen(self):
        if self.__x + self.__width < 0:
            self.__x = WIDTH
        elif self.__x > WIDTH:
            self.__x = 0

    def draw(self, screen):
        screen.blit(self.__image, (self.__x, self.__y))

    def jump(self):
        self.set_y_speed(-self.__jump_power)

    def get_position(self):
        return self.__x, self.__y

    def get_size(self):
        return self.__width, self.__height

    def get_bottom(self):
        return self.__y + self.__height

    def get_top(self):
        return self.__y - self.__height

    def get_y_speed(self):
        return self.__y_speed

    def get_doodle_rect(self): # САМОДЕЛЬНЫЙ МЕТОД ДЛЯ ПРОКРУТКИ ЭКРАНА
        return self.__doodler_rect

    def set_position(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        if not isinstance(x, (int, float)): raise TypeError
        self.__x = x

    def set_y(self, y):
        if not isinstance(y, (int, float)): raise TypeError
        self.__y = y

    def set_y_speed(self, value):
        if not isinstance(value, (int, float)): raise TypeError
        self.__y_speed = value

    def validate_platforms(self, platforms):
        if not isinstance(platforms, list):
            raise TypeError

    def update_doodler_rect(self):
        self.__doodler_rect.x = self.__x
        self.__doodler_rect.y = self.__y

    def check_collision_with_platform(self, platform):
        rect = pygame.Rect(platform.get_position()[0], platform.get_position()[1], platform.get_size()[0], platform.get_size()[1])
        if self.__doodler_rect.colliderect(rect) and self.__y_speed > 0:
            if self.__y + self.__height - self.__y_speed <= rect.y:
                self.__y = rect.y - self.__height
                self.set_y_speed(self.__jump_power)
                self.__doodler_rect.y = self.__y

                if platform not in self.__visited_platform:
                    self.__score_update.update()
                    self.__visited_platform.append(platform)

            if isinstance(platform, BrokenPlatform):
                return True
        return False

    def process_platforms(self, platforms):
        broken_platforms = []
        for platform in platforms[:]:
            if self.check_collision_with_platform(platform):
                platforms.remove(platform)
                broken_platforms.append(platform)
        return broken_platforms

    def check_collision(self, platforms):
        self.validate_platforms(platforms)
        self.update_doodler_rect()
        return self.process_platforms(platforms)