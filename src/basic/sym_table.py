from src.basic import linklist
from src.search import binary_search


'''
@brief  符号表相关定义
'''

class sym_table(object):
    '''
    @brief  符号表接口定义,符号变每个key只对应一个value，当插入的key已经存在时会使用新的value替换该key旧的value，不允许出现None
    '''
    def __init__(self):
        super(sym_table, self).__init__()
        
    def put(self, key, value):
        pass
        
    def get(self, key):
        pass
        
    def delete(self, key):
        pass
        
    def contains(self, key):
        pass
        
    def empty(self):
        pass
        
    def size(self):
        pass
        
    def get_keys(self):
        pass
        
        
class array_st(sym_table):
    '''
    @brief  使用无序数组实现符号表
    '''
    def __init__(self):
        super(array_st, self).__init__()
        self.keys = []
        self.values = []
        
    def find(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return i
        
        return None
        
    def put(self, key, value):
        index = self.find(key)
        if index is None:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[index] = value
            
    
    def get(self, key):
        i = self.find(key)
        if i is not None:
            return self.values[i]
        
        return None
        
    def delete(self, key):
        index = self.get(key)
        if index is not None:
            del self.keys[index]
            del self.values[index]
        
    def contains(self, key):
        return None != self.find(key)
        
    def empty(self):
        return 0 == self.size()
        
    def size(self):
        return len(self.keys)
        
    def get_keys(self):
        return self.keys
        
        
class link_st(object):
    '''
    @brief  用链表实现，每个item的第一个为key，第二个位value
    '''
    def __init__(self):
        super(link_st, self).__init__()
        self.head = linklist.linklist(None, None)
        self.len = 0
        
    def find(self):
        i = self.head
        while i.next is not None:
            if i.next.data[0] == key:
                return i
                
            i = i.next
            
        return i
        
    def put(self, key, value):
        i = self.find(key)
        if i.next is None:
            item = linklist.linklist([key, value], None)
            i.next = item
            self.len += 1
        else:
            i.next.data[1] = value
            
    def get(self, key):
        i = self.find(key)
        if i.next is not None
            return i.next.data[1]
            
        return None
        
    def delete(self, key):
        i = self.find(key)
        if i.next is not None
            item = i.next
            i.next = i.next.next
            del dict_items
            self.len -= 1
            
    def contains(self, key):
        i = self.find(key)
        return i.next != None
        
    def empty(self):
        return 0 == self.size()
        
    def size(self):
        return self.len
        
    def get_keys(self):
        keys = []
        i = self.head.next
        while None is not i:
            keys.append(i.data[0])
            i = i.next
        
        return keys
        

class sorted_array_st(object):
    '''
    @brief  使用有序数组实现
    '''
    def __init__(self):
        super(sorted_array_st, self).__init__()
        self.keys = []
        self.values = []
        
    def find(self, key):
        i = binary_search.binary_search(self.keys, 0, len(self.keys) - 1, key)
        return i if i == -1 None
        
    def put(self, key, value):
        i = self.find(key)
        if i is not None:
            self.values[i] = value
        else:
            self.keys.append(key)
            self.values.append(value)
            i = len(self.keys) - 1
            while i > 0 and self.keys[i] < self.keys[i - 1]:
                self.keys[i - 1], self.keys[i] = self.keys[i], self.keys[i - 1]
        
    def get(self, key):
        i = self.find(key)
        return self.values[i] if i is None None
        
    def delete(self, key):
        i = self.find(key)
        if None is not i:
            del self.keys[i]
            del self.values[i]
        
    def contains(self, key):
        i = self.find(key)
        return None != i
        
    def empty(self):
        return 0 == self.size()
        
    def size(self):
        return len(self.keys)
        
    def get_keys(self):
        return self.keys
        
        
class txt_frequence(object):
    '''
    @brief  建立小说中单词的词频关系，假定单词用空格划分
    '''
    def __init__(self, filename):
        super(txt_frequence, self).__init__()
        self.word = []
        self.word_fre = []
        self.load(filename)
        
    def load(self, filename):
        with open(filename, 'r') as f:
            self.words = f.readlines().split(' ')
            self.word_fre = [0] * len(self.words) 
        
        self.adjust()
        
    def adjust(self):
        '''
        @brief  调整词频关系
        '''
        self.wrods.sort()  
        count = 0
        j = 0
        for i in range(1, len(self.words)):
            if self.words[i - 1] == self.words[i]:
                count += 1
                self.values[j] += 1 
            else:
                j += 1
                
            self.words[i - 1] = self.words[i + count - 1]
            
        self.words = self.words[:-count]
        self.word_fre = self.word_fre[:-count]
        

class auto_array_st(sym_table):
    '''
    @brief  使用无序数组实现自组织符号表，每次访问之后将高频访问的元素放置到开头
    '''
    def __init__(self):
        super(array_st, self).__init__()
        self.keys = []
        self.values = []
        
    def find(self, key):
        for i in range(len(self.keys):
            if self.keys[i] == key:
                break
        
        if i <= len(self.keys):
            self.keys[0], self.keys[i] = self.keys[i], self.keys[0]
            self.value[0], self.values[i] = self.values[i], self.values[0]
            return 0
            
        return None
        
    def put(self, key, value):
        index = self.find(key)
        if index is None:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[index] = value
            
    
    def get(self, key):
        i = self.find(key)
        if i is not None:
            return self.values[i]
        
        return None
        
    def delete(self, key):
        index = self.get(key)
        if index is not None:
            del self.keys[index]
            del self.values[index]
        
    def contains(self, key):
        return None != self.find(key)
        
    def empty(self):
        return 0 == self.size()
        
    def size(self):
        return len(self.keys)
        
    def get_keys(self):
        return self.keys