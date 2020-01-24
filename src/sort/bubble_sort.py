def bubble_sort(l, start, end, hook_func=None):
    '''
    @brief  冒泡排序算法，排序区间[start, end)
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    for i in range(start, end):
        for j in range(i + 1, end):
            if hook_func is not None:
                hook_func(l, i, j)
            if l[j] < l[i]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
