from Book import Book
from Reader import Reader
from Writer import Writer
from Manager import Manager

import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.geometry('900x600')
    root.title('Readers Writers')
    root.grid()

    readers = 6
    writers = 4
    people = []

    manager = Manager()

    people.append(manager)

    label = ttk.Label(root, text="Book", width=20, font=("Colibri", 16))
    label.grid(row=readers+writers+2, column=1, padx=10, pady=5)
    book = Book("Book", manager, label)

    # Readers
    for i in range(readers):
        label = ttk.Label(root, text=f"Reader {i}", width=20, font=("Colibri", 16))
        label.grid(row=i, column=1, padx=10, pady=2)

        pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
        pb.grid(row=i, column=2, padx=20, pady=2)
        pb['maximum'] = 100

        tR = Reader(f"Reader {i}", book, label, pb)
        people.append(tR)

    # Writers
    for i in range(readers, writers+readers):
        label = ttk.Label(root, text=f"Writer {i-readers}", width=20, font=("Colibri", 16))
        label.grid(row=i + 2, column=1, padx=10, pady=2)

        pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
        pb.grid(row=i + 2, column=2, padx=20, pady=2)
        pb['maximum'] = 100

        tW = Writer(f"Writer {i-readers}", book, label, pb)
        people.append(tW)

    for p in people: p.start()

    root.mainloop()


if __name__ == '__main__':
    main()
