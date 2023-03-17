from threading import Thread
from time import sleep
import random


class Writer(Thread):
    def __init__(self, thread_name, book):
        Thread.__init__(self, name=thread_name)

        self.__delay = 0
        self.__book = book

    def Read(self) -> None:
        while 1:
            if not self.__book.IsWriting():
                self.__book.setIsReading(True)
                self.__book.increaseActiveReaders()
                print(f"[+] Thread {self.name} Is Reading.")

                sleep(self.__delay)

                if self.__book.getActiveReaders() == 1:
                    self.__book.setIsReading(False)

                self.__book.decreaseActiveReaders()
                print(f"[+] Thread {self.name} Finished Reading.")

    def Write(self) -> None:
        if not self.__book.IsReading() and not self.__book.IsWriting():
            self.__book.setIsWriting(True)
            print(f"[+] Thread {self.name} Is Writing.")

            sleep(self.__delay)

            self.__book.setIsWriting(False)
            print(f"[+] Thread {self.name} Finished Writing.")

    def run(self) -> None:
        print(f"[+] Thread {self.name} started!")
        while 1:
            self.__delay = random.randint(0, 5)
            sleep(self.__delay)
            self.Write()

            #sleep(self.__delay)
            #self.Read()
