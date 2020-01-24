def shell_sort(l, start, end, hook_func=None):
    '''
    @brief  希尔排序算法
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    k = 1
    while int((end - start)/3) > k:
        k = 3*k + 1
        
    while k >= 1:
        for i in range(start, end):
            j = i
            while j >= k and l[j] < l[j - k]:
                if hook_func is not None:
                    hook_func(l, i, j)
                    
                tmp = l[j]
                l[j] = l[j - k]
                l[j - k] = tmp
                
                j -= k
        
        k = int(k/3)
    
