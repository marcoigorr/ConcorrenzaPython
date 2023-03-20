from Book import Book
from Reader import Reader
from Writer import Writer

import tkinter as tk
from tkinter import ttk, Frame


def main():
    root = tk.Tk()
    root.geometry('600x300')
    root.title('Readers Writers')
    root.grid()

    labelB = ttk.Label(root, text="Book", width=20, font=("Colibri", 16))
    labelB.grid(row=6, column=1, padx=10, pady=5)

    book = Book("Book", labelB)

    for i in range(1,3):
        labelR = ttk.Label(root, text=f"Reader {i}", width=20, font=("Colibri", 16))
        labelR.grid(row=i, column=1, padx=10, pady=2)
        labelW = ttk.Label(root, text=f"Writer {i}", width=20, font=("Colibri", 16))
        labelW.grid(row=i+2, column=1, padx=10, pady=2)

        tR = Reader(f"Reader {i}", book, labelR)
        tW = Writer(f"Writer {i}", book, labelW)

        tR.start()
        tW.start()

    root.mainloop()

if __name__ == '__main__':
    main()
