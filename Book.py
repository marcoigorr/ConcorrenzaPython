
class Book:
    def __init__(self):
        self.__isReading: bool = False
        self.__isWriting: bool = False

    # Get
    def IsReading(self) -> bool:
        return self.__isReading

    def IsWriting(self) -> bool:
        return self.__isWriting

    # Set
    def setIsReading(self, boolean) -> None:
        self.__isReading = boolean

    def setIsWriting(self, boolean) -> None:
        self.__isWriting = boolean
