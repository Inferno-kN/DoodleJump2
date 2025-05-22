from refactoring.source.AbstractPlatform import AbstractPlatform

class SimplePlatform(AbstractPlatform):


    def __init__(self, x, y):
        super().__init__(x, y, "картинка")