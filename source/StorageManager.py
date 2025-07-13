import json
import os
import shutil
import sys

def _get_user_data_dir(app_name: str) -> str:
    """
    Возвращает кроссплатформенную папку для данных приложения.
    Windows: %APPDATA%/app_name
    *nix: ~/.local/share/app_name
    """
    if sys.platform.startswith("win"):
        base = os.environ.get("APPDATA", os.path.expanduser("~"))
    else:
        base = os.path.expanduser("~/.local/share")
    path = os.path.join(base, app_name)
    os.makedirs(path, exist_ok=True)
    return path

class StorageManager:
    def __init__(self, records: str, app_name: str = "DoodleJump2"):
        if not isinstance(records, str):
            raise TypeError
        # Исходный шаблон
        template = records
        # Папка для пользовательских данных
        user_dir = _get_user_data_dir(app_name)
        # Именем файла пользуемся тем же, что и шаблон
        user_records = os.path.join(user_dir, os.path.basename(template))
        # При первом запуске копируем шаблон (если есть) или создаём пустой файл
        if not os.path.exists(user_records):
            if os.path.isfile(template):
                shutil.copyfile(template, user_records)
            else:
                open(user_records, "w").close()
        # Работаем уже с файлом в user_dir
        self.__records = user_records

    def read(self) -> list[int]:
        if not os.path.exists(self.__records):
            return []
        if os.path.getsize(self.__records) == 0:
            return []
        with open(self.__records, "r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, value):
        if not isinstance(value, (str, int)):
            raise TypeError
        record = self.read()
        if value not in record:
            record.append(value)
            with open(self.__records, "w", encoding="utf-8") as file:
                json.dump(record, file)

    def get_records(self):
        return self.__records