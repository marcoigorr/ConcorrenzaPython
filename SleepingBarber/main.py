from Queue import Queue
from Barber import Barber
from Customer import Customer


def main() -> None:
    queue: Queue = Queue()
    barber: Barber = Barber(queue)
    customer1: Customer = Customer("Gino", barber)
    customer2: Customer = Customer("Pippo", barber)
    customer3: Customer = Customer("Zorzi", barber)
    customer4: Customer = Customer("Cani", barber)
    customer5: Customer = Customer("Gatti", barber)
    customer6: Customer = Customer("Topi", barber)
    customer7: Customer = Customer("Cicogne", barber)

    barber.start()
    customer1.start()
    customer2.start()
    customer3.start()
    customer4.start()
    customer5.start()
    #customer6.start()
    #customer7.start()


if __name__ == '__main__':
    main()
