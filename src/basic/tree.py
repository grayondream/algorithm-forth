from src.basic import queue


'''
树结构的实现
'''


class tree_node(object):
    '''
    @brief  二叉树结构
    '''
    def __init__(self, left, right):
        super(tree_node, self).__init__()
        self.left = left
        self.right = right
    

class thread_tree_node(tree_node):
    '''
    @brief  线索二叉树实现
    '''
    def __init__(self, left, right):
        super(thread_tree_node, self).__init__(left, right)
        self.pre = None
        self.next = None
        
    @staticmethod
    def in_threading(root, pre):
        '''
        @brief  中序线索化
        '''
        if root is None:
            return
        else:
            thread_tree_node.in_threading(root.left, pre)
            pre.next = root
            root.pre = pre
            pre = root
            thread_tree_node.in_threading(root.right, pre)
            
    @staticmethod
    def pre_threading(root, pre):
        '''
        @brief  前序线索化
        '''
        if root is None:
            return
        else:
            pre.next = root
            root.pre = pre
            pre = root
        
            thread_tree_node.pre_threading(root.left , pre)
            thread_tree_node.pre_threading(root.right, pre)
            
    @staticmethod
    def post_threading(root, pre):
        '''
        @brief  后序线索化
        '''
        if root is None:
            return
        else:
            thread_tree_node.post_threading(root.left, pre)
            thread_tree_node.post_threading(root.right, pre)
            pre.next = root
            root.pre = pre
            pre = root
    
    
def traverse_level(root, func):
    '''
    @brief  层序遍历
    @param  root    根节点
    @param  func    访问函数    func(node)
    '''
    q = queue.queue()
    q.enqueue(root)
    while not q.empty():
        root = q.dequeue()
        func(root)
        if root.left is not None:
            q.enqueue(root.left)
            
        if root.right is not None:
            q.enqueue(root.right)


def is_binary_tree(root, visited):
    '''
    @brief  判断树是不是二叉树
    @param  visited 访问字典
    '''
    if root is None:
        return True
    else:
        try:
            if visited[root] is True:
                return False
        except:
            visited[root] = True
        return is_binary_tree(root.left) and is_binary_tree(root.right)
        
        
