from time import sleep


class Reader:
    def __init__(self, book):
        self.book = book

    def Read(self):
        while 1:
            sleep(3)
            self.book.Reading()
