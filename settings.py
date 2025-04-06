import pygame
import random

WIDTH, HEIGHT = 800, 600
FPS = 90
GRAVITY = 1
JUMP_HEIGHT = -20
PLATFORM_WIDTH = 70
PLATFORM_HEIGHT = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()