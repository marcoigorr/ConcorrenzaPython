from Queue import Queue
from Barber import Barber
from Customer import Customer


def main() -> None:
    queue = Queue()
    barber = Barber(queue)
    customer1 = Customer("Gino", queue, barber)
    customer2 = Customer("Pippo", queue, barber)
    customer3 = Customer("Zorzi", queue, barber)
    customer4 = Customer("Cani", queue, barber)

    barber.start()
    customer1.start()
    customer2.start()
    customer3.start()
    customer4.start()


if __name__ == '__main__':
    main()
