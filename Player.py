import pygame
import settings
from Score import Score


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/images/doodle.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (settings.WIDTH / 2, settings.HEIGHT / 2)
        self.position = pygame.math.Vector2(self.rectangle.center)
        self.velocity = pygame.math.Vector2(0, 0)
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

        # Трение (рефакторинг)

    def friction(self):
        self.acceleration.x += self.velocity.x * -0.12

    def physics(self):
        # Физика (рефакторинг)
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

    def limitation_screen(self):
        # Ограничение по экрану
        if self.position.x < 0:
            self.position.x = settings.WIDTH
        if self.position.x > settings.WIDTH:
            self.position.x = settings.WIDTH

        self.rectangle.center = round(self.position.x), round(self.position.y)

    