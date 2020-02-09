'''
拉链法hash
'''
from src.basic import linklist


class hash_link(object):
    def __init__(self, size):
        '''
        @param  size    散列表大小
        '''
        super().__init__()
        self.list = [linklist.linklist()] * size
        
    @staticmethod
    def hash_code(key, size):
        return key % size
        
    def insert(self, key):
        linklist.linklist.insert_front(self.list[hash_link.hash_code(key)], key)
        
    def find(self, key):
        linklist.linklist.find(self.list[hash_link.hash_code(key)], key)
    
    def delete(self):
        linklist.linklist.delete_front(self.list[hash_link.hash_code((key))], key)
        
    def keys(self):
        ret = []
        for i in range(len(self.list)):
            node = self.list[i]
            while node is not None:
                ret.append(node.data)
                node = node.next
                
        return ret
                