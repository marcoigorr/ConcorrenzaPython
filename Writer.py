from time import sleep


class Writer:
    def __init__(self, book):
        self.book = book

    def Read(self):
        while 1:
            sleep(3)
            self.book.Reading()

    def Write(self):
        while 1:
            sleep(5)
            self.book.Writing()
