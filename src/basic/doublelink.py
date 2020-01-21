class double_node(object):
    '''
    @brief  双向单链表
    @param  pre last node
    @param  next    next node
    @param  data
    '''
    def __init__(self, pre=None, nex=None, dat=None):
        self.pre = pre
        self.next = nex
        self.data = dat
        
    @staticmethod
    def insert_head(self, head, node):
        '''
        @brief  在表头插入节点
        @param  head    要插入的链表
        @param  node    要插入的节点
        '''
        node.next = head
        head.pre = node
        head = node
        return head
    
    @staticmethod
    def insert_tail(self, head, node):
        '''
        @brief  在表尾插入节点
        @param  head    要插入的链表
        @param  node    要插入的节点
        '''
        # 找到表尾节点
        tail = head
        while tail.next is not None:
            tail = tail.next
            
        node.pre = tail
        tail.next = node
        return head
    
    @staticmethod
    def remove_head(self, head):
        '''
        @brief  删除头结点
        @param  head    链表头部
        '''
        tmp = head
        head = head.next
        del tmp
        return head

    @staticmethod
    def remove_tail(self, head):
        '''
        @brief  删除尾节点
        @param  head    链表头结点
        '''
        tail = head
        while tail.next is not None:
            tail = tail.next
        
        tmp = tail
        tail = tail.pre
        del tmp
        tail.next = None
        return head

    @staticmethod
    def insert_before(self, head, node):
        '''
        @brief  在指定节点head之前插入节点
        @param  head    要插入的节点位置
        @param  node    插入的节点
        '''
        if head.pre is None:
            node.head = head
            head.pre = node
            head = node
        else:
            node.next = head
            node.pre = head.pre
            head.pre.next = node
            head.pre = node
            
        return head
                
    @staticmethod
    def insert_after(self, head, node):
        '''
        @brief  在指定节点head之后插入节点
        @param  head    要插入的节点位置
        @param  node    插入的节点
        '''
        if head.next is None:
            head.next = node
            node.pre = head
        else:
            node.next = head.next
            node.pre = head
            head.next.pre = node
            head.next = node
        
        return head
    
    @staticmethod
    def remove(self, node):
        '''
        @brief  删除指定节点
        @param  node    要删除的节点
        '''
        node.next.pre = node.pre
        node.pre.next = node.next
        return node