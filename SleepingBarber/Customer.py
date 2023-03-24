from Queue import Queue
from Barber import Barber

from threading import Thread
import random
import time


class Customer(Thread):
    def __init__(self, thread_name, barber):
        Thread.__init__(self, name=thread_name)
        self.barber: Barber = barber

        self.queue: Queue = self.barber.queue  # get barber's queue

    def run(self) -> None:
        while 1:
            time.sleep(random.randint(2, 4))

            self.queue.Enter(self)

            if self.barber.isSleeping:
                self.barber.WakeUp()

            time.sleep(10)