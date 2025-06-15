import pygame
from configs import settings
from configs.settings import PLATFORM_WIDTH, PLATFORM_HEIGHT
from src.score import Score


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/images/doodle.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (settings.WIDTH / 2, settings.HEIGHT / 2)
        self.position = pygame.math.Vector2(self.rectangle.center)
        self.velocity = pygame.math.Vector2(0, settings.JUMP_HEIGHT) # Задаем начальную скорость вверх
        self.acceleration = pygame.math.Vector2(0, 0)
        self.score = Score()


    def update(self, platforms):
        self.acceleration = pygame.math.Vector2(0, settings.GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -0.8
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = 0.8

        self.friction()
        self.physics()
        self.limitation_screen()
        self.check_user(platforms)



    def friction(self):
        self.acceleration.x += self.velocity.x * -0.12

    def physics(self):
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        self.rectangle.center = (self.position.x, self.position.y)

    def limitation_screen(self):
        if self.position.x < 0:
            self.position.x = settings.WIDTH
        if self.position.x > settings.WIDTH:
            self.position.x = 0
        self.rectangle.center = (self.position.x, self.position.y)

    def check_user(self, platforms):
        if self.velocity.y > 0:  # Движение игрока вниз
            for platform in platforms:
                if self.rectangle.colliderect(platform.rectangle):
                    self.velocity.y = settings.JUMP_HEIGHT  # Отскок вверх
                    break


    def update_score(self):
        self.score.update()

    def draw(self, surface):
        surface.blit(self.image, self.rectangle)



