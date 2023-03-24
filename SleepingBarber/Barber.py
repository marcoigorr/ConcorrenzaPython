from Queue import Queue

from threading import Thread, Condition
import os
import random
import time

class Barber(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue: Queue = queue

        self.isSleeping: bool = True
        self.condition: Condition = Condition()

    def Sleep(self) -> None:
        with self.condition:
            self.isSleeping = True
            print(f"[+] Barber is sleeping")
            self.condition.wait()

    def WakeUp(self) -> None:
        with self.condition:
            self.isSleeping = False
            self.condition.notifyAll()

    def Work(self) -> None:
        while not self.queue.IsEmpty():
            customer = self.queue.chairs[0].name
            print(f"[+] Working on {customer}.")
            time.sleep(random.randint(1, 2))

            self.queue.chairs.pop(0)

            os.system("cls")
            print(f"[+] Queue -> {[self.queue.chairs[i].name for i in range(len(self.queue.chairs))]}")

    def run(self) -> None:
        while 1:
            os.system("cls")
            print(f"[+] Queue -> {[self.queue.chairs[i].name for i in range(len(self.queue.chairs))]}")

            if self.queue.IsEmpty():
                self.Sleep()
            else:
                self.Work()

