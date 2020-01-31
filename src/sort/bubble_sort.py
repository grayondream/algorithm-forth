def bubble_sort(l, start, end, hook_func=None):
    '''
    @brief  冒泡排序算法，排序区间[start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   hook函数这里主要是用作可视化
    '''
    count = 0
    for i in range(start, end + 1):
        for j in range(i + 1, end + 1):
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1
                
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
