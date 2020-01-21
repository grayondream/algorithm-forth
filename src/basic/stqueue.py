from src.basic import linklist
from src.basic import cyc_queue

class stk_queue(object):
    '''
    @brief  具有栈功能的队列，使用链表实现
    '''
    def __init__(self, size):
        super(stk_queue, self).__init__()
        self.head = cyc_queue.extend_link(None, size)
        self.tail = self.head
        self.len = 0
        
    def enqueue(self, data):
        '''
        @brief  入队
        @param  data    入队的数据
        '''
        if self.tail.next is None:
            cyc_queue.extend_link(self.tail, self.len * 2)
            
        self.tail.data = data
        self.tail = self.tail.next
        self.len += 1
        
    def dequeue(self):
        '''
        @brief  出队
        '''
        if self.empty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            self.len -= 1
            
        return data
        
    def empty(self):
        return self.head == self.tail and self.len == 0
        
    def size(self):
        return self.len
        
    def push(self, data):
        '''
        @brief  压入，从head操作
        @param  data    压入的数据
        '''
        node = linklist.linklist(self.head, data)
        self.head = node
        self.len += 1
        
    def pop(self):
        '''
        @brief  弹出操作
        '''
        data = self.head.data
        self.len -= 1
        self.head = self.head.next
        retur data
        
        