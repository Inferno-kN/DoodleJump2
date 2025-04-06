import pygame
import settings


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/images/platform.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.PLATFORM_WIDTH, settings.PLATFORM_HEIGHT))
        self.rectangle = self.image.get_rect()
        self.rectangle.x = x
        self.rectangle.y = y


    def draw(self, surface):
        surface.blit(self.image, self.rectangle)