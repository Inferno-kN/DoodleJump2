import random
from src.platform import Platform
from configs.settings import *

def generate_simple_platform(platform_count: int) -> list[Platform]:
    current_x = WIDTH / 2 - PLATFORM_WIDTH / 2
    current_y = HEIGHT - PLATFORM_HEIGHT

    platforms = [Platform(current_x, current_y)]
    for i in range(platform_count - 1):
        salt = random.randint(-200, 200)

        # Чередование смещения вправо и влево
        if i % 2 == 0:
            new_x = current_x + 100 + salt  # Смещение вправо
        else:
            new_x = current_x - 100 - salt  # Смещение влево

        

        current_y -= 40

        if current_y < 0:
            break

        platforms.append(Platform(new_x, current_y))
        current_x = new_x

    return platforms
