'''
线性探测法hash表
'''

class hash_array(object):
    '''
    @brief  使用-1表示元素未找到
    '''
    def __init__(self, size):
        super().__init__()
        self.list = [-1] * size
        self.len = 0
        
    def insert(self, key):
        i = hash_array.hash_code(key)
        while self.list[i] != -1:
            i = hash_array.hash_code(i + 1, len(self.list))
            
        self.list[i] = key
        self.len += 1
        
    def find(self, key):
        i = hash_array.hash_code(key)
        while self.list[i] != -1 and self.list[i] != key:
            i = hash_array.hash_code(i + 1, len(self.list))
            
        if self.list[i] == -1:
            return -1
            
        return i
        
    def delete(self, key):
        '''
        @brief  因为线性探测法的原因删除某个元素会导致之后的元素无法访问因此需要将右边的元素重新插入保证hash表的有效性
        '''
        i = self.find(key)
        if i == -1:
            return
        else:
            self.list[i] = -1
            i = hash_array(i + 1, len(self.list))
            while self.list[i] != -1:
                key = self.list[i]
                self.list[i] = -1
                self.insert(key)
                i = hash_array(i + 1, len(self.list))
                
        self.len -= 1
            
    def keys(self):
        ret = []
        for i in range(len(self.list)):
            if self.list[i] != -1:
                ret.append(self.list[i])
                
        return ret
        
    
    @staticmethod
    def hash_code(key, size):
        return key % size
        
    def full(self):
        return self.len == len(self.list)
        
    def size():
        return self.len