'''
红黑树
'''
red = True
black = False

class rbtree(object):
    '''
    @brief  每个节点只有一个边是red
    @note   TODO
    '''
    def __init__(self, key, left, right, color):
        super(rbtree, self).__init__()
        self.left = left
        self.right = right
        self.color = color
        self.key = key
        
    @staticmethod
    def is_red(node):
        if node is None:
            return False
        else:
            return red == node.color
            
    @staticmethod
    def rotate_left(node):
        '''
        @breif  左旋
        '''
        root = node.right
        node.right = root.left
        root.left = node
        
        root.color = node.color
        node.color = red
        
        return root
        
    @staticmethod
    def rotate_right(node):
        '''
        @brief  右旋
        '''
        root = node.left
        node.left = root.right
        root.rght = node
        
        root.color = node.color
        node.color = red
        return root
        
    @staticmethod
    def flip_color(node):
        '''
        @brief  将父节点设为red，子节点设为black
        '''
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color
        return node
        
    @staticmethod
    def put(node, key):
        '''
        @brief  向树种插入节点
        @note   基本分为三种情况    1 插入后导致root的两个节点为red
                                   2 插入后导致root的左节点为black，右节点为red
                                   3 插入后导致左节点和其左节点都为red
        '''
        if node is None:
            return rbtree(key, None, None, red)
        
        if key < node.key:
            node.left = rbtree.put(node.left, key)
        else:
            node.right = rbtree.put(node.right, key)
            
        if rbtree.is_red(node.left) and rbtree.is_red(node.right):
            node = rbtree.flip_color(node)
        elif rbtree.is_red(node.left) and rbtree.is_red(node.left.left):
            node = rbtree.rotate_right(node)
        elif rbtree.is_red(node.right) and not rbtree.is_red(node.left):
            node = rbtree.rotate_left(node)
            
        return node
    
    @staticmethod
    def insert(root, key):
        root = rbtree.put(root,key)
        root.color = black
        
    @staticmethod
    def move_red_left(node):
        '''
        @brief  处理2结点
        '''
        node = rbtree.flip_color(node)
        if rbtree.is_red(node.right.left):  #当前结点并不是三个2结点，右结点是一个3结点
            node.right = rbtree.rotate_right(node.right)
            node = rbtree.rotate_left(node)
            node = rbtree.flip_color(node)
        
        return node
        
    @staticmethod
    def del_min(root):
        '''
        @brief  删除红黑树中的最小值
        @param  root    红黑树的根结点
        '''
        if not rbtree.is_red(root.left) and not rbtree.is_red(root.right):
            root.color = red;
        
        root = rbtree.del_min_node(root)
        if root is not None:
            root.color = black
            
    @staticmethod
    def del_min_node(node):
        '''
        @brief 
        '''
        if root.left is None:
            return None
            
        if not rbtree.is_red(node.left) and not rbtree.is_red(node.left.left):
            #只会对2结点进行变换处理
            node = rbtree.move_red_left(node)
            
        node.left = rbtree.del_min_node(node.left)
        return rbtree.balance(node)
        
    @staticmethod
    def balance(node):
        '''
        @brief 进行颜色平衡，将临时的4结点分解
        @param  node    需要进行调整的结点过程基本和插入操作中的颜色转换完全相同
        '''
        if rbtree.is_red(node.right):
            node = rbtree.rotate_left(node)
        
        if rbtree.is_red(node.right) and not rbtree.is_red(node.left):
            node = rbtree.rotate_left(node)
            
        if rbtree.is_red(node.left) and rbtree.is_red(node.left.left):
            node = rbtree.rotate_right(node)
            
        if rbtree.is_red(node.left) and rbtree.is_red(node.right):
            rbtree.flip_color(node)
            
        return node
        
    @staticmethod
    def move_red_right(node):
        rbtree.flip_color(node)
        if rbtree.is_red(node.left.left):
            node = rbtree.rotate_right(node)
            node = rbtree.flip_color(node)
            
        return node
        
    @staticmethod
    def del_max_node(node):
        if rbtree.is_red(node.left):
            node = rbtree.rotate_right(node)
        
        if node.right is None:
            return None
            
        if not rbtree.is_red(node.right) and not rbtree.is_red(node.right.left):
            node = rbtree.move_red_right(node)
        
        node.right = rbtree.del_max_node(node.right)
        return rbtree.balance(node)
        
    @staticmethod
    def del_max(root):
        if not rbtree.is_red(root.right) and not rbtree.is_red(root.left):
            root.color = red
            
        root = rbtree.del_max_node(root)
        if root is not None:
            root.color = black
    
    @staticmethod
    def min(node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        
        return node
        
    @staticmethod
    def delete_node(node, key):
        if key < node.key:
            if not rbtree.is_red(node.left) and not rbtree.is_red(node.left.left):
                node = rbtree.move_red_left(node)
            
            node.left = rbtree.delete_node(node.left, key)
        else:
            if rbtree.is_red(node.left):
                node = rbtree.rotate_right(node)
            
            #删除的结点是底部
            if key == node.key and node.right is None:
                return None
            
            if not rbtree.is_red(node.right) and not rbtree.is_red(node.right.left):
                node = rbtree.move_red_right(node)
            
            #将当前树最小值和当前结点交换删除最小值即可
            if key == node.key:
                node.key = rbtree.min(node.right).key
                node.right = rbtree.del_min(node.right)
            else:
                node.right = rbtree.delete_node(node.right, key)
    
        return rbtree.balance(node)
        
        
    @staticmethod
    def delete(root, key):
        if not rbtree.is_red(root.right) and not rbtree.is_red(root.left):
            root.color = red
        
        root = rbtree.delete_node(root, key)
        if root is not None:
            root.color = black
        
        
        
        
        
        
        
        