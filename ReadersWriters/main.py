from Book import Book
from Reader import Reader
from Writer import Writer

import tkinter as tk
from tkinter import ttk, Frame


def main():
    root = tk.Tk()
    root.geometry('900x400')
    root.title('Readers Writers')
    root.grid()

    label = ttk.Label(root, text="Book", width=20, font=("Colibri", 16))
    label.grid(row=6, column=1, padx=10, pady=5)
    book = Book("Book", label)

    people = []

    for i in range(2):
        # Readers
        label = ttk.Label(root, text=f"Reader {i}", width=20, font=("Colibri", 16))
        label.grid(row=i, column=1, padx=10, pady=2)

        pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
        pb.grid(row=i, column=2, padx=20, pady=2)
        pb['maximum'] = 100

        tR = Reader(f"Reader {i}", book, label, pb)
        people.append(tR)

        # Writers
        label = ttk.Label(root, text=f"Writer {i}", width=20, font=("Colibri", 16))
        label.grid(row=i+2, column=1, padx=10, pady=2)

        pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
        pb.grid(row=i+2, column=2, padx=20, pady=2)
        pb['maximum'] = 100

        tW = Writer(f"Writer {i}", book, label, pb)
        people.append(tW)

    for p in people: p.start()

    root.mainloop()

if __name__ == '__main__':
    main()
