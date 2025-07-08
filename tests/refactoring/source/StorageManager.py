from refactoring.cfg.config import records
import json, os

class StorageManager:
    def __init__(self):
        self.__records = records
        if not isinstance(self.__records, str): raise TypeError

    def read(self) -> list[int]:
        if not isinstance(self.__records, str): raise TypeError
        with open(self.__records, "r") as file:
            if os.path.exists(self.__records) and os.path.getsize(self.__records) > 0:
                return json.load(file)
            return []


    def write(self, value):
        record = self.read()
        if not isinstance(value, (str, int)): raise TypeError
        if value not in record:
            with open(self.__records, "w") as file:
                record.append(value)
                json.dump(record, file)


    def get_records(self):
        return self.__records