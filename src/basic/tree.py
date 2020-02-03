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
    