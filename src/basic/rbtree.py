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
        node.color = red
        node.left.color = black
        node.right.color = black
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
        elif rbtree.is_red(node.left) and rbtree.is_red(node.lef.left):
            node = rbtree.rotate_right(node)
        elif rbtree.is_red(node.right) and rbtree.is_red(node.left):
            node = rbtree.rotate_left(node)
            
        return node
    
    @staticmethod
    def insert(root, key):
        root = rbtree.put(root,key)
        root.color = black
        
        
        
        
        
        
        
        
        
        
        
        