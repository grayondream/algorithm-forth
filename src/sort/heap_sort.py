from src.basic import heap


def heap_sort(l, start, end, hook_func):
    '''
    @brief  堆排序
    @param  l   list
    @param  left
    @param  right
    @param  hook_func   hook函数
    '''
    size = start - end + 1
    i = int(size/2)
    while i >= 0:
        heap.sink(l, start, end, i, heap.less)
        i -= 1
    
    count = 0
    while size > 0:
        l[size - 1], l[0] = l[0], l[size - 1]
        size -= 1
        heap.sink(l, start, size, 0, heap.less)
        count += 1
        if hook_func is not None:
            hook_func(l, 0, size, count)
        
