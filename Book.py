from time import sleep


class Book:
    def __init__(self):
        self.__isReading: bool = False
        self.__isWriting: bool = False

    def IsReading(self) -> bool:
        return self.__isReading

    def IsWriting(self) -> bool:
        return self.__isWriting

    def Reading(self):
        if not self.__isWriting:
            print("[+] Is Reading.")

            self.__isReading = True

    def Writing(self):
        if not self.__isReading and not self.__isWriting:
            print("[+] Is Writing.")

            self.__isWriting = True
            sleep(1)
            self.__isWriting = False
