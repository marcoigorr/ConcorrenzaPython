from Book import Book

from threading import Thread, Condition
from time import sleep
import random

from tkinter import ttk


class Writer(Thread):
    def __init__(self, thread_name, book, label, pb):
        Thread.__init__(self, name=thread_name)

        self.__delay: int = 0
        self.__book: Book = book
        self.__label: ttk.Label = label
        self.__pb: ttk.Progressbar = pb

        self.condition: Condition = Condition()

    # Get
    def getBook(self) -> Book:
        return self.__book

    def getDelay(self) -> int:
        return self.__delay

    def getLabel(self) -> ttk.Label:
        return self.__label

    def getProgressBar(self) -> ttk.Progressbar:
        return self.__pb

    # Set
    def setLabel(self, newLabel) -> None:
        self.__label['text'] = newLabel

    # main
    def Write(self) -> None:
        self.__book.Write(writer=self, delay=self.__delay)

    def Read(self) -> None:
        self.__book.Read(reader=self, delay=self.__delay)

    def run(self) -> None:
        self.__label['text'] = f"{self.name} - STARTED"
        sleep(random.randint(1, 5))

        while 1:
            self.__delay = random.randint(1, 5)
            sleep(self.__delay)

            with self.condition:
                if random.choices([1, 2], weights=(20, 80), k=1)[0] == 1:
                    action = "Read"
                else:
                    action = "Write"

                self.__book.getManager().addObject(self, action)

                self.condition.wait()

                if action == "Write":
                    self.Write()
                else:
                    self.Read()
