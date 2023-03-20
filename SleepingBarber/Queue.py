class Queue:
    def __init__(self):
        self.chairs = []

    def isEmpty(self) -> bool:
        return self.chairs == []

    def addCustomer(self, customer) -> bool:
        if not len(self.chairs) == 4:
            self.chairs.append(customer.name)
            return True
        return False

    def getNextCustomer(self) -> None:
        self.chairs.pop(0)
