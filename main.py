from Libro import Book
from Lettore import Reader
from threading import Thread

def main():
    book = Book()
    reader = Reader(book)
    threadR = Thread(target=reader.Read())



if __name__ == '__main__':
    main()