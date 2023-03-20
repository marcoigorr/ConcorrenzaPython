from Book import Book

from threading import Thread
from time import sleep
import random


class Writer(Thread):
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

    def Write(self) -> None:
        if self.__book.getActiveReaders() == 0 and not self.__book.isWriting():
            self.__book.setIsWriting(True)
            print(f"[+] Thread {self.name} Is Writing.")
            self.__label['text'] = f"{self.name} - Writing."

            sleep(self.__delay)

            self.__book.setIsWriting(False)
            print(f"[+] Thread {self.name} Finished Writing.")
            self.__label['text'] = f"{self.name} - IDLE"

    def run(self) -> None:
        print(f"[+] Thread {self.name} started!")
        self.__label['text'] = f"{self.name} - STARTED"
        while 1:
            self.__delay = random.randint(1, 5)

            if random.choices([1, 2], weights=(10, 90), k=1)[0] == 1:
                self.Read()
            self.Write()

            sleep(self.__delay)
