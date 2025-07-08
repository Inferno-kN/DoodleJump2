import os
import sys

# Параметры окна и цвета
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Физика персонажа
DOODLER_WIDTH = 30
DOODLER_HEIGHT = 40
DOODLER_JUMP_POWER = -15
DOODLER_GRAVITY = 0.5

# Параметры платформ
PLATFORM_WIDTH = 70
PLATFORM_HEIGHT = 15

def resource_path(*parts: str) -> str:
    """
    Возвращает абсолютный путь к ресурсу.
     - В «замороженном» exe: берём из sys._MEIPASS.
     - В режиме разработки: из папки src/refactoring.
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base = sys._MEIPASS
    else:
        # cfg.py лежит в src/refactoring/cfg,
        # поэтому поднимаемся на один уровень — в src/refactoring
        base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.normpath(os.path.join(base, *parts))

# Теперь ресурсы лежат в src/refactoring/rsrs
doodler         = resource_path('rsrcs', 'imgs', 'doodle.png')
simple_platform = resource_path('rsrcs', 'imgs', 'platform.png')
broken_platform = resource_path('rsrcs', 'imgs', 'broken_platform.png')
background      = resource_path('rsrcs', 'fnts', 'background.png')
records         = resource_path('records.json')

# ---- DEBUG ---
print("Doodler path:", doodler, file=sys.stderr)
print("Platform path:", simple_platform, file=sys.stderr)
print("Background path:", background, file=sys.stderr)
print("Records path:", records, file=sys.stderr)
