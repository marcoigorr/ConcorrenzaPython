from Book import Book

from threading import Thread
from time import sleep
import random


class Reader(Thread):
    def __init__(self, thread_name, book, label):
        Thread.__init__(self, name=thread_name)

        self.__delay = 0
        self.__book: Book = book
        self.__label = label

    def Read(self) -> None:
        if not self.__book.isWriting():
            self.__book.increaseActiveReaders()
            print(f"[+] Thread {self.name} Is Reading.")
            self.__label['text'] = f"{self.name} - Reading."

            sleep(self.__delay)

            self.__book.decreaseActiveReaders()
            print(f"[+] Thread {self.name} Finished Reading.")
            self.__label['text'] = f"{self.name} - IDLE"

    def run(self) -> None:
        print(f"[+] Thread {self.name} started!")
        self.__label['text'] = f"{self.name} - STARTED"
        while 1:
            self.__delay = random.randint(1, 5)
            sleep(self.__delay)
            self.Read()
            sleep(self.__delay)
