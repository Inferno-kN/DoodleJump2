"""
Скрипт сборки проекта DoodleJump2 с учетом PyInstaller и динамических путей к ресурсам.
Использует конфигурацию, где ресурсы находятся в папке refactoring/resources и файл records.json.
"""
import os
import sys
from PyInstaller.__main__ import run

# Настройки приложения
APP_NAME = "DoodleJump2"
ENTRY_POINT = "app.py"
ONEFILE = True
WINDOWED = False

# Папки и файлы ресурсов
# Включаем всю папку refactoring/resources и файл records.json
RESOURCE_DIRS = ["refactoring/resources"]
RESOURCE_FILES = ["records.json"]

# Формируем аргументы для PyInstaller
opts = [ENTRY_POINT, "--name", APP_NAME]
if ONEFILE:
    opts.append("--onefile")
if WINDOWED:
    opts.append("--windowed")

# Функция для формирования строки add-data
def make_add_data(path):
    sep = ';' if sys.platform.startswith('win') else ':'
    # dst — «rsrs», а не полный src/…
    dst = os.path.basename(path) if os.path.isfile(path) else os.path.basename(path)
    # но лучше явно:
    # dst = "rsrs"  для каталогов, и "rsrs/records.json" для файла
    return f"{path}{sep}resources"


# Добавляем каталоги
for d in RESOURCE_DIRS:
    if os.path.isdir(d):
        opts += ["--add-data", f"{d}{';' if sys.platform.startswith('win') else ':'}resources"]
    else:
        print(f"[ERROR] Директория ресурса не найдена: {d}", file=sys.stderr)
        sys.exit(1)

# Добавляем файлы
for f in RESOURCE_FILES:
    if os.path.isfile(f):
        opts += ["--add-data", make_add_data(f)]
    else:
        print(f"[ERROR] Файл ресурса не найден: {f}", file=sys.stderr)
        sys.exit(1)

# Чистим старые сборки
# Удаляем директории build и dist, а также spec-файл
import shutil
for path in ["build", "dist", f"{APP_NAME}.spec"]:
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

# Выводим итоговые опции для отладки
print("Запуск PyInstaller с опциями:", opts)

# Запускаем сборку
run(opts)
