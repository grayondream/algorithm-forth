from src.basic import queue


class node(object):
    def __init__(self, val=None, r=256):
        self.val = val
        self.nodes = [None] * r


class string_st(object):
    '''
    @brief  单词查找树
    '''
    def __init__(self):
        self.root = node(None, 256)
    
    def put(self, root, key, val, d):
        if root is None:
            return node()
        if d == len(key):
            root.val = val
            return root
        
        root.next[key[d]] = self.put(root.next[key[d]], key, val, d + 1)
        
    
    def get(self, root, key, d):
        '''
        @brief  从单词查找树中查找元素
        @param  root    进行查找的节点
        @param  key 需要进行查找的字符串
        @param  d   查找的深度
        '''
        if root is None:
            return None
        
        if d == len(key):
            return root
        
        return self.get(root.nodes[key[d]], key, d + 1)
    
    def contain(self, key):
        cur_node = self.get(self.root, key,  0)
        return cur_node is not None
        
    def empty(self):
        for cur_node in self.root.nodes:
            if cur_node is not None:
                return False
                
        return True
        
    def longest_prefix(self, line):
        pass
        
    def key_match(self, pat):
        q = queue.queue()
        self.match_collect(self.root, "", pat, q)
        return q
            
    def match_collect(self, root, pre, pt, q):
        d = len(pre)
        if root is None:
            return
        
        if d == len(pt) and root.val is not None:
            q.enqueue(pre)
            
        if d == len(pt):
            return
            
        for i in range(len(root.nodes)):
            if pat[d] == '.' or pat[d] == i:
                self.match_collect(root.nodes[i], pre + i, pt, q)
                
    def size(self, root):
        if root is None:
            return 0
            
        cnt = 0
        for cur in root.nodes:
            cnt += self.size(cur)
        
        return cnt
        
    def get_keys(self):
        return self.keys_with_prefix("")
        
    def collect(self, root, pre, q):
        '''
        @param  root    搜索开始的节点
        @param  pre     前缀
        @param  q       队列
        '''
        if root is None:
            return
        
        if root.val is None:
            q.enqueue(pre)
            
        for c in range(len(root.nodes)):
            self.collect(root.nodes[c], pre + str(c), q)
        
    def keys_with_prefix(self, pre):
        root = self.get(self.root, pre, 0)
        q = queue.queue()
        self.collect(root, pre, q)
        return q
        
    def longest_pre(self, key):
        return key[0: self.search(self.root, key, 0, 0)]
        
    def search(self, root, key, d, cur_len):
        if root is None:
            return cur_len
        
        if root.val is not None:
            cur_len = d
        
        if d == len(key):
            return cur_len
        
        return self.search(root.nodes[key[d]], key, d+1, cur_len)
        
    def delete(self, root, key, d=0):
        if root is None:
            return None
        if d == len(key):
            root.val = None
        else:
            root.next[key[d]] = self.delete(root.next[key[d]], key, d + 1)
            
        if root.val is not None:
            return root
        
        for i in range(len(root.nodes)):
            if root.next[i] is not None:
                return root
                
        return None
        

class tst_node:
    def __init__(self, val=None, ch=None, right=None, left=None, mid=None):
        self.val = val
        self.left = left
        self.right = right
        self.mid = mid
        self.ch = ch
        
    
class tst:
    '''
    @brief  三向单词查找树
    '''
    def __init__():
        pass
        
    def get(self, root, key, d):
        if root is None:
            return None
            
        cur_ch = key[d]
        if cur_ch < root.ch:
            return self.get(root.left, key, d)
        elif cur_ch > root.ch:
            return self.get(root.right, key, d)
        elif d < len(key) - 1:
            return self.get(root.mid, key, d + 1)
        else:
            return root
        
    def put(self, root, key, val, d):
        ch = key[d]
        if root is None:
            root = tst_node(ch=ch)
        elif ch < root.ch:
            root.left = self.put(root.left, key, val, d)
        elif ch > root.ch:
            root.right = self.put(root.right, key, val, d)
        else:
            root.val = val
            
        return root
    
    