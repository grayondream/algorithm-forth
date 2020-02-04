from src.basic import heap



count = 0
def heap_sort(l, start, end, hook_func):
    '''
    @brief  堆排序
    @param  l   list
    @param  left
    @param  right
    @param  hook_func   hook函数
    '''
    if hook_func is not None:
        hook_func(l, start, end, count)
        global count 
        count += 1
    size = end - start + 1
    for k in range(start, end + 1):
        heap.sink(l, start, end, end - k, heap.bigger)
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
        
    while size > 0:
        l[size - 1], l[0] = l[0], l[size - 1]
        size -= 1
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
        heap.sink(l, start, start + size - 1, 0, heap.bigger)
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
        

all = [heap_sort]