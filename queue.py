
class Queue:
    def __init__(self, max):
        self.__queue = []
        self.__maxlength = max

    def queue(self, element):
        if len(self.__queue) < self.__maxlength:
            return self.__queue.append(element)
        else:
            return 'Error. The queue is full.'

    def dequeue(self):
        if len(self.__queue) != 0:
            return self.__queue.pop(0)
        else:
            return 'Error. The queue is empty.'
