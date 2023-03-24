import tkinter as tk
from tkinter import ttk


class Queue:
    def __init__(self, limit, root):
        self.limit: int = limit
        self.chairs: list = []

        self.root: tk.Tk = root
        self.lQueue: ttk.Label = ttk.Label(self.root, text=f"Queue: [empty]", width=100, padding=10, font=("Colibri", 14))
        self.lQueue.pack()

    def IsEmpty(self) -> bool:
        return self.chairs == []

    def UpdateQueue(self) -> None:
        self.lQueue['text'] = f"Queue -> {[self.chairs[i].name for i in range(len(self.chairs))]}"

    def Enter(self, customer) -> bool:
        if len(self.chairs) == self.limit:
            return False

        if customer in self.chairs:
            return False

        self.chairs.append(customer)
        return True
