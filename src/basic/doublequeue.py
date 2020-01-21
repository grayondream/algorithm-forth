from src.basic import doublelink


class double_queue(object):
    '''
    @brief  双向队列，使用链表实现
    '''
    def __init__(self):
        self.left = doublelink.double_node(None, None, None)
        self.right = self.left
        self.len = 0
        
    def empty(self):
        return self.right == self.left and self.len == 0
        
    def size(self):
        return self.len
        
    def en_left(self, data):
        '''
        @brief  从左侧入队
        @param  data    入队的参数
        '''
        node = doublelink.double_node(None, self.left, data)
        self.left.pre = node
        self.len += 1
        
    def de_left(self):
        '''
        @brief  从左侧出队
        '''
        if self.empty():
            return None
        
        dat = self.left.data
        self.left = self.left.next
        self.left.pre = None
        self.len -= 1
        return dat
        
    def en_right(self, data):
        '''
        @brief  从右侧入队
        @param  data    入队的数据
        '''
        node = doublelink.double_node(self.right, None, data)
        self.right.next = node
        self.len += 1
        
    def de_right(self):
        '''
        @brief  从右侧出队
        '''
        if self.empty():
            return None
        
        dat = self.right.data
        self.right = self.right.pre
        self.right.next = None
        self.len -= 1
        return dat
        
    
    