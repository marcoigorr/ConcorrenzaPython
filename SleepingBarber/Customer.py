from threading import Thread
import random
import time


class Customer(Thread):
    def __init__(self, thread_name, queue, barber):
        Thread.__init__(self, name=thread_name)
        self.queue = queue
        self.barber = barber

    def run(self) -> None:
        while 1:
            if not self.name in self.queue.chairs:
                time.sleep(random.randint(5,10))

                if not self.queue.addCustomer(self):
                    print(f"[+] {self.name} found no empty chairs.")
                print(f"[+] {self.name} entered queue.")
                print(f"    Queue: {self.queue.chairs}")
                if self.barber.isSleeping:
                    self.barber.WakeUp()
