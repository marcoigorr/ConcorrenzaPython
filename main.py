from Book import Book
from Reader import Reader
from Writer import Writer


def main():
    book = Book()

    threadR1 = Reader("Reader1", book)
    threadW1 = Writer("Writer1", book)

    threadR1.start()
    threadW1.start()

    threadR1.join()
    threadW1.join()


if __name__ == '__main__':
    main()
