from tools import list_tools
import time


def sort_performance(n, sort_funcs, random_index='random', sorted=False, reverse=False, repeat=100):
    '''
    @brief  对排序算法的性能进行基本的评估
    @param  sort_funcs  排序算法，要求严格按照基本的结构定义func(l, start, end, hook_func)
    @param  random_index    生成随机数的方式
    @param  sorted      生成的数组是否有序
    @param  reverse    数组是否进行反转
    @param  repeat      实验循环次数
    '''
    res_time = [0] * len(sort_funcs)
    for i in range(repeat):
        data = list_tools.generate_list(n, 0, n, random_index, sorted, reverse)
        for func in sort_funcs:
            tmp = data.copy()
            start = time.clock()
            func(tmp, 0, len(tmp) - 1, None)
            end = time.clock()
            res_time[sort_funcs.index(func)] += (end - start)
            
    return [ele / repeat for ele in res_time]
            
        
    