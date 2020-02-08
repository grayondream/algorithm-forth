from src.basic import linklist, tree
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
        
        
class search_tree_st(tree.tree_node):
    '''
    @brief  用二叉查找树实现符号表
    '''
    def __init__(self, key, value, nodes):
        super(search_tree, self).__init__()
        self.nodes = nodes
        self.key = key
        self.value = value
        
    def get_nodes(self, node):
        if None is node:
            return 0
        else:
            return node.nodes
            
    def size(self):
        return self.get_nodes(self)
        
    @staticmethod
    def get(self, node, key):
        '''
        @brief  根据键值返回value
        '''
        if node == None:
            return None
            
        if node.key == key:
            return node.value
        elif node.key < key:
            return self.get(node.right, key)
        else:
            return self.get(node.left, key)
        
    @staticmethod
    def put(self, node, key, value):
        if None is node:
            return search_bin_st(key, value, 1)
        
        if node.key < key:
            self.right = self.put(self.right, key, value)
        elif node.key > key:
            self.left = self.put(self.left, key, value)
        
        node.nodes = self.get_nodes(node.left) + self.get_nodes(node.right) + 1
        return node
            
    @staticmethod
    def min(self, node):
        if node.left is None:
            return node
        else:
            return self.min(node)
            
    def floor(self, node, key):
        '''
        @brief  类似于数字的floor计算方式
        '''
        if key < node.key:
            return self.floor(node.left, key)
        elif key == node.key:
            return node
        
        ret = floor(node.right, key)
        if None is ret:
            return ret
        else:
            return node
            
    def select(self, node, k):
        '''
        @brief  返回排名为k的节点
        '''
        if node is None:
            return None
            
        ret = self.size(node.left)
        if ret < k:
            return select(node.right, k - ret - 1)
        elif ret > k:
            return select(node.left, k)
        else:
            return node
            
    def rank(self, node, key):
        '''
        @brief  返回以node为root的树中小于key键的数量
        '''
        if node is None:
            return 0
        
        if key < node.key:
            return self.rank(node.left, key)
        elif key > node.key:
            return 1 + self.size(node.left) + self.size(node.right) + self.rank(node.right, key)
        else:
            return self.size(node.left)
            
    def delete_min(self, node):
        '''
        @brief  删除树中的最小键值node
        '''
        if node is None:
            return node.right
        
        node.left = self.delete_min(node.left)
        node.nodes = self.size(node.left) + self.size(node.right) + 1
        return node
        
    def delete(self, node, key):
        '''
        @brief 删除键值为key的node
        '''
        if node is None:
            return None
        elif key < node.key:
            x.left = self.delete(node.left, key)
        elif key > node.key:
            x.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.left
                
            if node.right is None:
                return node.right
                
            tmp = node
            node = self.min(node.right)
            node.right = self.delete_min(tmp.right)
            node.left = tmp.left
            
        node.nodes = self.size(node.left) + self.size(node.right) + 1
        return node
        
    class search_ttree_st(tree.thread_tree_node):
    '''
    @brief  用线索二叉查找树实现符号表
    '''
    def __init__(self, key, value, nodes):
        super(search_ttree_st, self).__init__()
        self.nodes = nodes
        self.key = key
        self.value = value
        
    def get_nodes(self, node):
        if None is node:
            return 0
        else:
            return node.nodes
            
    def size(self):
        return self.get_nodes(self)
        
    @staticmethod
    def get(self, node, key):
        '''
        @brief  根据键值返回value
        '''
        if node == None:
            return None
            
        if node.key == key:
            return node.value
        elif node.key < key:
            return self.get(node.right, key)
        else:
            return self.get(node.left, key)
        
    @staticmethod
    def put(self, node, key, value):
        if None is node:
            return search_bin_st(key, value, 1)
        
        if node.key < key:
            self.right = self.put(self.right, key, value)
        elif node.key > key:
            self.left = self.put(self.left, key, value)
        
        node.nodes = self.get_nodes(node.left) + self.get_nodes(node.right) + 1
        return node
            
    @staticmethod
    def min(self, node):
        if node.left is None:
            return node
        else:
            return self.min(node)
            
    def floor(self, node, key):
        '''
        @brief  类似于数字的floor计算方式
        '''
        if key < node.key:
            return self.floor(node.left, key)
        elif key == node.key:
            return node
        
        ret = floor(node.right, key)
        if None is ret:
            return ret
        else:
            return node
            
    def select(self, node, k):
        '''
        @brief  返回排名为k的节点
        '''
        if node is None:
            return None
            
        ret = self.size(node.left)
        if ret < k:
            return select(node.right, k - ret - 1)
        elif ret > k:
            return select(node.left, k)
        else:
            return node
            
    def rank(self, node, key):
        '''
        @brief  返回以node为root的树中小于key键的数量
        '''
        if node is None:
            return 0
        
        if key < node.key:
            return self.rank(node.left, key)
        elif key > node.key:
            return 1 + self.size(node.left) + self.size(node.right) + self.rank(node.right, key)
        else:
            return self.size(node.left)
            
    def delete_min(self, node):
        '''
        @brief  删除树中的最小键值node
        '''
        if node is None:
            return node.right
        
        node.left = self.delete_min(node.left)
        node.nodes = self.size(node.left) + self.size(node.right) + 1
        return node
        
    def delete(self, node, key):
        '''
        @brief 删除键值为key的node
        '''
        if node is None:
            return None
        elif key < node.key:
            x.left = self.delete(node.left, key)
        elif key > node.key:
            x.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.left
                
            if node.right is None:
                return node.right
                
            tmp = node
            node = self.min(node.right)
            node.right = self.delete_min(tmp.right)
            node.left = tmp.left
            
        node.nodes = self.size(node.left) + self.size(node.right) + 1
        return node
        
    @staticmethod
    def in_thread(root, node, pre):
        '''
        @brief  对node进行线索化
        '''
        if root is None:
            return
        else:
            search_ttree_st.in_thread(root.left, node, pre)
            if root == node or pre == node:
                pre = root
                pre.next = root
                root.pre = pre
            
            search_ttree_st.in_thread(root.left, node, pre)