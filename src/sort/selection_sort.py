def selection_sort(l, start, end, hook_func=None):
    '''
    @brief  选择排序算法[start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    count = 0
    for i in range(start, end + 1):
        minindex = i
        for j in range(i + 1, end + 1):
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1
                
            if l[minindex] > l[j]:
                minindex = j
            
        l[minindex], l[i] = l[i], l[minindex]
    
