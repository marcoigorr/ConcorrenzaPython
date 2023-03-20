class Book:
    def __init__(self, name, label):
        self.__name = name
        self.__isWriting: bool = False
        self.__activeReaders: int = 0
        self.__label = label

    # Get
    def isWriting(self) -> bool:
        return self.__isWriting

    def getActiveReaders(self) -> int:
        return self.__activeReaders

    # Set
    def setIsWriting(self, boolean) -> None:
        self.__isWriting = boolean

    # Helpers
    def increaseActiveReaders(self) -> None:
        self.__activeReaders += 1
        self.__label['text'] = f"{self.__name} has {self.__activeReaders} reader(s)"

    def decreaseActiveReaders(self) -> None:
        self.__activeReaders -= 1
        self.__label['text'] = f"{self.__name} has {self.__activeReaders} reader(s)"
