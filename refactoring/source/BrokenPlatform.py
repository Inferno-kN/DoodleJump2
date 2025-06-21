from refactoring.source.AbstractPlatform import AbstractPlatform

class BrokenPlatform(AbstractPlatform):


    def __init__(self, x, y):
        super().__init__(x, y, "картинка")
        self.__is_broken = False
        self.__type = 'broken'



    def break_platform(self) -> bool:
        self.__is_broken = True


    def get_broken_platform(self):
        return self.__is_broken