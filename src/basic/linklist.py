import os
#链表的实现，暂时只有数据定义没有具体的内容

class linklist(object):
    def __init(self, data = None, next = None):
        super(linklist, self).__init__()
        self.data = data
        self.next = next

    @staticmethod
    def find(head, value):
        '''
        @brief  在链表head中查找value，如果不存在返回None，存在则返回节点的上一个节点，如果为表头则返回head
        '''
        if head.data == value:
            return head
        else:
            cur = head
            while cur.next is not None:
                if cur.next.data == value:
                    return cur
                cur = cur.next
        
        return None
    
    @staticmethod
    def insert_end(head, value):
        '''
        @brief  想链表的结尾插入元素
        '''
        index = head
        while index.next is not None:
            index = index.next
            
        new_node = linklist(value, None)
        index.next = new_node
        
    @staticmethod
    def insert_front(head, value):
        '''
        @brief  向链表的开头插入元素
        '''
        new_node = linklist(value, head.next)
        head.next = new_node
    
    @staticmethod
    def delete_front(head):
        head.next = head.next.next
        return head
    
    @staticmethod
    def delete_end(head):
        index = head
        if head.next.next is None:
            head.next = None
            return head
        else:
            index = head
            while index.next.next is not None:
                index = index.next
                
            index.next.next = None
        
        return head
        
def main():
    pass
if __name__ == '__main__':
    main()