class Queue:
    def __init__(self):
        self.limit: int = 10
        self.chairs: list = []

    def IsEmpty(self) -> bool:
        return self.chairs == []

    def Enter(self, customer) -> bool:
        if len(self.chairs) == self.limit:
            return False

        if customer in self.chairs:
            return False

        self.chairs.append(customer)
        return True
