from Queue import Queue

from threading import Thread, Condition
import random
import time

import tkinter as tk
from tkinter import ttk


class Barber(Thread):
    def __init__(self, queue, root):
        Thread.__init__(self)
        self.queue: Queue = queue

        self.isSleeping: bool = True
        self.condition: Condition = Condition()

        self.root: tk.Tk = root
        self.lStatus: ttk.Label = ttk.Label(self.root, text=f"Barber: sleeping", width=30, font=("Colibri", 14))
        self.lStatus.pack(padx=10, pady=10, fill='both')

        self.pb: ttk.Progressbar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
        self.pb.pack(padx=15, pady=0, side='top', anchor="w")
        self.pb['maximum'] = 100

    def Sleep(self) -> None:
        with self.condition:
            self.isSleeping = True
            self.lStatus['text'] = f"Barber: sleeping"
            self.condition.wait()

    def WakeUp(self) -> None:
        with self.condition:
            self.isSleeping = False
            self.lStatus['text'] = f"Barber: awake!"
            self.condition.notifyAll()

    def Work(self) -> None:
        while not self.queue.IsEmpty():
            customer = self.queue.chairs[0].name
            self.lStatus['text'] = f"Barber: Working on {customer}"

            # Progression bar takes "delay" seconds to complete
            delay = random.randint(1, 2)
            wait = 10
            p = 0
            while wait > 0:
                p = (p + 10) % 100
                self.pb['value'] = p
                self.pb.update_idletasks()
                time.sleep(delay / 10)
                wait -= 1

            self.queue.chairs.pop(0)

            self.queue.UpdateQueue()  # print queue

    def run(self) -> None:
        while 1:
            self.queue.UpdateQueue()  # print queue

            if self.queue.IsEmpty():
                self.Sleep()
            else:
                self.Work()

