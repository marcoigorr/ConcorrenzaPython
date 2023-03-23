from threading import Thread
import os
import time


class Manager(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__limit = 10
        self.__queue: list = []

    # Get
    def getQueue(self) -> list:
        return self.__queue

    # main
    def Enqueue(self, obj, action) -> None:
        # Using a dictionary to store info for execution {key: Reader/Writer, value: "Read/Write"}
        dictionary = {obj: action}

        if dictionary not in self.__queue:
            self.__queue.append(dictionary)

    def UpdateInfo(self) -> None:
        os.system("cls")  # edit configuration and tick "Emulate Terminal in output console"
        print(f"[+] Queue: ")
        for i in range(len(self.__queue)):
            threadName = list(self.__queue[i].keys())[0].name
            print(f"   {i}) {threadName}")

    def run(self) -> None:
        print(f"[+] Manager started!")

        while 1:
            self.UpdateInfo()
            time.sleep(.3)

            # If queue is not empty
            if self.__queue:
                elem = self.__queue[0]  # get first element of queue
                obj = list(elem.keys())[0]  # get reference of Reader/Writer object
                action = list(elem.values())[0]  # get action to perform

                if action == "Read" and not obj.getBook().isWriting():
                    with obj.condition:
                        obj.condition.notifyAll()  # continue execution of the thread
                    self.__queue.pop(0)  # remove from queue
                elif action == "Write" and not obj.getBook().isWriting() and obj.getBook().getActiveReaders() == 0:
                    with obj.condition:
                        obj.condition.notifyAll()
                    self.__queue.pop(0)
