from src.basic import heap

count = 0


def build_heap_sink(l, start, end, hook_func, com_func):
    '''
    @brief  堆排序使用下沉法构建堆[start, end]大根对
    @param  l   list
    @param  left
    @param  right
    @param  hook_func   hook函数
    '''
    i = int((end - start + 1) / 2 - 1)
    while i >= start:
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count
            count += 1
        heap.sink(l, start, end, i, com_func)
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count
            count += 1
        i -= 1


def heap_sort_sink(l, start, end, hook_func):
    '''
    @brief  堆排序使用下沉法构建堆[start, end]大根对
    @param  l   list
    @param  left
    @param  right
    @param  hook_func   hook函数
    '''
    size = end - start + 1
    if hook_func is not None:
        hook_func(l, start, end, count)
        global count
        count += 1
        
    build_heap_sink(l, start, end, hook_func, heap.bigger)
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


def build_heap_sinkn(l, start, end, hook_func, com_func, n):
    '''
    @brief  堆排序使用下沉法构建堆[start, end]大根对
    @param  l   list
    @param  left
    @param  right
    @param  hook_func   hook函数
    '''
    i = int((end - start + 1) / 2 - 1)
    while i >= start:
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count
            count += 1
        heap.sink_nway(l, start, end, i, n, com_func)
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count
            count += 1
        i -= 1


def heap_sort_sinkn(l, start, end, n, hook_func):
    '''
    @brief  堆排序使用下沉法构建堆[start, end]大根对
    @param  l   list
    @param  left
    @param  right
    @param  n 路数
    @param  hook_func   hook函数
    '''
    size = end - start + 1
    n = 4
    if hook_func is not None:
        hook_func(l, start, end, count)
        global count
        count += 1
    build_heap_sinkn(l, start, end, hook_func, heap.bigger, n)
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
        heap.sink_nway(l, start, start + size - 1, 0, n, heap.bigger)
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count
            count += 1


def heap_sort_sink2(l, start, end, hook_func):
    return heap_sort_sinkn(l, start, end, 2, hook_func)


def heap_sort_sink3(l, start, end, hook_func):
    return heap_sort_sinkn(l, start, end, 3, hook_func)


def heap_sort_sink4(l, start, end, hook_func):
    return heap_sort_sinkn(l, start, end, 4, hook_func)


def heap_sort_sink5(l, start, end, hook_func):
    return heap_sort_sinkn(l, start, end, 5, hook_func)


def heap_sort_sink6(l, start, end, hook_func):
    return heap_sort_sinkn(l, start, end, 6, hook_func)


def heap_sort_sink7(l, start, end, hook_func):
    return heap_sort_sinkn(l, start, end, 7, hook_func)


def heap_sort_sink8(l, start, end, hook_func):
    return heap_sort_sinkn(l, start, end, 8, hook_func)


all = [
    heap_sort_sink, heap_sort_sink2, heap_sort_sink3, heap_sort_sink4,
    heap_sort_sink5, heap_sort_sink6, heap_sort_sink7, heap_sort_sink8
]
