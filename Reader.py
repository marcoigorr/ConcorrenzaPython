from threading import Thread
from time import sleep


class Reader (Thread):
    def __init__(self, thread_name, book):
        Thread.__init__(self)

        self.thread_name = thread_name
        self.book = book

    def Read(self) -> None:
        if not self.book.IsWriting():
            self.book.setIsReading(True)
            print(f"[+] Thread {self.thread_name} Is Reading.")

            sleep(3)

            self.book.setIsReading(False)
            print(f"[+] Thread {self.thread_name} Finished Reading.")

    def run(self) -> None:
        print(f"[+] Thread {self.thread_name} started!")
        while 1:
            sleep(3)
            self.Read()
