from src.basic import linklist

def extend_link(link, size):
    '''
    @brief  扩展link节点，如果link为空则默认创建一个的链表
    @param  link链表需要插入的节点
    '''
    is_none = False
    if link is None:
        is_none = True
    
    index = link
    while size != 0:
        node = linklist.linklist(data=0, next=None)
        if index.next is not None:
            node.next = index.next.next
            
        index.next = node
        index = index.next
        size -= 1
    
    if is_none:
        index.next = link
            
    return link
    
    
class circle_queue(object):
    '''
    @brief  环形链表queue实现
    '''
    def __init__(self):
        super(circle_queue, self).__init__()
        self.head = extend_link(None, 4)        #magic number 4,默认链表长度
        self.tail = self.head
        self.len = 0
        
    def enqueue(self, item):
        if self.full():
            extend_link(self.head, self.len * 2)
            
        self.head = self.head.next
        self.head = item
        self.len += 1
    
    def dequeue(self):
        if self.empty():
            return None
        
        value = self.head.data
        self.tail = self.tail.next
        self.len -= 1
        return value
    
    def empty(self):
        return self.tail == self.head and self.len == 0
    
    def size(self):
        return self.len
    
    def full(self):
        return self.head.next == self.tail and self.len != 0