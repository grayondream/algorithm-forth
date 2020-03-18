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
            if pre is not None:
                pre.next = root
                
            root.pre = pre
            pre = root
            thread_tree_node.in_threading(root.right, pre)
            
    @staticmethod
    def in_threading_no(root):
        '''
        @brief  中序线索化非递归版本
        '''
        if root is None:
            reutrn 
        else:
            stk = stack.stack()
            index = root
            pre = None
            while not stk.empty() or index is not None:
                while index is not None:
                    stk.push(index)
                    index = index.left
                
                index = index.top()
                stk.pop()
                index.pre = pre
                if pre is not None:
                    pre.next = index
                
                index = index.right
        
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
    def pre_threading_no(root):
        '''
        @brief  先序线索化
        '''
        if root is not None:
            return 
        else:
            pre = None
            stk = stack.stack()
            index = root
            while index is not None and not stk.empty():
                while index is not None:
                    if pre is not None:
                        pre.next = root
                        root.pre = pre
                    
                    stk.push(index)
                    index = index.left
                
                if not stk.empty():
                    index = stk.top()
                    stk.pop()
                    index = index.right
                    
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
            
    @staticmethod
    def post_threading_no(root, visit_func):
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
                
        pre = None
        while not snd.empty():
            root = snd.top();
            if pre is not None:
                pre.next = root
                
            root.pre = pre
                
            snd.pop()
            visit_func(root)
        