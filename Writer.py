from threading import Thread
from time import sleep


class Writer(Thread):
    def __init__(self, thread_name, book):
        Thread.__init__(self)

        self.thread_name = thread_name
        self.book = book

    def Read(self) -> None:
        while 1:
            if not self.book.IsWriting():
                self.book.setIsReading(True)
                print(f"[+] Thread {self.thread_name} Is Reading.")

                sleep(1)

                self.book.setIsReading(False)
                print(f"[+] Thread {self.thread_name} Finished Reading.")

    def Write(self) -> None:
        if not self.book.IsReading() and not self.book.IsWriting():
            self.book.setIsWriting(True)
            print(f"[+] Thread {self.thread_name} Is Writing.")

            sleep(5)

            self.book.setIsWriting(False)
            print(f"[+] Thread {self.thread_name} Finished Writing.")

    def run(self) -> None:
        print(f"[+] Thread {self.thread_name} started!")
        while 1:
            sleep(1)
            self.Write()
