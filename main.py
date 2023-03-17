from Book import Book
from Reader import Reader
from Writer import Writer


def main():
    book = Book()

    threadR1 = Reader("Reader1", book)
    threadR2 = Reader("Reader2", book)
    threadW1 = Writer("Writer1", book)
    threadW2 = Writer("Writer2", book)

    threadR1.start()
    threadR2.start()
    threadW1.start()
    threadW2.start()


if __name__ == '__main__':
    main()
