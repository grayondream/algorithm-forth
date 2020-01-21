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

    @staticmethod
    def clone(self, stk):
        '''
        @brief  返回一个拷贝的版本
        @param  stk 需要拷贝的stack
        '''
        new_stk = stack()
        new_stk._data = stk._data.copy()
        return new_stk
        
    @staticmethod
    def catenation(self, rst, snd):
        '''
        @brief  将栈snd调拼接到栈rst后面
        @param  rst 第一个栈
        @param  snd 第二个栈
        '''
        new_stk = rst.clone(rst)
        new_stk._data += snd._data
        return new_stk
        
def main():
    pass

if __name__ == '__main__':
    main()

