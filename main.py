from Book import Book
from Reader import Reader
from threading import Thread


def main():
    book = Book()
    reader = Reader(book)
    threadR = Thread(target=reader.Read())


if __name__ == '__main__':
    main()
