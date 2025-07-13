from configs.config import simple_platform
from source.AbstractPlatform import AbstractPlatform

class SimplePlatform(AbstractPlatform):


    def __init__(self, x, y):
        super().__init__(x, y, simple_platform)