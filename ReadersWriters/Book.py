class Book:
    def __init__(self):
        self.__isWriting: bool = False
        self.__activeReaders: int = 0

    # Get
    def IsReading(self) -> bool:
        return self.__isReading

    def IsWriting(self) -> bool:
        return self.__isWriting

    def getActiveReaders(self) -> int:
        return self.__activeReaders

    # Set
    def setIsReading(self, boolean) -> None:
        self.__isReading = boolean

    def setIsWriting(self, boolean) -> None:
        self.__isWriting = boolean

    def setActiveReaders(self, n_readers) -> None:
        self.__activeReaders = n_readers

    # Helpers
    def increaseActiveReaders(self) -> None:
        self.__activeReaders += 1

    def decreaseActiveReaders(self) -> None:
        self.__activeReaders -= 1
