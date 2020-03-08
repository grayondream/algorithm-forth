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
        for j in range(start, end - i):
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1

            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]

    return l


def bubble_sort_II(l, start, end, hook_func=None):
    '''
    @brief  冒泡排序算法，排序区间[start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   hook函数这里主要是用作可视化
    @note   使用sorted标志位记录后续的位置是否已经排序，按照冒泡排序算法的思路如果已经后面的位置未经过交换元素，后面一定已经有序
    '''
    count = 0
    sorted = False
    for i in range(start, end + 1):
        sorted = True
        for j in range(start, end - i):
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1

            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
                sorted = False

        if sorted:
            break
    return l


def bubble_sort_III(l, start, end, hook_func=None):
    '''
    @brief  冒泡排序算法，排序区间[start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   hook函数这里主要是用作可视化
    @note   使用sorted标志位记录后续的位置是否已经排序，按照冒泡排序算法的思路如果已经后面的位置未经过交换元素，后面一定已经有序
    '''
    count = 0
    sorted = False
    sorted_border = end
    last_swap_index = 0
    for i in range(start, end + 1):
        sorted = True
        for j in range(start, sorted_border):
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1

            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
                sorted = False
                last_swap_index = j

        sorted_border = last_swap_index
        if sorted:
            break

    return l


all = [bubble_sort, bubble_sort_II, bubble_sort_III]
