import os
#


class queue(object):
    def __init__(self):
        super(queue, self).__init__()
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        ret = self._data[0]
        del self._data[0]
        return ret

    def empty(self):
        return 0 == len(self._data)

    def size(self):
        return len(self._data)

def main():
    pass

if __name__ == '__main__':
    main()