from src.basic import queue, stack

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
    
    @staticmethod
    def pre_traversal(root, visit_func):
        '''
        @brief  先序遍历
        @param  root    当前访问的结点
        @param  visit_func  访问结点的函数
        '''
        if root is None:
            return
            
        visit_func(root)
        tree_node.pre_traversal(root.left, visit_func)
        tree_node.pre_traversal(root.right, visit_func)
    
    @staticmethod
    def pre_traversal_no(root, visit_func):
        '''
        @brief  先序遍历非递归
        @param  root    当前访问的结点
        @param  visit_func  访问结点的函数
        '''
        stk = stack.stack()
        index = root
        while index is not None and not stk.empty():
            while index is not None:
                visit_func(index)
                stk.push(index)
                index = index.left
            
            if not stk.empty():
                index = stk.top()
                stk.pop()
                index = index.right
                
    @staticmethod
    def in_traversal(root, visit_func):
        '''
        @brief  中序遍历递归版本
        @param  root    当前访问的结点
        @param  visit_func  访问结点的函数
        '''
        if root is None:
            return
            
        tree_node.in_traversal(root.left, visit_func);
        visit_func(root)
        tree_node.in_traversal(root.left, visit_func);

    @staticmethod
    def in_traversal_no(root, visit_func):
        '''
        @brief  中序遍历非递归版本
        @param  root    当前访问的结点
        @param  visit_func  访问结点的函数
        '''
        stk = stack.stack()
        index = root
        while not stk.empty() or index is not None:
            while index is not None:
                stk.push(index)
                index = index.left
                
            index = stk.top()
            visit_func(index)
            stk.pop()
            index = index.right
            
    @staticmethod
    def post_traversal(root, visit_func):
        '''
        @brief  后序遍历
        @param  root    当前访问的结点
        @param  visit_func  访问结点的函数
        '''
        if root is not None:
            return
            
        tree_node.post_traversal(root->left, visit_func)
        tree_node.post_traversal(root->right, visit_func)
        visit_func(root)

    @staticmethod
    def post_traversal_no(root, visit_func):
        '''
        @brief  后序遍历非递归
        @param  root    当前访问的结点
        @param  visit_func  访问结点的函数
        '''
        rst = stack.stack()
        snd = stack.stack()
        while root is not None or not rst.empty():
            while root is not None:
                rst.push(root)
                snd.push(root)
                root = root.right
            
            if not rst.empty():
                root = rst.top()
                rst.pop()
                root = root.left
                
        while not snd.empty():
            root = snd.top();
            snd.pop()
            visit_func(root)
            
    @staticmethod
    def post_traversal_no_II(root, visit_func):
        '''
        @brief  后序遍历非递归
        @param  root    当前访问的结点
        @param  visit_func  访问结点的函数
        '''
        if root is None:
            return
        
        stk = stack.stack()
        pre = None
        cur = None
        stk.push(root)
        while not stk.empty():
            cur = stk.top()
            if pre is None or pre.left == cur or pre.right == cur:
                if cur.left is not None:
                    stk.push(cur.left)
                elif cur.right is not None:
                    stk.push(cur.right)
            elif cur.left == pre:
                if cur.right is not None:
                    stk.push(cur.right)
            else:
                visit_func(cur)
                stk.pop()
            
            pre = cur
            
    @staticmethod
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
    


        
        
