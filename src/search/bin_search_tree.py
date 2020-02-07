from src.basic import tree, queue, stack


class bi_search_tree(tree.tree_node):
    '''
    @brief  二叉查找树
    '''
    def __init__(self, key, value, nodes):
        super(search_tree, self).__init__()
        self.nodes = nodes
        self.key = key
        
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
    def depth(self, node):
        if node is None:
            return 0
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1
            
        
class bi_search_tree_II(tree.tree_node):
    '''
    @brief  使用非递归的方式实现二叉查找树中的各种算法
    '''
    def __init__(self, left, right, key):
        super(bi_search_tree_II, self).__init__(left, right)
        self.key = key    
    
    def depth(self, node):
        q = queue.queue()
        height = 0

        q.enqueue(node)
        while q.empty():
            node = q.dequeue()
            if node.left is not None:
                q.enqueue(node.left)
            
            if node.right is not None:
                q.enqueue(node.right)
                
            height += 1
        
        return height
        
    def min(self, node):
        '''
        @brief  返回node中的最小node
        '''
        while node.left is not None:
            node = node.left
            
        return node
        
    def max(self, node):
        '''
        @brief  返回node中的最大node
        '''
        while node.right is not None:
            node = node.right
            
        return node
        
    def floor(self, node, key)：
        parent = node
        child = node
        if child.key == key:
            return child
        elif child.key < key:
            child = parent.right
        else:
            child = parent.left
            
        while child is not None:
            parent = child
            if parent.key < key and child.key > key:
                return parent
            elif parent.key > key and child.key < key:
                return child
            elif child.key == key:
                return child
            elif child.key < key:
                child = parent.right
            else:
                child = parent.left
                
        if parent.key < key:
            return parent
        else:
            return None
            
            
    def select(self, node, k):
        '''
        @brief 返回排名为k的节点
        @note   使用中序遍历的思路
        '''
        stk = stack.stack()
        while not stk.empty() and node is None and k != 0:
            while node is not None:
                stk.push(node)
                node = node.left
                
            if not stk.empty():
                node = stk.pop()
                k -= 1
                    
                node = node.right
            
        return node
        
        
    def rank(self, node, key):
        '''
        @brief  返回node中的子树种小于key键的数量
        '''
        stk = stack.stack()
        no = 0
        while not stk.empty() and node is None:
            while node is not None:
                stk.push(node)
                node = node.left
                
            if not stk.empty():
                node = stk.pop()
                if node.key < key:
                    no += 1
                else:
                    return no
                    
                node = node.right
            
        return no
            
            