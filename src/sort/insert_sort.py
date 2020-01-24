def insert_sort(l, start, end, hook_func=None):
    '''
    @brief  插入排序，排序范围[startm end)
    @param  l   进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   hook函数
    '''
    for i in range(start + 1, end):
        j = min(end - 1, i + 1)
        while j > start and l[j - 1] < l[j]:
            if hook_func is not None:
                hook_func(l, i, j)
                
            tmp = l[j]
            l[j] = l[j - 1]
            l[j - 1] = tmp
            
            j -= 1
            