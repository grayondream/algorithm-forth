'''
堆相关的定义，0处的元素为root
使用数组表示堆，parent的index为i，左孩子和右孩子的index分别为2*i+1,2*i+2，
同理左孩子的index为i，parent的index为floor((i-1)/2)
右孩子的index为i,parent的index为floor((i - 1)/2)
'''
import abc
from src.basic import linklist


def less(rst, snd):
    return rst < snd
    

def bigger(rst, snd):
    return rst > snd
    
    
def swim(l, start, end, k, com_func):
    '''
    @brief  l       当前进行上浮的列表[start, end]，区间内的元素应该以start为根节点构成一棵树
    @param  start    当前元素的左边界,start处的元素为根
    @param  end   当前元素的右边界
    @param  k       当前进行上浮的元素
    @param  com_func    比较函
    @note   上浮从下到上，大根堆, parent = floor((i-1)/2)，具体构造大根堆还是小根堆完全由用户指定的com_func确定，bigger为大根堆，less为小根堆
    '''
    parent = int((k - 1)/2)
    while k != start and com_func(l[parent], l[k]):
        l[parent], l[k] = l[k], l[parent]
        k = parent
        parent = int((k - 1)/2)
        
        
def swim_im(l, start, end, k, com_func):
    '''
    @brief  l       当前进行上浮的列表[start, end)
    @param  start    当前元素的左边界,start处的元素为根
    @param  end   当前元素的右边界
    @param  k       当前进行上浮的元素
    @param  com_func    比较函数
    @note   上浮从下到上 parent = floor((i-1)/2)，使用哨兵较少内存的访问
    '''
    parent = int((k - 1)/2)
    sent = l[k]
    while k != start and com_func(l[parent], l[k]):
        l[k] = l[parent]
        k = parent
        parent = int((k - 1)/2)
    
    l[k] = sent
        
        
def sink(l, start, end, k, com_func):
    '''
    @brief  l       当前进行下沉的列表[start, end]
    @param  start    当前元素的左边界，start处的元素为根
    @param  end   当前元素的右边界
    @param  k       当前进行进行下沉的元素
    @param  com_func    比较函数
    @note   从上到下,左孩子的index为2*i+1, 右孩子的index为2*i+2
    '''
    while k < end:
        left_child = 2 * k + 1
        right_child = 2 * k + 2
        i = left_child
        if com_func(l[right_child], l[left_child]):
            i = right_child
        
        if not com_func(l[k], l[i]):
            break
            
        l[i], l[k] = l[k], l[i]
        k = i
    

def sink_im(l, start, end, k, com_func):
    '''
    @brief  l       当前进行下沉的列表[start, end)
    @param  start    当前元素的左边界，start处的元素为根
    @param  end   当前元素的右边界
    @param  k       当前进行进行下沉的元素
    @note   从上到下，大根堆，左孩子的index为2*i+1, 右孩子的index为2*i+2,使用哨兵减少内存的访问
    '''
    sent = l[k]
    while k < end:
        left_child = 2 * k + 1
        right_child = 2 * k + 2
        i = left_child
        if  com_func(l[right_child], l[left_child]):
            i = right_child
        
        if not com_func(l[k], l[i]):
            break
        
        l[k] = [i]
        k = i
    
    l[k] = sent
    
    
def swim_nway(l, start, end, k, n, com_func):
    '''
    @brief  nway堆，堆的构造和普通堆相同，在进行元素交换时选择线性搜索找到的第一个元素，也可以采用binary_search，问题是如何组织元素
    @param  l   list
    @param  start
    @param  end
    @param  n   n-way
    @param  k   当前元素标签
    @param  com_func    比较函数
    @note   child   k   parent  floor((k - 1)/n)
    '''
    sent = l[k]
    parent = int((k-1)/n)
    while k != start and com_func(l[k], l[parent]):
        l[k] = l[parent]
        k = parent
        parent = int((k-1)/n)
        
    l[k] = sent
    
    
def sink_nway(l, start, end, k, n, com_func):
    '''
    @brief  nway堆，堆的构造和普通堆相同，在进行元素交换时选择线性搜索找到的第一个元素，也可以采用binary_search，问题是如何组织元素
    @param  l   list
    @param  start
    @param  end
    @param  n   n-way
    @param  k   当前元素下表
    @param  com_func    比较函数
    @note   parent  k   child   n*k+1~n*k+n
    '''
    def find_first_less(l, k, n):
        '''
        @brief  找到第一个不符合条件的当前元素l[k]的子结点的下标
        @param  l   list
        @param  k   当前元素的下表
        @param  n   n-way
        @return 第一个小于l[k]的index
        '''
        for i in range(1, n + 1):
            if not com_func(l[k], l[i]):
                return i
                
        return -1
    sent = l[k]
    child = find_first_less(l, k, n)
    while k < end and child != -1:
        l[child] = l[k]
        k = child
        child = find_first_less(l, k, n)
    
    l[k] = sent
    
    
def is_big_heap(l, start, end):
    '''
    @brief  判断是否为大根堆
    @param  l   list
    @param  start    根节点   
    @param  end   边界
    '''
    left_child = 2 * start + 1
    right_child = 2 * start + 2
    if left_child >= end and right_child >= end:
        return True
        
    if left_child >= end and l[right_child] > l[start]:
        return False
    
    if right_child >= end and l[left_child] > l[start]:
        return False
    
    if l[left_child] > l[start] or l[right_child] > l[start]:
        return False
        
    return is_big_heap(l, left_child, end) and is_big_heap(l, right_child, end)
    
    
def is_small_heap(l, start, end):
    '''
    @brief  判断是否为小根堆
    @param  l   list
    @param  start    
    @param  end
    '''
    left_child = 2 * start + 1
    right_child = 2 * start + 2
    if left_child >= end and right_child >= end:
        return True
        
    if left_child >= end and l[right_child] < l[start]:
        return False
    
    if right_child >= end and l[left_child] < l[start]:
        return False
    
    if l[left_child] < l[start] or l[right_child] < l[start]:
        return False
        
    return is_big_heap(l, left_child, end) and is_big_heap(l, right_child, end)
    
    
class max_queue(object):
    def __init__(self):
        super(max_queue, self).__init__()
        self.len = 0
        
    def insert(self, item):
        '''
        @brief  插入元素
        '''
    
    def max(self):
        '''
        @brief  返回最大值
        '''
        
    def pop_max(self):
        '''
        @brief  返回并且删除最大值    
        '''
        
    def empty(self):
        return 0 == self.len
        
    def size(self):
        return self.len
        
    
class max_queue_array(max_queue):
    '''
    @brief  数组类优先队列的abstract
    '''
    def __init__(self):
        super(max_queue_array, self).__init__()
        self.data = []
        
    def pop_max(self):
        '''
        @brief  -1处为max
        '''
        ret = self.max()
        del self.data[-1]
        return ret
        
    def size(self):
        return len(self.data)
        
    def min(self):
        pass
        

class max_queue_order(max_queue_array):
    '''
    @brief  有序数组的优先队列
    @note   每次插入元素时进行排序
    '''
    def __init__(self):
        super(max_queue_order, self).__init__()
        
    def insert(self, item):
        self.data.append(item)
        i = self.size() - 1
        while i > 0 and self.data[i] > item:
            self.data[i], self.data[i - 1] = self.data[i - 1], self.data[i]
            
        self.data[i] = item
        
    def max(self):
        return self.data[-1]
        
    def min(self):
        return self.data[0]
        
        
class max_queue_unorder(max_queue_array):
    '''
    @brief  无序数组的优先队列
    @note   每次获取最大值时直接选择最大值和末尾元素交换
    '''
    def __init__(self):
        super(max_queue_unorder, self).__init__()
        
    def insert(self, item):
        self.data.append(item)
        
    def max(self):
        max_index = 0
        for i in range(1, self.size()):
            if self.data[i] > self.data[max_index]:
                max_index = i
            
        self.data[-1], self.data[max_index] = self.data[max_index], self.data[-1]
        return self.data[-1]
    
        
class max_queue_link(max_queue):
    '''
    @brief  链表优先队列，最大值位于头节点的下一个节点
    '''
    def __init__(self):
        self.head = linklist.linklist(0)        #头节点
        
    def pop_max(self):
        ret = self.max()
        node = self.head.next
        self.head.next = node.next
        del node
        self.len -= 1 
        return ret
        
        
class max_queue_link_order(max_queue_link):
    '''
    @brief  有序优先队列
    @note   插入时便排序好
    '''
    def __init__(self):
        super(max_queue_link_order, self).__init__()
        
    def insert(self, item):
        index = self.head
        while None is not index and index.next.data > item:
            index = index.next
            
        node = linklist.linklist(item, index.next)
        index.next = node
        self.len += 1
        
    def max(self):
        return self.head.next.data
        
        
class max_queue_link_unorder(max_queue_link):
    '''
    @brief  有序优先队列
    @note   寻找时再查找
    '''
    def __init__(self):
        super(max_queue_link_unorder, self).__init__()
        
    def insert(self, item):
        node = linklist.linklist(item, self.head.next)
        self.head.next = node
        self.len += 1
        
    def max(self):
        max_node = self.head
        index = self.head
        while None is not index.next and max_node.next.data <= index.next.data:
            index = index.next
            
        max_node.next = self.head.next
        self.head.next = max_node
        return self.head.next.data
        
        
class min_max_queue(object):
    '''
    @brief  支持最大最小元素快速取出，使用两个堆进行操作
    '''
    def __init__(self):
        super(min_max_queue, self).__init__()
        self.max_heap = []
        self.min_heap = []
    
    def adjust(self):
        for i in range(len(self.min_heap)):
            swim(self.min_heap, 0, len(self.min_heap), i, less)
            
        for i in range(len(self.max_heap)):
            swim(self.max_heap, 0, len(self.max_heap), i, bigger)
        
    def find_min(self, item):
        for i in range(len(self.min_heap)):
            if self.min_heap[i] == item:
                return i
        
        return -1

    def find_max(self, item):
        for i in range(len(self.max_heap)):
            if self.max_heap[i] == item:
                return i
        
        return -1
        
    def insert(self, item):
        self.min_heap.append(item)
        self.max_heap.append(item)
        
        swim(self.min_heap, 0, len(self.min_heap), len(self.min_heap) - 1,less)
        swim(self.max_heap, 0, len(self.max_heap), len(self.max_heap) - 1,bigger)
        
    def max(self):
        return self.max_heap[0]
        
    def min(self):
        return self.min_heap[0]
        
    def pop_max(self):
        ret = self.max()
        index = self.find_min(ret)
        del self.min_heap[index]
        self.adjust()
        return ret
        
    def pop_min(self):
        ret = self.min()
        index = self.find_max(ret)
        del self.max_heap[index]
        self.adjust()
        return ret
    