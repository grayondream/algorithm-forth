import src.basic import heap


'''
2.4.3   见src.basic.heap中的max_queue各子类实现
'''


'''
2.4.15  见src.basic.heap中的is_heap两个实现
'''


'''
2.4.23  多路堆，见src.basic.heap中的swim_nway和sink_nway
'''


def cube_sum(n):
    '''
    @brief  2.4.25按顺序打印所有a^3+b^3的值,a in [0,n], b in [0,n]
    @param  n   
    @note   这里暂时之血一下伪代码min_queue表示小堆
    '''
    class node:
        def __init__(self,i,j):
            self.a = a
            self.b = b
            self.value = a * a * a + j * j * j
            
    min_queue = None
    for i in range(n):
        min_queue.insert(node(i,0))
        
    while not min_queue.empty():
        min_node = min_queue.pop_min()
        #TODO:访问代码
        if min_node.j < n:
            min_queue.insert(node(min_node.a, min_node.b + 1))
    
        
'''
2.4.26  见src.basic.heap中的sink_im, swim_im
'''


'''
2.4.29  见src.basic.heap中的min_max_queue
'''
    
    
class medium_heap(object):
    '''
    @brief 2.4.30   小跟堆维护大于midum的数字，大根堆维护小于medium的数字
    TODO:unkonwn
    '''
    def __init__(self):
        super(midum_heap, self).__init__()
        self.min_heap = []
        self.max_heap = []
            
    def insert(self, item):
        self.min_heap 
        
    