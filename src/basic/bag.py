import os
#


class bag(object):
    '''
    @brief  背包
    相关的函数简单明了不做注释
    '''
    def __init__(self):
        super(bag, self).__init__()
        self._data = []


    def add(self, ele):
        self._data.append(ele)

    def empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __iter__(self):
        return self._data.__iter__()

    def __getitem__(self, index):
        return self._data[index]


def main():
    pass
if __name__ == '__main__':
    main()