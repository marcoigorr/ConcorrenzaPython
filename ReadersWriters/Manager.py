from threading import Thread
import time


class Manager(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queue: list = []

    def addObject(self, obj, action):
        dictionary = {obj: action}
        self.queue.append(dictionary)

    def run(self) -> None:
        print(f"[+] Manager started!")
        while 1:
            time.sleep(0.5)

            if self.queue:
                print(self.queue)

                elem = self.queue.pop(0)

                obj = list(elem.keys())[0]
                action = list(elem.values())[0]

                if action == "Read" and not obj.getBook().isWriting():
                    obj.Read()
                elif action == "Write" and not obj.getBook().isWriting() and obj.getBook().getActiveReaders() == 0:
                    obj.Write()
