from threading import Thread
from time import sleep
import random


class Reader(Thread):
    def __init__(self, thread_name, book):
        Thread.__init__(self, name=thread_name)

        self.__delay = 0
        self.__book = book

    def Read(self) -> None:
        if not self.__book.IsWriting():
            self.__book.setIsReading(True)
            self.__book.increaseActiveReaders()
            print(f"[+] Thread {self.name} Is Reading.")

            sleep(self.__delay)

            if self.__book.getActiveReaders() == 1:
                self.__book.setIsReading(False)

            self.__book.decreaseActiveReaders()
            print(f"[+] Thread {self.name} Finished Reading.")

    def run(self) -> None:
        print(f"[+] Thread {self.name} started!")
        while 1:
            self.__delay = random.randint(1, 5)
            sleep(self.__delay)
            self.Read()
