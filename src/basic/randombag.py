import random


class random_bag(object):
    '''
    @brief  随即背包，只能添加元素，访问时元素的顺序不一
    @note   TODO:实现有点儿问题
    '''
    def __init__(self):
        self.data = []
        self.len = 0
        
    def add(self, data):
        '''
        @brief  添加元素
        @data   要添加的元素
        '''
        self.data.append(data)
        self.len += 1
        
    def size(self):
        return self.len
        
    def empty(self):
        return 0 == self.len
        
    def get(self):
        self.data[random.randint(0, self.len - 1)]