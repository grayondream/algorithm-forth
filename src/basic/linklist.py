import os
#链表的实现，暂时只有数据定义没有具体的内容

class linklist(object):
    def __init(self, data = None, next = None):
        super(linklist, self).__init__()
        self.data = data
        self.next = next

    @staticmethod
    def find(self, head, value):
        '''
        @brief  在链表head中查找value，如果不存在返回None，存在则返回节点的上一个节点，如果为表头则返回head
        '''
        if head.data == value:
            return head
        else
            cur = head
            while cur.next is not None:
                if cur.next.data == value:
                    return cur
                cur = cur.next
        
        return None
        
def main():
    pass
if __name__ == '__main__':
    main()