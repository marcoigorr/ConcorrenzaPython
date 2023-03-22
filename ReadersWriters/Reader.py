from Book import Book

from threading import Thread
from time import sleep
import random

from tkinter import ttk


class Reader(Thread):
    def __init__(self, thread_name, book, label, pb):
        Thread.__init__(self, name=thread_name)

        self.__delay = 0
        self.__book: Book = book
        self.__label: ttk.Label = label
        self.__pb: ttk.Progressbar = pb

    def getBook(self) -> Book:
        return self.__book

    def Read(self) -> None:
        p = 0
        if not self.__book.isWriting():
            self.__book.increaseActiveReaders()
            self.__label['text'] = f"{self.name} - Reading."

            wait = 10
            while wait > 0:
                p = (p + 10) % 100
                self.__pb['value'] = p
                self.__pb.update_idletasks()
                sleep(self.__delay / 10)
                wait -= 1

            self.__book.decreaseActiveReaders()
            self.__label['text'] = f"{self.name} - IDLE"

    def run(self) -> None:
        self.__label['text'] = f"{self.name} - STARTED"
        while 1:
            self.__delay = random.randint(1, 8)
            sleep(5)

            self.__book.manager.addObject(self, "Read")
