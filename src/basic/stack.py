import os
#


class stack(object):
    '''
    @brief  栈
    相关函数简单明了不做具体的注释
    '''
    def __init__(self):
        super(stack, self).__init__()
        self._data = []

    def push(self, ele):
        self._data.append(ele)

    def pop(self):
        res = self._data[-1]
        del self._data[-1]
        return res

    def top(self):
        return self._data[-1]

    def empty(self):
        return 0 == len(self._data)


def main():
    pass

if __name__ == '__main__':
    main()

