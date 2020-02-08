from src.basic import tree


'''
3.2.6   见src.search.bin_search_tree中bi_search_tree的定义
'''


'''
3.2.13-3.2.14   见src.search.bin_search_tree_II中的实现
'''

'''
3.2.21  见src.search.bin_search_tree_II中的random_key实现
'''

'''
3.2.29  见src.basic.tree中的is_binary_tree实现
'''


def is_ordered(root, min_value, max_value):
    ''' 
    @brief  3.2.30 判断root是否符合二叉查找树的结构，并且值域在[min_value, max_value]之间
    '''
    if root is None:
        return True
    else:
        if root.key < min_value or root.key > max_value:
            return False
        else:
            if root.left is not None and root.key < root.left.key:
                return False

            if root.right is not None and root.key > root.right.key:
                return False
                
            return is_ordered(root.left, min_value, max_value) and is_ordered(root.right, min_value, max_value)
            
            
def has_no_duplicates(root):
    '''
    @brief  3.2.31  判断二叉查找树中是否包含相等的键值，包含则False
    '''
    if root is None:
        return True
    else:
        if root.left is not None and root.key == root.left.key:
            return False

        if root.right is not None and root.key == root.right.key:
            return False
            
        return has_no_duplicates(root.left) and has_no_duplicates(root.right)
        
    
def is_bst(root, min_value, max_value):
    '''
    @brief  3.2.32 判断root是否为二叉查找树的根节点
    '''
    if not tree.is_binary_tree(root):
        return False
    
    if not is_ordered(root, min_value, max_value):
        return False
        
    if not has_no_duplicates:
        return False
        
    return True
    
    
'''
3.2.37  见src.basic.tree中的traverse_level实现
'''

class search_tree_array(object):
    '''
    @brief  使用数组开发二叉查找树的实现
    @note   TODO:unsolved
    '''
    def __init__(self):
        super().__init__()
        self.root = []
        self.lefts = []
        self.rights = []
     
        
        