'''
堆相关的定义
'''
import abc


def swim(l, left, right, k):
    '''
    @brief  l       当前进行上浮的列表[left, right)
    @param  left    当前元素的左边界,left处的元素为根
    @param  right   当前元素的右边界
    @param  k       当前进行上浮的元素
    @note   上浮从下到上
    '''
    
def sink(l, left, right, k):
    '''
    @brief  l       当前进行上浮的列表[left, right)
    @param  left    当前元素的左边界，left处的元素为根
    @param  right   当前元素的右边界
    @param  k       当前进行进行上浮的元素
    @note   从上到下
    '''
    
    
class max_queue(abc.ABCMeta):
    '''
    @brief  无序数组优先队列
    '''
    def __init__(self, size=None, data=None):
        '''
        @brief  创建一个优先队列
        @param  size    新建的优先队列的尺寸
        @param  data    使用数据data构建优先队列，如果已经提供size则不再检查是否提供data
        '''
        super(max_queue, self).__init__()
        
    @abc.abstractmethod
    def insert(self, item):
        '''
        @brief  插入元素
        @param  item    需要插入的元素
        '''
    
    @abc.abstractmethod
    def max(self):
        '''
        @breif  返回最大的元素
        @return 当前队列中的最大值
        '''
        
    @abc.abstractmethod
    def pop_max(self):
        '''
        @brief  返回并删除最大值
        @return 当i去哪队列中的最大值
        '''
        
    @abc.abstractmethod
    def empty(self):
        '''
        @brief  判断当前队列是不是空
        '''
        
    @abc.abstractmethod
    def size(self):
        '''
        @brief  返回队列的尺寸
        @return size
        '''
        

class max_queue_unorder(max_queue):
    '''
    @brief  使用无序的数组构建优先队列
    '''
    def __init__(self, size=None, data=None):
        super(max_queue_unorder, self).__init__()
        
        
class max_queue_order(max_queue):
    '''
    @brief  使用有序的数组构建优先队列
    '''
    def __init__(self, size=None, data=None):
        super(max_queue_order, self).__init__()
        
    
class max_queue_unorder_link(max_queue):
    '''
    @brief  使用无序的链表构建优先队列
    '''
    def __init__(self, size=None, data=None):
        super(max_queue_unorder_link, self).__init__()
        
    
class max_queue_order_link(max_queue):
    '''
    @brief  使用有序的链表构建优先队列
    '''
    def __init__(self, size=None, data=None):
        super(max_queue_order_link, self).__init__()
        