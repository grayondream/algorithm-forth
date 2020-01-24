def selection_sort(l, start, end, hook_func=None):
    '''
    @brief  选择排序算法
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    for i in range(start, end):
        for j in range(i + 1, end):
            if hook_func is not None:
                hook_func(l, i, j)
                
            mid = i
            if l[mid] > l[j]:
                mid = j
            
        tmp = l[mid]
        l[mid] = l[i]
        l[i] = tmp
    
