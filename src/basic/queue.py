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
    
    @staticmethod
    def clone(self, q):
        '''
        @brief  返回一个queue的拷贝版本
        @param  q   需要进行拷贝的queue
        '''
        new_q = queue()
        new_q._data = q._data.copy()
        return new_q
        
    @staticmethod
    def catenation(self, rst, snd):
        '''
        @brief  将队列snd接在队列rst后面
        @param  rst 第一个队列
        @param  snd 第二个队列
        '''
        new_q = rst.clone(rst)
        new_q._data += snd._data
        return new_q
        
def main():
    pass

if __name__ == '__main__':
    main()