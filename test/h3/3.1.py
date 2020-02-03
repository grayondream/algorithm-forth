'''
3.1.2   见sym_table中的array_st实现
'''


'''
3.1.3   见sym_table中的link_st实现
'''


class time_object(object):
    '''
    @brief  3.1.4   
    '''
    def __init__(self, h, m, s):
        super().__init__()
        self.time = [h, m, s]
        
    def compare_to(self, item):
        for i in range(len(self.time)):
            if self.time[i] < item.time[i]:
                return -1
            elif self.time[i] > item.time[i]:
                return 1
            else:
                return 0
                
                
'''
3.1.24 见binary_search中的binary_search_inter实现
'''