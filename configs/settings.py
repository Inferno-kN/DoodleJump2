import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_HEIGHT = -15
PLATFORM_WIDTH = 70
PLATFORM_HEIGHT = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()