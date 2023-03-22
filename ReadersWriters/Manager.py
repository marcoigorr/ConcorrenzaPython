from threading import Thread
import time


class Manager(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__limit = 10
        self.__queue: list = []

    # Get
    def getQueue(self) -> list:
        return self.__queue

    def addObject(self, obj, action) -> None:
        if len(self.__queue) < self.__limit:
            dictionary = {obj: action}
            self.__queue.append(dictionary)

    def run(self) -> None:
        while 1:
            elem = self.__queue.pop(0)
            action = list(elem.values())[0]
            obj = list(elem.keys())[0]
            if action == "Read" and not obj.getBook().isWriting():
                obj.Read()

    def run2(self) -> None:
        print(f"[+] Manager started!")
        while 1:
            if self.__queue:
                time.sleep(.5)
                print(self.__queue)
                elem = self.__queue[0]

                obj = list(elem.keys())[0]
                action = list(elem.values())[0]

                if action == "Read" and not obj.getBook().isWriting():
                    obj.Read()
                    self.__queue.pop(0)
                    print(f"[+] Removed {obj} - {action}")
                elif action == "Write" and not obj.getBook().isWriting() and obj.getBook().getActiveReaders() == 0:
                    obj.Write()
                    self.__queue.pop(0)
                    print(f"[+] Removed {obj} - {action}")
