from src.basic import heap


def heap_sort(l, left, right, hook_func):
    '''
    @brief  堆排序
    @param  l   list
    @param  left
    @param  right
    @param  hook_func   hook函数
    '''
    size = right - left
    i = int(size/2)
    while i >= 0:
        heap.sink(l, left, right, i, heap.less)
        i -= 1
    
    count = 0
    while size > 0:
        l[size - 1], l[0] = l[0], l[size - 1]
        size -= 1
        heap.sink(l, left, size, 0, heap.less)
        count += 1
        if hook_func is not None:
            hook_func(l, 0, size, count)
        
