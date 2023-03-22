from Manager import Manager

from time import sleep

from tkinter import ttk


class Book:
    def __init__(self, name, manager, label):
        self.__name: str = name
        self.__manager: Manager = manager
        self.__isWriting: bool = False
        self.__activeReaders: int = 0
        self.__label: ttk.Label = label

    # Get
    def getName(self) -> str:
        return self.__name

    def getManager(self) -> Manager:
        return self.__manager

    def isWriting(self) -> bool:
        return self.__isWriting

    def getActiveReaders(self) -> int:
        return self.__activeReaders

    def getLabel(self) -> ttk.Label:
        return self.__label

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

    # main
    def Read(self, reader, delay) -> None:
        p = 0
        if not self.isWriting():
            self.increaseActiveReaders()
            reader.setLabel(f"{reader.name} - Reading.")

            wait = 10
            while wait > 0:
                p = (p + 10) % 100
                reader.getProgressBar()['value'] = p
                reader.getProgressBar().update_idletasks()
                sleep(delay / 10)
                wait -= 1

            self.decreaseActiveReaders()
            reader.setLabel(f"{reader.name} - IDLE")

    def Write(self, writer, delay) -> None:
        p = 0
        if self.getActiveReaders() == 0 and not self.isWriting():
            self.setIsWriting(True)
            writer.setLabel(f"{writer.name} - Writing.")

            wait = 10
            while wait > 0:
                p = (p + 10) % 100
                writer.getProgressBar()['value'] = p
                writer.getProgressBar().update_idletasks()
                sleep(delay / 10)
                wait -= 1

            self.setIsWriting(False)
            writer.setLabel(f"{writer.name} - IDLE")
