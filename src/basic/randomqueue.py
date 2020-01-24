import random


def swap(rst, snd):
    tmp = rst
    rst = snd
    snd = tmp


class random_queue(object):
    '''
    @brief  随机队列，元素出队时将随机从队列中挑选一个元素出对并和对位互换，左边为队头，出元素
    '''
    def __init__(self):
        super(random_queue, self).__init__()
        self.data = []
        
    def empty(self):
        return self.size() == 0
        
    def size(self):
        return len(self.data)
        
    def en_queue(self, data):
        '''
        @brief  入队，list的右边
        @param  data    入队的数据
        '''
        self.data.append(data)
        
    def de_queue(self):
        '''
        @brief  将右边队尾的元素和随机挑选中的互换出对
        '''
        index = random.randint(0, self.size() - 1)
        swap(self.data[index], self.data[0])
        res =  self.data[0]
        del self.data[0]
        return res