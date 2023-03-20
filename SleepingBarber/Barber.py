import random
from threading import Thread, Event
import time

class Barber(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.flag = Event()
        self.isSleeping = True

    def Sleep(self) -> None:
        self.isSleeping = True
        print(f"[+] Barber has fallen asleep.")
        while self.isSleeping:
            pass

    def WakeUp(self) -> None:
        self.isSleeping = False
        print(f"[+] Barber woke up.")

    def Work(self) -> None:
        customer = self.queue.chairs[0]
        print(f"[+] Working on {customer}.")
        self.queue.getNextCustomer()
        print(f"    Updated queue: {self.queue.chairs}")

        time.sleep(random.randint(1,2))

    def run(self) -> None:
        while 1:
            if self.queue.isEmpty():
                self.Sleep()
            else:
                self.Work()
