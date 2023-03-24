from Queue import Queue
from Barber import Barber
from Customer import Customer

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.geometry('600x300')
    root.title('Sleeping Barber')
    root.grid()

    queue: Queue = Queue(limit=6, root=root)
    barber: Barber = Barber(queue, root)

    threads = [barber]
    names = ['Pino', 'Beppe', 'Zorzi', 'Ciscogna', 'Topi', 'Cani', 'Polli']

    for name in names:
        customer = Customer(name, barber)
        threads.append(customer)

    for thread in threads:
        thread.start()

    root.mainloop()


if __name__ == '__main__':
    main()
