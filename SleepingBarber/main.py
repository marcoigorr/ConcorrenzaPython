from Queue import Queue
from Barber import Barber
from Customer import Customer


def main() -> None:
    queue: Queue = Queue()
    barber: Barber = Barber(queue)

    threads = [barber]
    names = ['Pino', 'Beppe', 'Zorzi', 'Ciscogna', 'Topi', 'Cani', 'Polli']

    for name in names:
        customer = Customer(name, barber)
        threads.append(customer)

    for thread in threads:
        thread.start()


if __name__ == '__main__':
    main()
