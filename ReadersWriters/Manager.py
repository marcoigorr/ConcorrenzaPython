from threading import Thread
import time


class Manager(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__limit = 100
        self.__queue: list = []

    # Get
    def getQueue(self) -> list:
        return self.__queue

    def addObject(self, obj, action) -> None:
        if len(self.__queue) < self.__limit:
            dictionary = {obj: action}
            self.__queue.append(dictionary)

    def run2(self) -> None:
        while 1:
            if self.__queue:
                elem = self.__queue.pop(0)
                action = list(elem.values())[0]
                obj = list(elem.keys())[0]
                if action == "Read" and not obj.getBook().isWriting():
                    pass

    def run(self) -> None:
        print(f"[+] Manager started!")
        while 1:
            if self.__queue:
                elem = self.__queue[0]
                obj = list(elem.keys())[0]
                action = list(elem.values())[0]

                if action == "Read" and not obj.getBook().isWriting():
                    with obj.condition:
                        obj.condition.notifyAll()
                    self.__queue.pop(0)
                    print(f"[+] Removed {obj} - {action}")
                elif action == "Write" and not obj.getBook().isWriting() and obj.getBook().getActiveReaders() == 0:
                    with obj.condition:
                        obj.condition.notifyAll()
                    self.__queue.pop(0)
                    print(f"[+] Removed {obj} - {action}")
