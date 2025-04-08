import random

from src.platform import Platform
from configs.settings import  *

def generate_simple_platform(platform_count: int) -> list[Platform]:
    current_x = WIDTH / 2 - PLATFORM_WIDTH / 2
    current_y = HEIGHT - PLATFORM_HEIGHT

    platforms = [Platform(current_x, current_y)]
    for i in range(platform_count - 1):
        salt = random.randint(-200, 200)

        if i % 2 == 0:
            current_x += 100 + salt
        else:
            current_x -= 100 + salt

        current_y -= 40
        platforms.append(Platform(current_x, current_y))

    return platforms
