def selection_sort(l, start, end, hook_func=None):
    '''
    @brief  选择排序算法
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    count = 0
    for i in range(start, end):
        minindex = i
        for j in range(i + 1, end):
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1
                
            if l[minindex] > l[j]:
                minindex = j
            
        tmp = l[minindex]
        l[minindex] = l[i]
        l[i] = tmp
    
